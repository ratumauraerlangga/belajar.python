def menyapa(nama, jurusan = "", tempat = "ancol"):
    print("haloo", nama)
    print("kelas", jurusan)
    print("selamat datang di", tempat)

menyapa("salman", "12 rpl")
menyapa("siti", "12 tkj", "dufan")

#tugas1
def menghitung(angka1, angka2, op):
    if op == "*":
        return angka1 * angka2
    elif op == "+":
        return angka1 + angka2
    elif op == "-":
        return angka1 - angka2
    else:
        print("operasi tidak valid")
  
print(menghitung(2, 4, "*"))  
print(menghitung(4, 5, "+"))     
print(menghitung(10, 5, "-"))   
print()

#tugas2
def pengulangan(kata, jumlah):
    for i in range(jumlah):
        print(kata)

pengulangan("haiii, salman", 4)
pengulangan ("selamat datang", 2)
print()