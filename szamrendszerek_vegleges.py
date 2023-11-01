import random

alap_szamrendszer = int(input("Adja meg annak a számrendszernek a számát amelyből átszeretne válatani: "))
cel_szamrendszer = int(input("Adja meg annak a számrendszernek a számát amelybe átszeretne váltani: "))

#--------------------------------------------- Tizes számrendszerből való átváltások --------------------------------------------- 

def tizesbol_kilencesbe (atvaltott_szam):
    # a tizes számrendszerben lévő szám már át lett váltava egy másik számrendszerből
    i = 0
    kilences_szamrenszer = ""

    while 9**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 9**i*8 <= atvaltott_szam:
            kilences_szamrenszer += "8"
            atvaltott_szam -= 9**i*8

        elif 9**i*7 <= atvaltott_szam:
            kilences_szamrenszer += "7"
            atvaltott_szam -= 9**i*7

        elif 9**i*6 <= atvaltott_szam:
            kilences_szamrenszer += "6"
            atvaltott_szam -= 9**i*6

        elif 9**i*5 <= atvaltott_szam:
            kilences_szamrenszer += "5"
            atvaltott_szam -= 9**i*5

        elif 9**i*4 <= atvaltott_szam:
            kilences_szamrenszer += "4"
            atvaltott_szam -= 9**i*4

        elif 9**i*3 <= atvaltott_szam:
            kilences_szamrenszer += "3"
            atvaltott_szam -= 9**i*3

        elif 9**i*2 <= atvaltott_szam:
            kilences_szamrenszer += "2"
            atvaltott_szam -= 9**i*2

        elif 9**i <= atvaltott_szam:
            kilences_szamrenszer += "1"
            atvaltott_szam -= 9**i
        else:
            kilences_szamrenszer += "0"
    print(f"Kilences számrendszerben lévő szám: {kilences_szamrenszer}\n")

def tizesbol_nyolcasba (atvaltott_szam):
    i = 0
    nyolcas_szamrenszer = ""

    while 8**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 8**i*7 <= atvaltott_szam:
            nyolcas_szamrenszer += "7"
            atvaltott_szam -= 8**i*7

        elif 8**i*6 <= atvaltott_szam:
            nyolcas_szamrenszer += "6"
            atvaltott_szam -= 8**i*6

        elif 8**i*5 <= atvaltott_szam:
            nyolcas_szamrenszer += "5"
            atvaltott_szam -= 8**i*5

        elif 8**i*4 <= atvaltott_szam:
            nyolcas_szamrenszer += "4"
            atvaltott_szam -= 8**i*4

        elif 8**i*3 <= atvaltott_szam:
            nyolcas_szamrenszer += "3"
            atvaltott_szam -= 8**i*3

        elif 8**i*2 <= atvaltott_szam:
            nyolcas_szamrenszer += "2"
            atvaltott_szam -= 8**i*2

        elif 8**i <= atvaltott_szam:
            nyolcas_szamrenszer += "1"
            atvaltott_szam -= 8**i
        else:
            nyolcas_szamrenszer += "0"
    print(f"Nyolcas számrendszerben lévő szám: {nyolcas_szamrenszer}\n")

def tizesbol_hetesbe (atvaltott_szam):
    i = 0
    hetes_szamrenszer = ""

    while 7**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 7**i*6 <= atvaltott_szam:
            hetes_szamrenszer += "6"
            atvaltott_szam -= 7**i*6

        elif 7**i*5 <= atvaltott_szam:
            hetes_szamrenszer += "5"
            atvaltott_szam -= 7**i*5

        elif 7**i*4 <= atvaltott_szam:
            hetes_szamrenszer += "4"
            atvaltott_szam -= 7**i*4

        elif 7**i*3 <= atvaltott_szam:
            hetes_szamrenszer += "3"
            atvaltott_szam -= 7**i*3

        elif 7**i*2 <= atvaltott_szam:
            hetes_szamrenszer += "2"
            atvaltott_szam -= 7**i*2

        elif 7**i <= atvaltott_szam:
            hetes_szamrenszer += "1"
            atvaltott_szam -= 7**i
        else:
            hetes_szamrenszer += "0"
    print(f"Hetes számrendszerben lévő szám: {hetes_szamrenszer}\n")

