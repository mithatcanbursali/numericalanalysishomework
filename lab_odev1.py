import numpy as np

# Fonksiyon Tanımlaması(örnek fonksiyon)
def f(x):
    return x ** 5 - 5 * x ** 3 - 7 * x - 7

# Fonksiyonun Türevi(örnek fonksiyon)

def fd(x):
    return -7 - 15 * x ** 2 + 5 * x ** 4


def my_regula_falsi(xl, xh, max_hata, max_iter):
    count = 1
    while True:
        x2 = xl - (xh - xl) * f(xl) / (f(xh) - f(xl))

        if f(xl) * f(x2) < 0:
            xh = x2
        else:
            xl = x2

        count = count + 1

        if max_hata > abs(f(x2)):
            return x2,(count-1),abs(f(x2))
        elif (count-1) == max_iter:
            return x2,(count-1),abs(f(x2))



def my_newton(x0, max_hata, max_iter):

    count = 1
    while True:
        x1 = x0 - f(x0) / fd(x0)
        x0 = x1
        count = count + 1

        if max_hata > abs(f(x1)):
            return x1, (count - 1), abs(f(x1))
        elif (count - 1) == max_iter:
            return x1, (count - 1), abs(f(x1))



def my_secant(xl, xh, max_hata, max_iter):
    count = 1
    while True:
        x2 = xl - (xh - xl) * f(xl) / (f(xh) - f(xl))
        xl = xh
        xh = x2
        count = count + 1

    if max_hata > abs(f(xh)):
            return x2, (count - 1), abs(f(x2))
    elif (count - 1) == max_iter:
            return x2, (count - 1), abs(f(x2))