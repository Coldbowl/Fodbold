import pickle
import itertools

filename = 'betalinger.pk'

fodboldtur = {}
navne = []

kører = True

least_dict = {}

def afslut():
    global kører
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")
    kører = False

def printliste():
    for item in fodboldtur:
        beløb = fodboldtur[item]
        print(f"{item} har betalt {beløb} kr og mangler at betale {4500 - beløb} kr\n")

def modtag_betaling():
    while True:
        navn = input("Indtast navnet på personen der betaler (Skriv 'b', hvis du ønsker at gå tilbage): ")
        if navn == "b":
            break

        if navn in navne:

            break
        else:
            print("Ikke et validt navn")
    
    while True:
        beløb = input("Indtast beløbet der betales: ")
        try:
            beløb = float(beløb)
        except ValueError:
            print("Ikke et validt tal")
            return
        
        fodboldtur[navn] += beløb
        break

def udskam():
    global least_dict
    keys = list(fodboldtur.keys())

    least_dict = dict(sorted(fodboldtur.items(), key=lambda x:x[1]))
    least_dict = dict(itertools.islice(least_dict.items(), 3))

    l_keys = list(least_dict.keys())

    print(f"""De tre medlemmer der har betalt mindst er:
        1. {l_keys[0]} med {least_dict[l_keys[0]]} kr
        2. {l_keys[1]} med {least_dict[l_keys[1]]} kr
        3. {l_keys[2]} med {least_dict[l_keys[2]]} kr""")



def menu():
    while kører:
        print("1: Print liste")
        print("2: Afslut program")
        print("3: Registrer betaling")
        print("4: Udskam")

        valg = input("Indtast dit valg:")
        if (valg == '1'):
            printliste()
        elif (valg == '2'):
            afslut()
        elif (valg == '3'):
            modtag_betaling()
        elif (valg == '4'):
            udskam()
        else:
            print("Ikke en kendt kommando")

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)

# Pre-processing
for item in fodboldtur.items():
    navne.append(item[0])

infile.close()
menu()

