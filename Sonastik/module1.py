from random import*

def Loe_failist(fail:str)->str:
    fail=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in fail:
        jarjend.append(rida.strip()) 
    fail.close()
    return jarjend 

def Lisa_sõna(fail1:str,fail2:str):
    eng=[]
    rus=[]
    fail=open(fail1,"r",encoding="utf-8-sig")
    for rida in fail:
        eng.append(rida.strip())
    fail.close()
    fail=open(fail2,"r",encoding="utf-8-sig")
    for rida in fail:
        rus.append(rida.strip())
    fail.close()
    sõnastiku_keel=input("Mis keeles soovite selle sõna lisada? eng või rus: ")
    while sõnastiku_keel=="eng" or "rus":
        sõna=input("Lisa sõna: ")
        sõna_tõlk=input("Mis seda sõna tähendab: ")
        if sõnastiku_keel=="rus":
            fail=open(fail1,"a",encoding="utf-8-sig")
            fail.write(sõna+"\n")
            fail.close
            fail=open(fail2,"a",encoding="utf-8-sig")
            fail.write(sõna_tõlk+"\n")
            fail.close
        elif sõnastiku_keel=="eng":
            fail=open(fail2,"a",encoding="utf-8-sig")
            fail.write(sõna+"\n")
            fail.close
            fail=open(fail1,"a",encoding="utf-8-sig")
            fail.write(sõna_tõlk+"\n")
            fail.close
        else:
            sõnastiku_keel=input("Mis keeles soovite selle sõna lisada? eng või rus: ")
        return eng,rus

def Tõlk(fail1:str,fail2:str):
    eng=[]
    rus=[]
    fail=open(fail1,"r",encoding="utf-8-sig")
    for rida in fail:
        rus.append(rida.strip())
    fail.close()
    fail=open(fail2,"r",encoding="utf-8-sig")
    for rida in fail:
        eng.append(rida.strip())
    fail.close()
    sõna=input("Kirjutage sõna, mida soovite tõlkida: ")
    while sõna.isdigit():
        sõna=input("Kirjutage õige sõna: ")
    if sõna not in rus and sõna not in eng:
        print("Seda sõna pole sõnastikus: ")
    for i in range(len(rus)):
        if sõna==rus[i]:
            print(f'{rus[i]} - {eng[i]}')
        elif sõna==eng[i]:
            print(f'{eng[i]} - {rus[i]}')


def Paranda(fail1:str,fail2:str):
    eng=[]
    rus=[]
    fail=open(fail1,"r",encoding="utf-8-sig")
    for rida in fail:
        rus.append(rida.strip())
    fail.close()
    fail=open(fail2,"r",encoding="utf-8-sig")
    for rida in fail:
        eng.append(rida.strip())
    fail.close()
    sõnastiku_keel=input("Millises sõnastikus me sõna parandame? eng või rus: ")
    while sõnastiku_keel not in ["rus","eng"]:
        sõnastiku_keel=input("Millises sõnastikus me sõna parandame? eng või rus: ")
    if sõnastiku_keel=="rus":
        sõna=input("Millist sõna soovite parandada? ")
        while sõna not in rus:
            sõna=input("Kirjutage õige sõna: ")
        for i in range(len(rus)):
            if sõna==rus[i]:
                ind=rus.index(sõna) 
        paranda_sõna=input("Kirjutage parandatud sõna: ")
        while paranda_sõna.isdigit():
            paranda_sõna=input("Kirjutage õige sõna: ")
        rus[ind]=paranda_sõna
        for i in range(len(rus)):
            rus[i]=rus[i]+"\n"
        fail=open(fail1,"w",encoding="utf-8-sig")
        fail.writelines(rus)
        fail.close()
    elif sõnastiku_keel=="eng":
        sõna=input("Millist sõna soovite parandada? ")
        while sõna not in eng:
            sõna=input("Kirjutage õige sõna: ")
        for i in range(len(eng)):
            if sõna==eng[i]:
                ind=eng.index(sõna)
        paranda_sõna=input("Kirjutage parandatud sõna: ")
        while paranda_sõna.isdigit():
            paranda_sõna=input("Kirjutage õige sõna: ")
        eng[ind]=paranda_sõna
        for i in range(len(eng)):
            eng[i]=eng[i]+"\n"
        fail=open(fail2,"w",encoding="utf-8-sig")
        fail.writelines(eng)
        fail.close()

def test(fail1:str,fail2:str):
    eng=[]
    rus=[]
    test=[]
    s=[]
    v=k=0
    fail=open(fail1,"r",encoding="utf-8-sig")
    for rida in fail:
        rus.append(rida.strip())
    fail.close()
    fail=open(fail2,"r",encoding="utf-8-sig")
    for rida in fail:
        eng.append(rida.strip())
    fail.close()
    v=int(input("Kui mitu korda? "))
    for i in range(v):
        num=randint(0,(len(rus)-1))
        while num in s:
            num=randint(0,(len(rus)-1))
        sõnastiku_keel=input("Millisest sõnastikust me testime? eng või rus: ")
        while sõnastiku_keel not in ("rus","eng"):
            sõnastiku_keel=input("Mis keeles soovite sõnu näha? eng või rus: ")
        if sõnastiku_keel=="rus":
            game=rus[num] 
            tõlk=input(f"Sõna tõlge {game}: ")
            if tõlk==eng[num]:
                test.append(f"{i+1} {sõnastiku_keel} mäng - võit")
                print("Võit") 
                v+=1
            else:
                test.append(f"{i+1}, {sõnastiku_keel} mäng - kaotus") 
                print("Kaotus")
                k+=1
        elif sõnastiku_keel=="eng":
            game=eng[num] 
            tõlk=input(f"Sõna tõlge {game}: ")
            if tõlk==rus[num]:
                test.append(f"{i+1} {sõnastiku_keel} mäng - võit")
                print("Võit") 
                v+=1
            else:
                test.append(f"{i+1}, {sõnastiku_keel} mäng - kaotus") 
                print("Kaotus")
                k+=1
        s.append(num)
    print()
    print(test)
    if k==0:
        resÕ=100
        resV=0
    elif v==0:
        resÕ=0
        resV=100
    else:
        resÕ=round((v/i)*100),1
        resV=round((k/i)*100),1
    print(f"Võiduprotsent - {resÕ}%")
    print(f"Kaotusprotsent - {resV}%")