matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9 ]]
for data in matriks: 
    for angka in data:
        print(angka)
    print()

print("=======")

buku_alamat = [["John Doe", "555-1234"], ["Jane Smith", "555-5678"], ["Bob Johnson", "555-7890"]] 
for data in buku_alamat: 
    for item in data : 
        print(item, end=" ")
    print()

print("========")

for i in range (1, 6):
    for j in i :