import pickle as pk
import os
dataPath = os.getcwd()+"\\Data"



def start(dataPath):
    with open(dataPath+"\\DICTIONARY", "rb") as f:
        myDict = pk.load(f)
        f.close()

    print("FIND WORD IN DiCT")
    inp = str(input(">>> "))
    inp = inp.upper()
    inp = inp.replace(" ", "")
    if inp in myDict:
        print("word is in dictionary")
    else:
        print("word is not in dictionary")
    print("ADD WORD? [Y/N]")
    inp = str(input(">>> "))
    if inp.upper() == "Y":
        print("Enter word:")
        inp = str(input(">>> "))
        print("Enter Language[CASE SENSITIVE!!!]")
        inp1 = str(input(">>> "))
        myDict[inp.upper()] = inp1
        with open(dataPath+"\\DICTIONARY", "wb") as f:
            pk.dump(myDict, f)
            f.close()
    else:
        pass
    start(dataPath)

start(dataPath)

