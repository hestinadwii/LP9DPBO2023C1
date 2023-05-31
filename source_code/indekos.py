from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga_sewa, foto):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_sewa = harga_sewa
        self.foto = foto

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_harga_sewa(self):
        return self.harga_sewa
    
    def get_foto(self):
        return "D:/Nguli ... ah/sem 4/DPBO/Python GUI/LatihanPyGUI/assets/" + self.foto

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nHarga Sewa per Bulan : " + self.harga_sewa + "\nFoto Penyewa : " + self.foto + "\n"