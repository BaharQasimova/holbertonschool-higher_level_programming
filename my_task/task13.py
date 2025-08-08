class BoyukKicik:
    def __init__(self, eded1, eded2):
        self.eded1 = eded1
        self.eded2 = eded2

    def netice(self):
        if self.eded1 > self.eded2:
            return f"{self.eded1} boyukdur, {self.eded2} kicikdir."
        elif self.eded1 < self.eded2:
            return f"{self.eded2} boyukdur, {self.eded1} kicikdir."
        else:
            return "Her iki eded beraberdir."


numune = BoyukKicik(10, 7)
print(numune.netice())

numune2 = BoyukKicik(2, 8)
print(numune2.netice())

numune3 = BoyukKicik(3, 3)
print(numune3.netice())