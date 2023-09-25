print(14*"=")
print("SELAMAT DATANG")
print(14*"=" + "\n")

print("Silahkan Login")
nama = input("Masukkan Nama Anda: ")
nim = int(input("Masukkan Nim: "))
print("Login Berhasil")
print("\n")

print(38*"-")
print("Menghitung Massa Kg")
print(38*"-")

lb = 2.20462
ons = 35.27396
gram = 1000
satuan_kg = int(input("Masukkan Satuan Kg: "))
operator = input("Konversikan ke? (lb, ons, gram): ")

if operator == "lb":
    satuan_lb = satuan_kg * lb
    print(f"{satuan_kg} kilogram sama dengan {satuan_lb} lb")
elif operator == "ons":
    satuan_ons = satuan_kg * ons
    print(f"{satuan_kg} kilogram sama dengan {satuan_ons} ons")
elif operator == "gram":
    satuan_gram = satuan_kg * gram
    print(f"{satuan_kg} kilogram sama dengan {satuan_gram} gram")
else:
    print ("Salah itu bang, coba ulang kembali\n")
print(38*"-")
print("\n")

print(14*"=")
print("mksh")
print(14*"=")
