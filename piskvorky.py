# Hra piškvorky

# Funkce vyhodnoť - dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec, podle stavu hry. 
# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)


def vyhodnot (pole):
    """Funkce dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec, podle stavu hry"""
    if "xxx" in pole:   # vitez "x"
        return "x"
    elif "ooo" in pole: # vitez "o"
        return "o"
    elif "-" not in pole:   # remíza
        return "!"
    else:   # ani jedna ze situací výše
        return "-"

print(vyhodnot("xoxxoooxoxo-oxoxo"))
