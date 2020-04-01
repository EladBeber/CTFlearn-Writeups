
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

<img width="669" alt="Capture" src="https://user-images.githubusercontent.com/57364083/78027385-f22abe00-7365-11ea-9978-38d2a68e31cb.PNG">


Flag : ```CTF{THUMBS_UP} ```

