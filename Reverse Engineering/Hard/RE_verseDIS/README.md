# RE_verseDIS

* **Category:** Reverse Engineering
* **Points:** 90
* **level:** Hard


## [Challenge](https://ctflearn.com/challenge/188)

> Could you find the hidden password? 
>https://mega.nz/#!XOwVmCSC!ut_5r6b32j2kD6EvlvsvJhmm58pbswusUXF08yI93Zo


## Solution
Lets open the file in IDA.  

<img width="463" alt="Capture" src="https://user-images.githubusercontent.com/57364083/78185762-415f1480-7474-11ea-93aa-76c9ea7a223f.PNG">

As you can see there is output "Input password" and our input go to the variable **input**  
After that the value in key that is "IdontKnowWhatsGoingOn" mov to key2.  
In the next instruction we put in **msg** the result of "str[4 * i] ^ LOBYTE(key2[i]);".  
Later we are going through every letter in out **input** and checking if this equal to the letter ing **msg**  
So our only job is to break before the check and see what in **msg**  :)


 
Flag : ```333333```

