# Hra piškvorky

# Funkce vyhodnoť - dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec, podle stavu hry. 
# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)




def vyhodnot (pole):
    """Funkce dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec, podle stavu hry"""
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

print(vyhodnot("xoxoxxoxoxoxoxoxo"))




#Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

def tah (pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    pozice = 0
    # for cyklus prochází postupně jednotlivá políčka pole od pozice nula. Pokud se při procházení pozice rovná cislu policka, pak vyskoci z funkce a vrátí nové pole se zapsaným symbolem na dané pozici" 
    for i in pole:
        print(pozice)
        if pozice == cislo_policka:
            nove_pole = pole[:cislo_policka] + symbol + pole[cislo_policka+1 :]
            return(nove_pole)
        else:
            pozice = pozice + 1 
            print(pozice)



print(tah("---xo--", 0, "x"))
print(tah("---xo--", 3, "o"))       # ve fci není ošetřeno, jestli je políčko volné. Takže tento tah přepíše "x" na "o". Bude řešeno
