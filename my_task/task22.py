class Futbolcu:

    def __init__(self, ad, vezife, yas, milli_komanda):

        self.ad = ad
        self.vezife = vezife
        self.yas = yas
        self.milli_komanda = milli_komanda

    def melumat_goster(self):
        print(f"Futbolcu: {self.ad}, Vezife: {self.vezife}, Yas: {self.yas}, Milli komanda: {self.milli_komanda}")
class FutbolKlubu:

    def __init__(self, ad):
        self.ad = ad
        self.heyet = []

    def futbolcu_elave_et(self, futbolcu):
        self.heyet.append(futbolcu)

    def heyeti_goster(self):
        print(f"\n{self.ad} futbol klubunun heyeti:")
        for f in self.heyet:
            f.melumat_goster()

real_madrid = FutbolKlubu("REAL Madrid")
futbolcu1 = Futbolcu("Thibaut Courtois", "Qapici", 31, "Belcika")
futbolcu2 = Futbolcu("Dani Carvajal", "Mudafieci", 31, "Ispaniya")
futbolcu3 = Futbolcu("Eder Militao", "Mudafieci", 25, "Brazilia")
futbolcu4 = Futbolcu("David Alaba", "Mudafieci", 31, "Avstriya")
futbolcu5 = Futbolcu("Ferland Mendy", "Mudafieci", 27, "Fransa")
futbolcu6 = Futbolcu("Luka Modric", "Yarimmudafieci", 37, "Xorvatiya")
futbolcu7 = Futbolcu("Toni Kroos", "Yarimmudafieci", 33, "Almaniya")
futbolcu8 = Futbolcu("Eduardo Camavinga", "Yarimmudafieci", 21, "Fransa")
futbolcu9 = Futbolcu("Vinicius Junior", "Hucumcu", 23, "Brazilia")
futbolcu10 = Futbolcu("Karim Benzema", "Hucumcu", 35, "Fransa")
futbolcu11 = Futbolcu("Rodrygo", "Hucumcu", 22, "Brazilia")

real_madrid.futbolcu_elave_et(futbolcu1)
real_madrid.futbolcu_elave_et(futbolcu2)
real_madrid.futbolcu_elave_et(futbolcu3)
real_madrid.futbolcu_elave_et(futbolcu4)
real_madrid.futbolcu_elave_et(futbolcu5)
real_madrid.futbolcu_elave_et(futbolcu6)
real_madrid.futbolcu_elave_et(futbolcu7)
real_madrid.futbolcu_elave_et(futbolcu8)
real_madrid.futbolcu_elave_et(futbolcu9)
real_madrid.futbolcu_elave_et(futbolcu10)
real_madrid.futbolcu_elave_et(futbolcu11)
real_madrid.heyeti_goster()