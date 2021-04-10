# II zad 4 (u)(bez samej liczby)
liczby = int(input("Wprowadź liczbę:"))
dzielniki = []

for i in range(1, liczby):
    if liczby % i ==0:
        dzielniki.append(i)
print(dzielniki)