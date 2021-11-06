import os
import pickle as pk
import requests as rq
import ast

cwd = os.getcwd()
print("[Setting Data path]")
dataPath = cwd+"\\Data"
url = "https://raw.githubusercontent.com/MyGuyArrow/SPACE_INSERTER/master/ENGDICT.txt"
lockState = True

try:
    print("[Checking files and directories]")

    os.mkdir(dataPath)
    print("[Creating Directory: Data, in CWD]")

    print("[Creating file: CODE.txt]")
    with open(dataPath+"\\CODE.txt","w") as f:
        f.write("[insert code here]")
        f.close()

    print("[Creating file: readme.txt]")
    with open(dataPath+'\\readme.txt', 'w') as f:
        f.write('please append the file "CODE" for space insertion program.')
        f.close()

    print("[Downloading file: ENGDICT.txt]")
    r = rq.get(url)
    stuff = str(r.content)
    stuff = stuff[2 : -1]
    #print(stuff)
    with open(dataPath+"\\ENGDICT.txt", "w") as f:
        f.write(stuff)
        f.close()

    print("[Converting to binary dict file]")
    with open(dataPath+"\\ENGDICT.txt", "r") as f:
        content = f.read()
        vocab = ast.literal_eval(content)
        f.close()
    with open(dataPath+"\\DICTIONARY", "wb") as f:
        pk.dump(vocab, f)
        f.close()


    print("[Removing redundant files]")
    os.remove(dataPath+"\\ENGDICT.txt")

    print("[Dependencies have been created]")
    print("[Please append file: CODE.txt, for futher use]")
    

except FileExistsError:
    print("[Initialising]")
    with open(dataPath+"\\DICTIONARY","rb") as f:
        vocab = pk.load(f)
        f.close()



with open(dataPath+"\\CODE.txt","r") as f:
        text = f.read()
        f.close()
if text == "[insert code here]":
    lockState = True
    
else:
    lockState = False
while lockState == True:
    print("[Script Locked]")
    inp = input("")
    with open(dataPath+"\\CODE.txt","r") as f:
        text = f.read()
        f.close()
    if text == "[insert code here]":
        lockState = True
    else:
        lockState = False

with open (dataPath+"\\CODE.txt", "r")as f:
    text = f.read()
    f.close()

print("TEXT:\n============================================================================")
print(text)
print("============================================================================")


