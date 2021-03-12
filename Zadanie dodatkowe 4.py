#Zad dodatkowe 4 (nd?)
a = int(input('wprowadź dochód'))
b = a * 0.18
c = 85528 * 0.32
if a <= 85528:
    print(b - 556.02)
else:
    if a >= 85528:
        print(14839.02 + c)