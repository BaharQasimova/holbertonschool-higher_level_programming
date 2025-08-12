class Muellim:

    def __init__(self, ad, fenn, maas, is_gunu):

        self.ad = ad
        self.fenn = fenn
        self.maas = maas
        self.is_gunu = is_gunu

    def melumat_goster(self):
        print(f"Muellim: {self.ad}, Fenn: {self.fenn}, Maas: {self.maas} AZN, Is Gunu: {self.is_gunu} saat")
    def umumi_gelir_hesabla(self):

        return self.maas * self.is_gunu / 160
        
class Universitet:

    def __init__(self, ad):

        self.ad = ad
        self.muellimler = []

    def muellim_elave_et(self, muellim):
        self.muellimler.append(muellim)

    def muellimleri_goster(self):
        print(f"\n{self.ad}  muellimleri:")

        for m in self.muellimler:
            m.melumat_goster()
            
            print(f"Umumi gelir (nisbet): {m.umumi_gelir_hesabla():.2f} AZN\n")
muellim1 = Muellim("Bahar", "Tarix", 1800, 160)
muellim2 = Muellim("Tunar", "Fizika", 1700, 140)
uni = Universitet("Baki Dövlet Universiteti-nin")
uni.muellim_elave_et(muellim1)
uni.muellim_elave_et(muellim2)
uni.muellimleri_goster()