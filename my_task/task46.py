class Restoran:

    def __init__(self, ad):
        self.ad = ad
        self.menyu = {}
        self.sifarisler = {}
        
    def yemek_elave_et(self, yemek, qiymet):
        self.menyu[yemek] = qiymet
        print(f"{yemek} menyuya elave edildi ({qiymet} AZN)")

    def menyunu_goster(self):
        print(f"\n {self.ad} restoraninin menyusu:")
        for yemek, qiymet in self.menyu.items():
            print(f"- {yemek}: {qiymet} AZN")

    def sifaris_elave_et(self, yemek, miqdar):
        if yemek in self.menyu:
            if yemek in self.sifarisler:
                self.sifarisler[yemek] += miqdar
            else:
                self.sifarisler[yemek] = miqdar
            print(f"{miqdar} eded {yemek} sifaris edildi.")
        else:
            print(f"{yemek} menyuda yoxdur!")

    def sifarisleri_goster(self):
        print("\n (Sifarisler:")
        if not self.sifarisler:
            print("Hec bir sifaris yoxdur.")
            return
        for yemek, miqdar in self.sifarisler.items():
            print(f"- {yemek}: {miqdar} eded")

    def hesab_goster(self):
        toplam = 0
        for yemek, miqdar in self.sifarisler.items():
            toplam += self.menyu[yemek] * miqdar
        print(f"\n Umumi hesab: {toplam} AZN")

restoran = Restoran("AILE")
restoran.yemek_elave_et("Kabab", 13)
restoran.yemek_elave_et("Pizza", 17)
restoran.yemek_elave_et("Çay", 2.5)
restoran.yemek_elave_et("Salat", 4)
restoran.yemek_elave_et("Doner", 3)
restoran.yemek_elave_et("Pepsi", 1.2)
restoran.yemek_elave_et("Sirniyyat", 3)
restoran.yemek_elave_et("Pive", 2.6)
restoran.menyunu_goster()

while True:
    yemek = input("\nSifaris etmek istediyiniz yemeyi yazin ('stop' yazib bitirin): ")
    if yemek.lower() == "stop":
        break
    if yemek not in restoran.menyu:
        print("Bu yemek menyuda yoxdur!")
        continue
    try:
        miqdar = int(input(f"{yemek} ucun miqdari daxil edin: "))
        restoran.sifaris_elave_et(yemek, miqdar)
    except ValueError:
        print("Miqdar reqem olmalidir!")
        
restoran.sifarisleri_goster()
restoran.hesab_goster()