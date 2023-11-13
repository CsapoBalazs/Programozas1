
def fejlec (cim):
    szeleseg = 30
    csillagok = "*"*szeleseg
    kozepso_csillag = "*"*int((szeleseg-len(cim)/2))
    print(csillagok*2)
    print(kozepso_csillag+cim+kozepso_csillag)
    print(csillagok*2)
#program_neve = " Programcíme "
#fejlec(program_neve)
#
#teszt=""
#for i in range(2,20):
#    teszt += "C"
#    fejlec(teszt)

x = 11_123_321
print(x+1)

print(0o123)#8-as számrendszer
print(0xABBA)#16os számendszer
print(0b11000000)#2es számrendszer

x = int("345", 36)#tetszőleges számrendszerből váltás 10-esbe
print(x)

x = oct(321)
print(x)

x = hex(4096)# váltás 16-os szr-be 
print(x)

x = bin(192)#Váltás 2-es szr-be
print(x)

print(1/100000000)#1e-08

str = 'Anya azt mondta hogy : "Érj haza időben!"'
print(str)
str = "Anya azt mondta hogy : \"Érj haza időben!\""

x = 6/4 # 1.5
y = 6//4 # 1
y = 6//-4# -2
z =  6%4 # 2

print(9%6%2) # 1