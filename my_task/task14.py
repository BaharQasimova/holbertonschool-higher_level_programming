class Animal:
    def __init__(self, ad, yas):
        self.__ad = ad
        self.__yas = yas
    def get_ad(self):
        return self.__ad
    def get_yas(self):
        return self.__yas
    def set_yas(self, yas):
        self.__yas = yas
    def set_ad(self, ad):
        self.__ad = ad
    def ses_ver(self):
        print(f"{self.__ad} Heyvan seslenir.")

class cat(Animal):
    def ses_ver(self):
        print(f"{self.get_ad()} Meow sesi cixarir.")

class dog(Animal):
    def ses_ver(self):
        print(f"{self.get_ad()} Hav sesi cixarir.")

animal1 = Animal("bulut", 4)
animal2 = Animal("qarabas", 3)
print(animal1.get_ad(), animal1.get_yas())
print(animal2.get_ad(), animal2.get_yas())

cat1 = cat("bulut", 4)
cat1.ses_ver()
dog1 = dog("qarabas", 3)
dog1.ses_ver()