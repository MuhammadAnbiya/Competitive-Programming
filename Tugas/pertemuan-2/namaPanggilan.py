# - Menentukan panggilan berdasarkan umur
# 0-2 = Bayi
# 2-5 = Balita
# 5-12 = Anak-anak
# 12-17 = Remaja
# >17 = Dewasa
# >30 = Orangtua

umur = int(input("Masukan Umur Anda : "))

if umur <=2:
    panggilan = "Bayi"  
elif umur <= 5:
    panggilan = "Balita"
elif umur <= 12:
    panggilan = "Anak-anak"
elif umur <= 17:
    panggilan = "Remaja"
elif umur > 17 :
    if umur <= 30:
        panggilan = "Dewasa"
    else:
        panggilan = "Orangtua"
    
print("Jadi Nama Panggilan Kamu Adalah "  + panggilan)