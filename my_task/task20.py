class Kosmonavt:

    def __init__(self, ad, yas, tecrube):
        self.ad = ad
        self.yas = yas
        self.tecrube = tecrube

    def melumat_goster(self):
        print(f"Kosmonavt: {self.ad}, Yas: {self.yas}, Tecrube: {self.tecrube} il")
class Peyk:
    def __init__(self, ad, tip, orbit_vaxti):
        self.ad = ad
        self.tip = tip
        self.orbit_vaxti = orbit_vaxti

    def melumat_goster(self):
        print(f"Peyk: {self.ad}, Tip: {self.tip}, Orbit vaxti: {self.orbit_vaxti} gun")
class Missiya:
    def __init__(self, ad, yer, vaxt, marsda_heyat_veziyyeti=False):
        self.ad = ad
        self.yer = yer
        self.vaxt = vaxt
        self.marsda_heyat_veziyyeti = marsda_heyat_veziyyeti
        self.kosmonavtlar = []
        self.peykler = []

    def kosmonavt_elave_et(self, kosmonavt):
        self.kosmonavtlar.append(kosmonavt)

    def peyk_elave_et(self, peyk):
        self.peykler.append(peyk)
        
    def melumat_goster(self):
        print(f"\nMissiya: {self.ad}, Yer: {self.yer}, Vaxt: {self.vaxt}")
        print(f"Marsda heyat veziyyeti: {'Var' if self.marsda_heyat_veziyyeti else 'Yoxdur'}")
        print("Kosmonavtlar:")
        for k in self.kosmonavtlar:
            k.melumat_goster()
        print("Peykler:")
        for p in self.peykler:
            p.melumat_goster()
kosmos_missiyasi = Missiya("Arasdirma", "Mars", "2025", marsda_heyat_veziyyeti=True)
kosmonavt1 = Kosmonavt("Teymur", 30, 12)
kosmonavt2 = Kosmonavt("Fidan", 33, 8)
peyk1 = Peyk("Hubble", "Kosmik teleskop", 3650)
peyk2 = Peyk("Mars Orbiter", "Arasdirma peyki", 180)
kosmos_missiyasi.kosmonavt_elave_et(kosmonavt1)
kosmos_missiyasi.kosmonavt_elave_et(kosmonavt2)
kosmos_missiyasi.peyk_elave_et(peyk1)
kosmos_missiyasi.peyk_elave_et(peyk2)
kosmos_missiyasi.melumat_goster()