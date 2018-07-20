#100 rzutów monetą
#program podaje liczbę orzełków i reszek

import random

rzut = 100
reszka = 0
orzelek = 0

while rzut != 0:
    losowanie = random.randint(1,2)
    if losowanie == 1:
        reszka += 1
    else:
        orzelek += 1
    rzut -= 1
    
print("Program rzucił 100 razy monetą.")
print("Na 100 rzutów wypadło ", reszka, "reszek i ", orzelek, "orzełków.")
input("\nAby zakończyć program, naciśnij Enter.") 
