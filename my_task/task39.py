class KinoSerial:

    def __init__(self, ad, janr, il, tip, reytinq=0):
        
        self.ad = ad
        self.janr = janr
        self.il = il
        self.tip = tip
        self.reytinq = reytinq

    def reytinq_elave_et(self, yeni_reytinq):

        if 0 <= yeni_reytinq <= 10:
            if self.reytinq == 0:
                self.reytinq = yeni_reytinq
            else:
                self.reytinq = (self.reytinq + yeni_reytinq) / 2
        else:
            print("Reytinq 0-10 araliginda olmalidir.")

    def melumat(self):

        return (f"{self.ad} ({self.tip}), Janr: {self.janr}, il: {self.il}, "
                f"Reytinq: {round(self.reytinq,1)}")

film = KinoSerial("Forsaj", "dram", 1900, "kino")
serial = KinoSerial("Aramizda qalsin", "komediya", 2000, "serial", 9)

print(film.melumat())
film.reytinq_elave_et(8)

print(film.melumat())
print(serial.melumat())

serial.reytinq_elave_et(7)
print(serial.melumat())