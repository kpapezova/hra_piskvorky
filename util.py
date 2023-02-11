#Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

def tah (pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    pozice = 0
    # for cyklus prochází postupně jednotlivá políčka pole od pozice nula. Pokud se při procházení pozice rovná cislu policka, pak vyskoci z funkce a vrátí nové pole se zapsaným symbolem na dané pozici" 
    for i in pole:
        # tah v hernim poli
        if cislo_policka >= 0 and cislo_policka <= 19:
            pass
        else:
            raise ValueError(f"Zadaná pozice {cislo_policka} je mimo hrací pole")
        
        # tah na volne pole
        if pole[cislo_policka] == "-":
            pass
        else:
            raise ValueError(f"Pozice {cislo_policka} je obsazena")   

        # spravny symbol
        if symbol == "x" or symbol == "o":
            pass
        else:
            raise ValueError(f"Symbol by měl být 'x' nebo 'o'")

        # tah
        if pozice != cislo_policka:
                pozice = pozice + 1
        else:
            nove_pole = pole[:cislo_policka] + symbol + pole[cislo_policka+1 :]
            return(nove_pole)


print(tah("---xo---------------", 10, "x"))
print(tah("---xo---------------", 3, "o"))