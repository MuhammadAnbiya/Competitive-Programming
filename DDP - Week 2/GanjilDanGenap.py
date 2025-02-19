# Buatlah Program Membedakan Bilangan Ganjil dan Genap
angka = int(input("Masukan angka yang ingin di uji coba? "))

if angka % 2 == 0:
    print(str(angka) + " Adalah bilangan Genap")
    
elif angka % 2 == 1:
    print(str(angka) + " Adalah bilangan Ganjil")

