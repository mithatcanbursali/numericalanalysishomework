import lab_odev1

print('\nMETHODLAR LİSTESİ')
print('\n1. REGULA FALSİ')
print('\n2. NEWTON RAPHSON')
print('\n3. SECANT')

choice = input('Yapmak istediğiniz işlemi giriniz:')
choice = int(choice)

if choice == 1:
    xl = input('İlk Tahmin: ')
    xh = input('İkinci Tahmin:')
    max_hata = input('Maksimum Hata:')
    max_iter = input('Maksimum iterasyon sayısı')

    xl = float(xl)
    xh = float(xh)
    max_hata = float(max_hata)
    max_iter = int(max_iter)

    print(lab_odev1.my_regula_falsi(xl, xh, max_hata, max_iter))

elif choice == 2:
    x0 = input('Tahmin: ')
    max_hata = input('Maksimum Hata:')
    max_iter = input('Maksimum iterasyon sayısı')

    x0 = float(x0)
    max_hata = float(max_hata)
    max_iter = int(max_iter)

    print(lab_odev1.my_newton(x0, max_hata, max_iter))

elif choice == 3:
    xl = input('İlk Tahmin: ')
    xh = input('İkinci Tahmin:')
    max_hata = input('Maksimum Hata:')
    max_iter = input('Maksimum iterasyon sayısı')

    xl = float(xl)
    xh = float(xh)
    max_hata = float(max_hata)
    max_iter = int(max_iter)

    print(lab_odev1.my_secant(xl, xh, max_hata, max_iter))

else:
    print("Hatalı işlem numarası girdiniz!")