def cetak_bilangan_ganjil(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")

# Contoh penggunaan
n = int(input("Masukkan batas bilangan: "))
cetak_bilangan_ganjil(n)
