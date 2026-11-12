# FIFA / EA FC Adatelemzés – Dokumentáció

## 1. Kérdések

1. **Legkiegyensúlyozottabb játékosok:** Kik a legalább 75-ös átlaggal rendelkező, legkisebb képesség-szórású mezőnyjátékosok?
2. **Posztok specializáltsága:** Melyik poszt igényli a legszélsőségesebb (legnagyobb szórás), és melyik a legkiegyensúlyozottabb (legkisebb szórás) profil?
3. **Nemzetek eltérése:** Miben tér el leginkább a top 5 nemzet képességátlaga a globális mezőnyátlagtól?
4. **Sebesség vs. játéklátás korral:** Hogyan alakul a sprintsebesség és a játéklátás 20 és 35 éves kor között?
5. **Elit csatárok előnye:** Mely tulajdonságban a legnagyobb a pontkülönbség az elit (85+) és az átlagos (70–74) csatárok (ST) között?

---

## 2. Soronkénti magyarázat és parancsok

* **1–2. sor:** Szükséges könyvtárak betöltése (`import`).
  * `import`: külső csomagok beemelése a programba.
* **4. sor:** A futó fájl mappájának lekérdezése.
  * `os.path.abspath(__file__)`: a szkript teljes elérési útja.
  * `os.path.dirname()`: kinyeri a könyvtárat a fájlnévből.
* **5. sor:** Teljes elérési út összerakása a CSV-hez.
  * `os.path.join()`: mappák és fájlnevek platformfüggetlen összefűzése.
* **6. sor:** Adattábla beolvasása.
  * `pd.read_csv()`: CSV fájl DataFrame-be töltése.
* **8–12. sor:** Egységes név létrehozása a becenévből vagy a teljes névből.
  * `.fillna()`: hiányzó (`NaN`) értékek helyettesítése.
  * `.str.strip()`: felesleges kezdő és záró szóközök levágása.
* **14. sor:** Születési dátum szövegből dátum típussá alakítása.
  * `pd.to_datetime()`: dátummá konvertálás (`errors="coerce"` hibás adatnál üres értéket ad).
* **15. sor:** Életkor kiszámítása években a mai napból kivonva.
  * `pd.to_datetime("today")`: aktuális dátum.
  * `.dt.days`: eltelt napok száma.
  * `//`: egészosztás az évek megkapásához.
* **17–24. sor:** A vizsgált 6 alaptulajdonság oszlopneveinek listába gyűjtése.
* **26. sor:** Hiányos sorok eldobása a képességek alapján.
  * `.dropna()`: `NaN` értékeket tartalmazó sorok törlése.
  * `.copy()`: önálló másolat készítése memóriahiba elkerülésére.
* **27. sor:** Kapusok kiszűrése (csak mezőnyjátékosok megtartása).
  * `!=`: szűrés a nem egyenlő feltételre.
* **32. sor:** A 6 képesség soronkénti átlagának kiszámítása.
  * `.mean(axis=1)`: számtani átlag soronként.
* **33. sor:** A 6 képesség soronkénti szórásának kiszámítása.
  * `.std(axis=1)`: szórás soronként (ingadozás mértéke).
* **35–42. sor:** 75+ átlagú játékosok szűrése, szórás szerinti rendezése és az első 5 kiválasztása.
  * `.sort_values()`: sorba rendezés (alapértelmezés szerint növekvő).
  * `.head()`: az első megadott számú sor levágása.
* **43–49. sor:** Oszlopok átnevezése magyar elnevezésekre.
  * `.rename(columns={...})`: fejlécnevek cseréje szótár alapján.
* **50–51. sor:** 1. kérdés eredményének kiírása.
  * `.round()`: tizedesjegyek kerekítése.
  * `.to_string(index=False)`: szép táblázatos kiírás sorszámok nélkül.
* **56–61. sor:** Posztonkénti tulajdonságátlagok és azok szórásának számítása, csökkenő sorrendben.
  * `.groupby()`: csoportosítás adott oszlop értékei szerint.
  * `ascending=False`: csökkenő sorrend.
* **63–66. sor:** A leginkább egyoldalú (legnagyobb szórású) poszt kiírása.
  * `.head(1)`: a legelső elem lekérése.
* **68–71. sor:** A legkiegyensúlyozottabb (legkisebb szórású) poszt kiírása.
  * `.tail(1)`: a legutolsó elem lekérése.
* **76. sor:** A legtöbb játékost adó 5 nemzet nevének kigyűjtése.
  * `.value_counts()`: egyedi értékek gyakoriságának számolása.
  * `.index`: a csoportnevek lekérése.
* **77–82. sor:** Top nemzetek átlagának kivonása a mezőnyátlagból.
  * `.isin()`: benne-van vizsgálat listához képest.
  * `-`: elemi kivonás az átlagok közötti különbséghez.
* **83–84. sor:** 3. kérdés különbségeinek kerekített kiírása.
* **89–98. sor:** 20–35 év közötti korcsoportok átlagsebességének és játéklátásának képzése, oszlopok átnevezése.
  * `&`: logikai ÉS feltétel szűrésnél.
* **99. sor:** Index mező elnevezése.
  * `.index.name`: az index tengely feliratozása.
* **101–102. sor:** 4. kérdés korosztályos táblázatának kiírása.
* **107. sor:** Csatárok szűrése.
  * `==`: egyenlőség vizsgálata.
* **109–112. sor:** Elit (85+) és átlagos (70–74) csatárok képességátlagának kiszámítása.
  * `>=`: nagyobb vagy egyenlő feltétel.
* **115. sor:** Elit és átlagos átlagok kivonása, csökkenő rendezés a rés nagysága szerint.
* **117–118. sor:** 5. kérdés pontkülönbségeinek kiírása.