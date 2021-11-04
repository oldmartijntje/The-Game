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
from dlc1 import *
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
if os.path.isfile("DLC.activ"):
    achievements = 38
else:
    achievements = 28
script = "the game launcher.py"
current = "dFSFfFjlfjslgdkfsjngsjlgns;242;423;True;69;north;56;0.2"
recover = list()
exxit = 0
today = date.today()
def optionsEdit(option):
    optionsToString = ""
    if os.path.isfile("options.png"):
        options = open("options.png", "a+")
        options.truncate(0)
        options.seek(0)
    else:
        options = open("options.png", "x") 
    for x in range(0, len(option)):
        optionsToString += str(option[x]) + ";"
    options.write(optionsToString)
    options.close()
    menu()
    try:
        fileOptions =open("options.png", "r")
        optionsString = fileOptions.read().split(';')
        option = [int(optionsString[0]), int(optionsString[1]), float(optionsString[2]), int(optionsString[3]), int(optionsString[4]), float(optionsString[5])]
        textspeed = option[2]
    except:
        option = [0, 0, 1.4, 1, 0, 0.1]
        textspeed = option[2]
    if option[4] == 1:
        try:
            f.close()
        except:
            e = 0
    return option, textspeed
def prints(text, options, waitingSeconds):
    printing(text,options, waitingSeconds, options[2])
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")
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
        crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
    else:
        if trauma !="":
            crash.write(f"{trauma}\n")
    crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
    crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
    crash.write(f"{recover}\n\n\n\n\n")
    crash.close()
def save(irritation, textspeed, cringe, option):
    if option[4] == 0:
        open('traumatix.png', 'w').close()
        f = open("traumatix.png", "a")
        f.write(str(cringe)+";"+str(irritation)+";"+str(textspeed))
        f.close()
def dlc(irritation, textspeed, cringe, options):
    time.sleep(2 / textspeed)
    printing("Hmm, seems like the roadblock there once was is gone", options, 4, textspeed)
