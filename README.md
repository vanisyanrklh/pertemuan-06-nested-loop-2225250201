# Pertemuan 06 Nested Loop Python

Algoritma dan Pemrograman | Pertemuan 06 | 11

Nama: Vanisya Nur Khalimah  
NIM: 2225520201  
Kelas: S1 Pendidikan Matematika FKIP Untirta  

---

## Tujuan
Menggunakan nested loop untuk membuat pola, melakukan akumulasi, dan pencacahan.

## Cara Menjalankan
```bash
python3 tugas/tabel_perkalian_dan_statistik.py

# Algoritma Tugas 3
# 1. Loop luar mengatur baris tabel perkalian (1 sampai n).
# 2. Loop dalam mengatur kolom tabel perkalian (1 sampai n).
# 3. Akumulator menjumlahkan seluruh hasil perkalian.
# 4. Counter menghitung banyaknya operasi perkalian.

def tabel_perkalian(n: int):
    akumulator = 0
    counter = 0

    print(f"Tabel Perkalian 1 sampai {n}")
    for i in range(1, n + 1):          # loop luar
        for j in range(1, n + 1):      # loop dalam
            hasil = i * j
            print(f"{hasil:4}", end=" ")
            akumulator += hasil        # akumulasi
            counter += 1               # pencacahan
        print()

    print("\nStatistik:")
    print(f"Total akumulasi hasil perkalian = {akumulator}")
    print(f"Jumlah operasi perkalian = {counter}")
    return akumulator, counter

# Hasil Pengujian
def uji_coba(n, expected_sum, expected_count):
    print(f"\n=== Pengujian dengan n={n} ===")
    akumulator, counter = tabel_perkalian(n)
    print(f"Expected sum = {expected_sum}, Actual sum = {akumulator}")
    print(f"Expected count = {expected_count}, Actual count = {counter}")
    print("Status:", "✅ Sesuai" if (akumulator == expected_sum and counter == expected_count) else "❌ Tidak sesuai")
    print("-" * 40)


if __name__ == "__main__":
    # Contoh pengujian
    uji_coba(3, expected_sum=36, expected_count=9)   # 3x3 tabel
    uji_coba(5, expected_sum=225, expected_count=25) # 5x5 tabel

# Analisis Efisiensi
def analisis_efisiensi(n: int):
    total_iterasi = n * n
    print(f"\nAnalisis Efisiensi:")
    print(f"Loop luar berjalan {n} kali.")
    print(f"Loop dalam berjalan {n} kali untuk setiap loop luar.")
    print(f"Total eksekusi badan loop dalam = {total_iterasi} kali.")

# Refleksi
def refleksi():
    print("\nRefleksi:")
    print("Kesalahan umum: meletakkan inisialisasi akumulator di dalam loop luar.")
    print("Akibatnya, nilai akumulator selalu reset setiap baris.")
    print("Perbaikan: inisialisasi akumulator harus ditempatkan di luar loop,")
    print("sehingga hasil akumulasi benar-benar menjumlahkan seluruh operasi.")
