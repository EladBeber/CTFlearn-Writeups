# BRUXOR

* **Category:** Cryptography
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/158)

> Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x. 0xc4115 0x4cf8


## Solution
From the beginning we can notice to a big hint -"Meet **ROX**y" - **ROX** -> **XOR** , So probably we use xor operation.\
Another hint is "a coder obsessed with being **exclusively** the worlds best hacker" , And if you remember XOR = **Exclusive or**.\
So lets xor the hex value we get in the CTF, Using [xor calculator](http://xor.pw/).

<img width="414" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68809523-c5a32d80-0674-11ea-99bc-5712859579c3.PNG">

Dont forget add "0x." in the beginning as write above.

Flag : ```0xc0ded```

