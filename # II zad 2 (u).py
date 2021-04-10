# II zad 2 (u)
t = []
ilość = int(input('podaj ilosc'))
for i in range(0,ilość):
    a = int(input('podaj liczbe'))
    t.append(a)
wynik = 0
for i in range(0,ilość):
    wynik = wynik +t[i]
final = wynik / ilość
print('średnia arytmetyczna: {}'.format(final))

