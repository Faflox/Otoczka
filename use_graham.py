from graham import graham

##
# Tutaj wprowadź punkty do otoczki
punkty_do_otoczki = [(0.5,17), (2,3), (102,6), (3,12), (3,5), (3.5, 8)]
# Jeśli nie chcesz opisu wyników oraz wykresu, zmień ich wartości na False
##

punkty_otoczki = graham(punkty_do_otoczki, opis=True, wykres=True)
