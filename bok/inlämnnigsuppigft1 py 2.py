# Namn: Haron Osman
# Datum: 2020-10-12
# Klass: TE19

class Djur:

    def __init__(self, djurtyp, namn, ålder, hunger, hungrig_text, lek, lek_text):

        self.djurtyp = djurtyp.rstrip("\n")
        self.namn = namn.rstrip("\n")
        self.ålder = str(ålder).rstrip("\n")
        self.hunger = hunger
        self.hungrig_text = hungrig_text.rstrip("\n")
        self.lek = lek
        self.lek_text = lek_text.rstrip("\n")

    def hunger_system(self):
        if self.hunger == 0:
            self.hungrig_text = "och är hungrig"

        elif self.hunger > 4:
            self.hungrig_text = "och vägrar att äta mer mat"

        elif self.hunger < -4:
            self.hungrig_text = "och kommer strax att fly på grund av hunger"

        elif self.hunger > 2:
            self.hungrig_text = "och är väldigt mätt"

        elif self.hunger < -2:
            self.hungrig_text = "och är väldigt hungrig"

        elif self.hunger < 0:
            self.hungrig_text = "och är ganska hungrig"


        elif self.hunger > 0:
            self.hungrig_text = "och är mätt"

        return

    def lek_system(self):
        if self.lek == 0:
            self.lek_text = "och vill leka"

        elif self.lek > 4:
            self.lek_text = "och är trött på att leka"

        elif self.lek < -4:
            self.lek_text = "och hotar om att fly om du inte leker med den"

        elif self.lek > 2:
            self.lek_text = "och vill verkligen inte leka"

        elif self.lek < -2:
            self.lek_text = "och vill verkligen leka"

        elif self.lek < 0:
            self.lek_text = "och är uttråkad"

        elif self.lek > 0:
            self.lek_text = "och är inte sugen på att leka"

        return

    def __repr__(self):

        self.hunger_system()
        self.lek_system()

        return self.namn + ": " + self.djurtyp + " " + self.ålder + " år " + self.hungrig_text + " " + self.lek_text


# --------------------------------------------------


# --------------------------------------------------

def val_1(antaldjur):
    if antaldjur != 5:
        djurtyp = input("Vad har du för djur?: ")
        namn = input("Vad heter djuret?: ")
        ålder = int(input("Hur gammal är djuret?: "))
        hunger = 0
        hungrig_text = "inget"
        lek = 0
        lek_text = "inget"

        djuret = Djur(djurtyp, namn, ålder, hunger, hungrig_text, lek, lek_text)

        djur_lista.append(djuret)

        antaldjur += 1
        return antaldjur


    else:
        print("Du har nått ett max antal djur!")
        print("Ta bort ett djur genom att välja alternativ 2 vid huvudmenyn.")


# --------------------------------------------------

def val_2(djur_lista):
    nmr = 0
    for x in djur_lista:
        nmr += 1
        print(str(nmr) + ".", x)

    tabort_loop = 0

    print("Tryck 1 för att sälja ett djur, tryck 2 för att återgå till huvudmenyn")
    while tabort_loop == 0:
        tabort_val = int(input("Skriv in här: "))

        if tabort_val == 1:
            tabort = int(input("Vilken siffra har djuret du vill sälja?: "))
            print(djur_lista[tabort - 1].namn, "har blivit såld...")
            djur_lista.remove[tabort - 1]
            print("Du återgår nu till huvudmenyn...")
            print()
            tabort_loop += 1

        elif tabort_val == 2:
            print("Du återgår nu till huvudmenyn...")
            print()
            tabort_loop += 1

        else:
            print("Välj ett av alternativen!")
            print()


# ---------------------------------------------------
"""Här väljer man vilket djur man vill utföra en aktivitet med"""


def välj_djur(djur_lista):
    # listnummer är nummret som skrivs ut åt vänster om namnen som listas upp på for slingan
    # nummret går upp med ett för varje gång slingan körs exempel: (första gången 1. haron, andra gången 2. Alexander)
    # x är varje djur som är med i listan, x.namn skriver ut vad de heter.
    # X symboliserar alltså något okänd i och med att det är användaren som väljer vilket djur och vad de heter som ska vara med på listan
    listnummer = 0
    for x in djur_lista:
        listnummer += 1
        print(listnummer, x.namn)

    # Användaren skriver in nummret som står bredvid djuret de vill välja
    valt_nummer = int(input("vilket nummer har djuret du vill välja?: "))

    # det första djuret i listan har plats 0 då listor börjar från 0.
    # om de väjer det första djuret (1. haron) i listan så ligger den egentligen på plats 0 och 2an på 1an osv)
    # Därför så vet vi att djuret de valt ligger på nummret de valt - 1 i listan
    valtdjur = (djur_lista[valt_nummer - 1])

    # Endast ett mellanrum
    print()

    # När man valt ett djur får man alternativ som man i huvudprogrammet får välja. 1an kör en funktion som gör så att man leker med djuret
    print("Tryck 1 för att leka", valtdjur.namn)
    print("Tryck 2 för att mata", valtdjur.namn)
    print("Tryck 3 för att återgå till huvudmeny")
    return valtdjur


