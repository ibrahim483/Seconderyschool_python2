class Bok:

    def __init__(self, titeln, förffatare, sidor, puplaceras):
        self.titeln = titeln
        self.förffatare = förffatare
        self.sidor = sidor
        self.puplaceras = puplaceras
        self.is_on= False


    def start_reading(self):
        self.is_on= True

    def stop_reading(self):
        self.is_on= False

#the_reader = input("skriv in läsarensnamn ")
#the_reader_1 = input("skriv in läsarensnamn ")
class Action(Bok):
    def __init__(self, titeln, förffatare, sidor, puplaceras):
        super().__init__(titeln, förffatare, sidor, puplaceras)


    def read (self):
        print("läser ")

class Herror(Bok):
    def __init__(self, titeln, förffatare, sidor, puplaceras):
        super().__init__(titeln, förffatare, sidor, puplaceras)


    def read(self):
        print("läser")


action_bok = Bok("Outsiders", "S.E. Hinton", "192", "24 april 1967")
heror_bok = Bok("Dracula", "Bram Stoker", "418", "26 maj 1897")

Action.read()