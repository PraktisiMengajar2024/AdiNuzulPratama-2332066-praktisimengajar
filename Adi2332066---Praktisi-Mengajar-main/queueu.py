class Barang:
    def __init__(self, namabarang, harga):
        self.namabarang = namabarang
        self.harga = harga
        
    def get_namabarang(self):
        return self.namabarang
    
    def get_harga(self):
        return self.format_harga(self.harga)  # Menggunakan fungsi format_harga untuk memformat harga

    @staticmethod
    def format_harga(harga):
        reversed_harga = str(harga)[::-1]  # Balik urutan karakter harga
        formatted_harga = '.'.join([reversed_harga[i:i+3] for i in range(0, len(reversed_harga), 3)])  # Pisahkan setiap tiga digit dengan titik
        return formatted_harga[::-1]  # Balik urutan kembali ke semula

class Transaksi:
    def __init__(self, barang, jumlah):
        self.barang = barang
        self.jumlah = jumlah
        self.total = self.hitung_total()
        
    def hitung_total(self):
        return self.barang.harga * self.jumlah
    
    def get_info(self):  # Memperbaiki parameter self
        return f"Nama barang: {self.barang.get_namabarang()}, Harga: {self.barang.get_harga()}, Jumlah: {self.jumlah}, Total: {self.barang.format_harga(self.total)}"

barang1 = Barang("asus", 2000000)
barang2 = Barang("vivo", 1500000)

transaksi1 = Transaksi(barang1, 5)
transaksi2 = Transaksi(barang2, 2)

print("Transaksi 1:", transaksi1.get_info())
print("Transaksi 2:", transaksi2.get_info())
