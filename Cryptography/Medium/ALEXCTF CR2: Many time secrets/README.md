
# ALEXCTF CR2: Many time secrets

* **Category:** Cryptography 
* **Points:** 60
* **level:** Medium 

## [Challenge](https://ctflearn.com/challenge/177)

> This time Fady learned from his old mistake and decided to use onetime pad as his encryption
> technique, but he never knew why people call it one time pad! Flag will start with ALEXCTF{.
> https://mega.nz/#!DGxBjaDR!tMWkHf0s0svmkboGd-IASHsS9jACxSYx4zi_ETsyzyQ


## Solution
In the description we see an encryption with the name - **onetime pad** https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_one_time_pad_cipher.htm  
In this kind of encryption we use a key with the same size or longer of the plaintext that we want to encrypt.
So is kind of Vigenère Cipher but the different is that for any letter we have a special shift.  
For example we have a msg with 10 letters like "plain text" so we need to execute 26^10 possibilities to find the plaintext.  

The is vulnerability in this encrpytion if the plaintext is small or there is **reused of the key**.  
In our challenge we can see 11 lines of numbers. Maybe each line is a cipher text and each line encrypted with the same key.  

We will use the tool **crib drag** to check that. https://github.com/SpiderLabs/cribdrag  
We know that part of the key is **ALEXCTF{** is a good start.

![Screenshot from 2020-04-01 15-51-47](https://user-images.githubusercontent.com/57364083/78129418-3ed2cf80-7420-11ea-8324-64eb3abf5599.png)

We will get a lot of possibilities for plain text , We need to make a calculate guess of the each line.  

![Screenshot from 2020-04-01 15-51-57](https://user-images.githubusercontent.com/57364083/78129555-76da1280-7420-11ea-80e7-b0ebf7cac6b3.png)

After a little work we can get the full key that reused again and again.  

![Screenshot from 2020-04-01 15-59-42](https://user-images.githubusercontent.com/57364083/78129968-20210880-7421-11ea-84ae-c8a694f1a62e.png)




Flag : ```ALEXCTF{HERE_GOES_THE_KEY}```

