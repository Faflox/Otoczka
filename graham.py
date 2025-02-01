import os
import math
import matplotlib.pyplot as plt
from typing import List, Tuple
from datetime import datetime

def graham(punkty: List[Tuple[float, float]], opis:bool=1, wykres:bool=1) -> List[Tuple[float, float]]:
    """
    Funkcja tworzy otoczkę wypukłą na płaszczyźnie na podstawie przekazanych do niej punktów.
    Args:
        punkty (list): punkty muszą zostać opisane przez krotki ze współrzędnymi x i y

    Returns:
        list: Zwraca listę punktów tworzącą otoczkę na liście początkowych punktów
    """
    punkty = wyczysc_dane(punkty)
    start = min(punkty, key=lambda p: (p[1], p[0]))

    def wielkosc_kąta(punkt):
        return math.atan2(punkt[1] - start[1], punkt[0] - start[0])

    def odleglosc(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    punkty.sort(key=lambda punkt: (wielkosc_kąta(punkt), odleglosc(start, punkt)))
    otoczka = stworz_otoczke(punkty)
    if opis == 1:
        print(opisz_wynik(otoczka))
    if wykres == 1:
        narysuj(punkty, otoczka)
    return otoczka

def stworz_otoczke(punkty: List) -> List:
    """Funkcja pomocniczna dla funkcji graham. 
    Korzysta z iloczynu wektorowego dla 3 kolejnych punktów w celu określenia prawoskrętności.
    Jeśli iloczyn wektorowy < 0 to usuwamy punkt środkowy.

    Args:
        punkty (List): posortowana i wyczyszczona lista punktów.

    Returns:
        List: Zwraca listę punktów wymaganych do stworzenia otoczki.
    """
    if len(punkty) <= 2:
        return punkty

    otoczka = []
    for punkt in punkty:
        while len(otoczka) > 1: 
            p1, p2 = otoczka[-2], otoczka[-1]
            # iloczyn wektorowy dla 3 pkt:
            # tworzy 2 wektory 
            # (x = p2 - p1) * (y = sprawdzany pkt - p2) -
            # (y = p2 - p1) * (x = sprawdzany pkt - p2)
            # Jeśli wynik jest ujemny, oznacza to prawy skręt, więc usuń p2.
            wektor1 = (p2[0] - p1[0]) * (punkt[1] - p2[1])
            wektor2 = (p2[1] - p1[1]) * (punkt[0] - p2[0])
            iloczyn_wektorowy = wektor1 - wektor2
            if iloczyn_wektorowy >= 0:
                break
            otoczka.pop()
        otoczka.append(punkt)
    return otoczka

def wyczysc_dane(punkty: List) -> List:
    #czyści dane w przypadku podania więcej niz raz tego samego punktu
    #sprawdza poprawność typu danych 
    if not isinstance(punkty, list):
        raise ValueError('Błędny typ danych. Podaj listę punktów o współrzędnych (x, y).')
    
    if not punkty:
        raise ValueError('Lista punktów jest pusta.')
    
    punkty = list(set(punkty))
    for punkt in punkty:
        if not (isinstance(punkt, tuple) and len(punkt) == 2 and
                all(isinstance(wspolrzedne, (int, float)) for wspolrzedne in punkt)):
            raise ValueError(f'Niepoprawny element: {punkt}')
    return punkty

def opisz_wynik(otoczka: List) -> str:
    odpowiedź = 'Otoczką wypukłą jest: '
    if len(otoczka) == 1:
        odpowiedź += 'Punkt\n'
    elif len(otoczka) == 2:
        odpowiedź += 'Odcinek\n'
    else:
        odpowiedź += f'{len(otoczka)}-kąt\n'
    odpowiedź += 'o współrzędnych: ' + ', '.join(f'{punkt}' for punkt in otoczka)
    return odpowiedź

def narysuj(punkty: List, otoczka: List):
    x, y = zip(*punkty)
    plt.scatter(x, y, color='blue')

    if len(otoczka) > 1:
        otoczka_zamknieta = otoczka + [otoczka[0]]
        x_otoczka, y_otoczka = zip(*otoczka_zamknieta)
        plt.plot(x_otoczka, y_otoczka, color='red')

    for px, py in punkty:
        plt.text(px, py, f'({px}, {py})', fontsize=9, ha='right')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Otoczka wypukła')
    plt.grid()
    if not os.path.exists('wykresy'):
        os.makedirs('wykresy')
        
    teraz = datetime.now()
    nazwa = f'otoczka-{teraz.strftime("%Y-%m-%d-%H-%M")}'
    sciezka = os.path.join('wykresy', nazwa + '.png')
    
    numer = 1
    while os.path.exists(sciezka):
        sciezka = os.path.join('wykresy', f'{nazwa}-{numer}.png')
        numer += 1
    
    plt.savefig(sciezka)
    plt.close()


