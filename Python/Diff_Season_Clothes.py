def logic():
    opt = 'y'

    while(opt.lower() not in ('n', 'no', 'exit')):
        try:
            month = input(
                "Enter the month in which you want to visit India: ")

            if(month.lower() in ('4', '5', '6', 'summer', 'april', 'june', 'may', 'apr')):
                print("It is a season of Summer.\nMake sure to carry your Light clothes as well as cotton clothes."
                      "\nThe temperature relies between 30-45(or more in some field areas)degree Celsius."
                      "\nBe hydrated all the time if you go in Summers.\nSummers in India are very Exhausting"
                      "\nYou can be a Victim of Heat stoke if you don't follow safety precautions.")

            elif(month.lower() in ('2', '3', 'spring', 'feburary', 'march', 'feb', 'mar')):
                print("It is a season of Spring.\nOne of the best Seasons.\nMake sure to carry your Light woolen clothes."
                      "\nThe temperature relies between 15-25 degree Celsius.")

            elif(month.lower() in ('1', '12', 'winter', 'jan', 'dec', 'january', 'december')):
                print("It is a season of Winter.\nMake sure to carry your Woolen and body Warmers. "
                      "\nThe temperature can drop down up to 0 degree Celsius in some North part of the Country.")

            elif(month.lower() in ('7', '8', '9', 'monsoon', 'july', 'aug', 'august', 'sep', 'september')):
                print("It is a season of Monsoon.\nYou can Carry light cotton clothes as well as umbrella"
                      "\n The temperature at that time varies between 25 to 35 degree Celsius but it feels more due to humidity in the atmosphere.")

            elif(month.lower() in ('10', '11', 'autumn', 'oct', 'october', 'nov', 'november')):
                print("This is Autumn.\nPleasant Weather.\nTemperature in these days varies between 20-30 degree Celsius."
                      "\nCarry Light cotton with some woolen ones for precaution")
            else:
                print("Please try again.")
                continue

            opt = input("Wanna try again? (y/n): ")

        except:
            print("Please Try again.\n")


print("Hey!!\nI will assist you for your travel to India.")
print("There are 5 seasons in India.\n1. Winter(Months:)\n2. Spring\n3. Summer\n4. Monsoon\n5. Autumn")
logic()
