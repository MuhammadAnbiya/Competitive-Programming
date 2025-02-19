#Menghitung Gaji
# gajiBulanan = 
# transport = 100.000/hari
# makan = 50.000/hari
# uang lembur = 2 jam pertama itu 100.000, 5 jam berikutnya 150.000, selebihnya 200.000

# berapa honor yang saya dapatkan jika saya bekerja selama 21 hari dan lembur 10 jam.

hariKerja = int(input("berapa banyak hari kerja anda : "))
gajiBulanan = int(input("masukan gaji pokok anda : "))
transport = int(input("masukan uang transport pokok anda : "))
makan = int(input("masukan uang makan pokok anda : "))
totalTransport = transport * hariKerja
totalMakan = makan * hariKerja
lembur = int(input("berapa jam anda lembur : "))


if lembur <= 2:
    totalLembur = lembur * 100_000
    
elif lembur <= 7 :
    lembur = lembur - 2
    totalLembur = (lembur * 150_000 ) + 200_000
    
else:
    lembur = lembur - 7
    totalLembur = (lembur * 200_000) + 950_000
    
hasil = gajiBulanan + totalTransport + totalMakan + totalLembur
print("total honor anda adalah : " + str(hasil))



