daftar_nama = ["maura", "shaumi", "jesika", "suci", "ida"]
daftar_nilai_pplg1 = [90, 80, 90, 75, 80]

jumlah = len(daftar_nama)
total = sum(daftar_nilai_pplg1)

print(daftar_nama[1])
print("jumlah pplg 1 =", jumlah, "orang")
print("total nilai", total)
print(daftar_nama.count("maura"))      
print("shaumi" in daftar_nama)
print("jumlah nama ada :", len(daftar_nama))
print("nilai terbesar adalah :" + str(max(daftar_nilai_pplg1)))
print("nilai terkecil adalah :" + str(min(daftar_nilai_pplg1)))
for i in daftar_nama:
    print(i)





print("selamat datang taman bermain dafun")
nama = input("masukan nama:")
umur =input("masukan umur:")
print("selamat datang", nama)

daftar_wahana = ["biang lala Rp. 13.000", "kora-kora Rp. 10.000", "istana boneka Rp. 15.000", "rumah kaca Rp. 20.000"]
print("selamat datang wahana bermain dafun")
print("daftar wahana yang tersedia:")
angka = 1
for wahana in daftar_wahana: 
    print(str(angka) + ".", wahana)
    angka = angka + 1

pilihan = input("masukan pilihan :")
if pilihan == "1": 
    print("pilihan anda nomor 1 adalah biang lala")
    print("harga Rp. 13.000")
elif pilihan == "2":
    print("pilihan anda nomor 2 adalah kora-kora")
    print("harga Rp. 10.000")
elif pilihan == "3":
    print("pilihan anda nomor 3 adalah istana boneka")
    print("harga Rp. 15.000")
elif pilihan == "4":
    print("pilihan anda nomor 4 adalah rumah kaca")
    print("harga Rp. 20.000")


if int (umur) >= 18: 
    print("anda mendapatkan pajak Rp. 2.000")
    if pilihan == "1":
        print("total harga Rp. 13.000 + pajak Rp. 2.000 = Rp. 15.000 ")
    if pilihan == "2":
        print("total harga Rp. 10.00 + pajak Rp. 2.000 = Rp. 12.000 ")
    if pilihan == "3":
        print("total harga Rp. 15.000 + pajak Rp. 2.000 = Rp. 17.000 ")
    if pilihan == "4":
        print("total harga Rp. 20.000 + pajak Rp. 2.000 = Rp. 22.000 ")
    print("terimakasih, sudah membeli tiket di wahana kami")
elif pilihan == "2" and int(umur) < 18:
    print("anda belum mencukupi umur untuk naik wahana")

bulan = ["januari", "februari", "maret", "april", "mei", "juni", "desember"]
print(bulan[1])
print(bulan[4 - 6])

