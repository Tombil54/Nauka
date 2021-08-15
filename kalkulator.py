x = int(input("Podaj pierwszy argument: "))
y = int(input("Podaj drugi argument: "))
z = input("Podaj operator (+,-,*,/,**) ")
operatory = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}
if z == "+":
    print(operatory["+"])
elif z == "-":
    print(operatory["-"])
elif z == "*":
    print(operatory["*"])
elif z == "/":
    print(operatory["/"])
elif z == "**":
    print(operatory["**"])
else:
    print("Błąd: nie ma takiego operatora)")