'''\nProsta aplikacja do tworzenia rejestru ksiazek w domowej biblioteczce/ ver. 1.0\n'''

from ksiazka import Ksiazka
from regal import Regal

def dodaj():
    autor = input("Podaj autora: ")
    tytul = input("Podaj tytuł: ")
    oprawa = input("Podaj rodzaj oprawy: ")
    isbn = int(input('Podaj numer isbn: '))
    liczba_stron = int(input('Podaj liczbe stron: '))
    stan = input('Czy wypozyczona? (tak/nie): ')
    regal= input('Podaj regal: ')
    miejsce = input('Podaj miejsce: ')
    lokalizacja = Regal(regal,miejsce)

    nowa_ksiazka = Ksiazka(autor, tytul, oprawa, isbn, liczba_stron, stan)
    return [nowa_ksiazka.autor, nowa_ksiazka.tytul, nowa_ksiazka.oprawa,
            nowa_ksiazka.isbn, nowa_ksiazka.stan, f"{lokalizacja.regal} {lokalizacja.miejsce}"]