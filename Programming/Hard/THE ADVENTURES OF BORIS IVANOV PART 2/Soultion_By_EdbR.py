# Solution By EdbR
from PIL import Image

listimages=[]
for i in range(0,500):
    listimages.append(Image.open(str(i) + ".png"))  # Make a list of pointers to the 500 pictures.

concatenate=Image.new("RGB",(500,500))              # Size of the concatenate picture
Y_offset=0

for i in listimages:
    concatenate.paste(i,(0,Y_offset))
    Y_offset+=1                                     # Add 1 at a time , Because the height of each picture is 1.
concatenate.save("concatenate.png")

print(bytearray.fromhex("666c61677b7468335f4b47425f6c307633735f4354467d").decode())
