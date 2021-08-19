try:
    basic = int(input("podaj podstawę: "))
    silnia = 1
    for x in range(2,basic+1):
        silnia = silnia * x
    print(silnia)
except:
    print("Nieprawidłowa wartość!!!")