"""tool for restructuring the dictionary"""

import pickle

with open("C:\\Users\\soans\\source\\repos\\SPACEINSERTER\\Data\\ENGDICT", "rb") as f:
    temp = pickle.load(f)
    f.close()

#conversion
cTemp = str(temp)

#formating the dictionary
fTemp = cTemp.replace("None", "'English'")
    
with open("temp.txt", "w") as f:
    f.write(fTemp)
    f.close()
