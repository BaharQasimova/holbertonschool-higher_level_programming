class Mehsul:

    def __init__(self, ad, qiymet):
        self.ad = ad
        self.qiymet = qiymet

    def melumat_goster(self):
        print(f"Mehsul: {self.ad}, Qiymet: {self.qiymet} AZN")

    def endirim_hesabla(self):
        return self.qiymet

class Elektronika(Mehsul):

    def __init__(self, ad, qiymet, zemanet_illik):
        super().__init__(ad, qiymet)
        self.zemanet_illik = zemanet_illik

    def melumat_goster(self):
        print(f"Elektronika Mehsulu: {self.ad}, Qiymet: {self.qiymet} AZN, Zemanet: {self.zemanet_illik} il")
    def endirim_hesabla(self):
        return round(self.qiymet * 0.9, 2)

class Geyim(Mehsul):
    def __init__(self, ad, qiymet, olcu):
        super().__init__(ad, qiymet)
        self.olcu = olcu

    def melumat_goster(self):
        print(f"Geyim Mehsulu: {self.ad}, Qiymet: {self.qiymet} AZN, Olcu: {self.olcu}")
    def endirim_hesabla(self):
        return round(self.qiymet * 0.8, 2)

class Magaza:
    def __init__(self, ad):
        self.ad = ad
        self.mehsullar = []

    def mehsul_elave_et(self, mehsul):
        self.mehsullar.append(mehsul)

    def mehsullari_goster(self):
        print(f"\n{self.ad} magazasinin mehsullari:")
        for m in self.mehsullar:
            m.melumat_goster()
            print(f"Endirimli qiymet: {m.endirim_hesabla()} AZN\n")

magaza = Magaza("Kontakt Home")
elektronika1 = Elektronika("Telefon", 1200, 2)
geyim1 = Geyim("Kofta", 50, "M")

magaza.mehsul_elave_et(elektronika1)
magaza.mehsul_elave_et(geyim1)
magaza.mehsullari_goster()