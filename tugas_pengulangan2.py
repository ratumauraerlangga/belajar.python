#tugas 1
for i in range(1, 11):
    if i % 2 != 0:
        print("Angka ganjil pertama dalam rentang 1 hingga 10 adalah:", i)
        break

#tugas 2
total = 0
while True:
    bilangan = int(input("masukan bilangan bulat posifit (angka negatif untuk berhenti): "))
    if bilangan < 0:
            break 
    total += bilangan

print("jumlah dari bilangan positif yang dimasuka adalah :", total)

#tugas 3

angka = 0
for data in range(1, 51, 5):
     angka = angka + 5
     print(angka)
   