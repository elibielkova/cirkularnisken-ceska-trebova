# Zadání pro Claude – úprava webové prezentace Cirkulárního skenu města

## Kontext
Máme rozpracovaný webový koncept pro prezentaci výstupu z cirkulárního skenu města Česká Třebová.  
Teď potřebujeme připravit **upravenou verzi zadání pro Claude / vývoj**, která zapracuje interní připomínky týmu.

Cíl zůstává stejný:
- udělat z výstupu skenu atraktivní web,
- nezahlcovat obsahem,
- dát důraz na formu, jednoduchost a chuť stránku opravdu projít,
- vytvořit šablonu, kterou půjde později použít i pro další města.

Tahle verze zadání už má počítat s konkrétními úpravami, prioritami a novými nápady od kolegů.

---

# Hlavní směr úprav
## Co je potřeba posílit
- větší vizuální napojení na značku **Cirkulární hub**
- zároveň větší **customizace pro konkrétní město**
- více pohybu, interaktivity a hravosti už v horní části stránky
- silnější práce s mobilní verzí
- méně duplicitního textu
- lepší práce s grafy, zejména tam, kde jsou malé rozdíly špatně čitelné
- možnost rozšíření o další vrstvy obsahu: metodika, projekty, citace, průzkumy, dokumenty, gamifikace

---

# Hlavní změny oproti původní verzi

## 1. Branding a vizuální identita
Zapracovat branding Cirkulárního hubu výrazněji než dosud.

### Požadavky:
- vlevo nahoře nebo v horní liště umístit **logo Cirkulárního hubu**
- do designu zapracovat **barvy Cirkulárního hubu**
- hlavní pozadí nebo dominantní tón stránky může být **fialový**
- stránka ale zároveň musí být **víc přizpůsobená konkrétnímu městu**
- pro Českou Třebovou navrhnout individuální vizuální prvky:
  - fotka města
  - prolínačky / siluety města
  - případně silueta krajiny / hor
  - městské motivy v pozadí

### Doporučení:
Použít city-specific vizuální vrstvu:
- fotka města po pravé a levé straně,
- uprostřed ztmavená / zjemněná,
- aby vznikl výraznější a unikátní vizuální charakter každého města.

---

## 2. Úprava horní části stránky / hero
Hero sekce má být výraznější, živější a víc “aha” hned na začátku.

### Musí obsahovat:
- název v horní liště: **Cirkulární sken města Česká Třebová**
- jasně zdůraznit, že jde o produkt **Cirkulární sken**
- lepší a silnější slogan pro úvod
- případně krátké vysvětlení, co Cirkulární sken je
- vizuální prvek města
- pohyblivé prvky už nahoře

### Doporučení:
- grafy a další pohyblivé části posunout výš na stránku
- uživatel má mít hned po načtení pocit, že je stránka živá, interaktivní a jiná než běžný report
- zvážit zakomponování videa:
  - https://youtu.be/iMZy7FH0cC8

---

## 3. Přehodnotit informační flow stránky
Původní strukturu upravit tak, aby dávala větší smysl z pohledu UX a odstranily se duplicity.

## Ideální flow stránky:
1. Hero – co to je
2. Hlavní výsledek – celkové skóre + grafy
3. Co se daří
4. Na co navázat / co zlepšit – ideálně interaktivně
5. 5 klíčových oblastí
6. Projekty / příklady dobré praxe / case studies
7. Hlas města – citace, lidé, případně výsledky průzkumu
8. Metodika
9. Odkazy na dokumenty / zdroje / plný výstup

---

# Obsahové úpravy

## 4. Zrušit nebo sloučit duplicitní sekce
V původní verzi se významově duplikují některé části.

### Zapracovat:
- **odstranit duplicitní část**, kde se opakují podobné informace
- rozhodnout strukturu tak, aby se neopakovalo:
  - „Co se daří“
  - „Na co navázat“
  - „V čem město vyniká“
  - „Co město může udělat dál“

## Preferovaná varianta:
Zachovat primárně:
- **Co se daří**
- **Na co navázat**

a vypustit / upozadit:
- „V čem Česká Třebová vyniká“

Pokud bude potřeba pozitivní framing, může být obsažen právě v sekci **Co se daří**.

---

## 5. Sekci “Co se daří” a “Na co navázat” přepracovat vizuálně
Místo klasických textových bloků použít vizuálně atraktivnější formu.

### Doporučené varianty:
- úzké dlaždice s ikonami nebo emotikony
- horizontálně posuvný carousel zleva doprava
- ikonové karty převzaté stylem ze samotného CE skenu
- každá dlaždice = 1 stručný insight

