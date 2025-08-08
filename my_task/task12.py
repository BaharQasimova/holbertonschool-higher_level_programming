class Person:
    def __init__(self, ad, yas):
        self.ad = ad
        self.__yas = yas

    def yas_getir(self):
        return self.__yas

    def yas_set_et(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yas menfi ola bilmez!")

    def melumat_goster(self):
        print(f"Ad: {self.ad}, Yaş: {self.__yas}")

if __name__ == "__main__":
    insan = Person("Lale", 20)
    insan.melumat_goster()
    
    insan.yas_set_et(25)
    insan.melumat_goster()

    insan.yas_set_et(-5)