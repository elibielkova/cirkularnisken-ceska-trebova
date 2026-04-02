"""
scraping_webu.py
----------------
Stáhne a extrahuje relevantní obsah z webu obce.
Výstup je JSON soubor (data_obce.json) připravený pro zobrazení na webu.

Použití:
    python scraping_webu.py https://www.ceska-trebova.cz
    python scraping_webu.py https://www.ceska-trebova.cz --hloubka 2 --vystup data_obce.json
    python scraping_webu.py https://www.ceska-trebova.cz --max-stranek 60 --nazev "Česká Třebová"

Závislosti:
    pip install requests beautifulsoup4
"""

import sys
import re
import time
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Chyba: pip install requests beautifulsoup4")
    sys.exit(1)

# ---------------------------------------------------------------------------
# KATEGORIE A KLÍČOVÁ SLOVA
# ---------------------------------------------------------------------------

KATEGORIE = {
    "odpady": [
        "odpad", "trideni", "třídění", "recyklace", "komunalni", "komunální",
        "bioodpad", "kompost", "sberny", "sběrný", "svoz", "door-to-door",
        "popelnice", "kontejner",
    ],
    "doprava": [
        "doprava", "cyklostezk", "cyklo", "mobilita", "parkovani", "parkování",
        "mhd", "chodnik", "chodník", "autobus", "vlak", "elektromobil",
    ],
    "energie": [
        "energetik", "oze", "solarni", "solární", "fotovoltaik", "zatepleni",
        "zateplení", "uspory", "úspory", "tepelne", "tepelné", "kotelna",
        "obnovitelne", "obnovitelné",
    ],
    "priroda": [
        "zelen", "zeleň", "biodiverzita", "park", "voda", "destova", "dešťová",
        "retencni", "retenční", "zahrada", "strom", "priroda", "příroda",
        "sad", "louka",
    ],
    "strategie": [
        "strategie", "plan", "plán", "rozvoj", "udrzitelnost", "udržitelnost",
        "cirkularni", "cirkulární", "klimat", "adaptace", "dotace", "projekt",
        "grant", "inovace",
    ],
}

# Sloučený seznam všech klíčových slov pro rychlý test relevance
VSECHNA_SLOVA = [s for kw in KATEGORIE.values() for s in kw]

# URL části které vždy přeskočit
PRESKOCIT_URL = [
    "/wp-admin", "/wp-login", "/wp-content/uploads",
    ".pdf", ".doc", ".xls", ".zip", ".rar", ".jpg", ".png", ".gif", ".svg",
    "facebook.com", "twitter.com", "instagram.com", "youtube.com",
    "google.com", "mapy.cz", "/rss", "/feed",
    "javascript:", "mailto:", "tel:",
    # Statické stránky odborů a org. struktura – nechceme
    "/odbor", "/utvar", "/oddeleni", "/vedeni", "/zastupitel",
    "/rada-mesta", "/zastupitelstvo", "/komisar", "/tajemnik",
    "/kontakt", "/uredni-deska", "/formulare", "/poplatky",
    "/vismo/o_utvar", "/vismo/zobraz_dok",
    # Vismo – archivní a filtrovací parametry (duplicitní varianty té samé stránky)
    "&tzv=", "&archiv=", "&prich=", "&q=",
    # Sekce nesouvisející s cirkulární ekonomikou
    "sportov", "sokol", "bazenu", "bazen", "fotbal", "hokej",
    "kultura", "divadlo", "kino", "knihovna",
]

# Povolené zpravodajské sekce – scraper sleduje POUZE tyto vzory URL.
# Stránky mimo tyto vzory jsou přeskočeny (slouží jen jako rozcestníky).
ZPRAVODAJSKE_VZORY = [
    "aktualit", "aktuality",
    "zpravodaj", "zpravy", "zprava",
    "novink", "novinky",
    "tiskova", "tiskove",
    "stanovisko", "stanoviska",
    "oznameni", "vyhlasky",
    "clanek", "clanky",
    "udalost", "udalosti",
    # Vismo CMS – sekce dokumentů (ds-) s novinkovými klíči
    "ds-1166", "ds-1167", "ds-1168",  # typické zpravodajské sekce Vismo
]


