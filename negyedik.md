### 1. Specifikáció (miből?,mit?)
    - Bemenő adatok
    - előfeltétel(ismeret a bemenetről)
    - eredmény
    - utófeltétel(erdményt meghatározó állítás)
    - használt fogalmak
    - megoldással szembeni követelmények
    - korlátozó tényezők

### 2. Tervezés(Mivel?, Hogyan?)
    - algoritmus
        - elemi tevékenységek:
            - értékadás, beolvasás, kiírás
        - összetett tevékenységek:
            - szekvencia
            - elágazás
            - ciklus
            - alprogram
    - algoritmust leiíró nyelvek:
        - szöveges leiírás:
            - mondatokkal leiírás
            - elemekkel
        - rajzos leiírás
            - strugtogram
            - folyamat ábra

### 3. Kodolás(replezentáció, inplezentáció)
    - Robert L. Martin

### 4. Tesztelés(hibás-e?)
    - hibalista
    - Test Driven Developmnet-TDD
    - Unit test 

###  5. Hibakeresés
    - hibahely
    - hiba ok

### 6. Hibajavítás

### 7. Minőség javítás, hatékonyság növelés

### 8. Dokumentálás
    - fejlesztői
    - felhasználói

### 9. Használat, Karbantartás

# Programozási tételek

### Összegzés tétele
    x: tömb, lsita, tárolja az adatokat
    s: változó, ő tárolja az összeget
    1..N: lista indexei

    s := 0 
    i = 1..N
        s := s+x[i]

    s = 0
    for i in range(len(x)):
        s = s + x[i]

### Öszzeszorzás
    s := 0
    i = 1..N
    s := f(s,x[i])

    f: +, *, összefuzés, unió

### Megszámlálás
    c: változó, azok darbszáma. melyekre igaz T
    T: feltétel, igaz/hamis

    C := 0
    T = 1..N
    i\ T(x[i])
    h\ c := c +1

    def T(n):
        return n % 2 == 0

    c = 0
    for i in range(len(x)):
        if  T(x[i]):
            c = c + 1

### Max-kiválasztás
    Max Ért: Max érték
    Max indexe: Max érték indexe

    Max Ért := X[1]
    Max indexe := 1
    i = 2..N
    i\ x[i] > Max Ért
    h\ Max Ért := X[i]
       Max indexe := i

    L = [2,3,5,734,123,75,4,2342,678,1234,8,12,845,7,1234125]
    N = L[0]
    hely = 0

    for i in range(1, len(L)):
        if L[i] > N:
            N = L[i]
            hely = i + 1
    print(N, hely)

### Keresés

    i := 1
    i <= N és nem T(x[i])
        i := i + 1
    Van := i <= N
        Van
