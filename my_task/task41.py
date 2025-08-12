class Eser:

    def __init__(self, ad, muellif, tip, yer):

        self.ad = ad
        self.muellif = muellif
        self.tip = tip
        self.yer = yer

    def melumat(self):
        
        return f"Eser: {self.ad}, Muellif: {self.muellif}, Tip: {self.tip}, Yer: {self.yer}"
class Sergi:

    def __init__(self, ad):

        self.ad = ad
        self.eserler = []

    def eser_elave_et(self, eser):

        self.eserler.append(eser)

    def sergi_melumat(self):

        melumatlar = [eser.melumat() for eser in self.eserler]
        return f"Sergi: {self.ad}\n" + "\n".join(melumatlar)

sergi = Sergi("Baku Sanat Galerisi")
eser1 = Eser("Yasil ev", "Leyla Abdulova", "Resim", "Zal 1")
eser2 = Eser("Abstrakt Heykel", "Elmir Aliyev", "Heykel", "Zal 2")
eser3 = Eser("Seheng", "Nahid Seymurov", "Gil qab", "Zal 3")

sergi.eser_elave_et(eser1)
sergi.eser_elave_et(eser2)
sergi.eser_elave_et(eser3)

print(sergi.sergi_melumat())