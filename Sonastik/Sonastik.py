from module1 import *

laused=[]

while True:
    v=int(input("1 Loe failist\n2 Lisa sõna\n3 Sõnade tõlkimine\n4 Parandage viga sõnastikus\n5 Test\n"))
    if v==1:
        sõnastiku_keel=input("Mis keeles soovite sõnu näha? eng või rus: ")
        while sõnastiku_keel=="eng" or "rus":
            if sõnastiku_keel=="rus":
                laused=Loe_failist("rus.txt")
                for line in laused:
                    print(line)
                break
            elif sõnastiku_keel=="eng":
                laused=Loe_failist("eng.txt")
                for line in laused:
                    print(line)
                break
            else:
                sõnastiku_keel=input("Mis keeles soovite sõnu näha? eng või rus: ")
    elif v==2:
        Lisa_sõna("rus.txt","eng.txt")
    elif v==3:
        Tõlk("rus.txt","eng.txt")
    elif v==4:
        Paranda("rus.txt","eng.txt")
    elif v==5:
        test("rus.txt","eng.txt")