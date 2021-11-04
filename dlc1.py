import time
import datetime
import os.path
import os
from datetime import date
import time
import getpass
import webbrowser
import random
import sys
import pyttsx3
def smallScript():
    today = date.today()
    script = "small.py"
    current = "dFSFfFjlfjslgdkfsjngsjlgns;242;423;True;69;north;56;0.2"
    pissa = 0
    recover = list()
    def crashReport(recover,error,script):
        if os.path.isfile("crashLog.txt"):
            crash = open("crashLog.txt", "a")
        else:
            crash = open("crashLog.txt", "x")
        try:
            knowledge = open("knowledge.png","r")
            know = knowledge.read()
        except:   
            know = "F"
        try:
            traumatix = open("traumatix.png","r")
            trauma = traumatix.read()
        except:
            trauma = "F"
        try:
            data = open("data.png","r")
            vers = data.read().split(";")
            ver= "not F"
        except:
            ver = "F"
        try:
            crash.write(f"oopsie, you did a Error, here is all we now\n{recover[1]}/{recover[2]}/{recover[3]}\n")
        except:
            e =44
        if ver == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{vers[0]}\n")
        if know == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{know}\n")
        if trauma == "F":
            crash.write(f"no.sav//\n")
        else:
            if trauma !="":
                crash.write(f"{trauma}\n")
        crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
        crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
        crash.write(f"{recover}\n\n\n\n\n")
        crash.close()
    #check if version file sxists and if it is the same

    if os.path.isfile("data.png"):
        data = open("data.png","r")
        dataa = data.read().split(";")
        data.close()
        if dataa[0] == current:
            e = 4
        else:
            input("there is an error code 0006")
            error = "0006"
            crashReport(recover,error,script)
            exit()
    else:
        input("there is an error code 0007")
        error = "0007"
        crashReport(recover,error,script)
        exit()
    #check if the main program sent you to this script, or if someone just opened this one

    if os.path.isfile("check.png"):
        checker = open("check.png","r+")
        checkCheck = checker.read()
        if checkCheck == "AA"+str(today.strftime("%d/%m/%Y"))+"AC":
            checker.close()
        
            
        else:       
            error = "0004"
            crashReport(recover,error,script)
            input("there is an error code 0004")
            exit()
    else:
        error = "0001"
        crashReport(recover,error,script)
        input("there is an error code 0001")
        exit()
    #try to remove the redirect to this script, so no one can open it multiple times or change it
    checker.close()
    try:
        os.remove("check.png")
    except:
        error = "0002"
        crashReport(recover,error,script)
        input("there is an error code 0002\nTo protect against threats, the program has to be shutdown")
        exit()
    #load achievements.txt
    if os.path.isfile("achievements.txt"):
        achievement = open("achievements.txt", "a")
    else:
        achievement = open("achievements.txt", "x")
    achievement.close

    #just the script for the other exersice
    vraag9 = 0
    vraag8 = 0
    vraag10 = 0
    vraag11= 0
    vraag12= 0
    print("+++++++++++++++++++++++++++++++")
    print("good that you are here")
    print("we have a few questions for you")
    print("+++++++++++++++++++++++++++++++")
    pizza = input("do you want to order pizza? Y/N")
    if pizza == "Y" or pizza == "y":
        pissa = 1
        #redirect to the next script
        checker = open("knowledge.png", "x")
        checker.write("AA"+str(datetime.datetime.now())+"AD")
        checker.close()
        pizza1()
    if pissa == 0:    
        input("have you beaten the enderdragon?Y/N")
        vraag1 = int(input("how many years do you have practical experience with dressage?"))
        vraag2 = int(input("how many years do you have practical experience with juggling?"))
        input("do you want the job?Y/N")
        vraag3 = int(input("how many years do you have practical experience with acrobatics?"))
        vraag4 = input("do you have a MBO-4 Diploma? Y/N")
        vraag5 = input("do you own a truck driver's license? Y/N")
        input("does santaclaus exist?Y/N")
        vraag6 = input("do you own a tall hat? Y/N")
        input("how many people have you killed?")
        vraag7 = input("have you been born as a Male or as a Female? M/F")
        if vraag7 == "m" or vraag7 == "M":
            vraag8 = input("do you have a mustache? Y/N")
            if vraag8 == "y" or vraag8 =="Y":
                vraag9 = int(input("how tall is your mustache in CM?"))
            input("do you have a Hernia?Y/N")
        elif vraag7 == "f" or vraag7 == "F":
            vraag10 = input("what is your hair color? (r=red,b=blonde,ew = anything else)")
            vraag11 = input("what is your hairstyle? curled = C, braids = B,Bald = E")
            vraag12 = int(input("how tall is your hair in CM?"))
        input("how many kids do you have in your basement?")
        vraag13=int(input("how fat are you in KG?"))
        vraag14=int(input("how tall are you in CM?"))

        if vraag7 == "m" or vraag7 == "M":
            if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "Y" or vraag4 == "y") and (vraag5 == "Y" or vraag5 == "y") and (vraag6 == "Y" or vraag6 == "y") and (vraag8 == "Y" or vraag8 == "y") and vraag9 > 10 and vraag13 > 90 and vraag14 > 150:
                print("Congrats, you are a good canidate, we will call you.")
            else:
                print("Sorry, but ur not the man we are looking for, you better go empty my trash")
        elif vraag7 == "f" or vraag7 == "F":
            if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "y" or vraag4 == "Y") and (vraag5 == "y" or vraag5 == "Y") and (vraag6 == "y" or vraag6 == "Y") and vraag13 > 90 and vraag14 > 150 and (vraag10 == "r" or vraag10=="R") and (vraag11 == "C" or vraag11=="c") and vraag12 >20:
                print("Congrats, you are a good canidate, we will call you.")
            else:
                print("Nope, i think being stripper would fit a women like u more")
        #this is used for the achievement system
        know = open("knowledge.png", "r+")
        check = know.read().split(";")
        if check[22] != "True":
            print("(there is an achievement added to achievement.txt)")
            time.sleep(4)
            achievement=open("achievements.txt", "a+")
            achievement.write("\n |Hmm i am hungry| " +str(datetime.datetime.now()))
            achievement.close
            know.truncate(0)
            know.seek(0)
            check[22]= True
            for line in check:
                know.write(str(line) + ";")
            know.close()
        print("you die from a heart attack")
        time.sleep(2)        
