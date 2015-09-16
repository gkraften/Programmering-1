def is_int(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

questions = 3
correct = 0

answer = input("Vad är 1+1? ")
while not is_int(answer):
    print("Du måste skriva ett tal!")
    answer = input("Vad är 1+1? ")
if answer == "2":
    correct += 1
    print("Duktigt jobbat")
else:
    print("FEL!")

while not (answer.lower() == "nej" or answer.lower() == "ja"):
    answer = input("Finns hästar?")
    if answer.lower() == "nej":
        print("Helt rätt! De är frukter.")
        correct += 1
    elif answer.lower() == "ja":
        print("Fel! De är ju frukter!")
    else:
        print("Skriv ja eller nej")

answer = input("Vad är derivatan till 3sin(2x)? ")
if answer == "6cos(2x)":
    print("Bravo. Du är inte helt pantad.")
    correct += 1
else:
    print("Alltså du är helt jävla dum i huvudet.")

print("Du hade {} av {} rätt ({}% för de som inte kan räkna ut det)!".format(correct, questions, 100*correct/questions))