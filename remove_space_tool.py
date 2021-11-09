#tool to remove spaces in text

with open("TTC.txt", "r") as f:
    ttc = f.read()
    f.close()

at = ttc.replace(" ", "")

with open("TC.txt", "w") as f:
    f.write(at)
    f.close()
