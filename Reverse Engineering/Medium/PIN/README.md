
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

As  You can see in the beginning we have the print to the screen **"Masukan PIN ="** this shows up before our input.    
After that we put our pin and the value going to --- > **[rbp+var4]** and **var = -4** Its mean our value stored in **[rbp-4]**  
And the most important thing is - **"call cek"** In this function the important check been executed.  
If eax==0 , We get the bad message **"PIN salah !"** Else - We get the good message **"PIN benar ! !"**  

<img width="497" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69651038-2587d400-1078-11ea-85ae-97d381dffc6d.PNG">

### Verify with gdb-peda

![Screenshot from 2019-11-26 20-14-49](https://user-images.githubusercontent.com/57364083/69651410-b78fdc80-1078-11ea-9ee0-fc8ffd4ed7dd.png)

I put the pin **65** and the scanf@plt function covert my value to hex and stored it in eax and in edi after that  
Now lets enter to the **cek function**

![Screenshot from 2019-11-26 20-18-00](https://user-images.githubusercontent.com/57364083/69651687-240adb80-1079-11ea-9137-9682903c42e3.png)

We can see a compare between the value **0x51615** and our value **0x41** that stored in **[rbp-0x4]**    
If they are same we will jump to mov **eax, 01** :)  
Else - jump to mov   **eax, 00** :(  
So we just need to ensure that our pin will equal to **0x51615** in hex. Lets see that also in IDA  

<img width="315" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69652028-adbaa900-1079-11ea-883c-48ec30338a81.PNG">

If you notice carefully you can see the eax will get the value of the variable  **valid** , And guess what...
 
 <img width="419" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69652184-ec506380-1079-11ea-8b4f-f7416073663a.PNG">

valid equal to **0x51615** like we see in gdb-peda :)  
So we neet to convert  **0x51615** to decimal value :  

<img width="349" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69652295-1e61c580-107a-11ea-924b-9fc35d618838.PNG">

Lets check the flag - **"333333"**

![Screenshot from 2019-11-26 20-26-23](https://user-images.githubusercontent.com/57364083/69652521-74cf0400-107a-11ea-8877-efdd034be5ed.png)
 

 
Flag : ```333333```

