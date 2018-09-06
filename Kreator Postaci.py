("Witaj w Kreatorze Postaci.")
choice = None

print("Przydziel punkty atrybutom: siła, zdrowie, mądrość, zręczność.")

points = 30
strength = 0
health = 0
wisdom = 0
skill = 0

while choice != "0" and points != 0:
    print("Obecnie posiadasz", points, "punktów do przydzielenia.")
    print("""Instrukcja obsługi:
        0 - zakończ
        1 - dodaj punkty
        2 - odejmij punkty
        3 - zobacz rozkład punktów""")  

    choice = input("Co chcesz zrobić? ")
    if choice == "0":
        print("No to cześć!")
        input("\n\nAby zakończyć program, naciśnij Enter.")

    elif choice == "1" and points != 0:
        print("""To są Twoje atrybuty:
                    s - siła
                    zd - zdrowie
                    m - mądrość
                    zr - zręczność""")
        attribute = (input("Który atrybut Cię interesuje? "))
        
        if attribute == "s":
            assignment = int(input("Ile punktów chcesz mu przydzielić? "))
            while assignment <= 0:
                print("Tak nisko się oceniasz?")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            while assignment > points:
                print("Hola, hola! Masz tylko", points, "punktów!!")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            strength = strength + assignment
            points = points - assignment
            print("Jesteś silniejszy.\n")        
        elif attribute == "zd":
            assignment = int(input("Ile punktów chcesz mu przydzielić? "))
            while assignment <= 0:
                print("Tak nisko się oceniasz?")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            while assignment > points:
                print("Hola, hola! Masz tylko", points, "punktów!!")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            health = health + assignment
            points = points - assignment
            print("Jesteś zdrowszy.\n")
        elif attribute == "m":
            assignment = int(input("Ile punktów chcesz mu przydzielić? "))
            while assignment <= 0:
                print("Tak nisko się oceniasz?")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            while assignment > points:
                print("Hola, hola! Masz tylko", points, "punktów!!")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            wisdom = wisdom + assignment
            points = points - assignment
            print("Jesteś mądrzejszy.\n")
        elif attribute == "zr":
            assignment = int(input("Ile punktów chcesz mu przydzielić? "))
            while assignment <= 0:
                print("Tak nisko się oceniasz?")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            while assignment > points:
                print("Hola, hola! Masz tylko", points, "punktów!!")
                assignment = int(input("Jeszcze raz pomyśl: ile punktów chcesz przydzielić? "))
            skill = skill + assignment
            points = points - assignment
            print("Jesteś bardziej zręczny.\n")
        else:
            print("""Wybierz jeszcze raz. 
                        To są Twoje atrybuty:
                        s - siła
                        zd - zdrowie
                        m - mądrość
                        zr - zręczność\n""")

    elif choice == "2" and points >= 0:
        print("""To są Twoje atrybuty:
            s - siła
            zd - zdrowie
            m - mądrość
            zr - zręczność""")
        attribute = (input("Który atrybut Cię interesuje? "))

        if attribute == "s":
            if strength == 0:
                print("Jesteś za słaby na odejmowanie punktów.\n")                       
            else:
                subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                strength = strength - subtraction
                points = points + subtraction
                print("Jesteś słabszy.\n")
                  
        elif attribute == "zd":
            if health == 0:
                print("Ledwo dychasz! Nie odejmuj sobie punktów.\n")
            else:
                subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                health = health - subtraction
                points = points + subtraction
                print("Źle się czujesz.\n")

        elif attribute == "m":
            if wisdom == 0:
                print("Chyba nie umiesz dodawać, więc nie odejmuj sobie punktów mądrości.\n")
            else:
                subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                wisdom = wisdom - subtraction
                points = points + subtraction
                print("Jesteś głupszy!\n")

        elif attribute == "zr":
            if skill == 0:
                print("To niezręcznie tak na wstępie odejmować sobie punkty...\n")
            else:
                subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                skill = skill - subtraction
                points = points + subtraction
                print("Przedmioty wypadają Ci z rąk.\n")
        else:
            print("""Wybierz jeszcze raz. 
                        To są Twoje atrybuty:
                        s - siła
                        zd - zdrowie
                        m - mądrość
                        zr - zręczność\n""")
    elif choice == "3":
        attributes = [("siła", strength), ("zdrowie", health), ("mądrość", wisdom), ("zręczność", skill)]
        print("Twoje atrybuty mają następujące punkty: ")
        for entry in attributes:
            name, value = entry
            print(name, " - ", value)
    else:
        print("""Skup się i wybierz z tych opcji:
            0 - zakończ
            1 - dodaj punkty
            2 - odejmij punkty
            3 - zobacz rozkład punktów\n""")

    while choice != 0 and points == 0:
        print("Nie masz więcej punktów do przydzielania.")
        print("""Oto Twoje opcje:
        0 - zakończ
        2 - odejmij punkty
        3 - zobacz rozkład punktów\n""")
        choice = input("Co chcesz zrobić? ")
        
        if choice == "0":
            print("No to cześć!")
            input("\n\nAby zakończyć program, naciśnij Enter.")

        elif choice == "2" and points >= 0:
            print("""To są Twoje atrybuty:
                s - siła
                zd - zdrowie
                m - mądrość
                zr - zręczność""")
            attribute = (input("Który atrybut Cię interesuje? "))

            if attribute == "s":
                if strength == 0:
                    print("Jesteś za słaby na odejmowanie punktów.\n")                       
                else:
                    subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                    strength = strength - subtraction
                    points = points + subtraction
                    print("Jesteś słabszy.\n")
                    
            elif attribute == "zd":
                if health == 0:
                    print("Ledwo dychasz! Nie odejmuj sobie punktów.\n")
                else:
                    subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                    health = health - subtraction
                    points = points + subtraction
                    print("Źle się czujesz.\n")

            elif attribute == "m":
                if wisdom == 0:
                    print("Chyba nie umiesz dodawać, więc nie odejmuj sobie punktów mądrości.\n")
                else:
                    subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                    wisdom = wisdom - subtraction
                    points = points + subtraction
                    print("Jesteś głupszy!\n")

            elif attribute == "zr":
                if skill == 0:
                    print("To niezręcznie tak na wstępie odejmować sobie punkty...\n")
                else:
                    subtraction = int(input("Ile punktów chcesz mu odjąć? "))
                    skill = skill - subtraction
                    points = points + subtraction
                    print("Przedmioty wypadają Ci z rąk.\n")
            else:
                print("""Wybierz jeszcze raz. 
                            To są Twoje atrybuty:
                            s - siła
                            zd - zdrowie
                            m - mądrość
                            zr - zręczność\n""")
        elif choice == "3":
            attributes = [("siła", strength), ("zdrowie", health), ("mądrość", wisdom), ("zręczność", skill)]
            print("Twoje atrybuty mają następujące punkty: ")
            for entry in attributes:
                name, value = entry
                print(name, " - ", value)
        else:
            print("""Skup się i wybierz z tych opcji:
                0 - zakończ
                2 - odejmij punkty
                3 - zobacz rozkład punktów\n""")

    