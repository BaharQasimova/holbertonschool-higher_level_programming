class Avtomobil:
    def __init__(self, marka, model, il, gunluk_qiymet):
        self.marka = marka
        self.model = model
        self.il = il
        self.gunluk_qiymet = gunluk_qiymet
        self.kirayede = False

    def melumat_goster(self):
        status = "Kirayededir" if self.kirayede else "Bosdur"
        print(f"{self.marka} {self.model} ({self.il}) - {self.gunluk_qiymet} AZN/gun - {status}")
    def kiraye_ver(self):
        if not self.kirayede:
            self.kirayede = True
            print(f"{self.marka} {self.model} ugurla kiraye verildi.")
        else:
            print(f"{self.marka} {self.model} artiq kirayededir.")
    def kiraye_bitir(self):
        if self.kirayede:
            self.kirayede = False
            print(f"{self.marka} {self.model} geri qaytarildi.")
        else:
            print(f"{self.marka} {self.model} artiq bosdur.")

class Musteri:
    def __init__(self, ad, soyad, telefon):
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
    def melumat_goster(self):
        print(f"Musteri: {self.ad} {self.soyad}, Telefon: {self.telefon}")

class KirayeSistemi:
    def __init__(self):
        self.avtomobiller = []
        self.musteriler = []
    def avtomobil_elave_et(self, avtomobil):
        self.avtomobiller.append(avtomobil)
    def musteri_elave_et(self, musteri):
        self.musteriler.append(musteri)
    def butun_avtomobilleri_goster(self):
        print("\nAvtomobiller:")
        for avto in self.avtomobiller:
            avto.melumat_goster()
    def butun_musterileri_goster(self):
        print("\nMusteriler:")
        for m in self.musteriler:
            m.melumat_goster()

avto1 = Avtomobil("Mercedes", "CLS 63", 2020, 350)
avto2 = Avtomobil("BMW", "M5", 2019, 250)
musteri1 = Musteri("Bayram", "Hesenzade", "+994504731505")

sistem = KirayeSistemi()
sistem.avtomobil_elave_et(avto1)
sistem.avtomobil_elave_et(avto2)
sistem.musteri_elave_et(musteri1)
sistem.butun_avtomobilleri_goster()
sistem.butun_musterileri_goster()
avto1.kiraye_ver()
avto1.kiraye_ver()
avto1.kiraye_bitir()