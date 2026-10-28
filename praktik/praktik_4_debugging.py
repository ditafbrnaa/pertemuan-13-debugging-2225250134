def hitung_rata_rata(nilai):
    # Perbaikan: Membagi dengan len(nilai) agar dinamis, bukan statis dibagi 5
    return sum(nilai) / len(nilai)

def status(nilai):
    # Perbaikan: Mengubah operator dari > menjadi >= agar angka 60 terbaca Lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    # Perbaikan: Inisialisasi awal mengambil elemen pertama, dan operator diubah menjadi >
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

nilai = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))