# ---------------------------------------------------------------------------
# POMOCNÉ FUNKCE
# ---------------------------------------------------------------------------

def normalizuj(text: str) -> str:
    """Převede text na lowercase bez diakritiky pro porovnání."""
    import unicodedata
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text


def urcit_kategorii(text: str) -> str:
    """Vrátí dominantní kategorii stránky podle výskytu klíčových slov."""
    text_norm = normalizuj(text)
    skore = {kat: 0 for kat in KATEGORIE}
    for kat, slova in KATEGORIE.items():
        for slovo in slova:
            if slovo in text_norm:
                skore[kat] += 1
    nejlepsi = max(skore, key=skore.get)
    return nejlepsi if skore[nejlepsi] > 0 else "ostatni"


def urcit_klicova_slova(text: str) -> list:
    """Vrátí seznam nalezených klíčových slov ze stránky (max 5)."""
    text_norm = normalizuj(text)
    nalezena = []
    for slovo in VSECHNA_SLOVA:
        if slovo in text_norm and slovo not in nalezena:
            nalezena.append(slovo)
        if len(nalezena) >= 5:
            break
    return nalezena


# ---------------------------------------------------------------------------
# SCRAPER
# ---------------------------------------------------------------------------

class WebScraper:
    def __init__(self, zakladni_url: str, max_stranek: int = 80,
                 hloubka: int = 2, zpozdeni: float = 0.8):
        self.zakladni_url = zakladni_url.rstrip("/")
        self.domena = urlparse(zakladni_url).netloc
        self.max_stranek = max_stranek
        self.hloubka = hloubka
        self.zpozdeni = zpozdeni

        self.navstivene = set()
        self.fronta = [(zakladni_url, 0)]  # (url, hloubka)
        self.vysledky = []

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (compatible; CirkularniSken/1.0; "
                "+https://cirkularni-hub.cz)"
            )
        })

    def je_relevantni_url(self, url: str) -> bool:
        """Vrátí True jen pro zpravodajské URL (aktuality, novinky, stanoviska...)."""
        url_lower = url.lower()

        # Vždy přeskočit zakázané vzory
        for skip in PRESKOCIT_URL:
            if skip in url_lower:
                return False

        # Povolit pouze URL obsahující zpravodajské vzory
        url_norm = normalizuj(url_lower)
        return any(vzor in url_norm for vzor in ZPRAVODAJSKE_VZORY)

    def je_stejna_domena(self, url: str) -> bool:
        try:
            return urlparse(url).netloc == self.domena
        except Exception:
            return False

    def stahni_stranku(self, url: str):
        """Stáhne a zpracuje stránku. Vrátí dict nebo None."""
        try:
            response = self.session.get(url, timeout=15, allow_redirects=True)
            if response.status_code != 200:
                return None
            if "text/html" not in response.headers.get("content-type", ""):
                return None

            soup = BeautifulSoup(response.text, "html.parser")

            # Titulek
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else url

            # Odstranit nepotřebné elementy
            for tag in soup.find_all(["script", "style", "nav", "footer",
                                       "header", "aside", "noscript",
                                       "iframe", "form", "button"]):
                tag.decompose()

            # Hledat hlavní obsah – preferuj sémantické elementy,
            # jinak celé body (Vismo a podobné CMS nemají standard. ID)
            hlavni = soup.find("main") or soup.find("article") or soup.find("body")

            if not hlavni:
                return None

            # Text
            text = hlavni.get_text(separator="\n", strip=True)
            radky = [r.strip() for r in text.splitlines() if r.strip()]
            text = "\n".join(radky)

            # Interní odkazy
            odkazy = []
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                if not href or href.startswith("#"):
                    continue
                plna = urljoin(url, href).split("#")[0].split("?")[0]
                if (self.je_stejna_domena(plna) and
                        plna not in self.navstivene and
                        self.je_relevantni_url(plna)):
                    odkazy.append(plna)

            return {"title": title, "text": text, "odkazy": list(set(odkazy))}

        except requests.exceptions.Timeout:
            print(f"    → timeout: {url}")
            return None
        except requests.exceptions.ConnectionError:
            print(f"    → nedostupné: {url}")
            return None
        except Exception as e:
            print(f"    → chyba ({e}): {url}")
            return None

    def je_relevantni_obsah(self, text: str) -> bool:
        """True pokud stránka obsahuje alespoň 3 klíčová slova z oblastí skenu."""
        text_norm = normalizuj(text)
        pocet = sum(1 for slovo in VSECHNA_SLOVA if slovo in text_norm)
        return pocet >= 3

    def scraping(self) -> list:
        """Hlavní smyčka. Vrátí seznam zpracovaných stránek."""
        print(f"  Zahajuji scraping: {self.zakladni_url}")
        print(f"  Max. stránek: {self.max_stranek}, hloubka: {self.hloubka}")

        # Deduplikace podle normalizovaného titulku (Vismo zobrazuje 1 článek ve více sekcích)
        videtitulky = set()

        while self.fronta and len(self.vysledky) < self.max_stranek:
            url, hloubka_url = self.fronta.pop(0)

            if url in self.navstivene:
                continue
            self.navstivene.add(url)

            print(f"  [{len(self.vysledky)+1}/{self.max_stranek}] {url[:80]}")
            data = self.stahni_stranku(url)

            if data and data["text"] and len(data["text"]) > 100:
                # Přeskočit duplicitní titulky
                titulek_norm = normalizuj(data["title"].split(":")[0].strip())
                if titulek_norm in videtitulky:
                    continue
                videtitulky.add(titulek_norm)

                if self.je_relevantni_obsah(data["text"]):
                    kategorie = urcit_kategorii(data["text"])
                    klicova = urcit_klicova_slova(data["text"])
                    ukazka = data["text"][:400].replace("\n", " ")

                    self.vysledky.append({
                        "url": url,
                        "nadpis": data["title"],
                        "ukazka": ukazka,
                        "kategorie": kategorie,
                        "klicova_slova": klicova,
                    })

                    # Přidat nové odkazy do fronty
                    if hloubka_url < self.hloubka:
                        for odkaz in data["odkazy"]:
                            self.fronta.append((odkaz, hloubka_url + 1))

            time.sleep(self.zpozdeni)

        print(f"\n  Hotovo: staženo {len(self.vysledky)} relevantních stránek")
        return self.vysledky


