
# RSA Noob

* **Category:** Cryptography 
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/120)

> These numbers were scratched out on a prison wall. Can you help me decode them?    
> https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

## Solution
Ok , So we have a file with the variables  "e" , "c " and "n" and the title mention RSA.  
We will need to understand the RSA Encryption to solve that.  


## How to decrypt the flag ???
We need to write some **pass** that will be encrypted with SHA-256, And the first 16 bytes will stored in variable **passHash**.

<img width="882" alt="2" src="https://user-images.githubusercontent.com/57364083/68749564-1aa85a80-0607-11ea-912e-e9c0744d5585.PNG">

The variable **passHash** would be the **key** in the AES decryption of FLAG after that.

<img width="666" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68749712-57745180-0607-11ea-8c27-f9bbed268905.PNG">

Ok, After we understood all the process , we only have one missing piece in the puzzle - how we get the **pass** !?
The answer is the second file - **Heapdump.hpro**

## Heap dump memory analyzer 
The second file is a dump of the heap from the program as you can notice here:

<img width="535" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68750188-26485100-0608-11ea-95bc-fe1c86574c39.PNG">

So we need to analyze the dump to catch where the user input the pass.\
We will use the program **visualvm**.
Before we start i recommend to you to explore the dump by yourself and do a full analyze and exploring for good understanding.

## Analyze
After analyze all the dump i have notice a problem to find the pass... But i find the **passHash** !!!
By going to the main thread -> Decryptor$Password -> **passHash**

![Screenshot from 2019-11-13 13-38-22](https://user-images.githubusercontent.com/57364083/68751447-45e07900-060a-11ea-8acf-a84264264cb2.png)

Now that we have the passHash we can wirte a short program that would be decrypt the flag.

<img width="868" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68752045-56ddba00-060b-11ea-92f2-1cccacfb6fef.PNG">

You can find the code here - https://pastebin.com/5vXTpVEN

Run the program and get the flag :)



Flag : ```stCTF{h34p_6ump5_r_c00l!11!!}```

