import random
#--------------------------------1.feladat--------------------------------
print("\n--------------------------------1.feladat--------------------------------\n")
h = int(input("Add meg a hetek számát [1...5]: "))
while True:
    if h < 6 and h > 0:
        break
    else:
        print("Hibás adatbevitel! Próbáld meg újra...")
        h = int(input("Add meg a hetek számát [1...5]: "))

#--------------------------------2.feladat--------------------------------
print("\n--------------------------------2.feladat--------------------------------\n")

tamadasok = [[0]*7 for i in range(h)]


for het in range(h):
    for nap in range(7):
        tamadasok[het][nap] = random.randint(3,9)
print(tamadasok)

#--------------------------------3.feladat--------------------------------
print("\n--------------------------------3.feladat--------------------------------\n")

for het in range(len(tamadasok)):
    print(f"{het+1}.hét: {tamadasok[het]}")

#--------------------------------4.feladat--------------------------------
print("\n--------------------------------4.feladat--------------------------------\n")

ossz_tamadas = 0

for het in range(h):
    for nap in range(7):
        ossz_tamadas += tamadasok[het][nap]

print(f"Összes támadás száma: {ossz_tamadas}db")

#--------------------------------5.feladat--------------------------------
print("\n--------------------------------5.feladat--------------------------------\n")

c = 0

for het in range(h):
    for nap in range(7):
        if tamadasok[het][nap] > 5 and tamadasok[het][nap] < 8:
            c += 1
print(f"Feltételnek megfelelő napok száma: {c}db")

#--------------------------------6.feladat--------------------------------
print("\n--------------------------------6.feladat--------------------------------\n")

napok = ["Hétfő", "Kedd", "Szerda", "Csütörök", "Péntek", "Szombat", "Vasárnap"]
legtobb_tamadas = 0
het_hely = 0
nap_hely = 0

for het in range(h):
    for nap in range(7):
        if tamadasok[het][nap] >= legtobb_tamadas:
            legtobb_tamadas = tamadasok[het][nap]
            nap_hely = nap
            het_hely = het
print(f"Egy napon megtörtént legtöbb támadás száma: {legtobb_tamadas}db")
print(f"Helye: {het_hely+1}.hét, {napok[nap_hely]}")