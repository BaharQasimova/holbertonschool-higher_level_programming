class Forma:
    def sahe(self):
        pass

class Daire(Forma):
    def __init__(self, radius):
        self.radius = radius

    def sahe(self):
        return 4 * (self.radius ** 2)

class Kvadrat(Forma):
    def __init__(self, teref):
        self.teref = teref

    def sahe(self):
        return self.teref * self.teref

class Duzbucaqli(Forma):
    def __init__(self, en, uz):
        self.en = en
        self.uz = uz

    def sahe(self):
        return self.en * self.uz

def saheni_hesabla(forma: Forma):
    print(f"Sahe: {forma.sahe()}")

if __name__ == "__main__":
    formalar = [Daire(5), Kvadrat(4), Duzbucaqli(3, 7)]

    for f in formalar:
        saheni_hesabla(f)