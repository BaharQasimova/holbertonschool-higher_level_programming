class Yuk:

    def __init__(self, ad, cekisi, nov):

        self.ad = ad
        self.cekisi = cekisi
        self.nov = nov

    def melumat_goster(self):

        print(f"Yuk: {self.ad}, Cekisi: {self.cekisi} kg, Novu: {self.nov}")

class YukdasimaNəqliyyati:

    def __init__(self, ad, tutumu):

        self.ad = ad
        self.tutumu = tutumu
        self.yukler = []

    def yuk_elave_et(self, yuk):
        if self.cem_cekisi() + yuk.cekisi <= self.tutumu:
            self.yukler.append(yuk)
            print(f"Yuk elave olundu: {yuk.ad}")
        else:
            print("Tutuq doludur, yeni yuk elave etmek olmaz.")
            
    def cem_cekisi(self):
        toplam = 0
        for y in self.yukler:
            toplam += y.cekisi
        return toplam

    def yukleri_goster(self):
        print(f"\n{self.ad} yukdasima vasitesindeki yukler:")
        for y in self.yukler:
            y.melumat_goster()

        print(f"Toplam cekisi: {self.cem_cekisi()} kg")

yuk1 = Yuk("Esyalar", 200, "Konteyner")
yuk2 = Yuk("Mebel", 150, "Paket")
vasite = YukdasimaNəqliyyati("Kamaz", 500)

vasite.yuk_elave_et(yuk1)
vasite.yuk_elave_et(yuk2)
vasite.yukleri_goster()