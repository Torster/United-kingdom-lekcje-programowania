#zad 11
a = int(input('wprowadź a:'))
b = int(input('wprowadź b:'))
if a >= 0:
    if b >= 0:
        akw = a ** 2
        bkw = b ** 2
        ckw = akw + bkw
        c = ckw ** 0.5
    else:
        print('nieprawidłowa wartość')
if a - (b + c) <= 0:
    print ('trójkąt powstał z przekątną o wartości {}'.format(c))
else:
    if b - (a + c) <= 0:
        print ('trójkąt powstał z przekątną o wartości {}'.format(c))
    else:
            if c - (a + b) <= 0:
                print ('trójkąt powstał z przekątną o wartości {}'.format(c))
            else:
                print('boki trójkątu są za krótkie, aby utworzyć trójkąt')