def pizza2():
    today = date.today()
    current = "dFSFfFjlfjslgdkfsjngsjlgns;242;423;True;69;north;56;0.2"
    script = "big2.py"
    recover = list()
    def crashReport(recover,error,script):
        if os.path.isfile("crashLog.txt"):
            crash = open("crashLog.txt", "a")
        else:
            crash = open("crashLog.txt", "x")
        try:
            knowledge = open("knowledge.png","r")
            know = knowledge.read()
        except:   
            know = "F"
        try:
            traumatix = open("traumatix.png","r")
            trauma = traumatix.read()
        except:
            trauma = "F"
        try:
            data = open("data.png","r")
            vers = data.read().split(";")
            ver= "not F"
        except:
            ver = "F"
        try:
            crash.write(f"oopsie, you did a Error, here is all we now\n{recover[1]}/{recover[2]}/{recover[3]}\n")
        except:
            e =44
        if ver == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{vers[0]}\n")
        if know == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{know}\n")
        if trauma == "F":
            crash.write(f"no.sav//\n")
        else:
            if trauma !="":
                crash.write(f"{trauma}\n")
        crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
        crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
        crash.write(f"{recover}\n\n\n\n\n")
        crash.close()
    #see if there is a save file
    #do remove if not in part 2


        #check if version file sxists and if it is the same
        if os.path.isfile("data.png"):
            data = open("data.png","r")
            dataa = data.read().split(";")
            data.close()
            if dataa[0] == current:
                e = 4
            else:
                error = "0006"
                crashReport(recover,error,script)
                input("there is an error code 0006")
                exit()
        else:
            error = "0007"
            crashReport(recover,error,script)
            input("there is an error code 0007")
            exit()       

        #check if the main program sent you to this script, or if someone just opened this one
        if os.path.isfile("check.png"):
            checker = open("check.png","r+")
            checkCheck = checker.read()
            if checkCheck == "AA"+str(today.strftime("%d/%m/%Y"))+"AB":
                checker.close()
            
                
            else:        
                error = "0004"
                crashReport(recover,error,script)
                input("there is an error code 0004")
                exit()
        else:
            error = "0001"
            crashReport(recover,error,script)
            input("there is an error code 0001")
            exit()
        #try to remove the redirect to this script, so no one can open it multiple times or change it
        checker.close()
        try:
            os.remove("check.png")
        except:
            error = "0002"
            crashReport(recover,error,script)
            input("there is an error code 0002\nTo protect against threats, the program has to be shutdown")
            exit()

        if os.path.isfile("achievements.txt"):
            achievement = open("achievements.txt", "a")
        else:
            achievement = open("achievements.txt", "x")
        achievement.close

    #dit berekent de prijs per pizza
    def calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna):
        price = 0
        #grootte van pizza
        if dough == "small":
            price += 1
        if dough == "medium":
            price += 1.5
        if dough == "large":
            price += 2
        #als humongous gekozen is, kies large
        if dough == "humongous":
            price += 2
        #aantal pepperoni
        if pepperoni == "small":
            price += 0.4
        if pepperoni == "medium":
            price += 0.6
        if pepperoni == "large":
            price += 0.9
        if pepperoni == "humongous":
            price += 9
        #aantal kaas
        if cheese == "small":
            price += 0.2
        if cheese == "medium":
            price += 0.3
        if cheese == "large":
            price += 0.45
        if cheese == "humongous":
            price += 4.5
            #aantal pineapple
        if pineapple == "small":
            price += 0.2
        if pineapple == "medium":
            price += 4
        if pineapple == "large":
            price += 16
        if pineapple == "humongous":
            price += 256
            #aantal ham
        if ham == "small":
            price += 0.2
        if ham == "medium":
            price += 4
        if ham == "large":
            price += 16
        if ham == "humongous":
            price += 256
            #aantal tomaten saus
        if tomatosauce == "small":
            price += 0.1
        if tomatosauce == "medium":
            price += 0.2
        if tomatosauce == "large":
            price += 0.3
        if tomatosauce == "humongous":
            price += 0.5
            #aantal tonijn
        if tuna == "small":
            price += 1.2
        if tuna == "medium":
            price += 1.5
        if tuna == "large":
            price += 1.9
        if tuna == "humongous":
            price += 19
        return price
    #maakt random pizzas
    def randomTopping():
        from random import randrange
        number = (randrange(9))
        if number == 0 or number == 7:
            returnValue = "small"
        if number == 1 or number == 6:
            returnValue = "medium"
        if number == 2 or number == 5:
            returnValue = "large"
        if number == 3 or number == 4:
            returnValue = "humongous"
        if number == 8:
            returnValue = "NONE"
        return returnValue

    #dit is de setup zodat de rest werkt
    import os.path
    try:
        os.remove("pizCalc3.png")
    except:
        fd=2
    try:
        os.remove("pizCalc2.png")
    except:
        fd=1
    try:
        os.remove("pizCalc1.png")
    except:
        fd=4
    loop = True
    round = 1
    round2 = 1
    totalcosts = 0
    pizzaAmount = "startup"
    randomized = "no"
    keepRandomized = "no"
    import os
    know = open("knowledge.png", "r+")
    check = know.read().split(";")
    if check[23] != "True":
        print("(there is an achievement added to achievement.txt)")
        time.sleep(3)
        achievement=open("achievements.txt", "a+")
        achievement.write("\n |PIZZAAA| " +str(datetime.datetime.now()))
        achievement.close
        know.truncate(0)
        know.seek(0)
        check[21]= True
        for line in check:
            know.write(str(line) + ";")
        know.close()
    #dit is een loop die je blijft vragen of je meer wilt bestellen en of je de menu kaart wilt zien
    while loop == True:
        menukaart = input("do you want to look at the menu? >>>")
        if menukaart == "yes" or menukaart == "Yes":
            print("----------------------------------------------------------")   
            print("|             |  small  |  medium  |  large  | humongous | humangous==10*large") 
            print("|    Dough    |   €1    |   €1.5   |    €2   |           |") 
            print("|  Pepperoni  |  €0.4   |   €0.6   |   €0.9  |     €9    |")
            print("|   Cheese    |  €0.2   |   €0.3   |  €0.45  |    €4.5   |")
            print("|  pinapple   |  €0.2   |    €4    |   €16   |    €256   |")
            print("|    ham      |  €0.2   |    €4    |   €16   |    €256   |")
            print("| tomatosauce |  €0.1   |   €0.2   |  €0.3   |    €0.5   |")
            print("|    tuna     |  €1.2   |   €1.5   |  €1.9   |    €19    |")
            print("----------------------------------------------------------")   
        try:
            pizzaAmount = int(input("how many pizzas? >>>"))
        except:
            print("maybe try putting in a number next time")
        if pizzaAmount != "startup":
            if pizzaAmount > 0:

                #dit blijft herhalen tot het zoveel keer heeft herhaald als het aantal pizza's
                while round <= pizzaAmount:
                    round += 1

                    #check if file4 exists
                    if os.path.isfile("pizCalc4.png"):
                        file4 = open("pizCalc4.png", "a")
                    else:
                        file4 = open("pizCalc4.png", "x")
                    file4.close()
                    file4 = open("pizCalc4.png", "r")
                    allowRandom = file4.read()

                    #dit bekijkt of het al de 2e ronde is, want als je al een ronde bent geweest kan je de input skippen om de zelfde configuratie als de vorige pizza te nemen
                    if round > 2:
                        if keepRandomized == "yes" or keepRandomized == "Yes":
                            dough = randomTopping()
                            pepperoni = randomTopping()
                            cheese = randomTopping()
                            pineapple = randomTopping()
                            ham = randomTopping()
                            tomatosauce= randomTopping()
                            tuna = randomTopping()
                            print(round)
                        else:     
                            again = input("do you want to repeat the last order? >>>")
                            if again == "yes" or again == "Yes":
                                if randomized == "yes" or randomized == "Yes":
                                    keepRandomized = input("do you want to randomize all? >>>")
                                    if keepRandomized == "yes" or keepRandomized == "Yes":
                                        dough = randomTopping()
                                        pepperoni = randomTopping()
                                        cheese = randomTopping()
                                        pineapple = randomTopping()
                                        ham = randomTopping()
                                        tomatosauce= randomTopping()
                                        tuna = randomTopping()
                                    else:
                                        dough = randomTopping()
                                        pepperoni = randomTopping()
                                        cheese = randomTopping()
                                        pineapple = randomTopping()
                                        ham = randomTopping()
                                        tomatosauce= randomTopping()
                                        tuna = randomTopping()
                                else:
                                    print("Okay")

                            #hier vul je in welke topping je wilt als je een andere pizza wilt
                            else:
                                if allowRandom == "yes":
                                    randomized = input("do you want to randomize the order? >>>")
                                if randomized == "yes" or randomized == "Yes":
                                    dough = randomTopping()
                                    pepperoni = randomTopping()
                                    cheese = randomTopping()
                                    pineapple = randomTopping()
                                    ham = randomTopping()
                                    tomatosauce= randomTopping()
                                    tuna = randomTopping()

                                else:
                                    print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                                    dough = input("Dough >>>")
                                    pepperoni = input("Pepperoni >>>")
                                    cheese = input("Cheese >>>")
                                    pineapple = input("Pineapple >>>")
                                    ham = input("Ham >>>")
                                    tomatosauce = input("tomatosauce >>>")
                                    tuna = input("Tuna >>>")

                    #dit is voor de 1e pizza, waarbij je invult wat je wilt
                    else:
                        if allowRandom == "yes":
                            randomized = input("do you want to randomize the order? >>>")
                        if randomized == "yes" or randomized == "Yes":
                            dough = randomTopping()
                            pepperoni = randomTopping()
                            cheese = randomTopping()
                            pineapple = randomTopping()
                            ham = randomTopping()
                            tomatosauce= randomTopping()
                            tuna = randomTopping()

                        else:
                            print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                            dough = input("Dough >>>")
                            pepperoni = input("Pepperoni >>>")
                            cheese = input("Cheese >>>")
                            pineapple = input("Pineapple >>>")
                            ham = input("Ham >>>")
                            tomatosauce = input("tomatosauce >>>")
                            tuna = input("Tuna >>>")
                    file4.close()

                    #hier kijk je of de pizCalc2.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc2.txt
                    if os.path.isfile("pizCalc2.png"):
                        f = open("pizCalc2.png", "a")
                    else:
                        f = open("pizCalc2.png", "x")

                    #hier kijk je of de pizCalc1.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc1.txt
                    if os.path.isfile("pizCalc1.png"):
                        file2 = open("pizCalc1.png", "a")
                    else:
                        file2 = open("pizCalc1.png", "x")

                    #het aanroepen van de functie om de prijs van de pizza te berekenen
                    costPerPizza = calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna)
                    #het uploaden naar een file
                    file2.write(str(costPerPizza) + ",")

                    #kijken of er dingen niet zijn gekozen
                    if dough != "small" and dough != "medium" and dough != "large" and dough != "humongous":
                        dough = "NONE"
                    if dough == "humongous":
                        dough = "large"
                    if pepperoni != "small" and pepperoni != "medium" and pepperoni != "large" and pepperoni != "humongous":
                        pepperoni = "NONE"
                    if cheese != "small" and cheese != "medium" and cheese != "large" and cheese != "humongous":
                        cheese  = "NONE"
                    if pineapple != "small" and pineapple != "medium" and pineapple != "large" and pineapple != "humongous":
                        pineapple = "NONE"
                    if ham != "small" and ham != "medium" and ham != "large" and ham != "humongous":
                        ham = "NONE"
                    if tomatosauce != "small" and tomatosauce != "medium" and tomatosauce != "large" and tomatosauce != "humongous":
                            tomatosauce = "NONE"
                    if tuna != "small" and tuna != "medium" and tuna != "large" and tuna != "humongous":
                        tuna = "NONE"
                    f.write(dough + "," + pepperoni + "," + cheese + "," + pineapple + "," + ham + "," + tomatosauce + "," + tuna + ",")
                    totalcosts += costPerPizza
                    
                    #sluiten van de files
                    f.close()
                    file2.close()

                #het afrekenen
                print("that will be an amount of €" + str(totalcosts))
                receipt = input("do you want the receipt? >>>")
                if receipt == "yes" or receipt == "Yes":
                    while round2 <= pizzaAmount:
                        round2 += 1

                        #hier kijk je of de pizCalc3.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc3.txt
                        if os.path.isfile("pizCalc3.png"):
                            receipt = open("pizCalc3.png", "a")
                        else:
                            receipt = open("pizCalc3.png", "x")
                        #openen van andere files

                        file1 = open("pizCalc2.png", "r")
                        file2 = open("pizCalc1.png", "r")
                        #data opslaan

                        lines1 = file1.read().split(',', 7)
                        lines2 = file2.read().split(',', 1)
                        file1.close()
                        file2.close()

                        #bonnetje schrijven naar file
                        receipt.write("-------------------------------------\n")
                        receipt.write("|Pizza  size|"+lines1[0]+ "|\n")
                        receipt.write("| Pepperoni |"+lines1[1]+ "|\n")
                        receipt.write("|  Cheese   |"+lines1[2]+ "|\n")
                        receipt.write("| Pineapple |"+lines1[3]+ "|\n")
                        receipt.write("|    Ham    |"+lines1[4]+ "|\n")
                        receipt.write("|Tomatosauce|"+lines1[5]+ "|\n")
                        receipt.write("|   Tuna    |"+lines1[6]+ "|\n")
                        receipt.write("-------------------------------------\n")
                        receipt.write("|   Price   | €"+str(lines2[0])+ "|\n")
                        if allowRandom == "yes":
                            print(round2)
                        #files verwijderen
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines2[0]
                        #heropenen en herschrijven van files
                        file1 = open("pizCalc2.png", "w+")
                        file2 = open("pizCalc1.png", "w+")
                        for line in lines1:
                            file1.write(line + ",")
                        for line in lines2:
                            file2.write(line + ",")
                        
                        file1.close()
                        file2.close()
                
                    receipt.write("-------------------------------------\n")
                    receipt.write("|   Total   |€"+str(totalcosts)+ "|\n")
                    receipt.close()
                    receipt = open("pizCalc3.png", "r")
                    for x in receipt:
                        print(x.strip())
                    receipt.close()
                else:
                    print("okay")
                #zet de loop uit
                loop = False
                know = open("knowledge.png", "r+")
                check = know.read().split(";")
                if check[21] != "True":
                    print("(there is an achievement added to achievement.txt)")
                    time.sleep(3)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |True Ending !2! (original game)| " +str(datetime.datetime.now()))
                    achievement.close
                    know.truncate(0)
                    know.seek(0)
                    check[21]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
                print("congrats, this was the true ending! (of the original game)")
                try:
                    os.remove("pizcalc1.png")
                    os.remove("pizcalc2.png")
                except:
                    e = 8

                
                
            else:
                print("you need to atleast buy 1")
