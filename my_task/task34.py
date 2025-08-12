class Stansiya:
    def __init__(self, ad, xett):
        self.ad = ad
        self.xett = xett
    def melumat_goster(self):
        print(f"Stansiya: {self.ad}, Xett: {self.xett}")

class Qatar:
    def __init__(self, nomre, tutum):
        self.nomre = nomre
        self.tutum = tutum
        self.sernisin_sayi = 0

    def melumat_goster(self):
        print(f"Qatar {self.nomre} - Tutum: {self.tutum}, Sernisin sayi: {self.sernisin_sayi}")
    def sernisin_minik(self, say):
        if self.sernisin_sayi + say <= self.tutum:
            self.sernisin_sayi += say
            print(f"{say} nefer qatara minik etdi.")
        else:
            print("Qatarin tutumu doludur, elave minik mumkun deyil.")

    def sernisin_dusen(self, say):
        if say <= self.sernisin_sayi:
            self.sernisin_sayi -= say
            print(f"{say} nefer qatardan dusdu.")
        else:
            print("Bu qeder sernisin yoxdur.")

class MetroSistemi:
    def __init__(self):
        self.stansiyalar = []
        self.qatarlar = []
    def stansiya_elave_et(self, stansiya):
        self.stansiyalar.append(stansiya)
    def qatar_elave_et(self, qatar):
        self.qatarlar.append(qatar)
    def butun_stansiyalari_goster(self):
        print("\nStansiyalar:")
        for s in self.stansiyalar:
            s.melumat_goster()
    def butun_qatarlari_goster(self):
        print("\nQatarlar:")
        for q in self.qatarlar:
            q.melumat_goster()
            
st1 = Stansiya("28 May", "Yasil Xett")
st2 = Stansiya("8 Noyabr", "Benovseyi Xett")
q1 = Qatar(1, 200)
q2 = Qatar(2, 180)
metro = MetroSistemi()
metro.stansiya_elave_et(st1)
metro.stansiya_elave_et(st2)
metro.qatar_elave_et(q1)
metro.qatar_elave_et(q2)
metro.butun_stansiyalari_goster()
metro.butun_qatarlari_goster()
q1.sernisin_minik(50)
q1.sernisin_minik(160)
q1.sernisin_dusen(30)