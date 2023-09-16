while True:
    szam_str = input("adj meg egy szamot")
    if szam_str.isdecimal():
        szam = int(szam_str)
        break
if szam > 3:
    print("nagyobb")
elif szam < 3:
    print("kisebb")
    
print("2023.09.16")