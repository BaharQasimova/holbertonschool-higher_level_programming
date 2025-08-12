class Mehsul:
    def __init__(self, ad, qiymet, stok):
        self.ad = ad
        self.qiymet = qiymet
        self.stok = stok

    def stokdan_azalt(self, say):
        if say <= self.stok:
            self.stok -= say
            return True
        else:
            print(f"Stokda kifayet qeder {self.ad} yoxdur.")
            return False

    def melumat(self):
        return f"Mehsul: {self.ad}, Qiymet: {self.qiymet} AZN, Stok: {self.stok}"
class Istifadeci:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email
        self.sifarisler = []

    def sifaris_et(self, mehsul, say):
        if mehsul.stokdan_azalt(say):
            sifaris = {"mehsul": mehsul.ad, "say": say, "umumi": mehsul.qiymet * say}
            self.sifarisler.append(sifaris)
            print(f"{self.ad} {mehsul.ad} mehsulundan {say} dene sifaris verdi.")
        else:
            print(f"Sifaris olmadi, stok yetmedi.")

    def sifarisler_goster(self):
        if not self.sifarisler:
            print(f"{self.ad} henuz sifaris vermeyib.")
            return
        print(f"{self.ad} - Sifarisler:")
        for s in self.sifarisler:
            print(f"{s['mehsul']} - {s['say']} dene, Umumi: {s['umumi']} AZN")
mehsul1 = Mehsul("Telefon", 1050, 5)
mehsul2 = Mehsul("Planşet", 1300, 2)
istifadeci1 = Istifadeci("Elvin", "elvin@example.com")

istifadeci1.sifaris_et(mehsul1, 2)
istifadeci1.sifaris_et(mehsul2, 1)
istifadeci1.sifaris_et(mehsul2, 2)
istifadeci1.sifarisler_goster()

print(mehsul1.melumat())
print(mehsul2.melumat())