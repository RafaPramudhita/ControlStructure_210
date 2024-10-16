def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Contoh penggunaan
n = int(input("Masukkan jumlah angka Fibonacci yang ingin dicetak: "))
fibonacci(n)
