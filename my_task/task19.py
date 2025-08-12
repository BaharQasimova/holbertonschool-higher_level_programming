class ElektronKitab:

    def __init__(self, ad, muellif, janr, sehife_sayi, qiymet):
        self.ad = ad
        self.muellif = muellif
        self.janr = janr
        self.sehife_sayi = sehife_sayi
        self.qiymet = qiymet

    def melumat_goster(self):
        print(f"Kitab: {self.ad}, Muellif: {self.muellif}, Janr: {self.janr}, Sehife sayi: {self.sehife_sayi}, Qiymet: {self.qiymet} AZN")
class Musteri:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email

    def melumat_goster(self):
        print(f"Musteri: {self.ad}, Email: {self.email}")

class Sifaris:
    def __init__(self, musteri):
        self.musteri = musteri
        self.kitablar = []

    def kitab_elave_et(self, kitab):
        self.kitablar.append(kitab)

    def umumi_qiymet_hesabla(self):
        return sum(kitab.qiymet for kitab in self.kitablar)
        
    def melumat_goster(self):
        print(f"\nSifaris sahibi: {self.musteri.ad}")
        print("Sifarisdeki kitablar:")
        for kitab in self.kitablar:
            kitab.melumat_goster()
        print(f"Umumi qiymet: {self.umumi_qiymet_hesabla()} AZN")
muveffeq_kitab = ElektronKitab("Qara Qelem", "Mirze Şəfi Vazeh", "Ədəbiyyat", 250, 15)
tarix_kitab = ElektronKitab("Azərbaycan Tarixi", "Əhməd Cavad", "Tarix", 320, 20)
musteri1 = Musteri("Leyla", "leyla@example.com")
sifaris1 = Sifaris(musteri1)
sifaris1.kitab_elave_et(muveffeq_kitab)
sifaris1.kitab_elave_et(tarix_kitab)
sifaris1.melumat_goster()
