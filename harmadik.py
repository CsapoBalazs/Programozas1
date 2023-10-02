import random

print("------------------------------------1.feladat------------------------------------")

sor = 4
oszlop = 7

napok = [[0]*oszlop for i in range(sor)]

def feltoltes (lista):
    for so in range(sor):
        for osz in range(oszlop):
            lista[so][osz] = random.randint(0,9)
    return lista

print(feltoltes(napok))

print("------------------------------------2.feladat------------------------------------")

def ossz (lista):
    summ = 0
    for so in range(sor):
        for osz in range(oszlop):
            summ += lista[so][osz]
    return summ

print(ossz(napok))

print("------------------------------------3,4.feladat------------------------------------")

hetenteel = []
legsik = [0,0]

def hetente (lista,het,sikerhet):
    for so in range(sor):
        hetsumm = 0
        for osz in range(oszlop):
            hetsumm += lista[so][osz]
        if sikerhet[0] < hetsumm:
            sikerhet[0] = hetsumm
            sikerhet[1] = so+1
        het.append(f"A {so+1}. héten {hetsumm} db kokuszgolyót adtak el")
    return het,legsik

print(hetente(napok,hetenteel,legsik))
print(f"A legsikeresebb hét a {legsik[1]}-volt és {legsik[0]}db kokuszgolyóval")

print("------------------------------------5.feladat------------------------------------")

eladasmentesnap = 0

def eladmentes (lista,mentesnap):
    for so in range(sor):
        for osz in range(oszlop):
            if lista[so][osz] == 0:
                mentesnap += 1

    return mentesnap

eladasmentesnap = eladmentes(napok,eladasmentesnap)

print(f"{eladasmentesnap} db eladásmentes nap volt aug.-ban")

print("------------------------------------6.feladat------------------------------------")

hetnap = [0,0,0,0,0,0,0]
napok_str = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat","Vasárnap"]

def prtln_elad_nap (lista,napok):
    for osz in range(oszlop):
        for so in range(sor):
            prtln_summ = 0
            if lista[so][osz] % 2 == 1:
                prtln_summ += 1
            napok[osz] += prtln_summ
    leg_kev = min(hetnap)
    for i in range(len(hetnap)):
        if napok[i] == leg_kev:
            print(f"A legkevesebb páratlan számú eladás a {napok_str[i]}-hez/höz/hoz tartozik")
    return napok

print(prtln_elad_nap(napok, hetnap))