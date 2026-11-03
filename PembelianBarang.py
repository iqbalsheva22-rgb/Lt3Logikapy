print("=== SISTEM CHECKOUT DAN CEK VOUCHER) ===\n")
print("========================================")

total_belanja = float(input("Masukkan total belanja (Rp): "))
kode_voucher = input("Masukkan kode voucher (ketik 'TIDAK' jika tidak ada): ").upper()
metode_bayar = input("Metode pembayaran (COD / TRANSFER / E-WALLET): ").upper()

voucher_tersedia = "DISKONHEMAT"
voucher_expired = False
min_belanja_voucher = 150000

print("\n=== PROSES VALIDASI ===")

voucher_valid = (kode_voucher == voucher_tersedia) and (not voucher_expired) and (total_belanja >= min_belanja_voucher)
print(f"- Apakah voucher valid? {voucher_valid}")

bebas_biaya_layanan = (metode_bayar == "TRANSFER") or (metode_bayar == "E-WALLET")
print(f"- Bebas biaya layanan? {bebas_biaya_layanan}")

print("\n=== RINGKASAN PEMBAYARAN ===")

if voucher_valid:
    potongan = 25000
    print(f" Voucher {voucher_tersedia} berhasil digunakan!")
    print(f" Total potongan: Rp {potongan:,}")
else:
    potongan = 0
    if kode_voucher == voucher_tersedia and total_belanja < min_belanja_voucher:
        print(f" Voucher gagal digunakan. Minimal belanja harus Rp {min_belanja_voucher:,}")
    else:
        print(" Tidak ada potongan voucher yang diterapkan.")

if not bebas_biaya_layanan:
    biaya_layanan = 5000
    print(f" Biaya layanan COD: Rp {biaya_layanan:,}")
else:
    biaya_layanan = 0
    print(" Ongkir: Rp 0 (Gratis ongkir!)")

total_akhir = total_belanja - potongan + biaya_layanan
print(f" Total akhir yang harus dibayar: Rp {total_akhir:,}")