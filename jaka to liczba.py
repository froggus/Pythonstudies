#program będzie próbował odgadnąć liczbę użytkownika

print("Pomyśl o liczbie z przedziału 0 do 100.")
print("Spróbuję ją odganąć!")
print("Jeśli mi się uda, napisz ""tak"".")
print("Jeśli Twoja liczba jest mniejsza niż podana, napisz ""mniej"".")
print("Analogicznie, jeśli liczba ta jest większa, napisz ""wiecej"".")
print("Jeśli jesteś gotowy, naciśnij Enter.")

def play(fromm, to):
    if fromm == to:
        print("To jest na pewno", fromm, "!")
    else:
        mid = floor((fromm+to)/2)

atempt = input("Czy to jest", mid, "?")

if atempt == "tak":
    print("Zgadłem! Było proste!")
elif atempt >= "wiecej":
    play(mid+1, to)
else :
    play(fromm, mid-1)

play(1,100)

