#Zad dodatkowe 2
a = int(input('wprowadź pierwszą liczbę:'))
b = int(input('wprowadź drugą liczbę:'))
c = int(input('wprowadź trzecią liczbę:'))
if (a > b) and (a > c):
    print('największą liczbą jest: {}'.format(a))
    if (b > c):
        print('najmniejszą liczbą jest: {}'.format(c))
    else:
        print('najmniejszą liczbą jest: {}'.format(b)) 
else:
    print('najmniejszą liczbą jest: {}'.format(a))
    if (b > c):
        print('największą liczbą jest: {}'.format(b))
    else:
        print('największą liczbą jest: {}'.format(c))