def pizza1():
    today = date.today()
    current = "dFSFfFjlfjslgdkfsjngsjlgns;242;423;True;69;north;56;0.2"
    script = "big1.py"
    recover = list()
    def crashReport(recover,error,script):
        if os.path.isfile("crashLog.txt"):
            crash = open("crashLog.txt", "a")
        else:
            crash = open("crashLog.txt", "x")
        try:
            knowledge = open("knowledge.png","r")
            know = knowledge.read()
        except:   
            know = "F"
        try:
            traumatix = open("traumatix.png","r")
            trauma = traumatix.read()
        except:
            trauma = "F"
        try:
            data = open("data.png","r")
            vers = data.read().split(";")
            ver= "not F"
        except:
            ver = "F"
        try:
            crash.write(f"oopsie, you did a Error, here is all we now\n{recover[1]}/{recover[2]}/{recover[3]}\n")
        except:
            e =44
        if ver == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{vers[0]}\n")
        if know == "F":
            crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
        else:
            crash.write(f"{know}\n")
        if trauma == "F":
            crash.write(f"no.sav//\n")
        else:
            if trauma !="":
                crash.write(f"{trauma}\n")
        crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
        crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
        crash.write(f"{recover}\n\n\n\n\n")
        crash.close()
    #check if version file sxists and if it is the same

        if os.path.isfile("data.png"):
            data = open("data.png","r")
            dataa = data.read().split(";")
            data.close()
            if dataa[0] == current:
                e = 4
            else:
                error = "0006"
                crashReport(recover,error,script)
                input("there is an error code 0006")
                exit()
        else:
            error = "0007"
            crashReport(recover,error,script)
            input("there is an error code 0007")
            exit()
                
        #check if the main program sent you to this script, or if someone just opened this one

        if os.path.isfile("check.png"):
            checker = open("check.png","r+")
            checkCheck = checker.read()
            if checkCheck == "AA"+str(today.strftime("%d/%m/%Y"))+"AD":
                checker.close()
            
                
            else:        
                error = "0004"
                crashReport(recover,error,script)
                input("there is an error code 0004")
                exit()
        else:
            error = "0001"
            crashReport(recover,error,script)
            input("there is an error code 0001")
            exit()
        #try to remove the redirect to this script, so no one can open it multiple times or change it
        checker.close()
        try:
            os.remove("check.png")
        except:
            error = "0002"
            crashReport(recover,error,script)
            input("there is an error code 0002\nTo protect against threats, the program has to be shutdown")
            exit()

        if os.path.isfile("achievements.txt"):
            achievement = open("achievements.txt", "a")
        else:
            achievement = open("achievements.txt", "x")
        achievement.close

    #dit berekent de prijs per pizza
    def calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna):
        price = 0
        #grootte van pizza
        if dough == "small":
            price += 1
        if dough == "medium":
            price += 1.5
        if dough == "large":
            price += 2
        #als humongous gekozen is, kies large
        if dough == "humongous":
            price += 2
        #aantal pepperoni
        if pepperoni == "small":
            price += 0.4
        if pepperoni == "medium":
            price += 0.6
        if pepperoni == "large":
            price += 0.9
        if pepperoni == "humongous":
            price += 9
        #aantal kaas
        if cheese == "small":
            price += 0.2
        if cheese == "medium":
            price += 0.3
        if cheese == "large":
            price += 0.45
        if cheese == "humongous":
            price += 4.5
            #aantal pineapple
        if pineapple == "small":
            price += 0.2
        if pineapple == "medium":
            price += 4
        if pineapple == "large":
            price += 16
        if pineapple == "humongous":
            price += 256
            #aantal ham
        if ham == "small":
            price += 0.2
        if ham == "medium":
            price += 4
        if ham == "large":
            price += 16
        if ham == "humongous":
            price += 256
            #aantal tomaten saus
        if tomatosauce == "small":
            price += 0.1
        if tomatosauce == "medium":
            price += 0.2
        if tomatosauce == "large":
            price += 0.3
        if tomatosauce == "humongous":
            price += 0.5
            #aantal tonijn
        if tuna == "small":
            price += 1.2
        if tuna == "medium":
            price += 1.5
        if tuna == "large":
            price += 1.9
        if tuna == "humongous":
            price += 19
        return price
    #maakt random pizzas
    def randomTopping():
        from random import randrange
        number = (randrange(9))
        if number == 0 or number == 7:
            returnValue = "small"
        if number == 1 or number == 6:
            returnValue = "medium"
        if number == 2 or number == 5:
            returnValue = "large"
        if number == 3 or number == 4:
            returnValue = "humongous"
        if number == 8:
            returnValue = "NONE"
        return returnValue

    #dit is de setup zodat de rest werkt
    import os.path
    try:
        os.remove("pizCalc3.png")
    except:
        fd=2
    try:
        os.remove("pizCalc2.png")
    except:
        fd=1
    try:
        os.remove("pizCalc1.png")
    except:
        fd=4
    loop = True
    round = 1
    round2 = 1
    totalcosts = 0
    pizzaAmount = "startup"
    randomized = "no"
    keepRandomized = "no"
    import os

    #dit is een loop die je blijft vragen of je meer wilt bestellen en of je de menu kaart wilt zien
    while loop == True:
        menukaart = input("do you want to look at the menu? >>>")
        if menukaart == "yes" or menukaart == "Yes":
            print("----------------------------------------------------------")   
            print("|             |  small  |  medium  |  large  | humongous | humangous==10*large") 
            print("|    Dough    |   €1    |   €1.5   |    €2   |           |") 
            print("|  Pepperoni  |  €0.4   |   €0.6   |   €0.9  |     €9    |")
            print("|   Cheese    |  €0.2   |   €0.3   |  €0.45  |    €4.5   |")
            print("|  pinapple   |  €0.2   |    €4    |   €16   |    €256   |")
            print("|    ham      |  €0.2   |    €4    |   €16   |    €256   |")
            print("| tomatosauce |  €0.1   |   €0.2   |  €0.3   |    €0.5   |")
            print("|    tuna     |  €1.2   |   €1.5   |  €1.9   |    €19    |")
            print("----------------------------------------------------------")   
        try:
            pizzaAmount = int(input("how many pizzas? >>>"))
        except:
            print("maybe try putting in a number next time")
        if pizzaAmount != "startup":
            if pizzaAmount > 0:

                #dit blijft herhalen tot het zoveel keer heeft herhaald als het aantal pizza's
                while round <= pizzaAmount:
                    round += 1

                    #check if file4 exists
                    if os.path.isfile("pizCalc4.png"):
                        file4 = open("pizCalc4.png", "a")
                    else:
                        file4 = open("pizCalc4.png", "x")
                    file4.close()
                    file4 = open("pizCalc4.png", "r")
                    allowRandom = file4.read()

                    #dit bekijkt of het al de 2e ronde is, want als je al een ronde bent geweest kan je de input skippen om de zelfde configuratie als de vorige pizza te nemen
                    if round > 2:
                        if keepRandomized == "yes" or keepRandomized == "Yes":
                            dough = randomTopping()
                            pepperoni = randomTopping()
                            cheese = randomTopping()
                            pineapple = randomTopping()
                            ham = randomTopping()
                            tomatosauce= randomTopping()
                            tuna = randomTopping()
                            print(round)
                        else:     
                            again = input("do you want to repeat the last order? >>>")
                            if again == "yes" or again == "Yes":
                                if randomized == "yes" or randomized == "Yes":
                                    keepRandomized = input("do you want to randomize all? >>>")
                                    if keepRandomized == "yes" or keepRandomized == "Yes":
                                        dough = randomTopping()
                                        pepperoni = randomTopping()
                                        cheese = randomTopping()
                                        pineapple = randomTopping()
                                        ham = randomTopping()
                                        tomatosauce= randomTopping()
                                        tuna = randomTopping()
                                    else:
                                        dough = randomTopping()
                                        pepperoni = randomTopping()
                                        cheese = randomTopping()
                                        pineapple = randomTopping()
                                        ham = randomTopping()
                                        tomatosauce= randomTopping()
                                        tuna = randomTopping()
                                else:
                                    print("Okay")

                            #hier vul je in welke topping je wilt als je een andere pizza wilt
                            else:
                                if allowRandom == "yes":
                                    randomized = input("do you want to randomize the order? >>>")
                                if randomized == "yes" or randomized == "Yes":
                                    dough = randomTopping()
                                    pepperoni = randomTopping()
                                    cheese = randomTopping()
                                    pineapple = randomTopping()
                                    ham = randomTopping()
                                    tomatosauce= randomTopping()
                                    tuna = randomTopping()

                                else:
                                    print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                                    dough = input("Dough >>>")
                                    pepperoni = input("Pepperoni >>>")
                                    cheese = input("Cheese >>>")
                                    pineapple = input("Pineapple >>>")
                                    ham = input("Ham >>>")
                                    tomatosauce = input("tomatosauce >>>")
                                    tuna = input("Tuna >>>")

                    #dit is voor de 1e pizza, waarbij je invult wat je wilt
                    else:
                        if allowRandom == "yes":
                            randomized = input("do you want to randomize the order? >>>")
                        if randomized == "yes" or randomized == "Yes":
                            dough = randomTopping()
                            pepperoni = randomTopping()
                            cheese = randomTopping()
                            pineapple = randomTopping()
                            ham = randomTopping()
                            tomatosauce= randomTopping()
                            tuna = randomTopping()

                        else:
                            print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                            dough = input("Dough >>>")
                            pepperoni = input("Pepperoni >>>")
                            cheese = input("Cheese >>>")
                            pineapple = input("Pineapple >>>")
                            ham = input("Ham >>>")
                            tomatosauce = input("tomatosauce >>>")
                            tuna = input("Tuna >>>")
                    file4.close()

                    #hier kijk je of de pizCalc2.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc2.txt
                    if os.path.isfile("pizCalc2.png"):
                        f = open("pizCalc2.png", "a")
                    else:
                        f = open("pizCalc2.png", "x")

                    #hier kijk je of de pizCalc1.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc1.txt
                    if os.path.isfile("pizCalc1.png"):
                        file2 = open("pizCalc1.png", "a")
                    else:
                        file2 = open("pizCalc1.png", "x")

                    #het aanroepen van de functie om de prijs van de pizza te berekenen
                    costPerPizza = calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna)
                    #het uploaden naar een file
                    file2.write(str(costPerPizza) + ",")

                    #kijken of er dingen niet zijn gekozen
                    if dough != "small" and dough != "medium" and dough != "large" and dough != "humongous":
                        dough = "NONE"
                    if dough == "humongous":
                        dough = "large"
                    if pepperoni != "small" and pepperoni != "medium" and pepperoni != "large" and pepperoni != "humongous":
                        pepperoni = "NONE"
                    if cheese != "small" and cheese != "medium" and cheese != "large" and cheese != "humongous":
                        cheese  = "NONE"
                    if pineapple != "small" and pineapple != "medium" and pineapple != "large" and pineapple != "humongous":
                        pineapple = "NONE"
                    if ham != "small" and ham != "medium" and ham != "large" and ham != "humongous":
                        ham = "NONE"
                    if tomatosauce != "small" and tomatosauce != "medium" and tomatosauce != "large" and tomatosauce != "humongous":
                            tomatosauce = "NONE"
                    if tuna != "small" and tuna != "medium" and tuna != "large" and tuna != "humongous":
                        tuna = "NONE"
                    f.write(dough + "," + pepperoni + "," + cheese + "," + pineapple + "," + ham + "," + tomatosauce + "," + tuna + ",")
                    totalcosts += costPerPizza
                    
                    #sluiten van de files
                    f.close()
                    file2.close()

                #het afrekenen
                print("that will be an amount of €" + str(totalcosts))
                receipt = input("do you want the receipt? >>>")
                if receipt == "yes" or receipt == "Yes":
                    while round2 <= pizzaAmount:
                        round2 += 1

                        #hier kijk je of de pizCalc3.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc3.txt
                        if os.path.isfile("pizCalc3.png"):
                            receipt = open("pizCalc3.png", "a")
                        else:
                            receipt = open("pizCalc3.png", "x")
                        #openen van andere files

                        file1 = open("pizCalc2.png", "r")
                        file2 = open("pizCalc1.png", "r")
                        #data opslaan

                        lines1 = file1.read().split(',', 7)
                        lines2 = file2.read().split(',', 1)
                        file1.close()
                        file2.close()

                        #bonnetje schrijven naar file
                        receipt.write("-------------------------------------\n")
                        receipt.write("|Pizza  size|"+lines1[0]+ "|\n")
                        receipt.write("| Pepperoni |"+lines1[1]+ "|\n")
                        receipt.write("|  Cheese   |"+lines1[2]+ "|\n")
                        receipt.write("| Pineapple |"+lines1[3]+ "|\n")
                        receipt.write("|    Ham    |"+lines1[4]+ "|\n")
                        receipt.write("|Tomatosauce|"+lines1[5]+ "|\n")
                        receipt.write("|   Tuna    |"+lines1[6]+ "|\n")
                        receipt.write("-------------------------------------\n")
                        receipt.write("|   Price   | €"+str(lines2[0])+ "|\n")
                        if allowRandom == "yes":
                            print(round2)
                        #files verwijderen
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines1[0]
                        del lines2[0]
                        #heropenen en herschrijven van files
                        file1 = open("pizCalc2.png", "w+")
                        file2 = open("pizCalc1.png", "w+")
                        for line in lines1:
                            file1.write(line + ",")
                        for line in lines2:
                            file2.write(line + ",")
                        
                        file1.close()
                        file2.close()
                
                    receipt.write("-------------------------------------\n")
                    receipt.write("|   Total   |€"+str(totalcosts)+ "|\n")
                    receipt.close()
                    receipt = open("pizCalc3.png", "r")
                    for x in receipt:
                        print(x.strip())
                    receipt.close()
                else:
                    print("okay")
                #zet de loop uit
                loop = False
                know = open("knowledge.png", "r+")
                check = know.read().split(";")
                if check[20] != "True":
                    print("(there is an achievement added to achievement.txt)")
                    time.sleep(3)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |True Ending !1! (original game)| " +str(datetime.datetime.now()))
                    achievement.close
                    know.truncate(0)
                    know.seek(0)
                    check[20]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
                print("congrats, this was the true ending! but if u reopen it there might be new things to do")
                try:
                    os.remove("pizcalc1.png")
                    os.remove("pizcalc2.png")
                except:
                    e = 8
                
                
            else:
                print("you need to atleast buy 1")
