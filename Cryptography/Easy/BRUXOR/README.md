# BRUXOR

* **Category:** Cryptography
* **Points:** 20
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/227)

> There is a technique called bruteforce. Message: q{vpln'bH_varHuebcrqxetrHOXEj No key! Just brute .. brute .. brute ... 


## Solution
From the beginning we can notice to a big hint **"BRUXOR" - Bruteforce + XOR**.\
So we need to do bruteforce xor on the Message: q{vpln'bH_varHuebcrqxetrHOXEj.\
Notice that the flag start with - "flag{"  , So we have part of the plaintext.
We will use [xor bruteforce online](https://gchq.github.io/CyberChef/#recipe=XOR_Brute_Force(1,100,0,'Standard',false,true,false,'flag%7B')&input=IHF7dnBsbidiSF92YXJIdWViY3JxeGV0ckhPWEVq)

<img width="1026" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68810526-00a66080-0677-11ea-9264-f93620588e6f.PNG">

Flag : ```7flag{y0u_Have_bruteforce_XOR}```