### Cíl:
- lehčí čtení
- lepší přehled
- větší atraktivita na mobilu
- menší pocit “dalšího reportu”

---

## 6. 5 klíčových oblastí přepracovat do interaktivních karet
Jednotlivé oblasti neřešit jen jako klasické sekce pod sebou.

### Oblasti:
- Strategie a politika
- Výstavba a budovy
- Odpadové hospodářství
- Doprava
- Biodiverzita a lokálnost

### Nové řešení:
Každou oblast udělat jako **kartu**:
- na přední straně:
  - název oblasti
  - skóre
- po hoveru / tapu:
  - 2–3 silné stránky
  - 2–3 doporučení / na co navázat

### Důležité:
- na desktopu může karta reagovat na hover
- na mobilu musí fungovat přes klik / rozbalení
- mobilní UX je priorita

### Navíc:
Každá oblast by měla mít možnost **prokliku na odpovídající část v dokumentu Canva**:
- například tlačítko:
  - Zobrazit oblast v plném dokumentu
  - Více detailu v dokumentu

---

# Grafy a data

## 7. Grafy posunout výš na stránku
Grafy a pohyblivé datové prvky dát co nejvíc nahoru.

### Důvod:
- hned vytvoří “aha moment”
- stránka bude působit hravěji a víc digitálně
- uživatel se dřív chytí

---

## 8. Upravit typy grafů podle typu dat
Nenechávat jeden typ grafu za každou cenu.

### Konkrétně:
U menších změn nebo tam, kde je linka moc krátká a na mobilu není dobře čitelná, nepoužívat line chart.

### Místo toho zvážit:
- bar chart
- before / after srovnání
- procentní nárůst jako stat kartu
- dot plot
- jednoduché mini-komparace

### Příklad:
U růstu třídění, kde je malý rozdíl, je potřeba jiný graf než krátká linka, protože na mobilu není dobře vidět změna, např. u skla.

---

## 9. Přidat konkrétní grafy
Na stránce by měly být minimálně tyto grafy:

- **Směsný komunální odpad**
- **Plasty, kovy, papír, sklo**

### Požadavky:
- animace při načtení
- linky nebo sloupce se dynamicky vykreslí
- při hoveru na bod / hodnotu se zobrazí údaj v daném roce
- grafy musí být dobře čitelné i na mobilu
- každé načtení stránky může grafy znovu jemně rozehrát

---

## 10. Přidat i jednoduchý ukazatel plnění konkrétních opatření
V úrovni plnění je možné vybrat z každé oblasti jednu konkrétní věc a ukázat, v jaké fázi se nachází.

### Příklad:
- sběr gastroodpadu
- úroveň plnění formou:
  - loading baru
  - progress baru
  - stupnice
  - semaforu
  - “stav implementace”

### Cíl:
Ukázat konkrétnější a pro občana uchopitelný příklad.

---

# Interaktivita a gamifikace

## 11. “Co může město udělat dál” udělat interaktivněji
Tahle sekce nemá být jen obyčejný seznam.

### Možné formy:
- mapka opatření
- interaktivní sluníčko / rozcestník, podobně jako v dokumentu
- klikací roadmapa
- orbit / síť doporučení
- dlaždice, které se po kliknutí rozbalují

### Cíl:
Aby byla sekce víc živá, hravá a zapamatovatelná.

---

## 12. Přidat interaktivní mini hru nebo kvíz
Chceme do webu dostat hravý prvek pro běžného návštěvníka.

## Varianta A – kvíz
### Název:
**A co děláš pro svoje město ty?**

### Princip:
Krátký interaktivní kvíz:
- třídíš odpad?
- využíváš lokální služby?
- chodíš pěšky / jezdíš na kole?
- zajímáš se o veřejný prostor?
- omezuješ plýtvání?

### Výstup:
- např. „Jsi cirkulární občan na 62 %“
- tipy na zlepšení
- lehký, motivační tón

## Varianta B – mini hra
Například:
- Pacman-like hra
- postavička sbírá odpad nebo informace o cirkulární ekonomice
- pro Českou Třebovou lze inspirovat městským chatbotem / maskotem Četík a využít kohouta jako herní motiv
- hra může být “just for fun”, nemusí být složitá

### Důležité:
Gamifikace je plus, ale nemá rozbít výkon webu ani přehlušit hlavní obsah.  
Může být i ve formě volitelného modulu.

---

# Městský obsah a lidská rovina

## 13. Přidat hlas města
Stránka by neměla být jen o číslech.

### Zapracovat:
- fotku starosty s citací
- fotku místostarostky / zástupce města s citací
- případně další citace
- sekci “Hlas města”

