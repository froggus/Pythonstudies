message = input("Wprowadź komunikat i potwierdź go klawiszem Enter: ")
print("\n")
koniec = len(message)+1

for i in range (-1,-koniec,-1):
    #print("i=", i)
    print(message[i])
    
print("\n")

print(len(message))

input("\n\nAby zakończyć program, kliknij Enter.")


