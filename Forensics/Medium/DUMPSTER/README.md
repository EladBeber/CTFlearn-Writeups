
# DUMPSTER

* **Category:** Forensics
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/problems/355)

> I found a flag, but it was encrypted! Our systems have detected that someone has successfully decrypted this flag, and we stealthily took a heap dump of the program (in Java). Can you recover the flag for me? Here's the source code of the Java program and the heap dump:
> https://mega.nz/#!rHYGlAQT!48DlH2pSZg10Ei3f-Ivm7RoNBbV16Qw0wN4cWxANUwY

## Solution
Ok, so we have two files:
1. Decryptor.java.
2. Heapdump.hprof - The heap dump of the Decryptor.

By looking on the Decrypt file we can see the encrypted flag stored in the variable **FLAG**.

<img width="423" alt="1" src="https://user-images.githubusercontent.com/57364083/68749216-85a56180-0606-11ea-8ace-e7a20d9f9a6b.PNG">


## How we decrypt the flag ???
We need to write some **pass** that will be encrypted with SHA-256, And the first 16 bytes will stored in variable **passHash**.
The variable **passHash** would be the **key** in the AES decryption after that.




Flag : ```ABCTF{b1nw4lk_is_us3ful} ```

