# name:Ibrahim Baltah
# klass:Teck19
# data:2021/02/05

class My_zoo: #classen heter My_zoo.

   #Metod 1
   #Den här metoden som kallas när ett objekt skapas från klassen och gör det möjligt för klassen att initialisera attributen för en klass.
   def __init__(self, name ,old, color, hunger, health):# Here i have five arguments.
       self.n= name # En sträng
       self.o= old # En int
       self.l= health # En int
       self.c= color #
       self.h= hunger # En int

   #Metod 2
   # Denna metod returnerar strängrepresentationen av objektet.
   def __str__(self):
       return "your animal name is: " + self.n + " and is " + str(self.o) + ". his color is " + self.c + " and his health is"+ str(self.l) + ("and his hunger: ") + str(self.h)

   #Metod 3
   # Denna metod kan man ändra namnet på.
   def change_name(self):
       print(" your currant name is",self.n)# Här printar porogramet din nuvarande namn är.
       name = input( " which name do you want the animal will have for now")# Här när porogramet ska ändra namnet på djuret.
       self.n = name# confeirm the chenges. so self.n== with the new name .

   #Metod 4
   # Denna metod kan man ändra färgen på:
   def change_color(self):
       print(" Your current color is"+ self.c)# Här printar porogramet din nuvarande färge är.
       color = input(" wich color do you want to change to")# Här lägger man den nya färge på djuret.
       self.c= color # confeirm the chenges. so self.n== with the new name.

   #Metod 5
   # Denna metod kan man se hur hungrig är sin djur.
   def chake_hunger (self):
       if self.h <= 5:# Om hunger är  mindre eller lika med 5 då printa den som är nere.
           print(" Your animal is starving get hem som food")# Print den.
       elif self.h >= 6:# Om hunger är  store eller lika med 6 då printa den som är nere.
           print(" You animal is full and happy")# Print den.
       else:# Annars
           print("please Enter from 1 to 10 to see how hungry is your animal")# Print den.

   #Metod 6
   # Denna metod kan man mata sin djur på.
   def feed(self):
       self.h = self.h+1
       print(" YAM, YAM, YAM, the food is very delicious")# Print den.
       if self.h <=5:# Om hunger är fortforande mindre eller lika med 5 efter du har mattat din djur då printa den som är nere.
           print(" WA,WA,WA,WA, I still am hungry")# Print den.
       elif self.h >= 6:# Om hunger är store eller lika med  6 efter du har mattat din djur då printa den som är nere.
           print("Thank you I am full")# Print den.
   #_______________funktions____________#
#Inparameter animal lista och returvärde animal_lista.
def create_animal(animal_list):
   # Här kan användaren bestämma namn, färge,ålder hälsa och hunger på djuret.
   name = input( " Enter your animal name ") # Här bestämmer man vad sin djur ska heta.
   old = input( " How old is your animal? ")#Här bestämmer man sin djur ålder.
   color = input(" Which color do you prefer to your animal? ")#Här bestämmer man vad sin djur ska ha för färg.

   #_________________________health_____________________#
   #Här nere vill jag att användaren ska skriva in hälsa på djuret sen ska den kolla om den är mindre än 5 så behöver man mata den om den är mer då är den mätt.
   health = int(input(" which health dose your animal have from 1 to 10 "))
   if health <=5: # Om health är mindre eller lika med 5 då printa den som är nere.
       print("You need to blasphemy your animal or it will die")# printa den.
   elif health >=6:# Om health är store eller lika med 6 då printa den som är nere.
       print("Your animal is fine for now")# Printa den.

   elif health == 10: # Om health är lika med tio då printa den som är nere.
       print(" Yor animal is very healthy")# Printa den.

   else:
       print(" Your animal is fine (pleas chose a number from 1 to 10 for next time)")#Annars printa den här.

   #____________________Hunger ______________________#
   hunger = int(input(" How much hungry is your animal from 1 to 10 "))# här ska man skriva hur humgrig är sin djur
   animal = My_zoo(name, old, color,hunger, health )# variabel aanimal = My_zoo(name, old, color,hunger, health )
   animal_list.append(animal) #Lägg variabeln animal i animal_list.
   return animal_list # Returna animal_list
    #___________________creat a file___________________#
