nim = "022"
angka_akhir = int(nim[-1])
#soal 1 
episode = 10
menit_per_episode = 35
total_menit = episode * menit_per_episode
jam = total_menit // 60
menit = total_menit % 60

#soal 2 
harga_cupang = 10000
harga_koi = 20000
uang = (int(nim) + 100) * 1000
biaya = 5 * harga_cupang + 2 * harga_koi
sisa_uang = uang - biaya

#soal 3 
jarak_tempuh = int(nim)
masukkan = input(f"Masukkan jarak tempuh (km),tekan enter untuk pakai {jarak_tempuh}km: ").strip()
if masukkan == "":
    jarak = jarak_tempuh
else :
    jarak = float(masukkan)

konsumsi = 2.7
kapasitas_tangki = angka_akhir + 3
harga_awal = int("1" + nim + "0")
bensin_yang_dibutuhkan = jarak / konsumsi
if bensin_yang_dibutuhkan > 3:
    harga_per_liter = harga_awal - 500
else:
    harga_per_liter = harga_awal

total_biaya = bensin_yang_dibutuhkan * harga_per_liter
jumlah_isi = int(bensin_yang_dibutuhkan / kapasitas_tangki)


print("\n=== HASIL ===")
print(f"Soal 1: {jam} jam {menit} menit")
print(f"Soal 2: Uang = Rp{uang:,} ; Biaya = Rp{biaya:,} ; Sisa = Rp{sisa_uang:,}")
print(f"Soal 3: Jarak = {jarak} km")
print(f"  - Bensin dibutuhkan = {bensin_yang_dibutuhkan:.6f} L")
print(f"  - Harga/liter setelah diskon = Rp{harga_per_liter:,}")
print(f"  - Total biaya bensin ≈ Rp{total_biaya:,.0f}")
print(f"  - Perkiraan isi bensin (full tank {kapasitas_tangki} L) = {jumlah_isi} kali")