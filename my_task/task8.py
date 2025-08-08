
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        

    def yas_haqqinda(self):
        print(f"{self.ad} {self.yas} yaşındadır.")

class Usaq(Insan):
    def yas_haqqinda(self):
        if self.yas < 18:
            print(f"{self.ad} uşaqdır və yaşı {self.yas}-dir.")
        else:
            print(f"{self.ad} artıq uşaq deyil!")

class Boyuk(Insan):
    def yas_haqqinda(self):
        if self.yas >= 18:
            print(f"{self.ad} böyüktür və yaşı {self.yas}-dir.")
        else:
            print(f"{self.ad} hələ böyüməyib!")
            
if __name__ == "__main__":
    usaqlar = Usaq("Bayram", 17)
    boyuklar = Boyuk("Bahar", 21)

    usaqlar.yas_haqqinda()
    boyuklar.yas_haqqinda() 