def menu():
    

    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    def printing(text, options, waitingSeconds, textspeed):  
        if options[0] == 1:
            for letter in text:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(options[5])
            print()
            if waitingSeconds != 0:
                time.sleep(waitingSeconds / textspeed)
        else:
            print(text)
            
        if options[1] == 1:
            engine.say(text)
            engine.runAndWait()
        else:
            if waitingSeconds != 0:
                time.sleep(waitingSeconds / textspeed)
    def prints(text, options, waitingSeconds):
        printing(text,options, waitingSeconds, options[2])

    if os.path.isfile("options.png"): 
        fileOptions = open("options.png", "a")
    else:
        fileOptions = open("options.png", "x")
    fileOptions.close
    try:
        fileOptions =open("options.png", "r")
        optionsString = fileOptions.read().split(';')
        options = [int(optionsString[0]), int(optionsString[1]), float(optionsString[2]), int(optionsString[3]), int(optionsString[4]), float(optionsString[5])]
        textspeed = options[2]
    except:
        options = [0, 0, 1.4, 1, 0, 0.1]
        textspeed = options[2]
    fileOptions.close
    prints("hello, welcome to this options menu.", options, 3)
    prints("this is how your the text will work when you go back.", options, 4)
    loop1 = 1
    while loop1 == 1:
        prints("do you want to change the settings?", options, 0)
        answer = input("Y/N:")
        if answer.lower() == "y":
            prints("okay", options, 0)
            loop2 = 1
            while loop2 == 1:
                prints("do you want the letters coming in 1 by 1?", options, 0)
                answer1 = input("Y/N:")
                if answer1.lower() == "y":
                    options[0] = 1
                    loop7 = 1
                    while loop7 == 1:
                        prints("this is how it looks, do you want to confirm?", options, 0)
                        answer1 = input("Y/N:")
                        if answer1.lower() == "y":
                            loop2 = 0
                            loop7 = 0
                        elif answer1.lower() == "n":
                            prints("okay", options, 0)
                            loop7 = 0
                        else:
                            prints("sorry, i didn't get that",options, 0)
                elif answer1.lower() == "n":
                    options[0] = 0
                    loop6 = 1
                    while loop6 == 1:
                        prints("this is how it looks, do you want to confirm?", options, 0)
                        answer1 = input("Y/N:")
                        if answer1.lower() == "y":
                            loop6 = 0
                            loop2 = 0
                        elif answer1.lower() == "n":
                            prints("okay", options, 0)
                            loop6 = 0
                        else:
                            prints("sorry, i didn't get that",options, 0)
                else:
                    prints("sorry, i didn't get that",options, 0)
            if options[0] == 1:
                loop3 = 1
                while loop3 == 1:
                    prints("do you want to change the textspeed for the letters coming in 1 by 1?", options, 0)
                    answer1 = input("Y/N:")
                    if answer1.lower() == "y":
                        loop4 = 1
                        while loop4 == 1:
                            prints("input a number (0.1 is default, higher is slower, smaller is faster)", options, 0)
                            numberInput = input(">>>")
                            try:
                                number = float(numberInput)
                                notANumber = 0
                            except:
                                notANumber = 1
                            if notANumber == 1:
                                prints("this is not a number", options, 0)
                            elif number >= 0.5:
                                prints("it's not allowed to wait 1 second per 2 letters (or even longer), out of safety meassures", options, 0)
                            else:
                                loop5 = 1
                                while loop5 == 1:
                                    options[5] = number
                                    prints("this is how it looks, do you confirm?", options, 0)
                                    answer1 = input("Y/N:")
                                    if answer1.lower() == "y":
                                        loop4 = 0
                                        loop3 = 0
                                        loop5 = 0
                                    elif answer1.lower() == "n":
                                        prints("okay", options, 0)
                                        loop5 = 0
                                    else:
                                        prints("sorry, i didn't get that",options, 0)
                    elif answer1.lower() == "n":
                        loop3 = 0
                    else:
                        prints("sorry, i didn't get that",options, 0)
            loop8 = 1
            while loop8 == 1:
                prints("do you want to change the delay between the lines of text", options, 3)
                answer1 = input("Y/N:")
                if answer1.lower() == "y":
                    loop9 = 1
                    while loop9 == 1:
                        prints("input a number (1.4 is default, higher is faster, smaller is slower)", options, 3)
                        numberInput = input(">>>")
                        try:
                            number = float(numberInput)
                            notANumber = 0
                        except:
                            notANumber = 1
                        if notANumber == 1:
                            prints("this is not a number", options, 1)
                        elif number <= 0.4:
                            prints("it's not allowed to go smaller than 0.5, cause that means sometimes you need to wait 40 seconds", options, 4)
                        else:
                            loop10 = 1
                            while loop10 == 1:
                                options[2] = number
                                prints("this is how it looks, do you confirm?", options, 2)
                                answer1 = input("Y/N:")
                                if answer1.lower() == "y":
                                    loop9 = 0
                                    loop8 = 0
                                    loop10 = 0
                                elif answer1.lower() == "n":
                                    prints("okay", options, 0)
                                    loop10 = 0
                                else:
                                    prints("sorry, i didn't get that",options, 2)
                elif answer1.lower() == "n":
                    loop8 = 0
                else:
                    prints("sorry, i didn't get that",options, 2)
            loop2 = 1
            while loop2 == 1:
                prints("do you want to enable text to speech (if u have 1 by 1 letters enabled it wont work)", options, 0)
                answer1 = input("Y/N:")
                if answer1.lower() == "y":
                    options[1] = 1
                    loop7 = 1
                    while loop7 == 1:
                        prints("this is how it sounds (change voice next), do you confirm?", options, 0)
                        answer1 = input("Y/N:")
                        if answer1.lower() == "y":
                            loop2 = 0
                            loop7 = 0
                        elif answer1.lower() == "n":
                            prints("okay", options, 0)
                            loop7 = 0
                        else:
                            prints("sorry, i didn't get that",options, 0)
                elif answer1.lower() == "n":
                    options[1] = 0
                    loop2 = 0
                    
                else:
                    prints("sorry, i didn't get that",options, 0)

            if options[1] == 1:
                loop8 = 1
                while loop8 == 1:
                    prints("do you want to change the voice of the text to speech?", options, 0)
                    answer1 = input("Y/N:")
                    if answer1.lower() == "y":
                        loop9 = 1
                        while loop9 == 1:
                            prints("input a number 0, 1, or 2", options, 0)
                            numberInput = input(">>>")
                            if numberInput != "1" and numberInput != "0" and numberInput != "2":
                                prints("sorry, i didn't get that",options, 0)
                            options[3] = int(numberInput)
                            loop0 = 1
                            while loop0 == 1:
                                prints("this is how it sounds, do you confirm?", options, 0)
                                answer1 = input("Y/N:")
                                if answer1.lower() == "y":
                                    loop9 = 0
                                    loop8 = 0
                                    loop0 = 0
                                elif answer1.lower() == "n":
                                    prints("okay", options, 0)
                                    loop0 = 0
                                else:
                                    prints("sorry, i didn't get that",options, 0)
                    elif answer1.lower() == "n":
                        loop8 = 0
                    else:
                        prints("sorry, i didn't get that",options, 0)
            loop2 = 1
            while loop2 == 1:
                prints("do you want to disable the endgame?", options, 0)
                answer1 = input("Y/N:")
                if answer1.lower() == "y":
                    options[4] = 1
                    loop2 = 0
                elif answer1.lower() == "n":
                    options[4] = 0
                    loop2 = 0
                else:
                    prints("sorry, i didn't get that",options, 0)
            prints("here is the end result",options, 0)
        elif answer.lower() == "n":
            print()
            loop1 = 0
        else:
            prints("sorry, i didn't get that",options, 0)

    optionsToString = ""
    if os.path.isfile("options.png"):
        option = open("options.png", "a+")
        option.truncate(0)
        option.seek(0)
    else:
        option = open("options.png", "x") 
    for x in range(0, len(options)):
        optionsToString += str(options[x]) + ";" 
    option.write(optionsToString)
    option.close()

