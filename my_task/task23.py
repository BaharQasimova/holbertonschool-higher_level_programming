class AileUzvu:

    def __init__(self, ad, yas, vezife):
        self.ad = ad
        self.yas = yas
        self.vezife = vezife

    def melumat_goster(self):
        print(f"Aile uzvu: {self.ad}, Yas: {self.yas}, Vezife: {self.vezife}")
class Aile:

    def __init__(self, soyad):
        self.soyad = soyad
        self.uzvler = []

    def uzv_elave_et(self, uzv):
        self.uzvler.append(uzv)

    def aileni_goster(self):
        print(f"\n{self.soyad} ailesi:")
        for u in self.uzvler:
            u.melumat_goster()

uzv1 = AileUzvu("Kamran", 40, "Ata")
uzv2 = AileUzvu("Aysel", 38, "Ana")
uzv3 = AileUzvu("Nicat", 18, "Oglan")
uzv4 = AileUzvu("Leman", 14, "Qiz")
aile = Aile("Hesenov-lar")

aile.uzv_elave_et(uzv1)
aile.uzv_elave_et(uzv2)
aile.uzv_elave_et(uzv3)
aile.uzv_elave_et(uzv4)
aile.aileni_goster()