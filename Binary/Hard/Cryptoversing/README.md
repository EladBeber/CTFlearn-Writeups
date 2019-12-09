# Cryptoversing

* **Category:** Binary 
* **Points:** 90
* **level:** Hard


## [Challenge](https://ctflearn.com/challenge/667)

> Hello! My manager sent me a file named xor.bin, and he wants from you to crack this program, and get the flag.  
> https://mega.nz/#!neYzjQQS!mKNcdADY8u_V0Iy1a57gQpjNGTni03l7lTKOZVaYNes 

## Solution
We get a bin file , Lets execute and see what we get.  

![Screenshot from 2019-12-09 15-32-45](https://user-images.githubusercontent.com/57364083/70432722-940d5e80-1a88-11ea-8aee-306b3b1dc609.png)

So we need to guess the password and the password should be the flag.  
Take a look in IDA to see the flow of the program.

<img width="501" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70432900-f2d2d800-1a88-11ea-9bb1-7fb5a1bdb8ea.PNG">
 
Its look like after we enter the password the program store two important values-
1. strlen - len of our password
2. shr strlen , 1  =  **shr - shift right = divide by 2** , **shl - shift left = mul by 2** so the second value is **strlen/2**  

keep forward...

<img width="872" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70433183-b81d6f80-1a89-11ea-9663-10d802755a24.PNG">
Because of "mov [rbp+var_CC], 0" we will take the jump to the right side. In the end after some operations that we will see now 
we will visit in the left side where the important compare has been executed and decide if our password is the correct flag :)  
This is the operations that been executed on our password and after the been compared.  

<img width="479" alt="Capture" src="https://user-images.githubusercontent.com/57364083/70433973-b48ae800-1a8b-11ea-8f48-e0680cc4f165.PNG">

As you can see we have in the for loop this instruction "v18[j] = *(&v8 + i) ^ s[j];" 
s - array of our password  
*(&v8 + i) - we need to check the value , we will see in gdb
v18 - array where the xor result been saved 

After that we have this instruction "if ( v18[k] != v14[k] )" And if the value are not the same we message "Wrong Password"    
So, If all the values in **v18 will equal to v14** we will get the good message "Successful Login""  

We now that in xor operation:  
**if (a^b == c ) -------> a^c == b , b^c ==a** 
So we neet to preform **v14[k] ^ *(&v8 + i) To get s[k]** lets find the missing parts  


Flag : ```xOr_mUsT_B3_1mp0rt4nT```

