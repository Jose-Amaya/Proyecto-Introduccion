file = open ("testing.txt")
global string
string = "[ "
"""
length = (len(file.readlines()))
file = open ("testing.txt")
"""

for x in file:
    string = string + "\"" + x.replace("\n", "") + "\"" + " , "
string = string + " ]"
file = open ("testing.txt", "w")
file.write(string)

