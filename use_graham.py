from graham import graham

##
# Tutaj wprowadź punkty do otoczki
punkty_do_otoczki = [(7,10), (12,0), (5, 2), (-2,1)]
# Jeśli nie chcesz opisu wyników oraz wykresu, zmień ich wartości na False 2.71
##

graham(punkty_do_otoczki, opis=True, wykres=True)
# otoczka = graham(punkty_do_otoczki, opis=False, wykres=False)
# print(otoczka)