# Pertemuan 13 - Debugging dan Testing

Nama: Amandita Pebriana Putri  
NIM: 2225250134  
Kelas: 3A Pendidikan Matematika  

## Kasus
Jelaskan program yang diuji. Program ini berisi fungsi untuk menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi dari sebuah list data.

## Test Case
| ID | Input | Expected | Actual Awal | Status |
|----|-------|----------|-------------|--------|
| TC-01 | [80, 60, 90, 70] | 75.0 | 58.0 | Fail -> Pass |
| TC-02 | 60 | "Lulus" | "Tidak lulus" | Fail -> Pass |
| TC-03 | [80, 60, 90, 70] | 90 | 0 | Fail -> Pass |

## Bug Report
- **Fungsi `hitung_rata_rata`**: Terjadi kesalahan logika karena pembagian dilakukan secara statis dengan angka `5`, padahal jumlah data ada 4. Diperbaiki dengan membagi menggunakan `len(nilai)`.
- **Fungsi `status`**: Menggunakan operator `>` sehingga nilai `60` terbaca "Tidak lulus". Diperbaiki menggunakan operator `>=`.
- **Fungsi `nilai_tertinggi`**: Inisialisasi awal variabel `tertinggi = 0` menyebabkan hasil salah jika semua angka positif. Diperbaiki dengan menginisialisasi ke elemen pertama `nilai[0]` dan mengubah arah operator perbandingan menjadi `>`.

## Retest
Setelah dilakukan perbaikan pada ketiga fungsi tersebut, seluruh pengujian (*test case*) menghasilkan output yang sesuai dengan harapan (*Expected*).

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi
Apa teknik debugging yang paling membantu dan mengapa?
Teknik *tracing* manual dan penggunaan breakpoint di VS Code sangat membantu karena kita bisa melihat alur eksekusi variabel per baris secara langsung untuk mendeteksi letak kesalahan logika dengan cepat.