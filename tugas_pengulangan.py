#penggunaan for dalam pengulangan 
for i in range(10):
    print("belajar python")

#menampilkan data dengan bilangan yang di tambah 2 atau bilangan genap
angka = 0
for data in range(10):
    angka = angka + 2
    print(angka)

# menampilkan data mulai dari 1 dan kurang dari 10
for data in range(1, 10):
    print(data)

# pengulangan yang menampilkan list 
daftar_makanan = ["nasi goreng", "batagor", "mie ayam", "bakso"]

for data in daftar_makanan:
    print("makanan", daftar_makanan)

#penggunaan while dalam pengulangan
pilihan = input("apakah anda ingin mengulang? ya atau tidak :")

while(pilihan == "ya") :
    pilihan = input("apakah anda ingin mengulang? ya atau tidak :")

angka = 1

while(angka <= 10):
    print(angka)
    angka = angka + 1

angka = 1
while(angka <= 50):
    print(angka)
    angka = angka + 1


kumpulan_makanan = ["nasi goreng", 'mie goreng', 'nasi bakar', 'mie bakar']
print(kumpulan_makanan)
for makanan in kumpulan_makanan:
    print(makanan)

# pengulangan python cara lain 

for i in range (1, 11):
    print(i)

#jika ingin membuat perulangan bilangan bulat positif atau negatif

#positif
for i in range(2, 21):
    if i % 2 != 0:
        print(i)


# perulangan menggunakan break 

for i in range(3):
    if i == 2:
        break
    print(i)

kumpulan_makanan = ["nasi bakar", "nasi goreng", "nasi kucing", "nasi uduk"]

for makanan in kumpulan_makanan:
    if(makanan == "nasi goreng"):
        break
    print ("makanan :", makanan)

# perulangan menggunakan continue

for i in range(3):
    if i == 2:
        break
    print(i)

kumpulan_makanan = ["nasi bakar", "nasi goreng", "nasi kucing", "nasi uduk"]

for makanan in kumpulan_makanan:
    if(makanan == "nasi goreng"):
        continue
    print ("makanan :", makanan)