#Ciasteczko z wróżbą
#Generowanie liczb losowych oraz przećwiczenie procedury if

print("Oto wirtualne ciasteczko z wróżbą.")
print("Naciśnij Enter, aby wylosować ciasteczko i poznać wróżbę.")

losowanie = input("")

import random

wrozba = random.randint(1, 5)
if wrozba == 1:
    print("Już niedługo spotka Cię wielkie szczęście!")
elif wrozba == 2:
    print("Zakochasz się tej wiosny!")
elif wrozba == 3:
    print("Koniecznie zadbaj o swoje zdrowie!")
elif wrozba == 4:
    print("Zagraj w totka - szczęście Ci sprzyja!")
else :
    print("Niebawem odwiedzi Cię dobry przyjaciel!")

input("\nAby zakończyć program, naciśnij Enter.")

