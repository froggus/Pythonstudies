start = int(input("Wprowadź liczbę początkową i potwierdż ją klawiszem Enter: "))
stop = int(input("Wprowadź liczbę końcową i potwierdż ją klawiszem Enter: "))
pace = int(input("Wprowadź wielkość odstępu pomiędzy kolejnymi liczbami i potwierdż ją klawiszem Enter: \n\n\n"))

for i in range (start, stop, pace):
    print (i)

input("\n\n\nAby zakończyc program, kliknij Enter.")

