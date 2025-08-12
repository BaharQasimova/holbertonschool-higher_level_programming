class QacisYarisi:

    def __init__(self, mesafe):

        self.mesafe = mesafe
        self.yariscilar = []

    def yarisci_qat(self, ad):

        self.yariscilar.append({"ad": ad, "vaxt": None})

    def vaxt_yaz(self, ad, vaxt):
        
        for i in self.yariscilar:
            if i["ad"] == ad:
                i["vaxt"] = vaxt
                return
        print(f"{ad} adli yarisci tapilmadi.")

    def qalibi_tap(self):

        qalib = None
        en_yaxsi_vaxt = float('inf')
        for i in self.yariscilar:
            if i["vaxt"] is not None and i["vaxt"] < en_yaxsi_vaxt:
                en_yaxsi_vaxt = i["vaxt"]
                qalib = i["ad"]
        return qalib

yarish = QacisYarisi(1000)
yarish.yarisci_qat("Elmin")
yarish.yarisci_qat("Vusal")
yarish.vaxt_yaz("Elmin", 180)
yarish.vaxt_yaz("Vusal", 175)

print("Qalib:", yarish.qalibi_tap())