def tizesbol_hatosba (atvaltott_szam):
    i = 0
    hatos_szamrenszer = ""

    while 6**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 6**i*5 <= atvaltott_szam:
            hatos_szamrenszer += "5"
            atvaltott_szam -= 6**i*5

        elif 6**i*4 <= atvaltott_szam:
            hatos_szamrenszer += "4"
            atvaltott_szam -= 6**i*4

        elif 6**i*3 <= atvaltott_szam:
            hatos_szamrenszer += "3"
            atvaltott_szam -= 6**i*3

        elif 6**i*2 <= atvaltott_szam:
            hatos_szamrenszer += "2"
            atvaltott_szam -= 6**i*2

        elif 6**i <= atvaltott_szam:
            hatos_szamrenszer += "1"
            atvaltott_szam -= 6**i
        else:
            hatos_szamrenszer += "0"
    print(f"Hatos számrendszerben lévő szám: {hatos_szamrenszer}\n")

def tizesbol_otosbe (atvaltott_szam):
    i = 0
    otos_szamrendszer = ""

    while 5**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 5**i*4 <= atvaltott_szam:
            otos_szamrendszer += "4"
            atvaltott_szam -= 5**i*4

        elif 5**i*3 <= atvaltott_szam:
            otos_szamrendszer += "3"
            atvaltott_szam -= 5**i*3

        elif 5**i*2 <= atvaltott_szam:
            otos_szamrendszer += "2"
            atvaltott_szam -= 5**i*2

        elif 5**i <= atvaltott_szam:
            otos_szamrendszer += "1"
            atvaltott_szam -= 5**i
        else:
            otos_szamrendszer += "0"
    print(f"Ötös számrendszerben lévő szám: {otos_szamrendszer}\n")

def tizesbol_negyesbe (atvaltott_szam):
    i = 0
    negyes_szamrendszer = ""

    while 4**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 4**i*3 <= atvaltott_szam:
            negyes_szamrendszer += "3"
            atvaltott_szam -= 4**i*3

        elif 4**i*2 <= atvaltott_szam:
            negyes_szamrendszer += "2"
            atvaltott_szam -= 4**i*2

        elif 4**i <= atvaltott_szam:
            negyes_szamrendszer += "1"
            atvaltott_szam -= 4**i

        else:
            negyes_szamrendszer += "0"
    print(f"Négyes számrendszerben lévő szám: {negyes_szamrendszer}\n")

def tizesbol_harmasba (atvaltott_szam):
    i = 0
    harmas_szamrendszer = ""

    while 3**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 3**i*2 <= atvaltott_szam:
            harmas_szamrendszer += "2"
            atvaltott_szam -=  3**i*2

        elif 3**i <= atvaltott_szam:
            harmas_szamrendszer += "1"
            atvaltott_szam -=  3**i

        else:
            harmas_szamrendszer += "0"
    print(f"Hármas számrendszerben lévő szám: {harmas_szamrendszer}\n")

def tizesbol_kettesbe (atvaltott_szam):
    i = 0
    binaris_szam = ""

    while 2**i <= atvaltott_szam:
        i += 1

    while i != 0:
        i -= 1
        if 2**i <= atvaltott_szam:
            binaris_szam += "1"
            atvaltott_szam -= 2**i

        else:
            binaris_szam += "0"
    print(f"Kettes számrendszerben lévő szám {binaris_szam}\n")

#--------------------------------------------- Tizes számrendszerbe való átváltások --------------------------------------------- 

def kettesbol_tizesbe ():
    binaris_szam = ""
    szam = 0
    i = 0
    while i < 10:
        binaris_szam += str(random.randint(0,1))
        i+= 1
    print(f"\nKettes számrendszerben lévő szám: {binaris_szam}\n")

    i = 0
    while i <= len(binaris_szam)-1:
        if binaris_szam[len(binaris_szam)-1-i] == "1":
            szam += 2**i
        i += 1
    return szam
    
