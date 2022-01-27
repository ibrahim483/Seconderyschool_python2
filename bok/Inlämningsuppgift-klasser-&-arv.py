class Book:  # En class som heter Book, !!!class namn börjar alltid med en stor bokstav.
    def __init__(self, titel,arthur):  # Skapat en metod och la till atributer som är använda i dennna klassen är titel och arthur.
        self.t = titel  # En sträng
        self.a = arthur  # En sträng
        self.borrow = False

    def __str__(self):
        # Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        if self.borrow == False:
            return self.t + "\n" + self.a + " " + "boken är inne"
        else:
            return self.t + "\n" + self.a + " " + "boken är utlånad"

    def borrow_a_book(self):  # En metod som visar att boken är utlånad.
        self.borrow = True

    def return_a_book(self):  # En metod som visar att boken finns.
        self.borrow = False



class Audiobook(Book):  # En ny klass som arvar den gamla classen.
    def __str__(self):# Metoden __str__ gör en lista med de olika tärningarnas värden,
                        # sorterar den och returnerar den i sträng-form
        return self.t + " " + self.a + " " + str(self.v)

    def volym_set(self, volym):  # EN funktion med atributen volym.
        self.v = volym  # En int



class Library():  # Skapat en class som heter library


    def __init__(self):
        self.books = [] # En lista

    def search_book(self):
        print("Which book are you looking for: ")
        for book in self.books:
            print(book)
        sh = input(" write down the name of the book you are looking for: ")  # En input som låter dig att skriva in boken som du vill från listan.

        lb= False
        for book in self.books:

            if book.t == sh:
                lb = True

        if lb == True:
            print("Yes we have this book in our library")

        else:
            print(" Sorry we don't have this bok write know")

    def return_book(self):
        return_1 = (input("What is the name of the book you want to return: "))
        for book in self.books:  # loppar genom listan och sparar bok objekt i book.
            if book.t == return_1: # OM boken är den som användaren vill låna.
                if book.borrow == True: # Om boken är utlånad
                    book.return_a_book()
                else:
                    print(" The book has already been returned ")


    def borrow_book(self):
        for book in self.books:  # Loopar genom listan med böker.
            print(book.t)  # printar titel på bökerna.
        borrow = input("What is the name of the book you want to borrow: ")
        for book in self.books:  # loppar genom listan och sparar bok objekt i book.
            if book.t == borrow: # OM boken är den som användaren vill låna.
                if book.borrow == False:
                    book.borrow_a_book()  # boken är utlånad.
                else:
                    print(" The book is already borrowed")

    def all_books(self):
        for book in self.books: #Loopar genom listan med böker.
            print(book)


    def add_books(self):
        book_name = input(" Which book you want to add: ") # For att lägga till ett namn.
        auther = input(" Who is the auther ") # for att lägga till en förfater för boken.
        obi = Book(book_name,auther) # den skapar ett objekt som är bok.
        na = 1
        #print(" The book has been added")
        for book in self.books:  # loppar genom listan och sparar bok objekt i book.
            if book.t == book_name: # OM boken finns redan.
                print(" The book is already in the library ")
                na = 2
        if na == 1:
            self.books.append(obi)  # lägger till objekten i listan.
            print(" The book has been added")

   #______________While loop__________#
# def mian(): är en huvudfunktion i Python fungerar som körpunkten för alla program.
def main():  # En funktion som testar båda classerna
    librari = Library()
    choice = 5
    while choice != 6:
        print("[  Welcome to Ibrahim's library  ]")
        print("1. Look up a book")
        print("2. To return a book ")
        print("3. Borrow a bok ")
        print("4. Show all books ")
        print("5. add a new book ")
        print("6. Exit the library ")
        choice = int(input(" chose one of those alternative from 1 to 6: "))
        if choice == 1:
            librari.search_book()  # kallar funktionerna.

        elif choice == 2:
            librari.return_book()


        elif choice == 3:
            librari.borrow_book()


        elif choice == 4:
             librari.all_books()


        elif choice == 5:
            librari.add_books()

        else:
            print ("hej")
        #except:
#rint(" You need to write a number between 1 and 6: ")  # Om man inte valde av alternativa då porogramet printer detta.


main()  # kallar funktionen main
