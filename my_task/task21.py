class Erzaq:

    def __init__(self, ad, miqdar, olcu_vahidi):

        self.ad = ad
        self.miqdar = miqdar
        self.olcu_vahidi = olcu_vahidi

    def melumat_goster(self):
        print(f"Erzaq: {self.ad}, Miqdar: {self.miqdar} {self.olcu_vahidi}")

class ErzaqSiyahisi:

    def __init__(self):
        self.erzaqlar = []

    def erzaq_elave_et(self, erzaq):
        self.erzaqlar.append(erzaq)

    def butun_erzaqlari_goster(self):
        print("\nEv ucun erzaq alis-verisi siyahisi:")
        for e in self.erzaqlar:
            e.melumat_goster()
            
siyahi = ErzaqSiyahisi()
erzaq1 = Erzaq("Un", 2, "kq")
erzaq2 = Erzaq("Yumurta", 12, "eded")
erzaq3 = Erzaq("Sut", 3, "litr")
erzaq4 = Erzaq("Yag", 1, "litr")
erzaq5 = Erzaq("Duz", 1, "paket")
siyahi.erzaq_elave_et(erzaq1)
siyahi.erzaq_elave_et(erzaq2)
siyahi.erzaq_elave_et(erzaq3)
siyahi.erzaq_elave_et(erzaq4)
siyahi.erzaq_elave_et(erzaq5)
siyahi.butun_erzaqlari_goster()