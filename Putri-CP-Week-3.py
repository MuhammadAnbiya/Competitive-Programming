from datetime import datetime

nama_file = input("nama file?")
tanggal_awal = input("tanggal awal?")
tanggal_akhir = input("tanggal akhir")



def hitung_jumlah_surat(nama_file, tanggal_awal, tanggal_akhir):
    
    
    try:
        tanggal_awal = datetime.strptime(tanggal_awal, "%Y-%m-%d")
        tanggal_akhir = datetime.strptime(tanggal_akhir, "%Y-%m-%d")
        
        jumlah_surat = 0
        
        with open(nama_file, "r") as file:
            for line in file:
                
                kolom = line.strip().split(",")
                if len(kolom) != 2:
                    continue
                
                tanggal_surat = kolom[0]
                
                tanggal_surat = datetime.strptime(tanggal_surat, "%Y-%m-%d")
                
                if tanggal_awal <= tanggal_surat <= tanggal_akhir:
                    jumlah_surat += 1 
                    
                    
        print(jumlah_surat)
        
    except Exception as error:
        print(f"salah: {error}")
        
hitung_jumlah_surat(nama_file, tanggal_awal, tanggal_akhir)


# kak jujur aja aku cuma mampu segini, ini juga masih dibantu sama google, bulak balik google buat nyari penulisan syntax yg benar
# dari Putri yang sudah lelah lemah letih lesu lunglai love you :(