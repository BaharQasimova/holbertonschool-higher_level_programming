class Surucu:

    def __init__(self, ad, komanda):

        self.ad = ad
        self.komanda = komanda
        self.xal = 0

    def melumat_goster(self):

        print(f"Surucu: {self.ad}, Komanda: {self.komanda}, Xal: {self.xal}")
    def xal_elave_et(self, xal):
        self.xal += xal

class Yaris:
    
    def __init__(self, ad, tarix):
        self.ad = ad
        self.tarix = tarix
        self.suruculer = []

    def surucu_elave_et(self, surucu):
        self.suruculer.append(surucu)

    def qalibi_tap(self):
        if not self.suruculer:
            return None
        qalib = max(self.suruculer, key=lambda s: s.xal)
        return qalib

    def neticeleri_goster(self):
        print(f"Yaris: {self.ad}, Tarix: {self.tarix}")
        for s in self.suruculer:
            s.melumat_goster()

        qalib = self.qalibi_tap()
        if qalib:
            print(f"Qalib: {qalib.ad} ({qalib.komanda}) - {qalib.xal} xal")

class Formula1:

    def __init__(self):
        self.yarislari = []

    def yaris_elave_et(self, yaris):
        self.yarislari.append(yaris)

    def butun_yarislari_goster(self):
        print("\nFormula 1 Yarislari:")

        for y in self.yarislari:
            y.neticeleri_goster()

surucu1 = Surucu("Max Verstappen", "Red Bull")
surucu2 = Surucu("Lewis Hamilton", "Mercedes")
yaris1 = Yaris("Baku GP", "2025-25-05")

yaris1.surucu_elave_et(surucu1)
yaris1.surucu_elave_et(surucu2)
surucu1.xal_elave_et(25)
surucu2.xal_elave_et(18)

formula1 = Formula1()
formula1.yaris_elave_et(yaris1)
formula1.butun_yarislari_goster()