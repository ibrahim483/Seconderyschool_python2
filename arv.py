class Vehicle:
    def __init__(self, year, color): # Konstruktor
        self.year = year             # Tilldelar år och färg till objektet
        self.color = color
        self.is_on = False           # Boolean som avgör om fordonet är på eller av. False = av, True = på

    def start_vehicle(self):         # En funktion som startar fordonet
        self.is_on = True

    def stop_vehicle(self):          # En funktion som stänger av fordonet
        self.is_on = False

class Boat(Vehicle):                    # Skapar klassen Boat. Vi anger att Boat ärver från Vehicle

    def __init__(self, year, color):    # Konstruktor. Vi behöver year och color som inparametrar
        super().__init__(year, color)   # Kalla på superklassen, och ange egenskaperna

    def sail(self):                     # Funktion som gör att båten kan segla
        print("Seglar")

class Car(Vehicle):                          # Skapar klassen Car. Vi anger att Car ärver från Vehicle

    def __init__(self, year, color, brand):  # Konstruktor. Vi behöver year, color och brand som inparametrar
        super().__init__(year, color)        # Kalla på superklassen. Superklassen behöver year och color
        self.brand = brand                   # Car har i detta fall en extra egenskap, brand (modell)

    def drive(self):                         # Funktion som gör att bilen kör framåt
        print("Kör framåt")

boat = Boat("2000", "röd")      # Skapar ett objekt båt
car = Car(2019, "vit", "XC60")  # Skapar ett objekt bil

