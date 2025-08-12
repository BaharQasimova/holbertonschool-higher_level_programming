class Car:

    def __init__(self, marka, reng, suret=0):

        self.marka = marka
        self.reng = reng
        self.suret = suret

    def sureti_artir(self, artim):

        self.suret += artim
        print(f"Suret artirildi: {self.suret} km/saat")

    def sureti_azalt(self, azalma):

        self.suret -= azalma
        if self.suret < 0:
            self.suret = 0

        print(f"Suret azaldildi: {self.suret} km/saat")

    def melumat(self):

        print(f"Marka: {self.marka}, Rəng: {self.reng}, Suret: {self.suret} km/saat")
my_car = Car("BMW", "boz")
my_car.melumat()

my_car.sureti_artir(80)
my_car.sureti_azalt(30)

my_car.melumat()