
preces={'abols':1,'kvass':2.5,'siers':4,'teto':30}
x=input("Izveleties precu: abols, kvass, siers vai teto \n")
def calculate(a):
    grozs=0
    if a in preces:
        skaits=int(input(f"ievadiet {a} skaitu: "))
        grozs=int(skaits*preces[a])
        print(grozs)
        restr=input("Vai jums ir vajadzigas citas preces? Ievadiet ja vai ne. \n")
        if restr == "ja":
            x=input("Izveleties precu: abols, kvass, siers vai teto \n")
            skaits=int(input(f"ievadiet {x} skaitu: "))
            grozs=int(grozs+skaits*preces[x])
            print(grozs)
            restr=input("Vai jums ir vajadzigas citas preces? Ievadiet ja vai ne. \n")
            if restr == "ja":
                x=input("Izveleties precu: abols, kvass, siers vai teto \n")
                skaits=int(input(f"ievadiet {x} skaitu: "))
                grozs=int(grozs+skaits*preces[x])
                print(grozs)
                restr=input("Vai jums ir vajadzigas citas preces? Ievadiet ja vai ne. \n")
            else:
                if grozs > 50:
                    grozs=grozs-grozs*0.1
                    print(f"Groza summa ir {grozs}")
                else:
                    print(f"Groza summa ir {grozs}")

                if restr == "ja":
                    x=input("Izveleties precu: abols, kvass, siers vai teto \n")
                    skaits=int(input(f"ievadiet {x} skaitu: "))
                    grozs=int(grozs+skaits*preces[x])
                    print(grozs)
                    if grozs > 50:
                        grozs=grozs-grozs*0.1
                        print(f"Groza summa ir {grozs}")
                    else:
                        print(f"Groza summa ir {grozs}")
        else:
            if grozs > 50:
                grozs=grozs-grozs*0.1
                print(f"Groza summa ir {grozs}")
            else:
                print(f"Groza summa ir {grozs}")
            
calculate(x)
