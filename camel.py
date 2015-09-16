import random

print("Du har stulit en magisk kamel och ägeren har blivit arg. Han följer efter dig ridandes på en alpacka.")

distance = 0
owner_distance = -10
stamina = 100
thirst = 100
water = 3
goal = random.randint(50, 150)
day = 1

movement = ("b",)

print("\n****** Dag {} ******\n".format(day))
while True:
    print("==========\nDag: {}\nAvlagd sträcka: {}km\nAvstånd till ägare: {}km\nStamina: {}%\nTörst: {}%\nAntal vattenflaskor: {}\n=========".format(day, distance, distance - owner_distance, stamina, thirst, water))
    print("A) Drick\nB) Kuta\nC) Sov\nD) Status\nE) Avsluta")
    choice = input("Vad gör du? ").lower()
    print("")

    if choice == "a":
        if water == 0:
            print("Du har slut på vatten")
            continue
        if thirst == 100:
            print("Alltså du är inte törstig så det är bara dumt att dricka men gör som du vill.")
        thirst = 100
        water -= 1
        print("Du dricker en flaska vatten och din törst återställs.")
    elif choice == "b":
        if stamina < 10:
            print("Du är för trött för att springa.")
            continue
        else:
            dist = random.randint(int(10*(stamina / 100)), int(30*(stamina / 100)))
            distance += dist
            stamina -= dist
            print("Du har sprungit {}km".format(dist))
    elif choice == "c":
        print("Du tar en tupplur på 20 minuter, men vaknar efter 7 timmar.")
        print("Du och din kamel är nu utvilade.")
        stamina = 100
    elif choice == "d":
        print("==========\nDag: {}\nAvlagd sträcka: {}km\nAvstånd till ägare: {}km\nStamina: {}%\nTörst: {}%\nAntal vattenflaskor: {}\n=========".format(day, distance, distance - owner_distance, stamina, thirst, water))
        continue
    elif choice == "e":
        print("Du sparkar kamelen i magen och vrider om dess huvud ett varv så att den dör. Sedan skär du upp magen och dricker upp magsaften. Du dör av uttorkning efter kraftiga kräkningar.")
        break
    else:
        print("Vad vill du egentligen? Välj en bokstav från A-E.")
        continue

    #win
    if distance >= goal:
        print("Grattis! Du kom undan på {} dagar! Kamelen är din nu; för evigt.".format(day))
        break

    #Owner getting closer
    owner_distance += random.randint(0, 15)
    if distance - owner_distance < 15:
        print("Ägaren närmar sig!")

    #Thirst
    if choice != "a":
        thirst -= random.randint(0, 50)

    #Oasis
    if random.randint(0, 100) <= 10 and choice in movement:
        print("Du har hittat en oas! Du dricker dig otörstig och fyller på dina vattenflaskor.")
        thirst = 100
        water = 3

    #Warn about death
    if stamina < 40:
        print("Du känner dig väldigt trött.")
    if thirst <= 40:
        print("Du känner dig väldigt törstig.")

    #Death
    if stamina <= 0:
        print("Du dog av utmattning.")
        break
    if water <= 0:
        print("Du dog av törst.")
        break
    if distance - owner_distance <= 0:
        print("Ägaren har kommit ikapp!! Han plockar fram en yxa ur rockärmen, hugger av dina ben och lämnar dig att förblöda.")
        break

    input("Tryck på enter för att gå vidare till nästa dag.")
    day += 1
    print("\n****** Dag {} ******\n".format(day))
