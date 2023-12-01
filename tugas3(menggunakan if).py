total_belanja = int(input("masukan total belanja :"))
if total_belanja > 100000:
    print("anda mendapatkan diskon 10%")
    diskon = total_belanja * 0.10
    harga_setelah_diskon = total_belanja - diskon
    print("anda hanya membayar", harga_setelah_diskon)
else:
    print("anda tidak mendapatkan diskon")