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

### eldöntés

    i := 1
        i <= N and not T(x[i])
            i := i + 1
    van := i <= N

### kiválasztás

    i := 1
        not T(x[i])
            i := i + 1
        ind := i
        érték := x[i]

