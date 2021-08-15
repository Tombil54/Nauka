print("Kod działania\n1: dodawanie\n2: odejmowanie\n3: dzielenie\n4: mnożenie\n5: potęgowanie")
x = int(input("Podaj kod działania które chcesz wykonać: "))
if x == 1:
    print("wybrałeś dodawanie")
elif x == 2:
    print("wybrałeś odejmowanie")
elif x == 3:
    print("wybrałeś dzielenie")
elif x == 4:
    print("wybrałeś mnożenie")
elif x == 5:
    print("wybrałeś potęgowanie")
while x < 1 or x > 5:
    print("Wybrano nieprawidłowy kod: ", x)
    x = int(input("Kod działania to liczba w zakresie od 1 do 4. Podaj kod ponownie: "))
# while x > 1 and x < 4:
#     print("Wybrano kod: ", x)
# else:
#    print("Wpisałeś nieprawidłowy kod, działanie nie może zostać wykonane. Wpisz ponownie prawidłowy kod: ")
liczba1 = float(input("Podaj pierwszą liczbę (podstawę): "))
liczba2 = float(input("Podaj drugą liczbę (wykładnik): "))
if x == 1:
    print("wynik dodawania: ", liczba1 + liczba2)
elif x == 2:
    print("wynik odejmowania: ", liczba1 - liczba2)
elif x == 3:
    print("wynik dzielenia: ", liczba1 / liczba2)
elif x == 4:
    print("wynik mnożenia: ", liczba1 * liczba2)
elif x == 5:
    print("wynik potęgowania: ", liczba1 ** liczba2)