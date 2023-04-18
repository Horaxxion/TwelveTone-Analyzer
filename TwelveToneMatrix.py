#This is a simple program that will create a twelve-tone matrix.


def intervalClassCounter(toneList):
    x = toneList.pop(0)
    y = toneList.pop(0)
    


def checkNote(noteName, toneList):
    possibleNotesList = ['c', 'cs', 'd', 'ef', 'e', 'f', 
                     'fs', 'g', 'gs', 'a', 'bf', 'b']
    for x in possibleNotesList:
        if noteName == x:
            break
        else:
            if possibleNotesList[len(possibleNotesList)-1] == x:
                print("Error Code 01: Not a possible note.")
                return False
            else:
                continue
    for y in toneList:
        if noteName == y:
            print("Error Code 02: Note already exists in row.")
            return False
        else:
            continue
    return True



def main():
    toneRow = ['a', 'bf', 'ef', 'd', 'cs', 'c', 'b', 'gs', 'fs', 'g', 'f', 'e']
    toneRowDict = {'c': 0, 'cs': 1, 'd': 2, 'ef': 3, 'e': 4, 'f': 5, 'fs': 6, 'g': 7, 'gs': 8, 'a': 9, 'bf': 10, 'b': 11}
    while len(toneRow) < 12:
        userNote = input("Enter a note for your twelve-tone row (F for flat, S for sharp): ")
        if checkNote(userNote, toneRow) == True:
            toneRow.append(userNote)
        print(toneRow)
    intervalClassCounter(toneRow)


main()
