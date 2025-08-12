class Telebe:

    def __init__(self, ad):
        self.ad = ad
        self.qiymetler = []

    def qiymet_elave_et(self, qiymet):
        if 0 <= qiymet <= 100:
            self.qiymetler.append(qiymet)
            print(f"{self.ad} ucun {qiymet} bal elave edildi.")
        else:
            print("Qiymet 0 ile 100 arasinda olmalidir!")

    def ortalama_hesabla(self):
        if self.qiymetler:
            ortalama = sum(self.qiymetler) / len(self.qiymetler)
            print(f"{self.ad} telebesinin ortsalamasi: {ortalama:.2f}")
        else:
            print("Hele qiymet yoxdur.")

    def butun_qiymetleri_goster(self):
        print(f"{self.ad} telebesinin qiymetleri:")
        for qiymet in self.qiymetler:
            print(qiymet, end=" ")
        print()

telebe1 = Telebe("Aygun")
qiymetler = [90, 80, 75, 88]
for q in qiymetler:
    
    telebe1.qiymet_elave_et(q)
telebe1.butun_qiymetleri_goster()
telebe1.ortalama_hesabla()