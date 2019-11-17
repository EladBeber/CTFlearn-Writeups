# VIGENERE CIPHER

* **Category:** Cryptography
* **Points:** 30
* **level:** 20

## [Challenge](https://ctflearn.com/problems/305)

> The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.<br /> I’m not sure what this means, but it was left lying around: blorpy gwox{RgqssihYspOntqpxs}

## Solution
Ok , So we have the solution in the title as you can see "**VIGENERE CIPHER**" we need to decrypt the cipher with **VIGENERE**.\
As you can see in the site the flag start with "flag{" so we assume that **gwox** is encryption of **flag** so use this to find part of the key of the decryption , We will use this cyte - [VIGENERE CIPHER](https://www.dcode.fr/vigenere-cipher).

<img width="592" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69012994-e5439a00-0983-11ea-9728-bcdf7acd393f.PNG">

As you cann see part of the decryption key is blor , Buy wait ... if you notice before the chiper we get the key:
but it was left lying around: **blorpy** gwox{RgqssihYspOntqpxs}.So we also have the full key - **blorpy** , lets decrypt .

<img width="595" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69013045-71ee5800-0984-11ea-962b-62eb1fc9cffd.PNG">

Flag : ```flag{CiphersAreAwesome}```

