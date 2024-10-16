def cetak_pola(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
cetak_pola(n)
