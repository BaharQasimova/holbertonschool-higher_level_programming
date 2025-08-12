class Mahni:

    def __init__(self, adi, muellif, bestekar, not_sayi):

        self.adi = adi
        self.muellif = muellif
        self.bestekar = bestekar
        self.not_sayi = not_sayi

    def melumat_goster(self):

        print(f"Mahni adi: {self.adi}, Muellif: {self.muellif}, Bestekar: {self.bestekar}, Not sayi: {self.not_sayi}")
class MusiqiQalereyasi:

    def __init__(self):
        self.mahnilar = []

    def mahni_elave_et(self, mahni):
        self.mahnilar.append(mahni)

    def butun_mahnilari_goster(self):

        print("\nMusiqi Qalereyasindaki mahnilar:")

        for m in self.mahnilar:
            m.melumat_goster()

galereya = MusiqiQalereyasi()
mahni1 = Mahni("Sari Gelin", "Azerbaycan xalq mahnisi", "Xalq", 32)
mahni2 = Mahni("Leyla", "Fikret Amirov", "Fikret Amirov", 48)

galereya.mahni_elave_et(mahni1)
galereya.mahni_elave_et(mahni2)
galereya.butun_mahnilari_goster()