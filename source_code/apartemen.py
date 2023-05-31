from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga_beli, foto):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.harga_beli = harga_beli
        self.foto = foto

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_harga_beli(self):
        return self.harga_beli
    
    def get_foto(self):
        return "D:/Nguli ... ah/sem 4/DPBO/Python GUI/LatihanPyGUI/assets/" + self.foto
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) +"\nHarga Beli : " + self.harga_beli + "\nFoto Pembeli : " + self.foto + "\n"