### Cíl:
Dodat webu důvěryhodnost a lidský rozměr.

---

## 14. Přidat příklady úspěšně realizovaných projektů
Zařadit konkrétní příklady dobré praxe.

### Forma:
- karta projektu
- fotka
- krátký popis
- čím je projekt zajímavý / co ukazuje

### Cíl:
Ukázat, že cirkulární ekonomika není jen teorie, ale i konkrétní realizace.

---

## 15. Připravit prostor pro výsledky dotazníků a citace občanů
Do budoucna počítat s možností doplnit:
- výsledky dotazníkového šetření mezi občany
- citace občanů z ulic / anket
- názory veřejnosti

### Poznámka:
U některých měst to nemusí být ihned, ale šablona s tím má počítat.
Například u Žďáru nad Sázavou může být tato vrstva už důležitá.

---

# Dokumenty, odkazy, metodika

## 16. Přidat odkazy na plný dokument
Na stránce má být možnost prokliku na celý dokument.

### Přidat:
- tlačítko na celý dokument Canva pro dané město
- případně i odkaz na PDF verzi

### Důležité:
PDF dokumenty uložit na stránky Cirkulárního hubu tak, aby se na ně uživatel dostal ideálně přes stránku konkrétního města.

---

## 17. Metodika musí být dohledatelná
Pokud uvádíme celkovou míru cirkularity, musí být někde dostupné i vysvětlení, jak vznikla.

### Musí být uvedeno:
- že existuje metodika hodnocení
- bodové rozdělení dle velikosti města
- váhy oblastí
- princip výpočtu celkového skóre

### Forma:
- samostatná záložka
- akordeon
- modal
- nebo odkaz na samostatné PDF s metodikou

### Důležité:
Nemusí být hned viditelná v hlavním toku stránky, ale musí být snadno dohledatelná.

---

# Technické a UX priority

## 18. Mobilní verze je zásadní priorita
Na mobilní verzi si dát mimořádně záležet.

### To znamená:
- přehledná typografie
- velké klikací plochy
- dobře viditelné grafy
- žádné jemné detaily, které na telefonu zaniknou
- karty, carousely a interaktivní prvky musí fungovat přirozeně přes touch
- horizontální scroll používat jen tam, kde dává jasný smysl
- pozor na přetížení obrazovky

---

## 19. Animace ano, ale účelně
Pohyblivé prvky mají být výraznou součástí webu, ale ne přehnané.

### Povinně:
- animace grafů při načtení
- animace čísel
- mikrointerakce na kartách
- plynulé přechody

### Vhodné:
- jemný pohyb v hero sekci
- odkrývání obsahu při scrollu
- znovuspuštění jemné animace při reloadu

### Nevhodné:
- těžké efekty
- rušivá přebujelá animace
- vizuální chaos

---

# Shrnutí priorit pro Claude
Při úpravě webu se drž těchto priorit:

## Priorita 1
Vizuálně i obsahově silnější, hravější a interaktivnější úvod stránky.

## Priorita 2
Zapracování brandingu Cirkulárního hubu + customizace na konkrétní město.

## Priorita 3
Lepší práce s grafy:
- dát je výš,
- rozhýbat je,
- změnit typ tam, kde malé rozdíly nejsou dobře vidět.

## Priorita 4
Odstranění obsahových duplicit a zjednodušení flow.

## Priorita 5
Silný mobilní UX.

## Priorita 6
Přidání lidské a hravé roviny:
- citace,
- projekty,
- kvíz / mini hra,
- případně video.

---

# Výstup, který chceme
Claude má upravit web tak, aby výsledkem byla stránka, která:
- působí moderně a živě,
- není jen online verze PDF,
- zaujme i běžného občana,
- je hezká, přehledná a snadno pochopitelná,
- funguje dobře na mobilu,
- umí pracovat s daty atraktivně,
- je připravená jako šablona i pro další města.

---

# Praktický úkol pro Claude
Uprav návrh webu pro **Cirkulární sken města Česká Třebová** podle tohoto zadání.

Zaměř se hlavně na:
- novou strukturu stránky,
- vylepšený hero,
- silnější branding,
- grafy a jejich animace,
- redesign sekcí “Co se daří” a “Na co navázat”,
- interaktivní karty 5 oblastí,
- prostor pro metodiku, dokumenty, video, citace a případně kvíz / mini hru,
- maximálně dotaženou mobilní verzi.

Nevytvářej textově těžký web.  
Místo toho udělej lehký, atraktivní a vizuálně silný web s důrazem na UX, pohyb a srozumitelnost.
