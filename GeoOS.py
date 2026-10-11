import os, sys, subprocess, random, time

print(rf'''Welcome to
    ______          ____  ____
   / ____/__  ____ / __ \/ __/
  / / __/ _ \/ __ \ / / /\_ \ 
 / /_/ /  __/ /_/ //_/ /__/ /
/_____/\___/\____/____/____/

where all imagination comes to
 _     _  __
| |   (_)/ _|
| |    _| |_ ___
| |   | |   / _ \
| |___| | ||  __/  _
|_____|_|_| \___/ (_)
''')

Logo = "\n\
▣"

GDOSCodes = {

    22: "GDOS Code 22: Done Resetting",
    23: "GDOS Code 23: Done Setting",
    24: "GDOS Code 24: Done Adjusting",

    1: "GDOS Code 1: Command Too Short",
    2: "GDOS Code 2: Command Too Long",
    3: "GDOS Code 3: Command WAY Too Long",
    4: "GDOS Code 4: Unknown Command",
    5: "GDOS Code 5: Unknown Error",
    6: "GDOS Code 6: Crashed From Unknown Cause",

    7: "GDOS Code 7: Test Code",

    8: "GDOS Code 8: Math Too Long",
    9: "GDOS Code 9: Invalid Math Character",
    10: "GDOS Code 10: Number Overflowed Out Of Bounds",
    11: "GDOS Code 11: Number Underflowed Out Of Bounds",
    12: "GDOS Code 12: Tried to divide by 0",
    13: "GDOS Code 13: Number Passed 10⁴³⁰⁰",

    14: "GDOS Code 14: Tried deleting GDOS from GDOS",
    15: "GDOS Code 15: Tried creating file that already exists.",
    16: "GDOS Code 16: Tried Editing GDOS",
    17: "GDOS Code 17: Tried Creating, Editing or Deleting a System File",

    18: "GDOS Code 18: Directory Not Found",
    19: "GDOS Code 19: Not a directory",
    20: "GDOS Code 20: Permission denied",

    25: "GDOS Code 25: Invalid Value Inputed For Setting a Setting",

    21: "GDOS Code 21: Invalid Response",

    22: "GDOS Code 22: Broken Code",

}

Settings = {
    1: "test"
}

DisplaySetting = {
    1: "Test"
}

NotAllowedAddEditOrDeletion = {
    1: "sys",
    2: "ini",
    3: "con",
    4: "dll",
    5: "exe",
    6: "conf",

    7: "service",
    8: "so",
    9: "ko",
}

Ratt = 1
Patt = 1
Satt = 1

LogoCommand = '"Logo": Shows the Logo of GDOS.'
ExitCommand = '"Exit": Exits the GDOS.'
HelpCommand = '"Help": Shows all commands of the GDOS.'
SayCommand = '"Say": Says the input.'
MathCommand = '"Math": Calculates the input.'
AddfCommand = '"AddF": Creates an empty file of any extention and name.'
EditfCommand = '"EditF": Edits a file of choice, as so long as its in the same folder.'
DeletefCommand = '"DeleteF": Deletes a file of choice,  as so long as its in the same folder.'
ChangeDirCommand = '"ChangeDir": Changes Directory'
RPSCommand = '"RPS / Rock Paper Scissors": Plays Rock Paper Scissors with a Bot'
RandomCommand = '"Random": Asks a MIN & MAX for a random number'

Commands = [AddfCommand, EditfCommand, DeletefCommand, ChangeDirCommand, RandomCommand, RPSCommand, ExitCommand, HelpCommand, LogoCommand, MathCommand, SayCommand]

Math_Allowed_Characters = "1234567890+-*/.()% "

