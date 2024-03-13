from random import randint
import math

def zad1():
    a = [1 - x for x in range(1, 11)]
    b = [4 * x for x in range(8)]
    c = [x for x in b if x % 2 == 0]
    print(a,b,c)

def zad2():
    lista1 = []
    for i in range(10):
        lista1.append(randint(1, 1000))
    parzyste = [x for x in lista1 if x % 2 == 0]
    print(lista1, parzyste)


def zad3():
    produkty = {
        'jablka': 'kg',
        'mleko': 'litry',
        'chleb': 'sztuki',
        'pomidory': 'kg',
        'ziemniaki': 'kg'
    }
    produkty_sztuki = [p[0] for p in produkty.items() if p[1] == 'sztuki']
    print(produkty_sztuki)

def zad4(a,b,c):
    if (a**2 +b**2) == c**2:
        print("Jest trojkatny")
        return
    if (a**2 +c**2) == b**2:
        print("Jest trojkatny")
        return
    if (b**2 + c**2) == a**2:
        print("Jest trojkatny")
        return
    print("Nie jest trojkatny")


def zad5(a=3, b=5, h=3):
    print("Pole trapezu wynosi", (a+b)*h/2)


def zad6(a=1, b=4, ile=10):
    iloczyn = 1
    for i in range(1,ile):
        iloczyn = iloczyn * a * b**i
    print(iloczyn)

def zad7():
    liczba = int(input("Podaj liczbe: "))
    try:
        print("Pierwiastek: ",math.sqrt(liczba))
    except ValueError:
        print("Pierwiastek ujemny")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad4(6,8,10)
    zad5()
    zad6()
    zad7()
