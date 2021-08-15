print("Kod działania\n1: dodawanie\n2: odejmowanie\n3: dzielenie\n4: mnożenie\n5: potęgowanie")
operation_code = int(input("Podaj kod działania które chcesz wykonać: "))
if operation_code == 1:
    print("wybrałeś dodawanie")
elif operation_code == 2:
    print("wybrałeś odejmowanie")
elif operation_code == 3:
    print("wybrałeś dzielenie")
elif operation_code == 4:
    print("wybrałeś mnożenie")
elif operation_code == 5:
    print("wybrałeś potęgowanie")
while operation_code < 1 or operation_code > 5:
    print("Wybrano nieprawidłowy kod: ", operation_code)
    operation_code = int(input("Kod działania to liczba w zakresie od 1 do 4. Podaj kod ponownie: "))
# while x > 1 and x < 4:
#     print("Wybrano kod: ", x)
# else:
#    print("Wpisałeś nieprawidłowy kod, działanie nie może zostać wykonane. Wpisz ponownie prawidłowy kod: ")
liczba1 = float(input("Podaj pierwszą liczbę (podstawę): "))
liczba2 = float(input("Podaj drugą liczbę (wykładnik): "))
if operation_code == 1:
    print("wynik dodawania: ", liczba1 + liczba2)
elif operation_code == 2:
    print("wynik odejmowania: ", liczba1 - liczba2)
elif operation_code == 3:
    print("wynik dzielenia: ", liczba1 / liczba2)
elif operation_code == 4:
    print("wynik mnożenia: ", liczba1 * liczba2)
elif operation_code == 5:
    print("wynik potęgowania: ", liczba1 ** liczba2)