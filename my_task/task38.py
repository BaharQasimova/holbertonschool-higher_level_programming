import random

class Uzgucu:

    def __init__(self, ad, yas, milliyet):
        self.ad = ad
        self.yas = yas
        self.milliyet = milliyet
        self.vaxt = 0

    def uz(self, mesafe):
        self.vaxt = round(mesafe * random.uniform(0.8, 1.5), 2)
        print(f"{self.ad} {mesafe} m-i {self.vaxt} saniyeye bitirdi.")

class UzguculukYarisi:

    def __init__(self, mesafe):
        self.mesafe = mesafe
        self.istirakcilar = []

    def istirakci_elave_et(self, uzgucu):
        self.istirakcilar.append(uzgucu)
        print(f"{uzgucu.ad} yarisa elave olundu.")

    def yarisi_baslat(self):
        print("\n Yaris basladi!\n")
        for uzgucu in self.istirakcilar:
            uzgucu.uz(self.mesafe)
        siralama = sorted(self.istirakcilar, key=lambda u: u.vaxt)
        print("\n Neticeler Cedveli:")
        print(f"{'Yer':<5}{'Ad':<15}{'Milliyet':<15}{'Vaxt (s)':<10}")
        print("-" * 45)
        for yer, uzgucu in enumerate(siralama, start=1):
            print(f"{yer:<5}{uzgucu.ad:<15}{uzgucu.milliyet:<15}{uzgucu.vaxt:<10}")
        qalib = siralama[0]
        print(f"\n Qalib: {qalib.ad} ({qalib.vaxt} s)")

uzgucu1 = Uzgucu("Orxan", 28, "Azerbaycan")
uzgucu2 = Uzgucu("Osman", 22, "Turkiye")
uzgucu3 = Uzgucu("Brawn", 20, "ABŞ")
yaris = UzguculukYarisi(100)

yaris.istirakci_elave_et(uzgucu1)
yaris.istirakci_elave_et(uzgucu2)
yaris.istirakci_elave_et(uzgucu3)
yaris.yarisi_baslat()