import random
import time
class Avtomobil:
    def __init__(self, marka, reng):
        self.marka = marka
        self.reng = reng
        self.suret = 0
        self.mesafe = 0

    def sureti_artir(self):
        artim = random.randint(8, 30)
        self.suret += artim
        print(f"{self.marka} sureti artirdi: {self.suret} km/saat")

    def irelile(self):
        self.mesafe += self.suret / 15
        print(f"{self.marka} {self.mesafe:.1f} km mesafe qet etdi.")

class Yaris:
    def __init__(self, finis_mesafesi):
        self.finis_mesafesi = finis_mesafesi
        self.avtomobiller = []

    def avtomobil_elave_et(self, avtomobil):
        self.avtomobiller.append(avtomobil)

    def start(self):
        print("\n Yaris basladi!")
        while True:
            for avtomobil in self.avtomobiller:
                avtomobil.sureti_artir()
                avtomobil.irelile()
                if avtomobil.mesafe >= self.finis_mesafesi:
                    print(f"\n Qalib: {avtomobil.marka} ({avtomobil.reng})")
                    return
            time.sleep(1)

yaris = Yaris(finis_mesafesi=2)
avto1 = Avtomobil("CLS 63", "AG")
avto2 = Avtomobil("F 90", "GOY")
avto3 = Avtomobil("AUDI", "QARA")

yaris.avtomobil_elave_et(avto1)
yaris.avtomobil_elave_et(avto2)
yaris.avtomobil_elave_et(avto3)

yaris.start()