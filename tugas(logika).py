nama_user = input("Masukan nama anda : ")
password_user = input("Masukan Password anda : ")

if nama_user == "admin" and password_user == "admin123":
    print("selamat datang admin")
else:
    print("nama atau password yang anda masukan salah")