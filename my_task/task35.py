class Telebe:
    def __init__(self, ad, soyad, qrup):
        self.ad = ad
        self.soyad = soyad
        self.qrup = qrup
        self.neticeler = {}
        
    def melumat_goster(self):
        print(f"Telebe: {self.ad} {self.soyad}, Qrup: {self.qrup}")
    def netice_elave_et(self, fənn, bal):
        self.neticeler[fənn] = bal

    def kesr_yoxla(self):
        kesr_fennler = [f for f, bal in self.neticeler.items() if bal < 51]
        if kesr_fennler:
            print(f"{self.ad} {self.soyad} asagidaki fennlerden kesilib: {', '.join(kesr_fennler)}")
        else:
            print(f"{self.ad} {self.soyad} butun fennlerden kecib.")

class ImtahanSistemi:
    def __init__(self):
        self.telebeler = []
    def telebe_elave_et(self, telebe):
        self.telebeler.append(telebe)
    def butun_telebeleri_goster(self):
        print("\nTelebeler:")
        for t in self.telebeler:
            t.melumat_goster()
    def kesr_siyahisini_goster(self):
        print("\nKesr olan telebeler:")
        for t in self.telebeler:
            t.kesr_yoxla()

telebe1 = Telebe("Huseyn", "Huseynov", "IT-102")
telebe2 = Telebe("Aytac", "Memmedova", "IT-103")
telebe1.netice_elave_et("Back-end", 45)
telebe1.netice_elave_et("Foundation", 78)
telebe2.netice_elave_et("Full Stak", 90)
telebe2.netice_elave_et("Fronted", 48)

sistem = ImtahanSistemi()
sistem.telebe_elave_et(telebe1)
sistem.telebe_elave_et(telebe2)
sistem.butun_telebeleri_goster()
sistem.kesr_siyahisini_goster()