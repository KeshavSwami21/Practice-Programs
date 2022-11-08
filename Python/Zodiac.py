print("Let's find your zodiac")
opt = 'y'

while(opt.lower() != 'n'):

    DOB = input("\nEnter the date of birth in 'dd/mm' format: ")
    li = list(DOB.split("/"))
    try:
        # Aries
        if((((li[1] == '03' or li[1] == '3' or li[1].lower() == 'march' or li[1].lower() == 'mar') and (int(li[0]) >= 21 and (int(li[0]) >= 1)))
                or ((li[1] == '04' or li[1] == '4' or li[1].lower() == 'april' or li[1].lower() == 'apr') and (int(li[0]) <= 19 and (int(li[0]) >= 1))))):
            print("Your zodiac is Aries")

        # Taurus
        elif((((li[1] == '05' or li[1] == '5' or li[1].lower() == 'may') and (int(li[0]) <= 20 and (int(li[0]) >= 1)))
            or ((li[1] == '04' or li[1] == '4' or li[1].lower() == 'april' or li[1].lower() == 'apr') and (int(li[0]) >= 20 and (int(li[0]) >= 1))))):
            print("Your zodiac is Taurus")

        # Gemini
        elif((((li[1] == '05' or li[1] == '5' or li[1].lower() == 'may') and (int(li[0]) >= 21 and (int(li[0]) >= 1)))
            or ((li[1] == '06' or li[1] == '6' or li[1].lower() == 'june') and (int(li[0]) <= 21 and (int(li[0]) >= 1))))):
            print("Your zodiac is Gemini")

        # Cancer
        elif((((li[1] == '06' or li[1] == '6' or li[1].lower() == 'june') and (int(li[0]) >= 22 and (int(li[0]) >= 1)))
            or ((li[1] == '07' or li[1] == '7' or li[1].lower() == 'july') and (int(li[0]) <= 22 and (int(li[0]) >= 1))))):
            print("Your zodiac is Cancer")

        # Leo
        elif((((li[1] == '07' or li[1] == '7' or li[1].lower() == 'july') and (int(li[0]) >= 23 and (int(li[0]) >= 1)))
            or ((li[1] == '08' or li[1] == '8' or li[1].lower() == 'august' or li[1].lower() == 'aug') and (int(li[0]) <= 22 and (int(li[0]) >= 1))))):
            print("Your zodiac is Leo")

        # Virgo
        elif((((li[1] == '08' or li[1] == '8' or li[1].lower() == 'august' or li[1].lower() == 'aug') and (int(li[0]) >= 23 and (int(li[0]) >= 1)))
            or ((li[1] == '09' or li[1] == '9' or li[1].lower() == 'september' or li[1].lower() == 'sep') and (int(li[0]) <= 22 and (int(li[0]) >= 1))))):
            print("Your zodiac is Virgo")

        # Libra
        elif((((li[1] == '09' or li[1] == '9' or li[1].lower() == 'september' or li[1].lower() == 'sep') and (int(li[0]) >= 23 and (int(li[0]) >= 1)))
            or ((li[1] == '10' or li[1].lower() == 'october' or li[1].lower() == 'oct') and (int(li[0]) <= 23 and (int(li[0]) >= 1))))):
            print("Your zodiac is Libra")

        # Scorpius
        elif((((li[1] == '10' or li[1].lower() == 'october' or li[1].lower() == 'oct') and (int(li[0]) >= 24 and (int(li[0]) >= 1)))
            or ((li[1] == '11' or li[1].lower() == 'november' or li[1].lower() == 'nov') and (int(li[0]) <= 21 and (int(li[0]) >= 1))))):
            print("Your zodiac is Scorpius")

        # Sagittarius
        elif((((li[1] == '11' or li[1] == '11' or li[1].lower() == 'november' or li[1].lower() == 'nov') and (int(li[0]) >= 22 and (int(li[0]) >= 1)))
            or ((li[1] == '12' or li[1].lower() == 'december' or li[1].lower() == 'dec') and (int(li[0]) <= 21 and (int(li[0]) >= 1))))):
            print("Your zodiac is Sagittarius")

        # Capricornus
        elif((((li[1] == '12' or li[1].lower() == 'december' or li[1].lower() == 'dec') and (int(li[0]) >= 22 and (int(li[0]) >= 1)))
            or ((li[1] == '01' or li[1] == '1' or li[1].lower() == 'january' or li[1].lower() == 'jan') and (int(li[0]) <= 19 and (int(li[0]) >= 1))))):
            print("Your zodiac is Capricornus")

        # Aquarius
        elif((((li[1] == '01' or li[1] == '1' or li[1].lower() == 'january' or li[1].lower() == 'jan') and (int(li[0]) >= 20 and (int(li[0]) >= 1)))
            or ((li[1] == '02' or li[1] == '2' or li[1].lower() == 'february' or li[1].lower() == 'feb') and (int(li[0]) <= 18 and (int(li[0]) >= 1))))):
            print("Your zodiac is Aquarius")

        # Pisces
        elif((((li[1] == '02' or li[1] == '2' or li[1].lower() == 'february' or li[1].lower() == 'feb') and (int(li[0]) >= 19 and (int(li[0]) >= 1) and (int(li[0]) <= 29)))
            or ((li[1] == '03' or li[1] == '3' or li[1].lower() == 'march' or li[1].lower() == 'mar') and (int(li[0]) <= 20 and (int(li[0]) >= 1))))):
            print("Your zodiac is Pisces")

        else:
            print("Please try again.")
            continue

        opt = input("Wanna try again? (y/n): ")
    
    except:
        print("Please Try again.\n")

  
