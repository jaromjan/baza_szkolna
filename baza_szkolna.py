# Program do obsługi bazy szkolnej
# dane bedziemy umieszczac w trzech slownikach
uczniowie = {}
nauczyciele = {}
wychowawcy = {}
# zastosujemy liczby jako identyfikatory w slownikach, bo imiona i nazwiska moga sie powtarzac


def dodaj_ucznia():
    imie_nazwisko = input("Podaj imie_nazwisko: ")
    klasa = input("Podaj klase: ")
    if imie_nazwisko == '' or klasa == '':
        print(f"Nie dodano - wadliwe dane ucznia")
        return False
    else:
        idx = len(uczniowie)
        uczniowie[idx] = [idx, imie_nazwisko, klasa]
        print(f"Dodano ucznia {imie_nazwisko} do klasy {klasa}")
        return uczniowie


def dodaj_wychowawce():
    imie_nazwisko = input("Podaj imie_nazwisko: ")
    klasa = input("Podaj klase: ")
    if imie_nazwisko == '' or klasa == '':
        print(f"Nie dodano - wadliwe dane wychowawcy")
        return False
    else:
        idx = len(wychowawcy)
        wychowawcy[idx] = [idx, imie_nazwisko, klasa]
        print(f"Dodano wychowawce {imie_nazwisko} klasy {klasa}")
        return wychowawcy


def dodaj_nauczyciela():
    imie_nazwisko = input("Podaj imie_nazwisko: ")
    przedmiot = input("Podaj przedmiot: ")
    klasy = input("Podaj pierwsza klase w której uczy: ")
    if klasy:
        klasy = klasy + '',
    while True:
        klasa1 = input("Podaj kolejna klase w której uczy(pusta-koniec): ")
        if klasa1:
            if klasa1:
                klasa1 = klasa1 + '',
            klasy = klasy + klasa1
        else:
            break
        continue
    if imie_nazwisko == '' or przedmiot == '' or klasy == '':
        print(f"Nie dodano - wadliwe dane nauczyciela")
        return False
    else:
        idx = len(nauczyciele)
        nauczyciele[idx] = [idx, imie_nazwisko, przedmiot, klasy]
        print(f"Dodano nauczyciela {imie_nazwisko} przedmiotu {przedmiot} uczacego w klasach {klasy}")
        return nauczyciele


def prezentuj_klase():
    klasa2 = input("Podaj oznaczenie klasy: ")
    if klasa2 == '':
        print(f"Operacja niemozliwa - podano pusta wartosc")
        return False
    kontrolka = 0
    print(f"Klasa: {klasa2}")
    for x in wychowawcy:
        if wychowawcy[x][2] == klasa2:
            print(f"Wychowawca: {wychowawcy[x][1]}")
            kontrolka = 1
    if kontrolka == 0:
        print("Nie okreslono wychowawcy dla podanej klasy")
    kontrolka = 0
    for i in uczniowie:
        if uczniowie[i][2] == klasa2:
            print(f"Uczen: {uczniowie[i][1]}")
            kontrolka = 1
    if kontrolka == 0:
        print("Do podanej klasy nie przypisano uczniow")
    return True


def prezentuj_ucznia():
    uczen2 = input("Podaj imie i nazwisko ucznia: ")
    if uczen2 == '':
        print(f"Operacja niemozliwa - podano pusta wartosc")
        return False
    kontrolna = 0
    kontrolka = 0
    print(f"Podano imie i nazwisko ucznia: {uczen2}")
    for x in uczniowie:
        if uczniowie[x][1] == uczen2:
            print(f"Uczen: {uczniowie[x][1]}")
            kl = uczniowie[x][2]
            kontrolna = 1
    if kontrolna == 0:
        print("Nie odnaleziono podanego ucznia")
        return False
    elif kontrolna == 1:
        for i in nauczyciele:
            if kl in nauczyciele[i][3]:
                print(f"Nauczyciel: {nauczyciele[i][1]} przedmiot: {nauczyciele[i][2]}")
                kontrolka = 1
        if kontrolka == 0:
            print("Do podanego ucznia nie przypisano nauczycieli")
    return True


def prezentuj_nauczyciela():
    nauczyciel2 = input("Podaj imie i nazwisko nauczyciela: ")
    if nauczyciel2 == '':
        print(f"Operacja niemozliwa - podano pusta wartosc")
        return False
    kontrolna1 = 0