def harmasbol_tizesbe ():
    harmas = ""
    szam = 0
    i = 0
    while i < 10:
        harmas += str(random.randint(0,2))
        i+= 1
    print(f"\nHármas számrendszerben lévő szám: {harmas}\n")

    i = 0
    while i <= len(harmas)-1:
        if harmas[len(harmas)-1-i] == "2":
            szam += 3**i*2
        elif harmas[len(harmas)-1-i] == "1":
            szam += 3**i
        i += 1
    return szam

def negyesbol_tizesbe ():
    negyes = ""
    szam = 0
    i = 0
    while i < 10:
        negyes += str(random.randint(0,3))
        i+= 1
    print(f"\nNégyes számrendszerben lévő szám: {negyes}\n")

    i = 0
    while i <= len(negyes)-1:
        if negyes[len(negyes)-1-i] == "3":
            szam += 4**i*3
        elif negyes[len(negyes)-1-i] == "2":
            szam += 4**i*2
        elif negyes[len(negyes)-1-i] == "1":
            szam += 4**i
        i += 1
    return szam

def otosbol_tizesbe():
    otos = ""
    szam = 0
    i = 0
    while i < 10:
        otos += str(random.randint(0,4))
        i+= 1
    print(f"\nÖtös számrendszerben lévő szám: {otos}\n")

    i = 0
    while i <= len(otos)-1:
        if otos[len(otos)-1-i] == "4":
            szam += 5**i*4
        elif otos[len(otos)-1-i] == "3":
            szam += 5**i*3
        elif otos[len(otos)-1-i] == "2":
            szam += 5**i*2
        elif otos[len(otos)-1-i] == "1":
            szam += 5**i
        i += 1
    return szam

def hatosbol_tizesbe():
    hatos = ""
    szam = 0
    i = 0
    while i < 10:
        hatos += str(random.randint(0,5))
        i+= 1
    print(f"\nHatos számrendszerben lévő szám: {hatos}\n")

    i = 0
    while i <= len(hatos)-1:
        if hatos[len(hatos)-1-i] == "5":
            szam += 6**i*5
        elif hatos[len(hatos)-1-i] == "4":
            szam += 6**i*4
        elif hatos[len(hatos)-1-i] == "3":
            szam += 6**i*3
        elif hatos[len(hatos)-1-i] == "2":
            szam += 6**i*2
        elif hatos[len(hatos)-1-i] == "1":
            szam += 6**i
        i += 1
    return szam

def hetesbol_tizesbe():
    hetes = ""
    szam = 0
    i = 0
    while i < 10:
        hetes += str(random.randint(0,6))
        i+= 1
    print(f"\nHetes számrendszerben lévő szám: {hetes}\n")

    i = 0
    while i <= len(hetes)-1:
        if hetes[len(hetes)-1-i] == "6":
            szam += 7**i*6
        elif hetes[len(hetes)-1-i] == "5":
            szam += 7**i*5
        elif hetes[len(hetes)-1-i] == "4":
            szam += 7**i*4
        elif hetes[len(hetes)-1-i] == "3":
            szam += 7**i*3
        elif hetes[len(hetes)-1-i] == "2":
            szam += 7**i*2
        elif hetes[len(hetes)-1-i] == "1":
            szam += 7**i
        i += 1
    return szam

def nyolcasbol_tizesbe():
    nyolcas = ""
    szam = 0
    i = 0
    while i < 10:
        nyolcas += str(random.randint(0,7))
        i+= 1
    print(f"\nNyolcas számrendszerrben lévő szám: {nyolcas}\n")

    i = 0
    while i <= len(nyolcas)-1:
        if nyolcas[len(nyolcas)-1-i] == "7":
            szam += 8**i*7
        elif nyolcas[len(nyolcas)-1-i] == "6":
            szam += 8**i*6
        elif nyolcas[len(nyolcas)-1-i] == "5":
            szam += 8**i*5
        elif nyolcas[len(nyolcas)-1-i] == "4":
            szam += 8**i*4
        elif nyolcas[len(nyolcas)-1-i] == "3":
            szam += 8**i*3
        elif nyolcas[len(nyolcas)-1-i] == "2":
            szam += 8**i*2
        elif nyolcas[len(nyolcas)-1-i] == "1":
            szam += 8**i
        i += 1
    return szam