nummberOf_atributs= 5
nummberOf_animals=0
finsh=0
animal_list=[]
saveatribut_list=[]
try:
    fil = open('./djurpark.txt', 'r')#öppna en file och skriva in i den.

except:
    print("file last version saved.")#sk

else:
    fil = open('./djurpark.txt', 'r')
    row = fil.readline()
    atributs = 0
    while row:
        saveatribut_list.append(row)
        atributs += 1
        rad = fil.readline()#variabel "rad"
    nummberOf_objekts = atributs / nummberOf_atributs
    for x in range(int(nummberOf_objekts)):#loop, och där nere plaserr man alla atributter i listan.
        name = saveatribut_list[0]
        old = saveatribut_list[1]
        color = int(saveatribut_list[2])
        hunger = int(saveatribut_list[3])
        health = saveatribut_list[4]


        animal = My_zoo(name, old, color, hunger, health)

        animal_list.append(animal)#här ligger man till Djuret till listan Djur_lista

        nummberOf_animals += 1

        for y in range(nummberOf_atributs):#loop
            saveatribut_list.pop(0)# metoden tar bort objektet i det angivna indexet från listan och returnerar det borttagna objektet.
    print()

   #______________While loop__________#
# def mian(): är huvudfunktionen i Python fungerar som körpunkten för alla program.
def mian():

   choice = 6 #här säger man att choice är lika med 6.
   animal_list=[] #lista
   # Här har vi en loop som hjälper att användaren välja vad hon/han vill göra. genom att läsa altarnativa och välja.
   while choice != 7:# Om choicer är inte lika med 7:
       print("Welcome to tamagotchi game there you can create your one animal you can give it a name, age, color, ")# Printa den.
       print(" health and hunger. What are you waiting for lets create your dream animal")# Printa den.
       print("1.Create your tamagochi a ")# Printa den.
       print("2.show yur tamagochi ")# Printa den.
       print("3.Change your tamagochi name ")# Printa den.
       print("4.Change your tamagochi color ")# Printa den.
       print("5.look if your tamagochi is hunger ")# Printa den.
       print("6.Do you want to feed your tamagochi? ")# Printa den.
       print("7.End the the porogram ")# Printa den.
       #Jag använde try för att ge en till chanse till användaren, om han/ skriver i början fel.
       try:
           choice = int(input("chosse one of those alternative from 1 to 7 "))# Skriv in ett nummer mellan 1 och 7.
           # Härifrån och ner åt anropar jag funktionerna beror på vad användaren väljer.
           if choice == 1: # Om choice är lika med 1 gör följande.
               animal_list = create_animal(animal_list) #Anropar funktionen
           elif choice == 2: # Om choice är lika med 2 gör följande.
               for animal in animal_list:
                   print(animal) #Anropar funktionen
           elif choice == 3: # Om choice är lika med 3 gör följande.
               for animal in animal_list:
                   animal.change_name()#Anropar funktionen
           elif choice == 4: # Om choice är lika med 4 gör följande.
               for animal in animal_list:
                   animal.change_color()#Anropar funktionen
           elif choice == 5: # Om choice är lika med 5 gör följande.
               for animal in animal_list:
                   animal.chake_hunger()#Anropar funktionen
           elif choice == 6: # Om choice är lika med 6 gör följande.
               for animal in animal_list:
                   animal.feed()#Anropar funktionen
       except:
           print(" You need to write a number from 1 to 7: ")# Om man inte valde av alternativa då porogramet printer detta.
mian()
#______________________The porogram is done_____________________
