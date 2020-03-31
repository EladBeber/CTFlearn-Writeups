# RSA Noob

* **Category:** Cryptography
* **Points:** 60
* **level:** Medium

## [Challenge](https://ctflearn.com/challenge/120)

> These numbers were scratched out on a prison wall. Can you help me decode them?   
> https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ  

## Solution

As you can guess , This CTF is about RSA Encryption. I extremely recommend explore and learn about RSA.  
You can read about RSA - https://simple.wikipedia.org/wiki/RSA_algorithm . 

So we have the variables :
1. 'e' and 'n' ----> public key.  
2. 'c' cipher text.  

<img width="587" alt="Capture" src="https://user-images.githubusercontent.com/57364083/78020414-197b8e00-735a-11ea-9244-ae8034d2ff69.PNG">

We will use this tool - https://github.com/Ganapati/RsaCtfTool to find 'd' and decrypt the cipher- 'c'.  
Use this command ```./RsaCtfTool.py -n 245841236512478852752909734912575581815967630033049838269083 -e 1 --uncipher 9327565722767258308650643213344542404592011161659991421```


Flag : ```ABCTF{b1nw4lk_is_us3ful} ```

