def kiir(str):
    print(str)

kiir(5)
kiir("szia")

def g_fv(x,y,z):
    return x*x+y+z/2

x = g_fv(5,3,4)

kiir(x)
print("\n")

l1 = [1,3,5,7]
l2 = [7,2,9]
l3 = [6,3,0,4]

def lista_osszeg(lista):
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return(osszeg)


lista_osszeg(l1)
lista_osszeg(l2)
lista_osszeg(l3)

def lista_atlag(lista):
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return osszeg/len(lista)

print(lista_atlag(l1))
print(lista_atlag(l2))
print(lista_atlag(l3))

def lista_atlag(lista):
    summ = lista_osszeg(lista)
    return summ/len(lista)

print(lista_atlag(l1))
print(lista_atlag(l2))
print(lista_atlag(l3))

print("1.összeadás")
print("2.osszeszorzás")
print("3.átlag")

menupontod = int(input("add meg a menu pontod: "))

def f(elso, masodik):
    if menupontod == 1:
        print(elso + masodik) 
    elif menupontod == 2:
        print(elso * masodik) 
    else:
        print((elso + masodik)/2) 
    
f(int(input("adj meg egy számot")),int(input("adj meg egy számot")))

def szamok_beker():
    sz1 = int(input("adj meg egy számot"))
    sz2 = int(input("adj meg egy számot"))
    return(sz1, sz2)
y, z =  szamok_beker()
print(y,z)

gy = ["alma", "citrom", "barack", "pomelo"]

def nagybetusit(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista
print(gy)
print(nagybetusit(gy[:]))
print(gy)


d3 = {"név": "dobostorta", "szeletek": 12, "elfogyott": False}
print(d3["név"])