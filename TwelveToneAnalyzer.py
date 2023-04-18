#This is a simple program that will create a twelve-tone matrix.

global possibleNotesList
possibleNotesList = ['c', 'cs', 'd', 'ef', 'e', 'f', 
                     'fs', 'g', 'gs', 'a', 'bf', 'b']

def createInversion(intervalList):
    invertedIntervalRow = []    
    for x in intervalList:
        invertedValue = x - 12
        if invertedValue <= 0:
            invertedValue = invertedValue * -1
        invertedIntervalRow.append(invertedValue)

    return invertedIntervalRow


def intervalClassCounter(toneList):
    toneListFunc = toneList
    pitchClassList = []
    x = toneListFunc.pop(0)
    y = toneListFunc.pop(0)
    while len(toneListFunc) != 0 or x != y:
        counter = 0
        index = 0

        start = possibleNotesList.index(x)
        last = possibleNotesList.index(y)

        while True:
            if start == index:
                while True:
                    if last == index:
                        pitchClassList.append(counter)
                        break
                    elif index == len(possibleNotesList)-1:
                        index = 0
                    else:
                        index += 1
                    counter += 1
                break
            else:
                index += 1
                continue
        try:
            x = y
            y = toneListFunc.pop(0)
        except IndexError:
            continue
    return pitchClassList
    


def createRow(intervalList, toneRow):
    while len(intervalList) != 0:
        counter = 0
        for i in possibleNotesList:
            if possibleNotesList[counter] == toneRow[-1]:
                break
            counter += 1
        x = intervalList.pop(0)
        counter += x
        if counter >= len(intervalList):
            counter -= 12
            toneRow.append(possibleNotesList[counter])
        else:
            toneRow.append(possibleNotesList[counter])
    return toneRow

    

def checkNote(noteName, toneList):
    if noteName not in possibleNotesList:
        print("Error Code 01: Not a possible note.")
        return False
    elif noteName in toneList:
        print("Error Code 02: Note already exists in row.")
        return False
    else:
        return True


def createPrimeRow():
    toneRow = ['a', 'c', 'ef', 'd', 'cs', 'bf', 'b', 'gs', 'fs', 'g', 'e']
    while len(toneRow) < 12:
        userNote = input("Enter a note for your twelve-tone row (f for flat, s for sharp): ") # Enter f for test
        if checkNote(userNote, toneRow) == True:
            toneRow.append(userNote)

    return toneRow




def twelveToneMenu():
    print("*********************************************")
    print("*******Welcome to the Twelve-Tone Menu*******")
    print("*********************************************")
    while True:
        print("Please choose one of the following options: ")
        print("1. Enter prime tone row")
        print("2. Give me an inverted row")
        print("3. Give me a retrograde row")
        print("4. Give me a retrograde-inverted row")
        print("5. Give me a transposition")
        print("6. Give me a matrix")
        print("7. Exit\n")
        userChoice = int(input("Enter one of the numbers above: "))
        if userChoice == 1:
            primeRow = createPrimeRow()
            primeRowCopy = primeRow.copy()
            print(str(primeRow) + '\n')
        elif userChoice == 2:
            invertedInterval = createInversion(intervalClassCounter(primeRowCopy))
            print(createRow(invertedInterval, primeRow[0]))
        elif userChoice == 7:
            print("Thank you for using Twelve-Tone Menu!\n")
            exit()



def main():
    twelveToneMenu()
    
    
    
main()
