class BankHesabi:
    def __init__(self, ad, balans=0):
        self.ad = ad
        self.__balans = balans

    def pul_yatir(self, miqdar):
        if miqdar > 0:
            self.__balans += miqdar
            print(f"{miqdar} manat yatırıldı. Yeni balans: {self.__balans} manat.")
        else:
            print("Miqdar musbet olmalıdır.")

    def pul_cek(self, miqdar):
        if 0 < miqdar <= self.__balans:
            self.__balans -= miqdar
            print(f"{miqdar} manat cekildi. Yeni balans: {self.__balans} manat.")
        else:
            print("Emeliyyat mumkun deyil: balans kifayet deyil ve ya miqdar yalnis.")

    def balans_goster(self):
        print(f"{self.ad} adlı hesabın balansı: {self.__balans} manat.")

if __name__ == "__main__":
    hesab = BankHesabi("Bahar", 2000)
    hesab.balans_goster()
    hesab.pul_yatir(600)
    hesab.pul_cek(200)
    hesab.pul_cek(1000)