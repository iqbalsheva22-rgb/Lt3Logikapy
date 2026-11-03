print("=== SISTEM CEK KELULUSAN SISWA ===")
print("==================================")

nama = input("Masukkan nama siswa: ")
kelas = input("Masukkan kelas siswa: ")
nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))
absensi_persen = float(input("Masukkan persentase absensi (0-100): "))
input_izin = input("Apakah punya surat izin resmi? (y/t): ").lower()

punya_surat_izin = (input_izin == 'y' or input_izin == 'ya')

print("\n=== HASIL KELULUSAN SISWA ===")

lulus_murni = nilai_ujian >= 75 and absensi_persen >= 80
kehadiran = not (absensi_persen >= 80)

print(f"- Lulus syarat murni (Nilai >= 75 DAN Absen >= 80): {lulus_murni}")
print(f"- Apakah siswa dinilai jarang masuk? (NOT Absen >= 80): {kehadiran}")

print("\n=== KEPUTUSAN AKHIR ===")
print(nama, " dari kelas ", kelas)
if kehadiran or punya_surat_izin:
    print("Status: SISWA LULUS / DIIZINKAN LANJUT")
else:
    print("Status: SISWA TIDAK LULUS")