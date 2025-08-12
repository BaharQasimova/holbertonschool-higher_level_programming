class Ders:

    def __init__(self, ad, muddet):
        self.ad = ad
        self.muddet = muddet

    def melumat_goster(self):
        print(f"Ders: {self.ad}, Muddet: {self.muddet} saat")
class VideoDers(Ders):

    def __init__(self, ad, muddet, video_link):
        super().__init__(ad, muddet)
        self.video_link = video_link

    def melumat_goster(self):
        print(f"Video Ders: {self.ad}, Muddet: {self.muddet} saat, Video link: {self.video_link}")
class CanliDers(Ders):

    def __init__(self, ad, muddet, tarix, saat):
        super().__init__(ad, muddet)
        self.tarix = tarix
        self.saat = saat

    def melumat_goster(self):
        print(f"Canli Ders: {self.ad}, Muddet: {self.muddet} saat, Tarix: {self.tarix}, Saat: {self.saat}")
class OnlaynDersler:

    def __init__(self):
        self.dersler = []

    def ders_elave_et(self, ders):
        self.dersler.append(ders)

    def butun_dersleri_goster(self):
        print("\nButun onlayn dersler:")

        for d in self.dersler:
            d.melumat_goster()

video_ders1 = VideoDers("Riyaziyyat", 2, "https://video_link.com/riyaziyyat")
canli_ders1 = CanliDers("Fizika", 1.5, "2025-08-15", "15:00")
onlayn_dersler = OnlaynDersler()

onlayn_dersler.ders_elave_et(video_ders1)
onlayn_dersler.ders_elave_et(canli_ders1)
onlayn_dersler.butun_dersleri_goster()