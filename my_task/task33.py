class Platforma:
    def __init__(self, ad):
        self.ad = ad
    def melumat_goster(self):
        print(f"Platforma: {self.ad}")

class Istifadeci:
    def __init__(self, ad, soyad, istifadeci_adi, platforma):
        self.ad = ad
        self.soyad = soyad
        self.istifadeci_adi = istifadeci_adi
        self.platforma = platforma
        self.paylasimlar = []

    def melumat_goster(self):
        print(f"Istifadeci: {self.ad} {self.soyad}, Istifadeci adi: @{self.istifadeci_adi}, Platforma: {self.platforma.ad}")
    def paylasim_elave_et(self, paylasim):
        self.paylasimlar.append(paylasim)
        print(f"Yeni paylasim elave olundu: {paylasim.basliq}")

class Paylasim:
    def __init__(self, basliq, metn):
        self.basliq = basliq
        self.metn = metn
        self.beyenmeler = 0
        self.serhler = []
    def melumat_goster(self):
        print(f"Paylasim: {self.basliq}, Beyenme sayi: {self.beyenmeler}, Serhler: {len(self.serhler)}")
    def beyen(self):
        self.beyenmeler += 1
    def serh_elave_et(self, serh):
        self.serhler.append(serh)

class Serh:
    def __init__(self, istifadeci, metn):
        self.istifadeci = istifadeci
        self.metn = metn
    def melumat_goster(self):
        print(f"Serh (@{self.istifadeci.istifadeci_adi}): {self.metn}")

class SosialMediaSistemi:
    def __init__(self):
        self.platformalar = []
        self.istifadeciler = []
    def platforma_elave_et(self, platforma):
        self.platformalar.append(platforma)
    def istifadeci_elave_et(self, istifadeci):
        self.istifadeciler.append(istifadeci)
    def butun_platformalari_goster(self):
        print("\nPlatformalar:")
        for p in self.platformalar:
            p.melumat_goster()
    def butun_istifadecileri_goster(self):
        print("\nIstifadeciler:")
        for i in self.istifadeciler:
            i.melumat_goster()
    def butun_paylasimlari_goster(self):
        print("\nPaylasimlar:")
        for i in self.istifadeciler:
            for p in i.paylasimlar:
                p.melumat_goster()

instagram = Platforma("Instagram")
facebook = Platforma("Facebook")
threads = Platforma("Threads")
istifadeci1 = Istifadeci("Aytac", "Quliyeva", "aytac123", instagram)
istifadeci2 = Istifadeci("Rasim", "Mammadov", "rasim_m", facebook)
istifadeci3 = Istifadeci("Leyla", "Ismayilova", "leyla_i", threads)
paylasim1 = Paylasim("Yay tatili", "Dostlarla gozəl vaxt kecirdim.")
paylasim2 = Paylasim("Yeni kitab", "Oxudugum kitabi sizinle paylasiram.")
serh1 = Serh(istifadeci2, "Cox gozeldir!")
serh2 = Serh(istifadeci1, "Tesekkurler!")

paylasim1.beyen()
paylasim1.beyen()
paylasim1.serh_elave_et(serh1)
paylasim2.serh_elave_et(serh2)
istifadeci1.paylasim_elave_et(paylasim1)
istifadeci2.paylasim_elave_et(paylasim2)
sistem = SosialMediaSistemi()
sistem.platforma_elave_et(instagram)
sistem.platforma_elave_et(facebook)
sistem.platforma_elave_et(threads)
sistem.istifadeci_elave_et(istifadeci1)
sistem.istifadeci_elave_et(istifadeci2)
sistem.istifadeci_elave_et(istifadeci3)
sistem.butun_platformalari_goster()
sistem.butun_istifadecileri_goster()
sistem.butun_paylasimlari_goster()