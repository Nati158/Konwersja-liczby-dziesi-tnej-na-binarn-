def dziesietna_na_binarna(liczba):
    if liczba == 0:
        return "0"
    binarna = ""
    while liczba > 0:
        reszta = liczba % 2
        binarna = str(reszta) + binarna
        liczba //= 2
    return binarna

liczba = int(input("Podaj liczbę dziesiętną: "))
binarna = dziesietna_na_binarna(liczba)
print("Liczba binarna:", binarna)
