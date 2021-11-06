import os
import pickle as pk

cwd = os.getcwd()
print("[Setting Data path]")
dataPath = cwd+"\\Data"
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
    print
    with open(dataPath+"\\ENGDICT", "rb") as f:
        dict = pk.load(f)
    print("[Dependencies have been created]")
    print("[Please append file: CODE.txt, for futher use]")
    

except FileExistsError:
    pass


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


