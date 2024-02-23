# Menghitung uang yang harus dibayar untuk membeli mangga dengan kriteria
# jika beli 2 kilo atau kurang harga perkilonya 20_000
# jika beli dari 2 kilo s/d 5 kilo harga perkilonya 18_000
# jika beli lebih dari 5 kilo harga perkilonya 16_000

# Berapa banyak yang harus dibayar jika beli 10 kilo?

jumlah = int(input("Masukan Jumlah Mangga yang Anda Beli : "))

if jumlah <= 2:
    harga = jumlah * 20_000
elif jumlah <= 5:
    harga = jumlah * 18_000
else:
    harga = jumlah * 16_000
    
print("Harga yang harus dibayar " + str(harga))