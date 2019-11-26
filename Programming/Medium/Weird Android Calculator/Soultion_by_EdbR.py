#Soultion by EdbR 
import re
f=open("SuspiciousCode.txt","r")  # Txt file with the suspicious code
str=f.read()
p1="\s\d+"
y=re.findall(p1,str)              # Taking only the values in the array
for i in y:
    print(chr(int(i)^1337),end="")  # xor each value with 0x539 = 1337d
