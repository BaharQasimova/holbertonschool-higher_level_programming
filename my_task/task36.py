class Otaq:
    
    def __init__(self, nomre, nov, qiymet):
        self.nomre = nomre
        self.nov = nov
        self.qiymet = qiymet
        self.rezerv = False

    def melumat_goster(self):
        status = "Rezerv olunub" if self.rezerv else "Bosdur"
        print(f"Otaq {self.nomre} - {self.nov} - {self.qiymet} AZN/gun - {status}")
    def rezerv_et(self):
        if not self.rezerv:
            self.rezerv = True
            print(f"Otaq {self.nomre} ugurla rezerv olundu.")
        else:
            print(f"Otaq {self.nomre} artiq rezerv olunub.")

    def rezerv_legev_et(self):
        if self.rezerv:
            self.rezerv = False
            print(f"Otaq {self.nomre} rezerv legv edildi.")
        else:
            print(f"Otaq {self.nomre} artiq bosdur.")

class Musteri:
    def __init__(self, ad, soyad, telefon):
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
    def melumat_goster(self):
        print(f"Musteri: {self.ad} {self.soyad}, Telefon: {self.telefon}")

class OtelSistemi:

    def __init__(self):
        self.otaqlar = []
        self.musteriler = []
    def otaq_elave_et(self, otaq):
        self.otaqlar.append(otaq)
    def musteri_elave_et(self, musteri):
        self.musteriler.append(musteri)
    def butun_otaqlari_goster(self):
        print("\nOtaqlar:")
        for otaq in self.otaqlar:
            otaq.melumat_goster()
    def butun_musterileri_goster(self):
        print("\nMusteriler:")
        for m in self.musteriler:
            m.melumat_goster()

otaq1 = Otaq(101, "Tek neferlik", 80)
otaq2 = Otaq(102, "Iki neferlik", 100)
otaq3 = Otaq(110, "Lux", 200)
musteri1 = Musteri("Nigar", "Zeynalova", "+994774775767")

otel = OtelSistemi()

otel.otaq_elave_et(otaq1)
otel.otaq_elave_et(otaq2)
otel.otaq_elave_et(otaq3)
otel.musteri_elave_et(musteri1)
otel.butun_otaqlari_goster()
otel.butun_musterileri_goster()
otaq2.rezerv_et()
otaq2.rezerv_et()
otaq2.rezerv_legev_et()