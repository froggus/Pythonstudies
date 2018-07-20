# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "oko", "pies", "dwa")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
   Za zgdywanie bez podpowiedzi dostaniesz 100% punktów zwycięstwa.
   Aby zakończyć zgadywanie, naciśnij Enter bez podawania odpowiedzi.
   
"""
)
print("Zgadnij, jakie to słowo:", jumble)
points = len(correct)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "" and points != 0:
    print("Niestety, to nie to słowo.")
    hintwanted = input("Czy chcesz podpowiedzi w zamian za 1 punkt zwycięstwa? ")
    if hintwanted.lower() == "tak":
        print(correct[position])
        position += 1
        points -= 1
        print("Tracisz jeden punkt zwycięstwa.\n")
        if points == 0:
            input("Przegrałeś, przykro mi! (Naciśnij Enter, aby zakończyć grę.)")
    else:
        guess = input("\nTwoja odpowiedź: ")  
  
if guess == correct:
    print("Zgadza się! Zgadłeś!\n")
    print("Otrzymujesz", points, "punktów zwycięstwa!") #odmienić punkty od przypadku!!!
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
