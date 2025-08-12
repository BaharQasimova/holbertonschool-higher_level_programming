class Zavod:

    def __init__(self, isci_sayi):
        self.isci_sayi = isci_sayi
        self.isleme_saatlari = {}

    def isci_elave_et(self, isci_adi):
        if isci_adi not in self.isleme_saatlari:
            self.isleme_saatlari[isci_adi] = 0
            print(f"{isci_adi} iscilere elave edildi.")
        else:
            print(f"{isci_adi} artiq movcuddur.")

    def saat_elave_et(self, isci_adi, saat):
        if isci_adi in self.isleme_saatlari:
            self.isleme_saatlari[isci_adi] += saat
            print(f"{isci_adi} ucun {saat} saat elave edildi.")
        else:
            print(f"{isci_adi} tapilmadi.")

    def butun_isci_saatlari(self):
        toplam = sum(self.isleme_saatlari.values())
        print(f"Umumi islenmis saat sayi: {toplam}")
        return toplam

    def melumat(self):
        print(f"İsci sayı: {self.isci_sayi}")
        for isci, saat in self.isleme_saatlari.items():
            print(f"{isci}: {saat} saat işliyib.")

zavod = Zavod(isci_sayi=3)

zavod.isci_elave_et("Ayxan")
zavod.isci_elave_et("Aytac")
zavod.isci_elave_et("Tofiq")
zavod.saat_elave_et("Ayxan", 7)
zavod.saat_elave_et("Aytac", 6)
zavod.saat_elave_et("Tofiq", 4)

zavod.melumat()
zavod.butun_isci_saatlari()