# Solution By EdbR
import sys

def java_string_hashcode(s): # The hashCode function in java.
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def isFlag(str):
        return java_string_hashcode(str) == 1471587914 and java_string_hashcode(str.lower) == 1472541258 # The function from the CTF.

def main():
   list = []
   for i in range (48,58):
       list.append(i)
   for i in range (65,91):
       list.append(i)
   for i in range(97, 123):
       list.append(i)
   flag=""
   for i0 in list:
       if (i0 > 48):
           flag = flag[:-5]
       flag += chr(i0)
       for i1 in list:
           if (i1 > 48):
               flag = flag[:-4]
           flag += chr(i1)
           for i2 in list:
               if (i2 > 48):
                   flag = flag[:-3]
               flag += chr(i2)
               for i3 in list:
                   if (i3 > 48):
                       flag = flag[:-2]
                   flag += chr(i3)
                   for i4 in list:
                       if (i4 > 48):
                           flag = flag[:-1]
                       flag += chr(i4)
                       for i5 in list:
                           flag += chr(i5)
                           print(flag)
                           if(java_string_hashcode(flag)==1471587914 and java_string_hashcode(flag.lower())==1472541258):
                               print("The flag is:", flag)
                               sys.exit()
                           flag = flag[:-1]
main()
