class Sayici:

    def __init__(self, limit):

        self.limit = limit

    def for_ile_say(self):

        print("For dovru ile sayma:")

        for i in range(1, self.limit + 1):
            print(i, end=" ")
        print()

    def while_ile_say(self):

        print("While dovru ile sayma:")
        i = 1

        while i <= self.limit:
            print(i, end=" ")
            i += 1
        print()
        
sayici = Sayici(5)
sayici.for_ile_say()
sayici.while_ile_say()