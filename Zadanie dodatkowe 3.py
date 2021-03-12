#Zad dodatkowe 3 (nd)
a = int(input('Wprowadź wagę'))
#a to waga
b = int(input('Wprowadź wzrost'))
#b to wzrost
c = b ** 2
#c to wzrost do ^2
d = a / c 
#d jako wynik wzoru
if d >= 18.5 and d <= 24.9:
    print('waga prawidłowa')
else: 
    if d >= 18.5:
        print('nadwaga')
    else:
        print('niedowaga')
print(d)
    