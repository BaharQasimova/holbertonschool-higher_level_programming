class Doyuscu:

    def __init__(self, ad, cekisi, fight_class):

        self.ad = ad
        self.cekisi = cekisi
        self.fight_class = fight_class
        self.qelebeler = 0
        self.meglubiyyetler = 0
    def melumat_goster(self):
        print(f"Doyuscu: {self.ad}, Cekisi: {self.cekisi} kg, Fight class: {self.fight_class}, Qelebeler: {self.qelebeler}, Meglubiyyetler: {self.meglubiyyetler}")
    def qelebe_qazan(self):
        self.qelebeler += 1
    def meglub_ol(self):
        self.meglubiyyetler += 1

class Doyus:

    def __init__(self, yer, tarix):

        self.yer = yer
        self.tarix = tarix
        self.doyusculer = []

    def doyuscu_elave_et(self, doyuscu):

        if len(self.doyusculer) < 2:
            self.doyusculer.append(doyuscu)

    def qalibi_tap(self):

        if len(self.doyusculer) < 2:
            return None
        if self.doyusculer[0].qelebeler > self.doyusculer[1].qelebeler:
            return self.doyusculer[0]
        elif self.doyusculer[1].qelebeler > self.doyusculer[0].qelebeler:
            return self.doyusculer[1]
        else:
            return None

    def melumat_goster(self):

        print(f"Doyus yeri: {self.yer}, Tarix: {self.tarix}")

        for d in self.doyusculer:

            d.melumat_goster()
        qalib = self.qalibi_tap()

        if qalib:
            print(f"Qalib: {qalib.ad}")
        else:
            print("Qalib yoxdur ve ya beraber netice.")

mma_doyus = Doyus("Baku Arena", "2025-10-10")
doyuscu1 = Doyuscu("Eldar", 70, "Lightweight")
doyuscu2 = Doyuscu("Murad", 72, "Middleweight")
doyuscu1.qelebe_qazan()
doyuscu2.meglub_ol()

mma_doyus.doyuscu_elave_et(doyuscu1)
mma_doyus.doyuscu_elave_et(doyuscu2)
mma_doyus.melumat_goster()