while True:
    
    Command = input("Enter your command: ")

    if Command.lower() == "help":
        print("Command Help List:\n")

        for i in Commands:
            print(f"{i}")

        print()


    elif Command.lower() == "exit":
        break


    elif Command.lower() == "logo":
        print(Logo)


    elif Command.lower().startswith("say "):
        print(Command[4:])


    elif Command.lower().startswith("math "):
        Expression = Command[5:]


        if not all(i in Math_Allowed_Characters for i in Expression):
            print(GDOSCodes[9])
            continue

        if len(Expression) >= 100:
            print(GDOSCodes[8])
        try:
            Result = eval(Expression)

            if Result >= 10**4300 or Result <= -(10**4300):
                print(GDOSCodes[13])
            else:
                print(Result)

        except ZeroDivisionError:
            print(GDOSCodes[12])


    elif Command.lower() == "addf":

        GDOS_Dir = os.path.dirname(os.path.abspath(__file__))

        FileName = input("File Name: ")
        FileType = input("File Type: ")

        FilePath = os.path.join(GDOS_Dir, f"{FileName}.{FileType}")

        if os.path.exists(FilePath):
            print(GDOSCodes[15])

        elif FileType.lower() in NotAllowedAddEditOrDeletion.values() or os.path.isdir(FilePath):
            print(GDOSCodes[17])
            continue

        else:
            with open(FilePath, "x") as file:
                pass


    elif Command.lower() == "editf":

        FileText = input("File Text: ")
        AddOrWrite = input("A Or W?: ")
        FileName = input("File Name: ")
        FileType = input("File Type: ")

        GDOS_Dir = os.path.dirname(os.path.abspath(__file__))

        FilePath = os.path.join(GDOS_Dir, f"{FileName}.{FileType}")

        if FileType.lower() in NotAllowedAddEditOrDeletion.values() or os.path.isdir(FilePath):
            print(GDOSCodes[17])
            continue

        with open(FilePath, f"{AddOrWrite.lower()}") as file:
            file.write(f"{FileText}")


    elif Command.lower() == "deletef":
        FileName = input("File Name: ")
        FileType = input("File Type: ")

        GDOS_Dir = os.path.dirname(os.path.abspath(__file__))

        FilePath = os.path.join(GDOS_Dir, f"{FileName}.{FileType}")

        if not (FileName == "GeoOS" and FileType == "py"):
            os.remove(FilePath)

        elif FileType in NotAllowedAddEditOrDeletion.values() or os.path.isdir(FilePath):
            print(GDOSCodes[17])
            continue

        else:
            print(GDOSCodes[14])


    elif Command.lower() == "clear":
        subprocess.run(["cls" if os.name == "nt" else "clear"], shell=True)


    elif Command.lower() == "changedir":

        Path = input("What Path?: ")

        if Path == "":
            print(os.getcwd())
        else:
            try:
                os.chdir(Path)
                print(f"{os.getcwd()}> ", end="")

            except FileNotFoundError:
                print(GDOSCodes[18])

            except NotADirectoryError:
                print(GDOSCodes[19])

            except PermissionError:
                print(GDOSCodes[20])


    elif Command.lower() == "random":
        min = input("Minimum: ")
        max = input("Maximum: ")

        print(f"{random.randint(min, max)}, for minimum: {int(min)}, for maximum: {int(max)}")


    elif Command.lower() == "rock paper scissors":

        RPSp = input("Rock Paper or Scissors: ")

        adjustingBOT = input("Random or Adjusting Bot: ")

        if adjustingBOT.lower() == "adjusting":

            print("Adjusting...")

            time.sleep(1)

            if RPSp.lower() == "rock":
                Ratt += 1

            print("Adding...")

            time.sleep(0.7)

            if RPSp.lower() == "paper":
                Patt += 1

            print("Setting...")

            time.sleep(1.3)

            if RPSp.lower() == "scissors":
                Satt += 1

            print("Removing...")

            time.sleep(.2)

            print(GDOSCodes[24])

        elif adjustingBOT[0].lower() == "r":

            ResetOrNo = input("Reset or Don't Reset?: ")

            if ResetOrNo[1].lower() == "y":
                Ratt = 1
                Patt = 1
                Satt = 1

                print(GDOSCodes[22])

            elif ResetOrNo[1].lower() == "n":
                print(GDOSCodes[23])

        print(f"\nThe bot is thinking...\n")

        time.sleep(2)

        RPSb = random.choices(["Rock", "Paper", "Scissors"], [Satt ** 2, Ratt ** 2, Patt ** 2]) [0]

        if RPSp[0].lower() == "r":
            if RPSb == "Rock":
                print('You Tied, Opponent chose "Rock".')
            elif RPSb == 'Paper':
                print('You Lost, Opponent chose "Paper".')
            else:
                print('You Won, Opponent chose "Scissors".')

        elif RPSp[0].lower() == "p":
            if RPSb == "Rock":
                print('You Won, Opponent chose "Rock".')
            elif RPSb == 'Paper':
                print('You Tied, Opponent chose "Paper".')
            else:
                print('You Lost, Opponent chose "Scissors".')

        elif RPSp[0].lower() == "s":
            if RPSb == "Rock":
                print('You Lost, Opponent chose "Rock".')
            elif RPSb == 'Paper':
                print('You Won, Opponent chose "Paper".')
            else:
                print('You Tied, Opponent chose "Scissors".')

        else:
            print("Try another one.")

        print()

        ShowStats = input("Show stats? y / n ")
        DoneShowStats = False

        time.sleep(.5)
        while not DoneShowStats:

            if ShowStats.lower() == "y":
                print(f"\nDid {Ratt ** 2} Rocks, {Patt ** 2} Paper & {Satt ** 2} Scissors.\n")
                DoneShowStats = True

            elif ShowStats.lower() == "n":
                DoneShowStats = True

            else:
                print(GDOSCodes[21])
                ShowStats = input("Show stats? y / n ")

    elif len(Command) <= 3:
        print(GDOSCodes[1])

    elif len(Command) >= 256:
        print(GDOSCodes[2])

    elif len(Command) >= 2048:
        print(GDOSCodes[3])
    
    else:
        print(GDOSCodes[4])