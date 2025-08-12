class YemekResepti:
    def __init__(self, ad, terkibi, hazirlanma_vaxti, porsiya_sayi):
        self.ad = ad
        self.terkibi = terkibi
        self.hazirlanma_vaxti = hazirlanma_vaxti
        self.porsiya_sayi = porsiya_sayi

    def melumat_goster(self):
        print(f"Yemek: {self.ad}")
        print(f"Terkibi: {self.terkibi}")
        print(f"Hazirlanma vaxti: {self.hazirlanma_vaxti} deq")
        print(f"Porsiya sayı: {self.porsiya_sayi}")

class QonaqUcunMenyu:
    def __init__(self, qonaq_sayi):
        self.qonaq_sayi = qonaq_sayi
        self.yemekler = []

    def yemek_elave_et(self, yemek):
        self.yemekler.append(yemek)

    def menyu_goster(self):
        print(f"\nQonaq sayi: {self.qonaq_sayi}")
        print("Menyu:")
        for yemek in self.yemekler:
            yemek.melumat_goster()
            
resept1 = YemekResepti("Dovga", "Qatiq, duyu, kesnis, nane, yumurta, un, sarimsaq", 40, 4)
resept2 = YemekResepti("Yarpaq dolmasi", "Uzum yarpagi, duyu, sogan, mal eti, yag, duz, istiot, nane", 90, 6)
resept3 = YemekResepti("Piti", "Qoyun eti, noxud, sogan, kartof, yag", 120, 6)
menyu = QonaqUcunMenyu(10)
menyu.yemek_elave_et(resept1)
menyu.yemek_elave_et(resept2)
menyu.yemek_elave_et(resept3)
menyu.menyu_goster()