"""Den här funktionen ligger bakom matandet av djuret."""


def mata(djur_lista, valtdjur):
    # här skriver man in vad man vill mata djuret med
    mat = input("Vad vill du mata ditt djur med?: ")

    # här så skrivs det ut djurets namn (den man själv har valt) och vad man matat den med
    print("Du har matat", valtdjur.namn, "med", mat)

    # hungern på djuret man valt att mata går upp med två om den inte nått max gränsen på hunger 5 (vägrar att äta mer mat)
    if valtdjur.hunger != 5:
        valtdjur.hunger += 2

    # denna for slinga gör så att alla djuren i djur listan (förutom den man valt (den som blir 'passed') blir hungrigare
    # när den blir hungrigare blir det - 1 i hunger och det sker efter varje gång man matat ett djur.
    # därför ska man försöka att mata varje djur lika många gånger, ifall man endast fokuserar på ett djur kommer de andra slutligtvis att fly
    for x in djur_lista:
        if x.namn == valtdjur.namn:
            pass
        elif x.hunger == -5:
            print(x.namn, "har flytt på grund av hunger")
            djur_lista.remove(x)
        else:
            x.hunger -= 1


def leka(djur_lista, valtdjur):
    leksak = input("Vad vill du leka med djuret?: ")

    print("Du har lekt", leksak, "med", valtdjur.namn)

    if valtdjur.lek != 5:
        valtdjur.lek += 2

    for x in djur_lista:
        if x.namn == valtdjur.namn:
            pass
        elif x.hunger == -5:
            print(x.namn, "blev så uttråkad att den flydde")
            djur_lista.remove(x)
        else:
            x.hunger -= 1


# --------------------------------------------------------


ANTALATTRIBUT = 7

antaldjur = 0

avsluta = 0

djur_lista = []

sparadAttribut_lista = []

try:
    fil = open('./djurpark.txt', 'r') # Öppna filen och läs allt som finns i filen.

except:
    print("Fel vid inläsning av tidigare sparningar.")#print(det kommer vissas i skärm)

else:
    fil = open('./djurpark.txt', 'r') #Öppna filen och läs allt som finns i filen.
    rad = fil.readline()#
    attributer = 0# variabel
    while rad:
        sparadAttribut_lista.append(rad)#lägg till rad till attribut lista.
        attributer += 1
        rad = fil.readline()# varibel rad
    antalObjekt = attributer / ANTALATTRIBUT
    for x in range(int(antalObjekt)):#loop, och där nere plasera man alla atributter i listan.
        djurtyp = sparadAttribut_lista[0]
        namn = sparadAttribut_lista[1]
        ålder = int(sparadAttribut_lista[2])
        hunger = int(sparadAttribut_lista[3])
        hungrig_text = sparadAttribut_lista[4]
        lek = int(sparadAttribut_lista[5])
        lek_text = sparadAttribut_lista[6]

        djuret = Djur(djurtyp, namn, ålder, hunger, hungrig_text, lek, lek_text)#här anroppar man

        djur_lista.append(djuret)#här ligger man till Djuret till listan Djur_lista

        antaldjur += 1

        for y in range(ANTALATTRIBUT):#loop
            sparadAttribut_lista.pop(0)# metoden tar bort objektet i det angivna indexet från listan och returnerar det borttagna objektet.
    print()

while avsluta == 0:

    print("Välkommen till din virtuella djurpark!")
    print("För att lägga till ett djur i din djurpark, tryck 1.")
    print("För att lista husdjuren, se deras status eller sälja ett djur tryck 2.")
    print("För att leka eller mata ett djur, tryck 3.")
    print("för att avsluta tryck 4.")

    print()

    val = int(input("vad väljer du?: "))

    if val == 1:
        val_1(antaldjur)



    elif val == 2:
        val_2(djur_lista)


    elif val == 3:
        valtdjur = välj_djur(djur_lista)

        val_aktivitet = int(input("Vad väljer du?: "))

        if val_aktivitet == 1:
            leka(djur_lista, valtdjur)

        elif val_aktivitet == 2:
            mata(djur_lista, valtdjur)

        elif val_aktivitet == 3:
            print()



    elif val == 4:
        spara = int(input("Vill du spara ditt spel? Tryck 1 för ja eller 2 för nej: "))
        if spara == 1:
            fil = open('./djurpark.txt', 'w')
            for x in djur_lista:
                fil.write(x.djurtyp + "\n")
                fil.write(x.namn + "\n")
                fil.write(x.ålder + "\n")
                fil.write(str(x.hunger) + "\n")
                fil.write(x.hungrig_text + "\n")
                fil.write(str(x.lek) + "\n")
                fil.write(x.lek_text + "\n")

            fil.close()
            print("Ditt spel har nu sparats!")
        elif spara == 2:
            print("Ditt spel har inte sparats!")
        print("Hej då!")
        avsluta += 1

    else:
        print("välj ett av alternativen!")

    print("****************************************************************")
    print()