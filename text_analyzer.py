"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Rašticová
email: rasticova.barbora@seznam.cz
"""

# Databáze textů
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Seznam registrovaných uživatelů a hesel 
user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]

# Přihlášení uživatele
jmeno = input("username:")
heslo = input("password:")

print("----------------------------------------")

# Ověření jména a hesla
if jmeno in user and password[user.index(jmeno)] == heslo:           
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analysed:")
    print("Text 1:",TEXTS[0],
          "\nText 2:\n", TEXTS[1], 
          "\nText 3:\n", TEXTS[2]
          )
    print("----------------------------------------")

    # Volba textu k analýze
    analyzovany_text = input("Enter a number btw 1 and 3 to select:")
    print("----------------------------------------")

    # Kontrola, zda je vstup číslo 1-3
    if analyzovany_text.isdigit():
        analyzovany_text = int(analyzovany_text)
        if analyzovany_text in [1,2,3]:
            vybrany_text = TEXTS[analyzovany_text -1]

            # Počáteční hodnoty v proměnných 
            pocet_slov = 0
            velka_pocatecni = 0
            velka_pismena = 0
            mala_pismena = 0
            pocet_cisel = 0
            suma_cisel = 0
            delka_slov_pocet = {}

            # Projdi všechna slova textu
            for slovo in vybrany_text.split():
                # Odstraň interpunkci
                slovo_bez_interpunkce = slovo.strip(".,!?;:\"'()[]{}")
                pocet_slov +=1

                # Urči délku slova a ulož do slovníku
                delka_slov = len(slovo_bez_interpunkce)
                delka_slov_pocet[delka_slov] = delka_slov_pocet.get(delka_slov,0) +1

                # Zjištění typu slova
                if slovo_bez_interpunkce.istitle():
                    velka_pocatecni += 1
                elif slovo_bez_interpunkce.isupper():
                    velka_pismena += 1
                elif slovo_bez_interpunkce.islower():
                    mala_pismena += 1
                elif slovo_bez_interpunkce.isdigit():
                    pocet_cisel += 1
                    suma_cisel += int(slovo_bez_interpunkce)

            # Výsledky analýzy    
            print("There are", pocet_slov,"words in the selected text.")
            print("There are", velka_pocatecni, "titlecase words.")
            print("There are", velka_pismena, "uppercase words.")
            print("There are", mala_pismena, "lowercase words.")
            print("There are", pocet_cisel, "numeric strings.")
            print("The sum of all the numbers", suma_cisel, ".")

            # Vykreslení histogramu
            print("----------------------------------------",
            "\nLEN|    OCCURENCES    |NR.",
            "\n----------------------------------------"
            )

            for k, v in sorted(delka_slov_pocet.items()):
                print(" " + str(k).rjust(2) + "|" + ("*" * v) + (" " * (18 -v)) + "|" + str(v))   

        else:
            # Neplatný výběr textu
            print("Selected number not in the range btw 1 and 3, terminating the program..")
    else:
        # Zadán nečíselný vstup
        print("You entered an invalid character, terminating the program..")
else:
    # Špatné jméno nebo heslo
    print("Unregistered user, terminating the program..")   

