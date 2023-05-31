from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, pajak, foto):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.pajak = pajak
        self.foto = foto

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_pajak(self):
        return self.pajak
    
    def get_foto(self):
        return "D:/Nguli ... ah/sem 4/DPBO/Python GUI/LatihanPyGUI/assets/" + self.foto
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nPajak Bangunan : " + self.pajak + "\nFoto Pemilik : " + self.foto + "\n"
   