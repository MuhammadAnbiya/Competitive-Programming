#Menghitung Gaji
# gajiBulanan = 
# transport = 100.000/hari
# makan = 50.000/hari
# uang lembur = 2 jam pertama itu 100.000, 5 jam berikutnya 150.000, selebihnya 200.000

transport = 100_000
makan = 50_000
gajiPokok = int(input("Masukan Gaji Pokok Anda : "))
hariKerja = int(input("Masukan Berapa Lama Hari Kerja Anda : "))
lembur = int(input("berapa jam anda lembur : "))

totalTransport = transport * hariKerja
totalMakan = makan * hariKerja

if lembur <= 2:
    totalLembur = lembur * 100_000
    
else:
    lembur = lembur - 2
    totalLembur = (lembur * 150_000 ) + 200_000
    
honor = gajiPokok + totalTransport + totalMakan + totalLembur
print("total honor anda adalah : " + str(honor))



