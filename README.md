# FC / EA FC Adatbázis Elemzés - Dokumentáció

## 1. Kérdések

1. **Legkiegyensúlyozottabb játékosok:** Kik a legalább 75-ös átlaggal rendelkező, legkisebb képesség-szórású mezőnyjátékosok?
2. **Posztok specializáltsága:** Melyik poszt igényli a legszélsőségesebb (legnagyobb szórás), és melyik a legkiegyensúlyozottabb (legkisebb szórás) profilt?
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
  * `.copy()`: független memóriamásolat készítése.
* **27. sor:** Kapusok kiszűrése (`!= "GK"`).
* **32. sor:** Játékosonkénti tulajdonságátlag számítása (`.mean(axis=1)`).
* **33. sor:** Játékosonkénti szórás számítása (`.std(axis=1)`).
* **35–48. sor:** Legalább 75-ös átlagú játékosok szűrése, szórás szerinti növekvő rendezése (`.sort_values(ascending=True)`), az első 5 kiválasztása (`.head(5)`), és oszlopok átnevezése (`.rename()`).
* **50. sor:** Eredmény szöveges kiíratása sorszámok nélkül (`.to_string(index=False)`).
* **54–59. sor:** Posztonkénti csoportosítás (`.groupby("position")`), tulajdonságátlagok és soronkénti szórások képzése, majd rendezése.
* **64. és 68. sor:** A leginkább specializált poszt (`.head(1)`) és a legsokoldalúbb poszt (`.tail(1)`) kiíratása 2 tizedesre kerekítve (`.round(2)`).
* **72. sor:** Az 5 leggyakoribb nemzet kiválasztása (`.value_counts().head(5).index`).
* **73–78. sor:** Csak ezen nemzetek szűrése (`.isin()`), átlaguk kiszámítása, és a világátlag kivonása belőle.
* **83–94. sor:** 20 és 35 év közötti életkorszűrés, életévenkénti csoportosítás, sprint- és látásátlagok számítása, valamint oszlopok átnevezése.
* **98–104. sor:** Csatárok (`ST`) szűrése, külön az elit ($\ge$ 85) és átlagos (70–74) játékosok átlagának kiszámítása.
* **106. sor:** Képességbeli különbségek kivonása egymásból és csökkenő rendezése.
* **109. sor:** Végső pontkülönbségek kiíratása.
