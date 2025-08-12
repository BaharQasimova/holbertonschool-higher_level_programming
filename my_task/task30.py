class Konullu:

    def __init__(self, ad, yas):

        self.ad = ad
        self.yas = yas

    def melumat_goster(self):
        print(f"Konullu: {self.ad}, Yas: {self.yas}")

class DostXidmet(Konullu):

    def __init__(self, ad, yas, vezife):
        super().__init__(ad, yas)
        self.vezife = vezife

    def melumat_goster(self):
        print(f"DOST Xidmet - Konullu: {self.ad}, Yas: {self.yas}, Vezife: {self.vezife}")
class AsanXidmet(Konullu):

    def __init__(self, ad, yas, is_gunu):
        super().__init__(ad, yas)
        self.is_gunu = is_gunu

    def melumat_goster(self):
        print(f"ASAN Xidmet - Konullu: {self.ad}, Yas: {self.yas}, Is Gunu: {self.is_gunu}")
dost1 = DostXidmet("Emin", 25, "Mesul sexs")
asan1 = AsanXidmet("Xedice", 26, "Hefte ici")

dost1.melumat_goster()
asan1.melumat_goster()