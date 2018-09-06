#program ma za zadanie wypisać listę słów w przypadkowej kolejności, bez powtórzeń

import random
words = ["jeden", "dwa", "trzy", "cztery", "pięć", "sześć"]
print("Oto lista słów, o przypadkowej kolejności: ")
# while words != []:
#     item = random.choice(words)
#     print(item)
#     words.remove(item)


for i in range(len(words)):
    word = random.choice(words)
    print(word)
    words.remove(word)

input("Aby zakończyć program, kliknij Enter")
