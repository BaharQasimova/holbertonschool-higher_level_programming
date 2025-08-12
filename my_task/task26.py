class Reklam:

    def __init__(self, ad, nov, muddet, qiymet):

        self.ad = ad
        self.nov = nov
        self.muddet = muddet
        self.qiymet = qiymet

    def melumat_goster(self):

        print(f"Reklam: {self.ad}, Novu: {self.nov}, Muddet: {self.muddet} gun, Qiymet: {self.qiymet} AZN")
class ReklamAgentliyi:

    def __init__(self, ad):

        self.ad = ad
        self.reklamlar = []

    def reklam_elave_et(self, reklam):

        self.reklamlar.append(reklam)

    def butun_reklamlari_goster(self):

        print(f"\n{self.ad} agentliyinin reklamlari:")
        for r in self.reklamlar:
            r.melumat_goster()

agentlik = ReklamAgentliyi("ASC Reklam")

reklam1 = Reklam("Yeni kampaniya", "TV reklam", 30, 2500)
reklam2 = Reklam("Yay endirimi", "Istirahet paketi", 15, 500)

agentlik.reklam_elave_et(reklam1)
agentlik.reklam_elave_et(reklam2)
agentlik.butun_reklamlari_goster()