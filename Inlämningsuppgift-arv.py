class Book:  # En class som heter Book, !!!class namn börjar alltid med en stor bokstav.
    def __init__(self, titel,
                 arthur):  # Skapat en metod och la till atributer som är använda i dennna klassen är titel och arthur.
        self.t = titel  # En sträng
        self.a = arthur  # En sträng

    def __str__(self):  # Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        return self.t + "\n" + self.a


class Audiobook(Book):  # En ny klass som arvar den gamla classen.
    def __str__(self):# Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        return self.t + " " + self.a + " " + str(self.v)

    def volym_set(self, volym):  # EN funktion med atributen volym.
        self.v = volym  # En int


def main():  # En funktion som testar båda classerna
    obj = Book("Harry_Potter", "J.K Rowling")
    print(obj)
    audio = Audiobook("Harry_Potter", "J.K Rowling")
    audio.volym_set(4)  # sätter volymen lika med 4
    print(audio)


main()  # kallar funktionen main
