from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Masinin muherriki ise dusdu.")

    def stop_engine(self):
        print("Masinin muherriki dayandi.")

class Bicycle(Vehicle):
    
    def start_engine(self):
        print("Velosiped surmeye hazirdir, muherrik yoxdur.")

    def stop_engine(self):
        print("Velosiped dayandi.")

if __name__ == "__main__":
    car = Car()
    bike = Bicycle()

    car.start_engine()
    car.stop_engine()

    bike.start_engine()
    bike.stop_engine()