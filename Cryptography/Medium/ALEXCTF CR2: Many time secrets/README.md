
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



<img width="669" alt="Capture" src="https://user-images.githubusercontent.com/57364083/78027385-f22abe00-7365-11ea-9978-38d2a68e31cb.PNG">


Flag : ```CTF{THUMBS_UP} ```

