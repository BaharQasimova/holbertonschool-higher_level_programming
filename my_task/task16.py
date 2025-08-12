class Komanda:
    def __init__(self, ad, oyun_sayi, qalib_sayi, maglubiyyet_sayi):
        self.ad = ad
        self.oyun_sayi = oyun_sayi
        self.qalib_sayi = qalib_sayi
        self.maglubiyyet_sayi = maglubiyyet_sayi

    def melumat_goster(self):
        print(f"Komanda: {self.ad}, Oyunlar: {self.oyun_sayi}, Qalibler: {self.qalib_sayi}, Maglubiyyetler: {self.maglubiyyet_sayi}")
class BasketbolYarisi:
    def __init__(self, yer, tarix):
        self.yer = yer
        self.tarix = tarix
        self.komandalar = []
        self.qalib = None

    def komanda_elave_et(self, komanda):
        self.komandalar.append(komanda)

    def qalibi_təyin_et(self, komanda):
        if komanda in self.komandalar:
            self.qalib = komanda
        else:
            print("Qalib komandalar siyahisinda deyil")
            
    def melumat_goster(self):
        print(f"\nBasketbol Yarisi: Yer: {self.yer}, Tarix: {self.tarix}")
        print("Iştirak edən komandalar:")
        for k in self.komandalar:
            k.melumat_goster()
        if self.qalib:
            print(f"Qalib: {self.qalib.ad}")
        else:
            print("Qalib təyin olunmayıb")
komanda1 = Komanda("Baku Eagles", 15, 10, 5)
komanda2 = Komanda("Sumqayit Sharks", 15, 8, 7)
yarish = BasketbolYarisi("Baku Sport Complex", "2025-10-20")
yarish.komanda_elave_et(komanda1)
yarish.komanda_elave_et(komanda2)
yarish.qalibi_təyin_et(komanda1)
yarish.melumat_goster()