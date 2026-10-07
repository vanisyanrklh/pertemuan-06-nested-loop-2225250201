n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1
print(f"Banyak pasangan = {count}")

def tracing_manual(n: int):
    akumulator = 0
    counter = 0

    print(f"Tracing manual untuk n = {n}")
    print("i | j | hasil | akumulator | counter")
    print("-------------------------------------")

    for i in range(1, n + 1):          # loop luar
        for j in range(1, n + 1):      # loop dalam
            hasil = i * j
            akumulator += hasil
            counter += 1
            # tampilkan setiap langkah
            print(f"{i:2} | {j:2} | {hasil:5} | {akumulator:10} | {counter:7}")

    print("\nHasil akhir:")
    print(f"Total akumulasi = {akumulator}")
    print(f"Jumlah operasi = {counter}")


if __name__ == "__main__":
    tracing_manual(3)
    