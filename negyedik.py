"""s = 0
for i in range(len(x)):
    s = s + x[i]

def T(n):
    return n % 2 == 0

c = 0
for i in range(len(x)):
    if  T(x[i]):
        c = c + 1
"""

L = [2,3,5,734,123,75,4,2342,678,1234,8,12,845,7,1234125]
N = L[0]
hely = 0

for i in range(1, len(L)):
    if L[i] > N:
        N = L[i]
        hely = i + 1
print(N, hely)

Nev = "Csapó Balázs"

for i in range(len(Nev)):
    if Nev[i] == "a":
        print(i+1)
        break