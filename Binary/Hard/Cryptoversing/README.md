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
we will visit in the left side where the **important check been executed** and decide if our password is the correct flag :) 


Flag : ```xOr_mUsT_B3_1mp0rt4nT```

