
class Heyvan:
    def __init__(self, ad):
        self.ad = ad

    def ses_cixar(self):
        print(f"{self.ad} səssizdir.")


class Pisik(Heyvan):
    def ses_cixar(self):
        print(f"{self.ad} deyir: Miyav!")


class It(Heyvan):
    def ses_cixar(self):
        print(f"{self.ad} deyir: Hav hav!")

if __name__ == "__main__":
    pisik = Pisik("Pişik")
    it = It("İt")

    pisik.ses_cixar()  
    it.ses_cixar()     
