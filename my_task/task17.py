class Komanda:

    def __init__(self, ad, oyun_sayi, qalib_sayi, beraberlik_sayi, maglubiyyet_sayi):
        self.ad = ad
        self.oyun_sayi = oyun_sayi
        self.qalib_sayi = qalib_sayi
        self.beraberlik_sayi = beraberlik_sayi
        self.maglubiyyet_sayi = maglubiyyet_sayi

    def melumat_goster(self):
        print(f"Komanda: {self.ad}, Oyun: {self.oyun_sayi}, Qalib: {self.qalib_sayi}, Beraberlik: {self.beraberlik_sayi}, Maglubiyyet: {self.maglubiyyet_sayi}")
class Turnir:
    def __init__(self, ad, yer, tarix):
        self.ad = ad
        self.yer = yer
        self.tarix = tarix
        self.komandalar = []

    def komanda_elave_et(self, komanda):
        self.komandalar.append(komanda)

    def melumat_goster(self):
        print(f"\nTurnir: {self.ad}, Yer: {self.yer}, Tarix: {self.tarix}")
        print("Iştirak eden komandalar:")
        for k in self.komandalar:
            k.melumat_goster()
            
komanda1 = Komanda("Real Madrid", 10, 7, 2, 1)
komanda2 = Komanda("Barcelona", 10, 6, 3, 1)
komanda3 = Komanda("Atletico Madrid", 10, 5, 4, 1)
turnir = Turnir("La Liga 2025", "Ispaniya", "2025-07-07")
turnir.komanda_elave_et(komanda1)
turnir.komanda_elave_et(komanda2)
turnir.komanda_elave_et(komanda3)
turnir.melumat_goster()