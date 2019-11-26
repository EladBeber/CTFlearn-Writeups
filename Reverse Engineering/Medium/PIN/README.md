
# PIN

* **Category:** Reverse Engineering
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/379)

> Can you crack my pin?  
>https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ




## Solution
We get a ELF file as you can see :   
![Screenshot from 2019-11-26 19-38-39](https://user-images.githubusercontent.com/57364083/69648357-d3dd4a80-1073-11ea-851a-ab0c2e04786f.png)

We need to guess the correct pin , The pin will be the flag.  


![Screenshot from 2019-11-26 19-44-28](https://user-images.githubusercontent.com/57364083/69648773-9c22d280-1074-11ea-92ae-50aaaada5bab.png)


Lets change the extenesion to exe and run it in IDA , For those who dont familiar with IDA - https://www.hex-rays.com/products/ida/  
As , You can see in the beginning we have the print to the screen **"Masukan PIN ="** this show up before out input.    
After that we put our pin and the value going to --- > **[rbp+var4]** and **var = -4** Its mean our value stored in **[rbp-4]**  

 
Flag : ```stCTF{h34p_6ump5_r_c00l!11!!}```

