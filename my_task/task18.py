class Heyvan:
    def __init__(self, ad, nov, yas, saglamliq_veziyyeti):
        self.ad = ad
        self.nov = nov
        self.yas = yas
        self.saglamliq_veziyyeti = saglamliq_veziyyeti

    def melumat_goster(self):
        print(f"Heyvan: {self.ad}, Novu: {self.nov}, Yasi: {self.yas}, Saglamliq veziyyeti: {self.saglamliq_veziyyeti}")
class Sahiplenme:
    def __init__(self, heyvan, sahibe_ad, tarix):
        self.heyvan = heyvan
        self.sahibe_ad = sahibe_ad
        self.tarix = tarix

    def melumat_goster(self):
        print(f"Sahiplenme: {self.sahibe_ad}, Tarix: {self.tarix}")
        self.heyvan.melumat_goster()

class Baytar:
    def __init__(self, ad, ixtisas, tecrube):
        self.ad = ad
        self.ixtisas = ixtisas
        self.tecrube = tecrube

    def melumat_goster(self):
        print(f"Baytar: {self.ad}, Ixtisas: {self.ixtisas}, Tecrube: {self.tecrube} il")
class Qida:
    def __init__(self, ad, nov, miqdar):
        self.ad = ad
        self.nov = nov
        self.miqdar = miqdar

    def melumat_goster(self):
        print(f"Qida: {self.ad}, Novu: {self.nov}, Miqdar: {self.miqdar}")
        
heyvan1 = Heyvan("Qara", "It", 4, "Normal")
baytar1 = Baytar("Ramil", "Baytar", 10)
qida1 = Qida("It yemi", "Quru", "5 kg")
sahiplenme1 = Sahiplenme(heyvan1, "Aynur", "2024-10-01")
heyvan1.melumat_goster()
baytar1.melumat_goster()
qida1.melumat_goster()
sahiplenme1.melumat_goster()