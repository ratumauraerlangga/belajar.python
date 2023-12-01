tahun_lahir = int(input("masukan tahun lahir :"))
jenis_kelamin = input("masukan jenis kelamin :")
tempat_lahir = input("masukan tempat lahir :")
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("anda sekarang berumur", umur)

if (umur > 18 or tempat_lahir == "jakarta") and jenis_kelamin == "laki-laki":
    print("anda sudah bisa membuat ktp")
else:
    print("anda tidak bisa membuat ktp")

if(not umur == 18):
    print("hello")