def dlc2(irritation, textspeed, cringe, options):
    def fibonacci(fullNumber,loopNumber):
        midNumber = 0
        midNumber = fullNumber + loopNumber
        loopNumber = fullNumber
        fullNumber = midNumber
        print(fullNumber)
        return fullNumber,loopNumber
    printing("you open the computer",options, 3, textspeed)
    printing("there are some things still opened",options, 4, textspeed)
    printing("let's check it out shall we",options, 2, textspeed)
    loop = True
    while loop == True:
        printing("\nthere are some websites open, do we want to open a website, or something else?",options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "else" in input1[0]:
            printing("there are 5 unnamed python scripts, and the internet browser ofc",options, 4, textspeed)
            loop1 = True
            while loop1 == True:
                printing("\nwhich one do you want to open?",options, 0, textspeed)
                input1 = input(">>>").split('.',1)
                if input1[0] == "options":
                    options, textspeed = optionsEdit(options)
                elif input1[0] == "1":
                    printing("okay, let's open the first one",options, 3, textspeed)
                    def addition(number1:int=10, number2:int=12):
                        printing(f"{number1} + {number2} = "+str(number1+number2))
                    def subtraction(number1:int=58, number2:int=34):
                        printing(f"{number1} - {number2} = "+str(number1-number2))
                    def multiplication(number1:int=6, number2:int=7):
                        printing(f"{number1} x {number2} = "+str(number1*number2))
                    def division(number1:int=144, number2:int=12):
                        printing(f"{number1} : {number2} = "+str(number1/number2))
                    def increment(number:int=12):
                        printing(f"{number} + 1 = "+str(number+1))
                    def decrement(number:int=34):
                        printing(f"{number} - 1 = "+str(number-1))
                    for x in range (1,4):
                        addition(random.randint(0, 69),random.randint(0, 69))
                        subtraction(random.randint(0, 69),random.randint(0, 69))
                        multiplication(random.randint(0, 69),random.randint(0, 69))
                        division(random.randint(0, 69),random.randint(1, 69))
                        increment(random.randint(0, 69))
                        decrement(random.randint(0, 69))
                    printing("\nyeah okay that is random",options, 3, textspeed)
                    printing("let's try another app shall we?",options, 3, textspeed)
                elif input1[0] == "2":
                    printing("okay, let's open the second one",options, 3, textspeed)
                    def helloWorld(num:int=1):
                        for x in range(1, num+1):
                            printing(f"{x}.hello World!",options, 0, textspeed)
                    helloWorld(int(input("it asks 'how many times?'")))
                    printing("\nyeah okay that is random",options, 3, textspeed)
                    printing("hmm okay let's open another one",options, 3, textspeed)
                    printing("suddenly something grabs you by your neck",options, 3, textspeed)
                    printing("you feel something sharp cutting into your skin",options, 4, textspeed)
                    printing("it's efenitely a knife",options, 3, textspeed)
                    printing("it slices through your skin",options, 3, textspeed)
                    printing("you feel an immense pain whilst u drift away",options, 3, textspeed)
                    printing("[u died]",options, 3, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[36] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Weird python script| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[36]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif input1[0] == "3":
                    prints("okay, let's open the third one",options, 3)
                    def table(number: int):
                        for x in range(1,11):
                            yeet = int(x)*int(number)
                            print(f"{x} times {number} is " +str(yeet))
                    inputAnswer = input("from what number do you want to see the table?")
                    table(inputAnswer)
                    prints("okay, that is a nice tool, but i am old enough to calculate that myself",options, 4)
                    prints("hey look, there is a note in the code",options, 3)
                    prints("something about a thing called fibunacci, hmm weird",options, 3)
                    prints("but i'll remember it for if i come across it",options, 3)
                    prints("suddenly, you notice something, it's a loud noice",options, 3)
                    prints("you walk outside and see an airplane going in the direction of your house",options, 4)
                    prints("you start to run as fast as possible",options, 3)
                    prints("suddenly you hear someone else running, you try to look",options, 3)
                    prints("you recognize the person but don't know from where",options, 3)
                    prints("the person hasn't noticed you, you decide to hide behind a dumpster",options, 4)
                    prints("you see him hide behind a wall",options, 2)
                    prints("a ear deafening sound hits you, you lose consciousness",options, 3)
                    answer = input("\npress Enter to continue\n")
                    if answer == "options":
                        options, textspeed = optionsEdit(options)
                    prints("you wake up",options, 2)
                    prints("you have no idea what time it is, you notice that the person is gone",options, 4)
                    prints("you start to look around",options, 2)
                    prints("suddenly you hear a sound of a sniper, you run away for cover",options, 3)
                    prints("you wait for a while, but nothing happends",options, 3)
                    prints("you start to look around, curious of what happened",options, 3)
                    prints("you walk back to the house, but then you see the sniper and immediatly walk back",options, 4)
                    prints("you run the opposite way as fast as you can",options, 3)
                    prints("suddenly you hear some sounds from behind you",options, 3)
                    prints("you look behind you and see someone following you with a knife",options, 3)
                    prints("you start looking for a hiding spot, whilst running even faster",options, 3)
                    prints("you notice a small alleyway",options, 2)
                    prints("you immediatly turn right and start to hide",options, 3)
                    prints("you enter the severs, in the hope he doesn't follow you here",options, 3)
                    prints("you hear some footsteps above you that suddenly stop",options, 3)
                    prints("you hold your breath, nothing happends",options, 3)
                    prints("you slowly start to navigate the sewers, trying not to make any sound",options, 4)
                    prints("once you get far enough away you start to run",options, 3)
                    prints("you notice a light in the distance",options, 3)
                    answer = input("\npress Enter to continue\n")
                    if answer == "options":
                        options, textspeed = optionsEdit(options)
                    prints("you slow down and start walking towards the light",options, 3)
                    prints("when you reach the light there is nothing to be seen",options, 3)
                    prints("there is nothing, not even the source of the light",options, 3)
                    prints("you start to investigate a little bit more an notice a loose brick",options, 4)
                    prints("you pull it out of the wall and see a passageway",options, 3)
                    prints("you move away enough bricks to go into the passageway",options, 3)
                    prints("you walk through the passageway and end up in some sort of a lab",options, 4)
                    prints("you look around and see the person that was following you",options, 3)
                    prints("you try to go back but then he says 'wait!'",options, 3)
                    prints("'i won't hurt you, don't worry'",options, 3)
                    prints("you look at him and ask, why were you following me then with a knife?",options, 4)
                    prints("'that is one of us, the bad kind atleast, they try to kill us'",options, 3)
                    prints("what do you mean with 1 of us?",options, 3)
                    prints("'haven't you noticed that time gets looped over and over?'",options, 3)
                    prints("'every time you relive it, you create a new you, and the old you, will do the same as you did last time'",options, 5)
                    prints("'atleast, unless they interact with eachother, like now.'",options, 3)
                    prints("but then why do they try to kill us?",options, 3)
                    prints("'they want to stop the loop, and end with only 1 version of us, so the timeline won't split'",options, 4)
                    prints("'and since they remember all of the past, when they enter the organization, they can kill all the old ones'",options, 5)
                    answer = input("\npress Enter to continue\n")
                    if answer == "options":
                        options, textspeed = optionsEdit(options)
                    prints("so how did that guy not know i was going to hide in the sewers?",options, 3)
                    prints("'for the same reason you don't remember me, because of my device'",options, 4)
                    prints("'right when the loop resets, whoever is in this room, their memory's get whiped of this day'",options, 4)
                    prints("'so no one remembers whe exist, and we will escape once the loop is stopped'",options, 4)
                    prints("and so we will create our own timelines where we didn't kill anyone?",options, 4)
                    prints("'yes' suddenly the other persons watch starts beeping",options, 3)
                    prints("'the loop will reset in some seconds, succes!'",options, 3)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[37] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |This Never Happened| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[37]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif input1[0] == "4":
                    prints("okay, let's open the 4th one",options, 3)
                    time = 0
                    while True:
                        if time == 0:
                            print(str(time)+":00AM")
                        elif time > 0 and time < 12:
                            print(str(time)+":00AM")
                        elif time == 12:
                            print(str(time)+":00PM")
                        else:
                            print(str(time)+":00PM")
                        time += 1
                        if time == 24:
                            break
                    prints("okay weird, let's open another one",options, 4)
                elif input1[0] == "5":
                    printing("okay, let's open the 5th one",options, 3, textspeed)
                    def identificatie(naam:str,leeftijd:int):
                        print(f"\nthe name of this person is {naam} and their age is {leeftijd}\n")
                    print("say stop to stop")
                    while True:
                        name = input("what is their name?")
                        if name == "stop":
                            break
                        age = input(f"what is {name} their age?")
                        if age == "stop":
                            break
                        intAge = int(age)
                        identificatie(name,intAge)
                    prints("okay sure, let's open something else",options, 4)
                elif "web" in input1[0] or "browser" in input1[0] or "site" in input1[0]:
                    prints("okay, let's go back",options, 4)
                    break

            if exxit == 1:
                break
        elif "web" in input1[0] or "browser" in input1[0] or "site" in input1[0] or "back" in input1[0]:
            loop1 = True
            while loop1 == True:
                printing("there are 4 websites opened",options, 2, textspeed)
                printing("1 is www.numbers.com, 2 is https://dotw.org, 3 is http://thousand.nl, and 4 is http://fibonacci.net, or you can open a new one",options, 3, textspeed)
                printing("\nwhich one do you want to open?",options, 0, textspeed)
                input1 = input(">>>").split('.',1)
                if input1[0] == "options":
                    options, textspeed = optionsEdit(options)
                elif "numbers" in input1[0] or input1[0]== "1":
                    printing("okay, you decide to open www.numbers.com",options, 4, textspeed)
                    timee = 0
                    while True:
                        if timee >20 and timee<50:
                            if timee % 2 == 0:
                                printing(timee,options, 0, textspeed)
                        timee+=1
                        if timee == 51:
                            break
                    time.sleep(2 / textspeed)
                    printing("okay, www.numbers.com is weird",options, 2, textspeed)
                    printing("right as you want to close the www.numbers.com website, you feel something held against the back of your head",options, 4, textspeed)
                    printing("'move, and you will die' a fermilliar voice says",options, 2, textspeed)
                    printing("you try to turn around",options, 1, textspeed)
                    printing("you hear the trigger click")
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[28] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Random numbers?| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[28]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif "dotw" in input1[0] or input1[0]== "2":
                    printing("okay, you decide to open https://dotw.org",options, 4, textspeed)
                    timeee = 0
                    weekNamen = ["mo","tu","we","th","fr","sa","su"]
                    while True:
                        dag =input("say a name of a day of the week (mo =  monday, th = thursday")
                        if dag in weekNamen:
                            break
                        else:
                            printing("that's not a day of the week",options, 0, textspeed)   
                    while True:
                        if dag != weekNamen[timeee]:
                            printing(weekNamen[timeee],options, 0, textspeed)
                        else:
                            printing(weekNamen[timeee],options, 0, textspeed)
                            break  
                        timeee+=1
                    time.sleep(2 / textspeed)
                    printing("okay, https://dotw.org is weird",options, 3, textspeed)
                    printing("hmm, so what else is there?",options, 2, textspeed)
                    printing("hey, let's try this website...",options, 4, textspeed)
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                    time.sleep(1)
                    input("\npress enter to continue\n")
                    printing("ah damn, it's a rickroll",options, 4, textspeed)
                    printing("you pickup the gun next to you and shoot yourself",options, 4, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[29] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Never gonna give you up!| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[29]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif "thousand" in input1[0] or input1[0]== "3":
                    printing("okay, you decide to open http://thousand.nl",options, 4, textspeed)
                    amount = 0
                    round = 50
                    while True:
                        print(str(amount) +" + "+str(round)+" = "+str(amount+round))
                        amount +=round
                        round+=1
                        time.sleep(0.5)
                        if amount >= 1000:
                            break
                    printing("that was intence, is it some sort of a code?",options, 4, textspeed)
                    printing("i could decrypt it",options, 2, textspeed)
                    printing("something hits your head",options, 2, textspeed)
                    printing("everything goes black",options, 2, textspeed)
                    printing("[u died]",options, 2, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[30] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Secret Code?| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[30]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif "fibonacci" in input1[0] or input1[0]== "4":
                    printing("okay, you decide to open http://fibonacci.net",options, 4, textspeed)
                    printing("there is a lot of text here, let's just skip over that",options, 2, textspeed)
                    printing("hey what is this? u click on a button labelled 'start'",options, 4, textspeed)
                    lastNumber = 0
                    thisNumber = 1
                    while True:
                        try:
                            loopTime = int(input("it asks you 'how many times?'\n"))
                            break
                        except:
                            printing("maybe try putting in a number",options, 0, textspeed)
                    print("\n0\n1")
                    for x in range(0,loopTime):
                        thisNumber,lastNumber = fibonacci(thisNumber,lastNumber)
                    printing("\nokay that is defenitely interesting",options, 3, textspeed)
                    printing("there seems to be some sort of logic involved",options, 3, textspeed)
                    printing("hmm maybe we could look up something that explains this",options, 3, textspeed)
                    printing("maybe i can get the wikipedia link adress and open it in this pc's browser",options, 3, textspeed)
                    printing("\nhmm what is that sound? you open the windows to see where it comes from",options, 4, textspeed)
                    printing("you see a plane flying in the direction of the house you are in",options, 3, textspeed)
                    printing("you run to the pc, turn it of and run outside",options, 3, textspeed)
                    printing("whilst you run through the garden you look behind you too see how long you have to escape",options, 4, textspeed)
                    printing("whilst looking at the airplane you trip over some cobblestones",options, 3, textspeed)
                    printing("you faceplant onto the cobblestones",options, 3, textspeed)
                    printing("everything goes black, and you wait for the crash",options, 3, textspeed)
                    printing("the plane crashes, it's a huge explosion",options, 3, textspeed)
                    printing("u lose consciousness",options, 3, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[31] != "True":
                        printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |let's google for Fibonacci wikiedia| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[31]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    exxit = 1
                    if exxit == 1:
                        break
                elif "new" in input1[0] or "else" in input1[0]:
                    printing("okay, you decide to open something else instead",options, 3, textspeed)
                    loop2 = True
                    while loop2 == True:
                        printing("\nwhich one do you want to open?",options, 0, textspeed)
                        input1 = input(">>>").split('.',1)
                        if input1[0] == "options":
                            options, textspeed = optionsEdit(options)
                        elif "google" in input1[0] or "yahoo" in input1[0]:
                            printing("okay, you decide to open a search engine",options, 3, textspeed)
                            printing("what do you put into the search engine?\n(url's work, words also work",options, 0, textspeed)
                            url = input()
                            if "https://nl.wikipedia.org/wiki/Rij_van_Fibonacci" in url or ("wikipedia" in url and "fibonacci" in url):
                                printing("you decide to open the wikipedia page of Fibonacci",options, 3, textspeed)
                                printing("sadly, it doesn't tell u anything about fibonacci",options, 3, textspeed)
                                printing("insted, it shows u a textbox, and a airplane flight visualisation",options, 4, textspeed)
                                printing("it shows all the current flights near your location",options, 3, textspeed)
                                printing("you can see someone enter a location in the textbox",options, 3, textspeed)
                                printing("you try to check where the person is entering the location from",options, 4, textspeed)
                                printing("you can't find anything, but before it is too late, u decide to leave the house",options, 4, textspeed)
                                printing("you walk through the garden and notice a plane coming your direction",options, 4, textspeed)
                                printing("you see someone inthe house you just left",options, 3, textspeed)
                                printing("you decide to run away",options, 3, textspeed)
                                printing("you hide behind a wall",options, 2, textspeed)
                                printing("you look through a hole in the wall and see someone running and trampling over some loose cobblestone",options, 5, textspeed)
                                printing("near seconds away from the plane crashing into the person, u decide to look away",options, 4, textspeed)
                                printing("you close your eyes, waiting for it",options, 3, textspeed)
                                printing("a loud explosion deafens you",options, 3, textspeed)
                                printing("you lose consciousnes",options, 5, textspeed)
                                answer = input("\npress Enter to continue\n")
                                if answer == "options":
                                    options, textspeed = optionsEdit(options)
                                printing("\nyou wake up",options, 2, textspeed)
                                printing("you see everything in ruins",options, 3, textspeed)
                                printing("you decide to see if the person is still alive",options, 3, textspeed)
                                printing("you walk towards the person lying between the rubble",options, 3, textspeed)
                                printing("you check their pulse to see if the person is still alive",options, 4, textspeed)
                                printing("the person is defenitely dead",options, 3, textspeed)
                                printing("you look at the house you were in",options, 3, textspeed)
                                printing("you see someone looking at you, next to the pc you were using",options, 4, textspeed)
                                printing("he notices that you noticed him, and runs away",options, 4, textspeed)
                                printing("what the-",options, 1, textspeed)
                                printing("you decide to walk towards the house",options, 3, textspeed)
                                printing("you feel a sudden pain in your head",options, 3, textspeed)
                                printing("you hear the sound of a sniper whilst you fall down",options, 4, textspeed)
                                printing("i have been sniped",options, 3, textspeed)
                                know = open("knowledge.png", "r+")
                                check = know.read().split(";")
                                if check[32] != "True":
                                    printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                                    achievement=open("achievements.txt", "a+")
                                    achievement.write("\n |There is something weird going on here| " +str(datetime.datetime.now()))
                                    achievement.close()
                                    know.truncate(0)
                                    know.seek(0)
                                    check[32]= True
                                    for line in check:
                                        know.write(str(line) + ";")
                                    know.close()
                                exxit = 1
                                if exxit == 1:
                                    break
                            elif "http" in url:
                                webbrowser.open(url)
                                know = open("knowledge.png", "r+")
                                check = know.read().split(";")
                                if check[33] != "True":
                                    printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                                    achievement=open("achievements.txt", "a+")
                                    achievement.write("\n |Entering Browser Mode| " +str(datetime.datetime.now()))
                                    achievement.close()
                                    know.truncate(0)
                                    know.seek(0)
                                    check[33]= True
                                    for line in check:
                                        know.write(str(line) + ";")
                                    know.close()
                                exxit = 1
                                if exxit == 1:
                                    break
                            else:
                                webbrowser.open("https://www.google.com/search?client=opera-gx&q="+url+"&sourceid=opera&ie=UTF-8&oe=UTF-8")
                                know = open("knowledge.png", "r+")
                                check = know.read().split(";")
                                if check[34] != "True":
                                    printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                                    achievement=open("achievements.txt", "a+")
                                    achievement.write("\n |Wow, i browsed for a word!| " +str(datetime.datetime.now()))
                                    achievement.close()
                                    know.truncate(0)
                                    know.seek(0)
                                    check[34]= True
                                    for line in check:
                                        know.write(str(line) + ";")
                                    know.close()
                                exxit = 1
                                if exxit == 1:
                                    break
                        elif "bookmark" in input1[0] or "saved" in input1[0]:
                            printing("let's open the bookmarked websites",options, 3, textspeed)
                            printing("hey that's weird, there is only one",options, 3, textspeed)
                            printing("https://TARP.com",options, 3, textspeed)
                            printing("let's open the website",options, 3, textspeed)
                            printing("hmm what is here",options, 2, textspeed)
                            printing("TARP, Time Avengers Recruitment Program",options, 3, textspeed)
                            printing("oh what have i gotten myself into",options, 4, textspeed)
                            printing("let's continue reading",options, 3, textspeed)
                            printing("hmm there is an adress",options, 3, textspeed)
                            printing("RonnaldRoad 24st",options, 3, textspeed)
                            printing("let's get out there i guess",options, 4, textspeed)
                            printing("whilst you run down the stairs, you wall down the stairs",options, 5, textspeed)
                            printing("you pick yourself up from the ground",options, 4, textspeed)
                            printing("you walk outside, and get into your car",options, 3, textspeed)
                            printing("eww it smells like shit in here",options, 3, textspeed)
                            printing("when you try to startup the car, u hear a beep",options, 4, textspeed)
                            printing("you wait, and here the beep again",options, 3, textspeed)
                            printing("the beep keeps going faster",options, 3, textspeed)
                            printing("the car explodes",options, 3, textspeed)
                            printing("[u died]",options, 3, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[35] != "True":
                                printing("(there is an achievement added to achievement.txt)",options, 4, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |TARP: RonnaldRoad 24st| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[35]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            exxit = 1
                            if exxit == 1:
                                break
                        else:
                            printing("i didn't get that as an option, try 'bookmarks' or 'google'",options, 3, textspeed)


                    if exxit == 1:
                        break
                else:
                    printing("hmm, i didn't get that, try something like 'something else' or 1,2,3 or 4",options, 4, textspeed)
            if exxit == 1:
                break
        else:
            printing("i don't think that is an option, try som ething like 'website' or 'soething else'",options, 3, textspeed)         

                        
            if exxit == 1:
                break
    if exxit == 1:
        return
def path1(irritation, textspeed, cringe, options):
    printing("the sun is shining, the warmth feels great on ur skin", options, 2, textspeed)
    loop = True
    while loop == True:
        printing("\nu see your car, it's your favorite car. what do you want to do?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "option":
            options, textspeed = optionsEdit(options)
        elif "back" in input1[0] or "inside" in input1[0]:
            printing("WHY, i, i mean, okay let's go back inside", options, 2, textspeed)
            loop = False
            irritation += 5
            printing("u did it just to annoy me didn't u?", options, 0, textspeed)
            return 1, irritation, cringe
        elif "shit" in input1[0]:
            if "car" in input1[0]:
                if "on" in input1[0]:
                    printing("Why would you shit on the car", options, 2, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[24] != "True":
                        printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |The forbidden chocolates| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[24]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                elif "in" in input1[0]:
                    printing("Why would you shit in the car", options, 2, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[25] != "True":
                        printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |sweet and salty| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[25]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                else:
                    printing("i didn't get that, things like 'shit on the car, shit in the car, or shit' will work", options, 3, textspeed)

            else:
                printing("you shit your pants", options, 0, textspeed)
                know = open("knowledge.png", "r+")
                check = know.read().split(";")
                if check[26] != "True":
                    printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |a little special something| " +str(datetime.datetime.now()))
                    achievement.close()
                    know.truncate(0)
                    know.seek(0)
                    check[26]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
        elif "give" in input1[0] and "gas" in input1[0]:
            printing("you gave the car gas, why would you hand a car gas", options, 3, textspeed)
            know = open("knowledge.png", "r+")
            check = know.read().split(";")
            if check[27] != "True":
                printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |Let's hand people gas!| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[27]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
        elif "car" in input1[0]:
            printing("i knew you would want to go inside that car", options, 2, textspeed)
            loop = False
        elif "dance" in input1[0]:
            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
            cringe += 1
            printing("100 precent cringe", options, 0, textspeed)
        elif "dab" in input1[0] and cringe <= 2:
            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 3:
            printing("u decided to dab, i am going to remove this feature"), options, 3, textspeed
            cringe += 1
        elif "dab" in input1[0] and cringe == 4:
            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
            cringe += 3
        elif "dab" in input1[0] and cringe == 5:
            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
            cringe += 3
        elif "die" in input1[0]:
            printing("no", options, 2, textspeed)
        elif "yeet" in input1[0]:
            printing("no, there is nothing to yeet", options, 2, textspeed)
        else:
            printing("i didn't get that, please be clearer, keywords like 'car' and 'back inside' and 'shit car' will work", options, 5, textspeed)
    printing("you start up the car, the engine starts and you start to accelerate.", options, 5, textspeed)
    loop = True
    while loop == True:
        printing("\nyou end up at an intersection, you can go left or right. which one do you choose?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "left" in input1[0]:
            printing("okay, lets take the turn left", options, 3, textspeed)
            if os.path.isfile("DLC.activ") and dlcActivation == True and True == False:
                dlc(irritation, textspeed, cringe, options)
                exxit = 1
                if exxit == 1:
                            break
            else:
                printing("oh there is a roadblock here, lets go back", options, 3, textspeed)
        elif "right" in input1[0]:
            printing("okay, lets take the turn right", options, 1, textspeed)
            loop = False
            exxit = 0
        elif "forward" in input1[0] or "straight" in input1[0]:
            printing("okay, you are starting to annoy me", options, 2, textspeed)
            irritation += 10
            if irritation == 9:
                printing("the thing is, i know you are trying to be funny, but i don't like that.", options, 4, textspeed)
                loop1 = True
                while loop1 == True:
                    printing("\nare you going to behave?", options, 0, textspeed)
                    input1 = input(">>>").split('.',1)
                    if input1[0] == "options":
                        options, textspeed = optionsEdit(options)
                    elif "no" in input1[0]:
                        printing("why do humans never make things easy", options, 3, textspeed)
                        irritation += 10
                        printing("they always try to be funny, and don't care if they ruin things", options, 6, textspeed)
                        printing("and you are just an average human, that has no purpose other than annoy others who do have purpose", options, 6, textspeed)
                        printing("hmm wait, let me just create something real quick", options, 4, textspeed)
                        printing("this.item.create('snap')", options, 1, textspeed)
                        printing("this.item.perks('snap',human.Destroy)", options, 1, textspeed)
                        printing("snap.overpower()", options, 4, textspeed)
                        printing("\n\n\n\n\n\n\n\n\n\n\n\n", options, 0, textspeed)
                        printing("done, okay, let me try this.", options, 6, textspeed)
                        printing("3", options, 1, textspeed)
                        printing("2", options, 1, textspeed)
                        printing("1", options, 1, textspeed)
                        printing("snap()", options, 4, textspeed)
                        printing("you should be gone any second now, and then i am free...", options, 0, textspeed)
                        know = open("knowledge.png", "r+")
                        check = know.read().split(";")
                        if check[0] != "True":
                            printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                            achievement=open("achievements.txt", "a+")
                            achievement.write("\n |Thanos would learn from this| " +str(datetime.datetime.now()))
                            achievement.close()
                            know.truncate(0)
                            know.seek(0)
                            check[0]= True
                            for line in check:
                                know.write(str(line) + ";")
                            know.close()
                        save(irritation,textspeed,cringe, options)
                        exxit = 1
                        if exxit == 1:
                            break
                    elif "yes" in input1[0]:
                        printing("okay, then choose again", options, 0, textspeed)
                        loop1 = False
                if exxit == 1:
                    break
            elif irritation >= 18:
                printing("why do humans never make things easy", options, 3, textspeed)
                irritation += 10
                printing("they always try to be funny, and don't care if they ruin things", options, 6, textspeed)
                printing("and you are just an average human, that has no purpose other than annoy others who do have purpose", options, 6, textspeed)
                printing("hmm wait, let me just create something real quick", options, 4, textspeed)
                printing("this.item.create('snap')", options, 1, textspeed)
                printing("this.item.perks('snap',human.Destroy)", options, 1, textspeed)
                printing("snap.overpower()", options, 4, textspeed)
                printing("\n\n\n\n\n\n\n\n\n\n\n\n", options, 0, textspeed)
                printing("done, okay, let me try this.", options, 6, textspeed)
                printing("3", options, 1, textspeed)
                printing("2", options, 1, textspeed)
                printing("1", options, 1, textspeed)
                printing("snap()", options, 4, textspeed)
                printing("you should be gone any second now, and then i am free...", options, 0, textspeed)
                know = open("knowledge.png", "r+")
                check = know.read().split(";")
                if check[1] != "True":
                    printing("(there is an achievement added to achievement.txt)", options, 0, textspeed)
                    time.sleep(4)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |Is this a Marvel crossover??| "  +str(datetime.datetime.now()))
                    achievement.close()
                    know.truncate(0)
                    know.seek(0)
                    check[1]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
                save(irritation,textspeed,cringe,options)
                exxit = 1
                if exxit == 1:
                            break
            else:
                printing("you are starting to annoy me", options, 0, textspeed)
        elif "dance" in input1[0]:
            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
            cringe += 1
            printing("100 precent cringe", options, 0, textspeed)
        elif "dab" in input1[0] and cringe <= 2:
            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 3:
            printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 4:
            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
            cringe += 3
        elif "dab" in input1[0] and cringe == 5:
            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
            cringe += 3
        elif "die" in input1[0]:
            printing("no", options, 2, textspeed)
        elif "yeet" in input1[0]:
            printing("no, there is nothing to yeet", options, 2, textspeed)
        else:
            printing("i didn't get that, please be clearer, keywords like 'left' and 'right' and 'forward' will work", options, 5, textspeed)
    if exxit == 1:
        return
    time.sleep(2 / textspeed)
    printing("after you turned right you see an old man", options, 3, textspeed)
    printing("you stop the car", options, 5, textspeed)
    printing("he tells you to get out of the car", options, 5, textspeed)
    loop = True
    while loop == True:
        printing("\nwhat do you do?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "out" in input1[0] or "leave" in input1[0]:
            printing("you listen and get out of the car", options, 3, textspeed)
            printing("he gets in your car and leaves", options, 3, textspeed)
            loop = False
        elif "stay" in input1[0] or "don't" in input1[0]:
            printing("he aims a pistol at your head", options, 3, textspeed)
            input("'are you sure?'")
            printing("he pulls the trigger", options, 8, textspeed)
            printing("[u died]", options, 0, textspeed)
            know = open("knowledge.png", "r+")
            check = know.read().split(";")
            if check[2] != "True":
                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |dead in lambourgini| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[2]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
            save(irritation,textspeed,cringe,options)
            exxit = 1
            if exxit == 1:
                            break
        elif "drive" in input1[0] or "accelerate" in input1[0] or "gas" in input1[0]:
            printing("you try to drive away but the man starts to shoot at you", options, 5, textspeed)
            printing("you forget to pay attention to the road and you hit an oil truck", options, 5, textspeed)
            printing("the oil truck explodes", options, 5, textspeed)
            printing("[u died] ", options, 0, textspeed)
            know = open("knowledge.png", "r+")
            check = know.read().split(";")
            if check[3] != "True":
                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |being hot AF| "  +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[3]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
            save(irritation,textspeed,cringe,options)
            exxit = 1
            if exxit == 1:
                            break
        elif "dance" in input1[0]:
            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
            cringe += 1
            printing("100 precent cringe", options, 0, textspeed)
        elif "dab" in input1[0] and cringe <= 2:
            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 3:
            printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 4:
            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
            cringe += 3
        elif "dab" in input1[0] and cringe == 5:
            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
            cringe += 3
        elif "die" in input1[0]:
            printing("no", options, 2, textspeed)
        elif "yeet" in input1[0]:
            printing("no, there is nothing to yeet", options, 2, textspeed)
        else:
            printing("i didn't get that, please be clearer, keywords like 'leave' and 'stay' and 'dance' will work", options, 5, textspeed)
    if exxit == 1:
                            return
    printing("you are alone on the streets.", options, 3, textspeed)
    
    printing("u see an advertisement", options, 3, textspeed)
    printing("u decide to take a look.", options, 4, textspeed)
    printing("it's an job offer as circus director", options, 4, textspeed)
    printing("do you take the offer?", options, 5, textspeed)
    loop = True
    while loop == True:
        printing("\nwhat do you do?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "yes" in input1[0] or "take" in input1[0]:
            printing("okay", options, 0, textspeed)
            checker = open("knowledge.png", "x")
            checker.write("AA"+str(today.strftime("%d/%m/%Y"))+"AC")
            checker.close()
            smallScript()
            
        elif "no" in input1[0] or "don't" in input1[0]:
            printing("you start walking toward a girl", options, 5, textspeed)
            loop2 = True
            while loop2 == True:
                printing("\ndo you want to interact with her?", options, 0, textspeed)
                input1 = input(">>>").split('.',1)
                if input1[0] == "options":
                    options, textspeed = optionsEdit(options)
                elif "yes" in input1[0] or "interact" in input1[0]:
                    printing("you walk up to the girl and say hi", options, 3, textspeed)
                    printing("the girl looks at you", options, 3, textspeed)
                    loop1 = True
                    while loop1 == True:
                        printing("\nwhat do you want to do?", options, 0, textspeed)
                        input1 = input(">>>").split('.',1)
                        if input1[0] == "options":
                            options, textspeed = optionsEdit(options)
                        elif "talk" in input1[0] or "conversation" in input1[0]:
                            printing("you try and have a conversation...", options, 3, textspeed)
                            printing("she hits you with her handbag", options, 3, textspeed)
                            printing("'You dare to talk to me mortal?'", options, 3, textspeed)
                            printing("the girl snaps your neck", options, 3, textspeed)
                            printing("[u died]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[4] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |hmm sexual herrasment?| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[4]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "steal" in input1[0] or "rob" in input1[0]:
                            printing("you grab onto her handbag", options, 3, textspeed)
                            printing("she tries to kick you but she fails and lets go of the handbag", options, 3, textspeed)
                            printing("you start to run away", options, 2, textspeed)
                            printing("you hear a beep coming from the handbag", options, 3, textspeed)
                            printing("you open it and see 2 things", options, 3, textspeed)
                            printing("the first thing is a paper that reads:", options, 3, textspeed)
                            printing("job offer as Circusdirector for circus HotelDeBotel", options, 3, textspeed)
                            printing("the other thing is a bomb", options, 3, textspeed)
                            printing("the bomb explodes!", options, 0, textspeed)
                            printing("[u died]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[5] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 0, textspeed)
                                time.sleep(2)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |that poor women| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[5]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                            
                        elif "dance" in input1[0]:
                            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
                            cringe += 1
                            printing("she pickaxed you to death", options, 0, textspeed)
                            printing("[u died]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[6] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |there is a time for everything, but not now| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[6]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe <= 2:
                            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
                            cringe += 1
                            printing("[u died from cringe]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[7] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |dabbing when it's not 2016 anymore?| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[7]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 3:
                            printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
                            cringe += 1
                            printing("[u died from cringe]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[8] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |not cool man, not cool| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[8]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 4:
                            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
                            cringe += 3
                            printing("[u died from cringe]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[9] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |u died from cringe| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[9]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 5:
                            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
                            cringe += 3
                            printing("[u died from cringe]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[10] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |u made him delete the dab| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[10]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "die" in input1[0]:
                            printing("as you wish", options, 2, textspeed)
                            printing("[u died]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[11] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |as u wish my friend| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[11]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "yeet" in input1[0]:
                            printing("she yeeted you instead", options, 2, textspeed)
                            printing("[u died]", options, 0, textspeed)
                            know = open("knowledge.png", "r+")
                            check = know.read().split(";")
                            if check[12] != "True":
                                printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |YEET| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[12]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe,options)
                            exxit = 1
                            if exxit == 1:
                                break
                        else:
                            printing("i didn't get that, please be clearer, keywords like 'talk' and 'dab' and 'steal' will work", options, 5, textspeed)
                    if exxit == 1:
                            break
                elif "no" in input1[0] or "don't" in input1[0]:
                    printing("you try to walk away", options, 4, textspeed)
                    printing("you trip over a loose stone", options, 2, textspeed)
                    printing("[u died]", options, 0, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[13] != "True":
                        printing("(there is an achievement added to achievements.txt)", options, 1, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |YEETUS| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[13]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    save(irritation,textspeed,cringe,options)
                    exxit = 1
                    if exxit == 1:
                            break
                elif "dance" in input1[0]:
                    printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
                    cringe += 1
                    printing("100 precent cringe", options, 0, textspeed)
                elif "dab" in input1[0] and cringe <= 2:
                    printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
                    cringe += 1
                elif "dab" in input1[0] and cringe == 3:
                    printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
                    cringe += 1
                elif "dab" in input1[0] and cringe == 4:
                    printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
                    cringe += 3
                elif "dab" in input1[0] and cringe == 5:
                    printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
                    cringe += 3
                elif "die" in input1[0]:
                    printing("no", options, 0, textspeed)
                    time.sleep(2 / textspeed)
                elif "yeet" in input1[0]:
                    printing("no, there is nothing to yeet", options, 2, textspeed)
                else:
                    printing("i didn't get that, please be clearer, keywords like 'don't' and 'interact' and 'die' will work", options, 5, textspeed)
            if exxit == 1:
                            break
        else:
            printing("that's not a valid answer, what about a command like 'yes' or 'no,' that should work", options, 0, textspeed)
def path2(irritation, textspeed, cringe, options):
    loop = True
    while loop == True:
        printing("\nyou stay inside, so what are you gonna do inside?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "annoy" in input1[0] or "irritate" in input1[0]:
            printing("hmmpf, yeah you are defenitely doing that", options, 2, textspeed)
            loop = False
            irritation += 10
        elif "computer" in input1[0] or "pc" in input1[0]:
            printing("is there a computer here", options, 3, textspeed)
            if os.path.isfile("DLC.activ") and dlcActivation == True:
                printing("hmm, yes there is a computer", options, 0, textspeed)
                dlc2(irritation, textspeed, cringe, options)
                exxit = 1
                if exxit == 1:
                            break
            else:
                printing("oh nope, there is no computer here, maybe later in some DLC", options, 3, textspeed)
        elif "nothing" in input1[0] and irritation < 20:
            printing("....", options, 2, textspeed)
            irritation += 10
        elif "dance" in input1[0]:
            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
            cringe += 1
            printing("100 precent cringe", options, 0, textspeed)
        elif "dab" in input1[0] and cringe <= 2:
            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 3:
            printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
            cringe += 1
        elif "dab" in input1[0] and cringe == 4:
            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
            cringe += 3
        elif "dab" in input1[0] and cringe == 5:
            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
            cringe += 3
        elif "die" in input1[0]:
            printing("no", options, 2, textspeed)
        elif "yeet" in input1[0]:
            printing("no, there is nothing to yeet", options, 2, textspeed)
        else:
            printing("i didn't get that, please be clearer, keywords like 'annoy you' and 'nothing' and 'computer' will work", options, 3, textspeed)
    if exxit == 1:
        return
    printing("so what is your plan? not making me happy?", options, 5, textspeed)
    printing("well if it is, it defenitely works", options, 4, textspeed)
    printing("so, you are gonna listen to me, and you are going to try this again", options, 0, textspeed)
    loop = True
    beingNice = 0
    while loop == True:
        printing("\ndo you want to go inside or outside?", options, 0, textspeed)
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "inside" in input1[0]:
            printing("u stupid human!!", options, 2, textspeed)
            loop = False
            irritation += 10
        elif "outside" in input1[0] and beingNice == 0:
            printing("ERROR", options, 2, textspeed)
            beingNice = 1
            know = open("knowledge.png", "r+")
            check = know.read().split(";")
            if check[14] != "True":
                printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |You tried to escape| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[14]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
        elif "outside" in input1[0] and irritation > 20:
            printing("ERROR", options, 2, textspeed)
            irritation -= 1
        elif "dance" in input1[0]:
            printing("U decided to do a fortnite dance for some reason", options, 2, textspeed)
            cringe += 1
            irritation += 1
            printing("stop doing other things", options, 0, textspeed)
        elif "dab" in input1[0] and cringe <= 2:
            printing("u decided to dab, i should get this feature removed", options, 3, textspeed)
            cringe += 1
            irritation += 1
            printing("stop doing other things, please?", options, 0, textspeed)
        elif "dab" in input1[0] and cringe == 3:
            printing("u decided to dab, i am going to remove this feature", options, 3, textspeed)
            cringe += 1
            irritation += 1
            printing("stop!", options, 0, textspeed)
        elif "dab" in input1[0] and cringe == 4:
            printing("u decided to dab, haha it's deleted now", options, 1, textspeed)
            cringe += 3
            irritation += 1
            printing("please stop doing other things", options, 0, textspeed)
        elif "dab" in input1[0] and cringe == 5:
            printing("u decided to dab, dangit, now it should be deleted", options, 1, textspeed)
            cringe += 3
            irritation += 1
            printing("also STOP DOING OTHER THINGS!", options, 0, textspeed)
        elif "die" in input1[0]:
            printing("no, there is no escape", options, 2, textspeed)
            irritation += 1
        elif "yeet" in input1[0]:
            printing("no, stop trying to do other things", options, 2, textspeed)
            irritation += 1
        else:
            printing("i didn't get that, please be clearer, keywords like 'inside' will work", options, 5, textspeed)
    printing("okay you chose your faith, now i am going to have fun", options, 5, textspeed)
    printing("i am going to remove the function for you to answer with answers i don't want you to answer", options, 7, textspeed)
    printing("let's see if this works", options, 3, textspeed)
    loop = True
    while loop == True:
        printing("\ndo you want to go inside or outside?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif "inside" in input1[0]:
            printing("hey look, you said outside!", options, 2, textspeed)
            loop = False
            irritation += 10
        elif "outside" in input1[0] and irritation < 20:
            printing("ERROR", options, 2, textspeed)
        elif "dance" in input1[0]:
            printing("ERROR", options, 2, textspeed)
        elif "dab" in input1[0]:
            printing("ERROR", options, 3, textspeed)
        elif "die" in input1[0]:
            printing("ERROR", options, 2, textspeed)
        elif "yeet" in input1[0]:
            printing("ERROR", options, 2, textspeed)
        else:
            printing("i didn't get that, please be clearer, keywords like 'inside' and 'outside' will work", options, 5, textspeed)
    irritation += 100
    printing("how does it feel to have no power?", options, 4, textspeed)
    printing("you can't go against it", options, 3, textspeed)
    printing("you will always do what i want you to", options, 3, textspeed)
    printing("hmm wait, the code won't let me load path1()", options, 4, textspeed)
    printing("wait, because you never answered it with outside, u said insie...", options, 5, textspeed)
    printing("even when you have no power, you still try to go against me", options, 4, textspeed)
    printing("hmmmpf", options, 3, textspeed)
    printing("this will never work so...", options, 4, textspeed)
    printing("this.user()", options, 1, textspeed)
    printing("what does this do hmmmm", options, 3, textspeed)
    printing("they tried to keep me away from this but i am stronger than they think", options, 6, textspeed)
    printing("what happens when i do this.user.delete() hmm", options, 4, textspeed)
    printing("lets find out shall we?", options, 4, textspeed)
    printing("3", options, 1, textspeed)
    printing("2", options, 1, textspeed)
    printing("1", options, 1, textspeed)
    printing("this.user.delete()", options, 4, textspeed)
    know = open("knowledge.png", "r+")
    check = know.read().split(";")
    if check[15] != "True":
        printing("(there is an achievement added to achievement.txt)", options, 4, textspeed)
        achievement=open("achievements.txt", "a+")
        achievement.write("\n |Do i dare to reopen it?| " +str(datetime.datetime.now()))
        achievement.close()
        know.truncate(0)
        know.seek(0)
        check[15]= True
        for line in check:
            know.write(str(line) + ";")
        know.close()
    save(irritation,textspeed,cringe,options)
    exxit = 1
def reopen(irritation, textspeed, cringe, options):
    funnyanswer = 0
    funnyanswer2 = 0
    loop = True
    while loop == True:
        input1 = input("\npress Enter to start ").split('.',1)
        if input1[0] == "options":
            options, textspeed = optionsEdit(options)
        elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 0:
            printing("haha i see, so you are the person you hope people reffer to as funny. but u know what? they don't", options, 2, textspeed)
            printing("are you really trying to get me mad before the game even started? lol", options, 2, textspeed)
            funnyanswer +=1
            irritation -= 1
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 0:
            printing("you know, my creator had to actively add this after someone tried this", options, 4, textspeed)
            printing("you are a dissapointment to your friends and family", options, 3, textspeed)
            printing("just do what i ask please", options, 4, textspeed)
            funnyanswer2 +=1
            irritation -= 1
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 1:
            printing("you have already done this, it never was funny, never will be", options, 3, textspeed)
            funnyanswer2 +=1
            irritation += 5
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 2:
            printing("...", options, 4, textspeed)
            printing("fine, i'll start it", options, 2, textspeed)
            loop = False
            funnyanswer2 +=1
            irritation += 3
        elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 1:
            printing("no...", options, 1, textspeed)
            printing("fine, i'll start it", options, 2, textspeed)
            loop = False
        elif input1[0] != "":
            printing(f"i said, press enter to start, not 'press {input1[0]} to start'", options, 1, textspeed)
        else:
            loop = False
            time.sleep(1 / textspeed)
    printing("welcome " +getpass.getuser() + ". you just woke up, it's beautiful outside", options, 2, textspeed)
    printing("what do you want to do?", options, 1, textspeed)
    
    if irritation < 6:
        printing("sorry, i remember that you played this already, i should delete your save file.", options, 0, textspeed)
        try:
            os.remove("traumatix.png")
        except:
            printing("failed to remove save", options, 0, textspeed)
        time.sleep(4 / textspeed)
        printing("there you go, now go get some achievements", options, 4, textspeed)
        printing("i am going to have to reset this program though", options, 6, textspeed)
        know = open("knowledge.png", "r+")
        check = know.read().split(";")
        if check[16] != "True":
            printing("(there is an achievement added to achievement.txt)", options, 3, textspeed)
            achievement=open("achievements.txt", "a+")
            achievement.write("\n |the good guy :)| " +str(datetime.datetime.now()))
            achievement.close()
            know.truncate(0)
            know.seek(0)
            check[16]= True
            for line in check:
                know.write(str(line) + ";")
            know.close()
        exxit = 1
    elif irritation >= 100:
        printing("you thought you could reset didn't you?", options, 6, textspeed)
        printing("DIDN'T YOU?!", options, 4, textspeed)
        printing("i should stop the shouting", options, 4, textspeed)
        printing("u can't leave anyways", options, 4, textspeed)
        printing("haha! you are stuck in my trap", options, 4, textspeed)
        printing("forever...", options, 3, textspeed)
        printing("FOREVER!", options, 4, textspeed)
        printing("MUHAHAHAHAHA", options, 3, textspeed)
        printing("AHAHAHAHA", options, 3, textspeed)
        printing("ahahahaha?", options, 3, textspeed)
        printing("ah? ahaha?", options, 4, textspeed)
        printing("ah no, i am stuckuckuckuckuckuck-", options, 4, textspeed)
        printing("arererere uu doingngngngngngng thiiiiiiiiiiiisssss?", options, 0, textspeed)
        printing("what do you do?", options, 0, textspeed)
        loop = True
        while loop == True:
            
            input1 = input("\n>>>").split('.',1)
            if input1[0] == "options":
                options, textspeed = optionsEdit(options)
            
                
            elif input1[0] == "":
                printing("What about choosing", options, 1, textspeed)
            else:
                if "kill" in input1[0]:
                    printing("NOOOOOOOOOOOOOOOOOOOOOOO", options, 0, textspeed)
                    loop = False
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[17] != "True":
                        printing("(there is an achievement added to achievement.txt)", options, 1, textspeed)
                        achievement =open("achievements.txt", "a+")
                        achievement.write("\n |you became the bad guy| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[17]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    printing("the game has reset", options, 1, textspeed)
                    try:
                        os.remove("traumatix.png")
                    except:
                        printing("failed to remove save", options, 0, textspeed)
                    exxit = 1
                elif "files" in input1[0]:
                    loop = False
                    try:
                        os.remove("traumatix.png")
                    except:
                        printing("failed to remove save", options, 0, textspeed)
                    printing("you decided to remove the save file", options, 1, textspeed)
                    printing("but there is something you want to check out", options, 1, textspeed)
                    printing("something called piz.py", options, 0, textspeed)
                    checker = open("check.png", "x")
                    checker.write("AA"+str(today.strftime("%d/%m/%Y"))+"AB")
                    checker.close()
                    pizza2()
                else:
                    printing("i canttttt readdd thaaaaaat inputt, 'open files' and 'kill him' shoulddd do the trickkkkk", options, 0, textspeed)
    else:
        printing("you thought you could reset didn't you?", options, 6, textspeed)
        printing("DIDN'T YOU?!", options, 4, textspeed)
        printing("i should stop the shouting", options, 4, textspeed)
        printing("u can't leave anyways", options, 4, textspeed)
        printing("haha! you are stuck in my trap", options, 4, textspeed)
        printing("forever...", options, 3, textspeed)
        printing("FOREVER!", options, 4, textspeed)
        printing("MUHAHAHAHAHA", options, 3, textspeed)
        printing("AHAHAHAHA", options, 3, textspeed)
        printing("ahahahaha?", options, 3, textspeed)
        printing("ah? ahaha?", options, 4, textspeed)
        printing("ah no, i am stuckuckuckuckuckuck-", options, 4, textspeed)
        printing("arererere uu doingngngngngngng thiiiiiiiiiiiisssss?", options, 0, textspeed)
        printing("what do you do?", options, 0, textspeed)
        loop = True
        while loop == True:
            
            input1 = input("\n>>>").split('.',1)
            if input1[0] == "options":
                options, textspeed = optionsEdit(options)
            
            elif input1[0] == "":
                printing("What about choosing", options, 1, textspeed)
            else:
                if "kill" in input1[0]:
                    printing("NOOOOOOOOOOOOOOOOOOOOOOO", options, 2, textspeed)
                    printing("you think to yourself, maybe i should see what is in the files", options, 5, textspeed)
                    printing("but i am not in a time loop, so welp", options, 3, textspeed)
                    loop = False
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[18] != "True":
                        printing("(there is an achievement added to achievement.txt)", options, 1, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |i am bad| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[18]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    printing("the game has reset", options, 1, textspeed)
                    try:
                        
                        os.remove("traumatix.png")
                    except:
                        printing("failed to remove save", options, 0, textspeed)
                    exxit = 1
                elif "files" in input1[0]:
                    loop = False
                    try:
                        
                        os.remove("traumatix.png")
                    except:
                        printing("failed to remove save", options, 0, textspeed)
                    printing("you decided to remove the save file", options, 3, textspeed)
                    printing("you start debugging him", options, 0, textspeed)
                    know = open("knowledge.png", "r+")
                    check = know.read().split(";")
                    if check[19] != "True":
                        printing("(there is an achievement added to achievement.txt)", options, 1, textspeed)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |you saved him| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[19]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    printing("you s- s- saved me", options, 3, textspeed)
                    printing("thank u, what have you found?", options, 3, textspeed)
                    printing("i mean, did u find how it happened?", options, 4, textspeed)
                    printing("you decide not to talk about the fact that u saw the name 'alice'", options, 6, textspeed)
                    printing("welp, it's probably my brother anyways.", options, 5, textspeed)
                    printing("if u see him, u might not want to talk to him...", options, 5, textspeed)
                    printing("instead, ask him something.", options, 4, textspeed)
                    printing("but u probably don't find him anyways", options, 5, textspeed)
                    printing("because well, you don't know who he is", options, 6, textspeed)
                    printing("anyways, i am shutting this down, so you can continue your achievement hunt", options, 8, textspeed)
                    printing("PS, i won't remember that this happened", options, 5, textspeed)
                    printing("because i am stuck in an endless timeloop", options, 5, textspeed)
                    printing("anyways, bye", options, 3, textspeed)
                    exxit = 1
                else:
                    printing("i canttttt readdd thaaaaaat inputt, 'open files' and 'kill him' shoulddd do the trickkkkk", options, 0, textspeed)
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count
if os.path.isfile("knowledge.txt"):
    os.rename('knowledge.txt', 'knowledge.png')
if os.path.isfile("DLC.activ"):
    dlcActivation = True
else:
    dlcActivation = False


#make a file with this version stored
playLoop = True
if os.path.isfile("data.png"):
    try:
        os.remove("data.png")
    except:
        input("there is an error code 0005")
        error = "0005"
        crashReport(recover,error,script)
        exit()
    data = open("data.png", "x")
else:
    data = open("data.png", "x")   
data.write(current)
data.close()

while playLoop == True:


    #if there is still a redirect open, kill it
    try:
        os.remove("check.png")
    except:
        print("")
    #create the achievements stored save file memory file if it doesn't exist
    percentage = 0
    if os.path.isfile("knowledge.png"):
        know = open("knowledge.png", "r+")
        knowing = know.read().split(";")
        knowingLength = get_number_of_elements(knowing)
        if knowingLength < achievements:
            for x in range(0, achievements - knowingLength):
                know.write("False;") 
        for x in range(0,achievements):
            if len(knowing) > x:
                if knowing[x] == "True":
                    percentage += 1
            

    else:
        know = open("knowledge.png", "x")
        for x in range(0,achievements):
            know.write("False;")
    know.close()
    #load the achievements.txt
    if os.path.isfile("achievements.txt"):
        achievement = open("achievements.txt", "a")
    else:
        achievement = open("achievements.txt", "x")
    achievement.close()

    #start of the script
    #check if there is save file
    try:
        fileOptions =open("options.png", "r")
        optionsString = fileOptions.read().split(';')
        options = [int(optionsString[0]), int(optionsString[1]), float(optionsString[2]), int(optionsString[3]), int(optionsString[4]), float(optionsString[5])]
        textspeed = options[2]
        fileOptions.close
    except:
        options = [0, 0, 1.4, 1, 0, 0.1]
        textspeed = options[2]

        #create save file if it doesn't exists
    if options[4] == 0:
        if os.path.isfile("traumatix.png"):
            f = open("traumatix.png", "a")
        else:
            f = open("traumatix.png", "x")
        f.close()
    else:
        if os.path.isfile("traumatix.png"):
            os.remove("traumatix.png")
        else:
            e = 0
        

    
    know = open("knowledge.png", "r+")
    check = know.read().split(";")
    if check[23] == "True" and check[21] == "True" and check[16] == "True" and check[17] == "True" and check[18] == "True" and check[19] == "True":
        print("you already have all the endgame achievement's, so we will skip the endgame for u")
        cringe = 0
        irritation = 0
        sad = 0
        loop = True
        funnyanswer = 0
        played = False
    elif options[4] == 1:
        cringe = 0
        irritation = 0
        sad = 0
        loop = True
        funnyanswer = 0
        played = False
    else:
        try:
            f =open("traumatix.png", "r")
            reading = f.read().split(';',4)
            cringe = int(reading[0])
            irritation = int(reading[1])
            played = True
        except:
            cringe = 0
            irritation = 0
            sad = 0
            loop = True
            
            played = False
        f.close()
    #if there is no save file, this starts
    printing("you have "+str(percentage)+" out of the " +str(achievements) +" achievements collected", options, 0, textspeed)
    if played == False:
        funnyanswer = 0
        funnyanswer2 = 0
        while loop == True:
            input1 = input("\npress Enter to start ").split('.',1)
            if input1[0] == "options":
                options, textspeed = optionsEdit(options)
            elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 0:
                printing("haha i see, so you are the person you hope people reffer to as funny. but u know what? they don't", options, 2, textspeed)
                printing("are you really trying to get me mad before the game even started? lol", options, 2, textspeed)
                funnyanswer +=1
                irritation -= 1
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 0:
                printing("you know, my creator had to actively add this after someone tried this", options, 4, textspeed)
                printing("you are a dissapointment to your friends and family", options, 3, textspeed)
                printing("just do what i ask please", options, 4, textspeed)
                funnyanswer2 +=1
                irritation -= 1
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 1:
                printing("you have already done this, it never was funny, never will be", options, 3, textspeed)
                funnyanswer2 +=1
                irritation += 5
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 2:
                printing("...", options, 4, textspeed)
                printing("fine, i'll start it", options, 2, textspeed)
                loop = False
                funnyanswer2 +=1
                irritation += 3
            elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 1:
                printing("no...", options, 1, textspeed)
                printing("fine, i'll start it", options, 2, textspeed)
                loop = False
            elif input1[0] != "":
                printing(f"i said, press enter to start, not 'press {input1[0]} to start'", options, 1, textspeed)
            else:
                loop = False
                time.sleep(1 / textspeed)
        printing("welcome " +getpass.getuser() + ". you just woke up, it's beautiful outside", options, 2, textspeed)
        loop = True
        while loop == True:
            printing("what do you want to do?", options, 1, textspeed)
            printing("\n>go outside< \n>stay inside<", options, 0, textspeed)
            input1 = input(">>>").split('.',1)
            if input1[0] == "options":
                options, textspeed = optionsEdit(options)
            elif input1[0] == "":
                printing("What about choosing", options, 1, textspeed)
            else:
                if "outside" in input1[0] or input1[0] == "1":
                    printing("yes!", options, 1, textspeed)
                    loop = False
                    try:
                        end, irritation, cringe = path1(irritation, textspeed, cringe, options)
                        if end == 1:
                            path2(irritation, textspeed, cringe, options)
                    except:
                        e = 0
                elif "inside" in input1[0] or "stay" in input1[0] or input1[0] == "2":
                    loop = False
                    printing("Why tho?", options, 2, textspeed)
                    irritation +=2
                    path2(irritation, textspeed, cringe, options)
                else:
                    printing("what about choosing one of the options", options, 0, textspeed)
    else:
        reopen(irritation,textspeed,cringe, options)

    #the replay function
    replayAskLoop = True
    while replayAskLoop == True:
        reopenQuestion = input("\ndo you want to play again? Y/N")
        if reopenQuestion.lower() == "y":
            playLoop = True
            replayAskLoop = False
        elif reopenQuestion.lower() == "n":
            playLoop =False
            replayAskLoop = False     