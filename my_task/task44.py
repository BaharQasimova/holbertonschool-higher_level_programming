class Futbolcu:

    def __init__(self, ad, movqe):
        self.ad = ad
        self.movqe = movqe
        self.qol_sayi = 0
        
    def qol_artir(self, say=1):
        self.qol_sayi += say

        print(f"{self.ad} {say} qol vurdu! Umumi qol sayi: {self.qol_sayi}")
    def melumat_goster(self):
        print(f"Futbolcu: {self.ad} | Movqe: {self.movqe} | Qol sayi: {self.qol_sayi}")
class Klub:

    def __init__(self, ad):
        self.ad = ad
        self.futbolcular = []

    def futbolcu_elave_et(self, futbolcu):
        self.futbolcular.append(futbolcu)
        print(f"{futbolcu.ad} kluba elave olundu.")

    def klub_qol_sayi(self):
        toplam = sum(f.qol_sayi for f in self.futbolcular)
        return toplam

    def melumat_goster(self):
        print(f"\nKlub: {self.ad}")
        print(f"Umumi qol sayi: {self.klub_qol_sayi()}")
        print("Futbolcular:")

        for futbolcu in self.futbolcular:
            futbolcu.melumat_goster()

klub1 = Klub("Qarabag")
f1 = Futbolcu("Kady Borges", "Hucumcu")
f2 = Futbolcu("Emin Mahmudov", "Yarimmudafieci")
f3 = Futbolcu("Toral Bayramov", "Mudafieci")

klub1.futbolcu_elave_et(f1)
klub1.futbolcu_elave_et(f2)
klub1.futbolcu_elave_et(f3)

f1.qol_artir(3)
f2.qol_artir(1)
f3.qol_artir(0)

klub1.melumat_goster()