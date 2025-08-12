import random

class Komanda:

    def __init__(self, ad):
        self.ad = ad
        self.bal_sayi = 0
        self.oyun_sayi = 0
        self.qol_ferqi = 0

    def oyun_elave_et(self, vurulan_qol, buraxilan_qol):
        self.oyun_sayi += 1
        self.qol_ferqi += (vurulan_qol - buraxilan_qol)
        if vurulan_qol > buraxilan_qol:
            self.bal_sayi += 3
        elif vurulan_qol == buraxilan_qol:
            self.bal_sayi += 1

    def __repr__(self):
        return f"{self.ad}: xal={self.bal_sayi}, oyun={self.oyun_sayi}, ferq={self.qol_ferqi}"
class TurkiyeSuperLiqasi:

    def __init__(self):
        self.komandalar = {}

    def komanda_elave_et(self, komanda: Komanda):
        self.komandalar[komanda.ad] = komanda

    def oyun_yaz(self, ev_adi, qonaq_adi, ev_qol, qonaq_qol):
        ev = self.komandalar.get(ev_adi)
        qonaq = self.komandalar.get(qonaq_adi)
        if not ev or not qonaq:
            raise ValueError("Komanda tapilmadi.")
        ev.oyun_elave_et(ev_qol, qonaq_qol)
        qonaq.oyun_elave_et(qonaq_qol, ev_qol)

    def cedvel(self):
        return sorted(self.komandalar.values(),
                      key=lambda k: (k.bal_sayi, k.qol_ferqi, k.ad),
                      reverse=True)

    def cedveli_goster(self):
        print("Turkiye Super Liqasi - Cedvel")
        print("Sira | Komanda       | Xal  | Oyun | Qol ferqi")
        for sira, komanda in enumerate(self.cedvel(), start=1):
            print(f"{sira:>4} | {komanda.ad:<12} | {komanda.bal_sayi:>3}  | {komanda.oyun_sayi:>4} | {komanda.qol_ferqi:>9}")
    def kubok_sahibi(self):
        return self.cedvel()[0].ad

if __name__ == "__main__":
    liqa = TurkiyeSuperLiqasi()
    g = Komanda("Galatasaray")
    b = Komanda("Besiktas")
    f = Komanda("Fenerbahce")
    liqa.komanda_elave_et(g)
    liqa.komanda_elave_et(b)
    liqa.komanda_elave_et(f)
    komandalar = ["Galatasaray", "Besiktas", "Fenerbahce"]

    for ev in komandalar:
        for qonaq in komandalar:
            if ev != qonaq:
                if ev == "Galatasaray":
                    ev_qol = random.randint(2, 4)
                    qonaq_qol = random.randint(0, 2)
                elif qonaq == "Galatasaray":
                    ev_qol = random.randint(0, 2)
                    qonaq_qol = random.randint(2, 4)
                else:
                    ev_qol = random.randint(0, 3)
                    qonaq_qol = random.randint(0, 3)
                liqa.oyun_yaz(ev, qonaq, ev_qol, qonaq_qol)

    liqa.cedveli_goster()
    print("\nKubok sahibi:", liqa.kubok_sahibi())