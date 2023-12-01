#for i in range(1, 25):
####          print("---- menit ke", j, "datik ke", d)

for i in range(1, 6): 
   print(i)
   for j in range (1, 4):
    print(i, "x", j,"=", int(i * j))
print("========")
for i in range(1, 6):
   print(i)
   for j in range(1,6):
      print(i, "/", j, "=", int(i / j) )
print("========")

for i in range(1, 6):
   print(i)
   for j in range(1, 6):
      print(i, "+", j, "=", int(i + j))
print("========")

kumpulanbarang = [["meja", "kursi", "tatakan"], ["monitor", "tv", "handphone"]]
for barang in kumpulanbarang:
    for item in barang:
       print(item, end=", ")
    print()
print("========")
