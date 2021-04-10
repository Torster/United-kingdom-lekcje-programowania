# II zad 5 (u)
t = []
ilość = int(input('podaj ilosc'))
for i in range(0,ilość):
    a = int(input('podaj liczbe'))
    if (a >= 10 and a <=50): 
        t.append(a)
    else:
        print('nie wszystkie elementy mieszczą się w zakresie')
        exit()
print('wszystkie elementy mieszczą się w zakresie')