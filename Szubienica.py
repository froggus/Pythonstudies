# Gra w szubienicę
# Komputer wybiera losowo słowo
# Komputer informuje gracza ile liter znajduje się w wybranym słowie
# Gracz może zadać 5 pytań o obecność konkretnych liter
# Komputer odpowiada tak lub nie
# Potem gracz ma jedną szansę na odgadnięcie słowa

import random

WORDS = ("zabawa", "wakacje", "mieszkanie", "tramwaj", "samolot", "plebiscyt", "konkurs", "osiedle", "fryzjer", "muszelka")
word = random.choice(WORDS)
print("Komputer wylosował słowo, które ma", len(word), "liter.")
print("Możesz zapytać czy konkretnych pięć liter występuje w wylosowanym słowie.")

for a in range(0,5):
    letter = input("Jaką literę mam sprawdzić? ")
    if letter in word:
        print("Jest!")
    else:
        print("Nie ma :/")

guess = input("Zgadnij jakie słowo wylosował komputer! ")

if guess == word:
    print("Brawo! You did IT!!")
else:
    print("Nie udało się, spróbuj innym razem.")

#input("Aby zakończyć, naciśnij klawisz Enter.")


