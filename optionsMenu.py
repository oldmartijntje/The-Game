def menu():
    import time
    import getpass
    import os
    import os.path
    import datetime
    from datetime import date
    import webbrowser
    import random
    import sys
    import pyttsx3

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

    if os.path.isfile("options.txt"): 
        fileOptions = open("options.txt", "a")
    else:
        fileOptions = open("options.txt", "x")
    fileOptions.close
    try:
        fileOptions =open("options.txt", "r")
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
                prints("do you want to change the delay between the lines of text", options, 0)
                answer1 = input("Y/N:")
                if answer1.lower() == "y":
                    loop9 = 1
                    while loop9 == 1:
                        prints("input a number (1.4 is default, higher is faster, smaller is slower)", options, 0)
                        numberInput = input(">>>")
                        try:
                            number = float(numberInput)
                            notANumber = 0
                        except:
                            notANumber = 1
                        if notANumber == 1:
                            prints("this is not a number", options, 0)
                        elif number <= 0.4:
                            prints("it's not allowed to go smaller than 0.5, cause that means sometimes you need to wait 40 seconds", options, 0)
                        else:
                            loop10 = 1
                            while loop10 == 1:
                                options[2] = number
                                prints("this is how it looks, do you confirm?", options, 0)
                                answer1 = input("Y/N:")
                                if answer1.lower() == "y":
                                    loop9 = 0
                                    loop8 = 0
                                    loop10 = 0
                                elif answer1.lower() == "n":
                                    prints("okay", options, 0)
                                    loop10 = 0
                                else:
                                    prints("sorry, i didn't get that",options, 0)
                elif answer1.lower() == "n":
                    loop8 = 0
                else:
                    prints("sorry, i didn't get that",options, 0)
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
            print("okay")
            loop1 = 0
        else:
            prints("sorry, i didn't get that",options, 0)

    optionsToString = ""
    if os.path.isfile("options.txt"):
        option = open("options.txt", "a+")
        option.truncate(0)
        option.seek(0)
    else:
        option = open("options.txt", "x") 
    for x in range(0, len(options)):
        optionsToString += str(options[x]) + ";" 
    option.write(optionsToString)
    option.close()