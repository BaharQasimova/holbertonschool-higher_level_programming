
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        

    def yas_haqqinda(self):
        print(f"{self.ad} {self.yas}  yasindadir.")

class Usaq(Insan):
    def yas_haqqinda(self):
        if self.yas < 18:
            print(f"{self.ad} artiq usaqdir ve yasi {self.yas}-dir.")
        else:
            print(f"{self.ad} artiq usaq deyil!")

class Boyuk(Insan):
    def yas_haqqinda(self):
        if self.yas >= 18:
            print(f"{self.ad} boyukdur ve yasi {self.yas}-dir.")
        else:
            print(f"{self.ad} hele boyumeyib!")
            
if __name__ == "__main__":
    usaqlar = Usaq("Bayram", 17)
    boyuklar = Boyuk("Bahar", 21)

    usaqlar.yas_haqqinda()
    boyuklar.yas_haqqinda() 