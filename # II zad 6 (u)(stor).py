# II zad 6 (u)(stor)
t = []
n = []
ilość = int(input('podaj ilosc'))
for i in range(0,ilość):
    a = int(input('podaj liczbe'))
    if (a >= 10 and a <=50): 
        t.append(a)
    else:
        n.append(a)
if not n :
    print('wszystkie liczby należą do przedziału')
else:
    print('{} nie należy do przedziału'.format(n))