# ---------------------------------------------------------------------------
# FORMÁTOVÁNÍ VÝSTUPU
# ---------------------------------------------------------------------------

def uloz_json(vysledky: list, nazev_obce: str, url_zdroj: str, vystup: str):
    """Uloží výsledky jako JSON soubor pro frontend."""
    data = {
        "aktualizovano": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "obec": nazev_obce,
        "url_zdroj": url_zdroj,
        "pocet_stranek": len(vysledky),
        "stranky": vysledky,
    }
    Path(vystup).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nVýstup uložen: {vystup} ({len(vysledky)} stránek)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Stáhne obsah webu obce relevantní pro cirkulární sken."
    )
    parser.add_argument("url", help="Základní URL webu obce (např. https://www.ceska-trebova.cz)")
    parser.add_argument("--hloubka", type=int, default=2,
                        help="Hloubka procházení odkazů (výchozí: 2)")
    parser.add_argument("--max-stranek", type=int, default=80,
                        help="Maximální počet stránek (výchozí: 80)")
    parser.add_argument("--zpozdeni", type=float, default=0.8,
                        help="Zpoždění mezi požadavky v sekundách (výchozí: 0.8)")
    parser.add_argument("--vystup", default="data_obce.json",
                        help="Výstupní JSON soubor (výchozí: data_obce.json)")
    parser.add_argument("--nazev", default="Česká Třebová",
                        help="Název obce (výchozí: Česká Třebová)")
    args = parser.parse_args()

    scraper = WebScraper(
        zakladni_url=args.url,
        max_stranek=args.max_stranek,
        hloubka=args.hloubka,
        zpozdeni=args.zpozdeni,
    )

    vysledky = scraper.scraping()

    if vysledky:
        uloz_json(vysledky, args.nazev, args.url, args.vystup)
    else:
        print("\nŽádný relevantní obsah nenalezen.")
        # Uložit prázdný JSON aby frontend věděl, že proběhl pokus
        uloz_json([], args.nazev, args.url, args.vystup)
