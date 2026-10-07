def main():
    n = int(input("Masukkan bilangan bulat positif n: "))
    if n <= 0:
        print("n harus bilangan bulat positif!")
        return

    total_semua = 0
    jumlah_genap = 0

    print("\n=== Tabel Perkalian 1 sampai n ===")
    for i in range(1, n + 1):
        jumlah_baris = 0
        for j in range(1, n + 1):
            hasil = i * j
            print(f"{hasil:4}", end="")  # cetak dengan lebar 4
            total_semua += hasil
            jumlah_baris += hasil
            if hasil % 2 == 0:
                jumlah_genap += 1
        print(f" | Jumlah baris {i} = {jumlah_baris}")
    
    print("\n=== Statistik ===")
    print(f"Jumlah seluruh hasil perkalian = {total_semua}")
    print(f"Banyak hasil yang genap = {jumlah_genap}")

if __name__ == "__main__":
    main()
