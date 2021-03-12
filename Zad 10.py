#zad 10
a = int(input('wprowadź a:'))
b = int(input('wprowadź b:'))
if a >= 0:
    if b >= 0:
        akw = a ** 2
        bkw = b ** 2
        ckw = akw + bkw
        c = ckw ** 0.5
        print(c)
    else:
        print('nieprawidłowa wartość')