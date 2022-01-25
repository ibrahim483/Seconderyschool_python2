class Book:  # En class som heter Book, !!!class namn börjar alltid med en stor bokstav.
    def __init__(self, titel,arthur):  # Skapat en metod och la till atributer som är använda i dennna klassen är titel och arthur.
        self.t = titel  # En sträng
        self.a = arthur  # En sträng
        self.borrow = False

    def __str__(self):  # Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        return self.t + "\n" + self.a + str(self.borrow)


class Audiobook(Book):  # En ny klass som arvar den gamla classen.
    def __str__(self):# Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        return self.t + " " + self.a + " " + str(self.v)

    def volym_set(self, volym):  # EN funktion med atributen volym.
        self.v = volym  # En int



class Library(Book, Audiobook):


    def __init__(self):
        self.books = []

    def search_book(self):
        print("Which book are you looking for: ")
        for book in self.books:
            print(book)


    def return_book(self):
        return_1 = (input("What is the name of the book you want to return: "))
        for book in self.books:  # loppar genom listan och sparar bok objekt i book.
            if book.t == return_1: # OM boken är den som användaren vill låna.
                if book.borrow == True: # Om boken är utlånad
                    book.borrow = False # boken är utlånad.
                else:
                    print(" The book has already been returned ")

    def borrow_book(self):
        for book in self.books:  # Loopar genom listan med böker.
            print(book.t)  # printar titel på bökerna.
        borrow = input("What is the name of the book you want to borrow: ")
        for book in self.books:  # loppar genom listan och sparar bok objekt i book.
            if book.t == borrow:  # OM boken är den som användaren vill låna.
                book.borrow = True  # boken är utlånad.

    def all_books(self):
        for book in self.books: #Loopar genom listan med böker.
            print(book)


    def add_books(self):
        book_name = input(" Which book you want to add: ") # For att lägga till ett namn.
        auther = input(" Who is the auther ") # for att lägga till en förfater för boken.
        obi = Book(book_name,auther) # den skapar ett objekt som är bok.
        self.books.append(obi) #  lägger till objekten i listan.
        print(" The book has been added")

   #______________While loop__________#
# def mian(): är en huvudfunktion i Python fungerar som körpunkten för alla program.
def main():  # En funktion som testar båda classerna
    librari = Library
    choice = 5
    while choice != 6:
        print("Welcome to Ibrahim's library")
        print("1. Look up a book")
        print("2. To return a book ")
        print("3. Borrow a bok ")
        print("4. Show all books ")
        print("5. add a new book ")
        print("6. Exit the library ")
        try:
            choice = int(input(" chose one of those alternative from 1 to 6"))
            if choice == 1:

            elif choice == 2:


            elif choice == 3:


            elif choice == 4:


            elif choice == 5:


main()  # kallar funktionen main