def kilencesbol_tizesbe():
    kilences = ""
    szam = 0
    i = 0
    while i < 10:
        kilences += str(random.randint(0,8))
        i+= 1
    print(f"\nKilences számrendszerrben lévő szám: {kilences}\n")

    i = 0
    while i <= len(kilences)-1:
        if kilences[len(kilences)-1-i] == "8":
            szam += 9**i*8
        elif kilences[len(kilences)-1-i] == "7":
            szam += 9**i*7
        elif kilences[len(kilences)-1-i] == "6":
            szam += 9**i*6
        elif kilences[len(kilences)-1-i] == "5":
            szam += 9**i*5
        elif kilences[len(kilences)-1-i] == "4":
            szam += 9**i*4
        elif kilences[len(kilences)-1-i] == "3":
            szam += 9**i*3
        elif kilences[len(kilences)-1-i] == "2":
            szam += 9**i*2
        elif kilences[len(kilences)-1-i] == "1":
            szam += 9**i
        i += 1
    return szam

#--------------------------------------------- Átváltás --------------------------------------------- 

if alap_szamrendszer == 2:
    if cel_szamrendszer == 3:
        tizesbol_harmasba(kettesbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(kettesbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(kettesbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(kettesbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(kettesbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(kettesbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(kettesbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {kettesbol_tizesbe()}")

elif alap_szamrendszer == 3:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(harmasbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(harmasbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(harmasbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(harmasbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(harmasbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(harmasbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(harmasbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {harmasbol_tizesbe()}")

elif alap_szamrendszer == 4:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(negyesbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(negyesbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(negyesbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(negyesbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(negyesbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(negyesbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(negyesbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {negyesbol_tizesbe()}")

elif alap_szamrendszer == 5:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(otosbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(otosbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(otosbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(otosbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(otosbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(otosbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(otosbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {otosbol_tizesbe()}")

elif alap_szamrendszer == 6:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(hatosbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(hatosbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(hatosbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(hatosbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(hatosbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(hatosbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(hatosbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {hatosbol_tizesbe()}")

elif alap_szamrendszer == 7:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(hetesbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(hetesbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(hetesbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(hetesbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(hetesbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(hetesbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(hetesbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {hetesbol_tizesbe()}")

elif alap_szamrendszer == 8:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(nyolcasbol_tizesbe())
    elif cel_szamrendszer == 9:
        tizesbol_kilencesbe(nyolcasbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {nyolcasbol_tizesbe()}")

elif alap_szamrendszer == 9:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe(kilencesbol_tizesbe())
    elif cel_szamrendszer == 3:
        tizesbol_harmasba(kilencesbol_tizesbe())
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe(kilencesbol_tizesbe())
    elif cel_szamrendszer == 5:
        tizesbol_otosbe(kilencesbol_tizesbe())
    elif cel_szamrendszer == 6:
        tizesbol_hatosba(kilencesbol_tizesbe())
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe(kilencesbol_tizesbe())
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba(kilencesbol_tizesbe())
    else:
        print(f"Tizes számrendszerben lévő szám: {kilencesbol_tizesbe()}")

else:
    if cel_szamrendszer == 2:
        tizesbol_kettesbe()
    elif cel_szamrendszer == 3:
        tizesbol_harmasba()
    elif cel_szamrendszer == 4:
        tizesbol_negyesbe()
    elif cel_szamrendszer == 5:
        tizesbol_otosbe()
    elif cel_szamrendszer == 6:
        tizesbol_hatosba()
    elif cel_szamrendszer == 7:
        tizesbol_hetesbe()
    elif cel_szamrendszer == 8:
        tizesbol_nyolcasba()
    else:
        tizesbol_kilencesbe()