def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fehler: Division durch Null ist nicht erlaubt"
    else:
        return x / y

print("Willkommen zum einfachen Taschenrechner!")
print("Wähle eine Operation:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

choice = input("Gib die Nummer der Operation ein (1/2/3/4): ")

num1 = float(input("Gib die erste Zahl ein: "))
num2 = float(input("Gib die zweite Zahl ein: "))

if choice == '1':
    print("Ergebnis:", add(num1, num2))
elif choice == '2':
    print("Ergebnis:", subtract(num1, num2))
elif choice == '3':
    print("Ergebnis:", multiply(num1, num2))
elif choice == '4':
    print("Ergebnis:", divide(num1, num2))
else:
    print("Ungültige Eingabe")
