from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Kim Seokjin", 3, 3, "Rp 25.000.000.000", "seokjin.jpeg"))
hunians.append(Rumah("Uchinaga Aeri", 5, 2, "Rp 125.000", "giselle.jpeg"))
hunians.append(Indekos("Bp. Hoshi", "Yoon Jeonghan", "Rp 750.000", "jeonghan.jpeg"))
hunians.append(Rumah("Park Jimin", 1, 4, "Rp78.000", "jimin.jpeg"))
hunians.append(Apartemen("Jungkook", 1, 1, "Rp 2.350.500.000", "jungkook.jpeg"))
hunians.append(Indekos("Ibu Jennie", "Shin Ryujin", "Rp 1.750.000", "ryujin.jpeg"))

root = Tk()
root.title("Praktikum DPBO Python")

landing_frame = Frame(root, padx=10, pady=10)
landing_frame.pack(padx=10, pady=10)

def show_data():
    global landing_page_shown
    landing_page_shown = True

    landing_frame.destroy() # Hapus tampilan halaman utama 
    def details(index): 

        frame.pack(padx=10, pady=10)
        opts.pack(padx=10, pady=10)
        b_add.config(state="normal")
        top = Toplevel()
        top.title("Detail " + hunians[index].get_jenis())

        d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
        d_frame.pack(padx=10, pady=10)

        d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + 
                          hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

        # Tambahkan gambar
        image =  Image.open(hunians[index].get_foto())
        image = image.resize((200, 200))  # Sesuaikan ukuran gambar
        photo = ImageTk.PhotoImage(image)
        image_label = Label(d_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=1, column=0)

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

landing_label = Label(landing_frame, text="Selamat datang di halaman utama!")
landing_label.pack()

landing_button = Button(landing_frame, text="Lihat Data", command=show_data)
landing_button.pack()

root.mainloop()
