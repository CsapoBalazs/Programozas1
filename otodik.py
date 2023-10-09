"""import random

valasz = int(input("Adjon meg egy számot: "))
if valasz % 2 == 0:
    print("A felhasználó által megadott szám osztható 2-vel")
else:
    print("A felhasználó által megadot szám nem osztható 2-vel!")

gy = "körta"
i = 0
N = len(gy)
while i < N and not (gy[i] == "a"):
    i += 1
van = i < N
print(i < N)

a = "van egy kosár almám. Nemtudom!"
mondat = 0

for i in range(len(a)):
    if a[i] == "." or a[i] == "?" or a[i] == "!":
        mondat += 1

print(f"{mondat}db mondatból áll a szöveg")"""

lista = [["Béla", "f", "18:00"],["Judit", "n", "18:01"], ["Zoli", "f", "18:05"],["Kata", "n", "18:08"]]

for so in range(len(lista)):
    while (not(lista[so][1] == "n")):
        if lista[so][1] == "n":
            print(lista[so][0])