#    kontrolna2 = 0
    print(f"Podano imie i nazwisko nauczyciela: {nauczyciel2}")
    for i in nauczyciele:
        if nauczyciele[i][1] == nauczyciel2:
            print(f"Nauczyciel: {nauczyciele[i][1]} przedmiot: {nauczyciele[i][2]} klasy: {nauczyciele[i][3]}")
            k = nauczyciele[i][0]
            kontrolna1 = 1
    if kontrolna1 == 0:
        print("Nie odnaleziono podanego nauczyciela")
        return False
    elif kontrolna1 == 1:
        for n in nauczyciele[k][3]:
            print(f"Lista uczniow klasy {n} :")
            kontrolna2 = 1
            for m in uczniowie:
                if n == uczniowie[m][2]:
                    print(uczniowie[m])
                    kontrolna2 = 0
            if kontrolna2 == 1:
                print(f"Brak uczniow w klasie")


def prezentuj_wychowawce():
    wychowawca2 = input("Podaj imie i nazwisko wychowawcy: ")
    if wychowawca2 == '':
        print(f"Operacja niemozliwa - podano pusta wartosc")
        return False
    kontrolna0 = 0
    kontrolka0 = 0
    print(f"Podano imie i nazwisko wychowawcy: {wychowawca2}")
    for x in wychowawcy:
        if wychowawcy[x][1] == wychowawca2:
            print(f"Wychowawca: {wychowawcy[x][1]}")
            wy = wychowawcy[x][2]
            kontrolna0 = 1
    if kontrolna0 == 0:
        print("Nie odnaleziono podanego wychowawcy")
        return False
    elif kontrolna0 == 1:
        for i in uczniowie:
            if wy in uczniowie[i][2]:
                print(f"Uczeń: {uczniowie[i][1]} klasa: {uczniowie[i][2]}")
                kontrolka0 = 1
        if kontrolka0 == 0:
            print("Do podanego wychowawcy nie przypisano uczniow")
    return True


# Menu glowne
dostepne_operacje = ['Utworz', 'Zarzadzaj', 'Koniec']
# pobieramy i weryfikujemy dostepnosc operacji
while True:
    while True:
        print(f"Dostepne operacje: {dostepne_operacje}")
        operacja = input("Podaj operacje: ")
        if operacja in dostepne_operacje:
            break
        else:
            print("Operacja z poza listy dostępnych operacji")
    # Menu Utworz
    if operacja == "Utworz":
        dostepne_utworz = ['Uczen', 'Nauczyciel', 'Wychowawca', 'Koniec']
        # Pobieramy i weryfikujemy dostepnosc operacji - po wykonaniu powrot do menu
        while True:
            while True:
                print(f"Dostepne operacje: {dostepne_utworz}")
                operacja_utworz = input("Podaj operacje: ")
                if operacja_utworz in dostepne_utworz:
                    break
                else:
                    print("Operacja z poza listy dostępnych operacji")
            if operacja_utworz == "Koniec":
                print("Powrot do menu glownego")
                break
            # wywolujemy funkcje obsługujaca nasz wybor
            if operacja_utworz == "Uczen":
                uczniowie = dodaj_ucznia()
            if operacja_utworz == "Nauczyciel":
                nauczyciele = dodaj_nauczyciela()
            if operacja_utworz == "Wychowawca":
                wychowawcy = dodaj_wychowawce()
    # Menu Zarzadzaj
    elif operacja == "Zarzadzaj":
        dostepne_zarzadzaj = ['Klasa', 'Uczen', 'Nauczyciel', 'Wychowawca', 'Koniec']
        # Pobieramy i weryfikujemy dostepnosc operacji - po wykonaniu powrot do menu
        while True:
            while True:
                print(f"Dostepne operacje: {dostepne_zarzadzaj}")
                operacja_zarzadzaj = input("Podaj operacje: ")
                if operacja_zarzadzaj in dostepne_zarzadzaj:
                    break
                else:
                    print("Operacja z poza listy dostępnych operacji")
            if operacja_zarzadzaj == "Koniec":
                print("Powrot do menu glownego")
                break
            # wywolujemy funkcje obslugujaca nasz wybor
            if operacja_zarzadzaj == "Klasa":
                prezentuj_klase()
            if operacja_zarzadzaj == "Uczen":
                prezentuj_ucznia()
            if operacja_zarzadzaj == "Nauczyciel":
                prezentuj_nauczyciela()
            if operacja_zarzadzaj == "Wychowawca":
                prezentuj_wychowawce()
    # Koniec - konczymy program
    elif operacja == "Koniec":
        print("Koniec programu")
        break
