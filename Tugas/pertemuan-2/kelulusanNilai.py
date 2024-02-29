english = int(input("Masukan Nilai english : "))
MTK = int(input("Masukan Nilai MTK : "))
indo = int(input("Masukan Nilai indo : "))
ipa = int(input("Masukan Nilai ipa : "))
ips = int(input("Masukan Nilai ips : "))


if (english + MTK + indo)/3 >= 75:
    print("Lulus")
elif (english + MTK + indo + ipa + ips)/5 >= 70:
    print("Lulus")    
elif english > 90 and MTK > 90:
    print("Lulus")
else:
    print("Tidak Lulus") 