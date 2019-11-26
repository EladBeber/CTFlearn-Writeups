
# Weird Android Calculator

* **Category:** Programming 
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/290)

> I've found this very weird android application.Seems to be some kind of calculator, but there is something strange with it. Can you find out what it is?
> https://mega.nz/#!qXIAgSKZ!u2QBlLV-3G8kmsr6yR0wqpQOFyv89e0WvBt45alBIRY .\
> Flag is in Format: FLAG{...}
> Note: You don't really need an android device to solve this. But it might be helpful :)

## Solution
First lets run the app in android eumulator. I am using  **BlueStacks** emulator.\
As you can see its simple calculator...

<img width="184" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69641316-a8a12e00-1068-11ea-8daa-02a9944d019e.PNG">

After try some inputs in the calculator we get nothing interesting... , But in some cases i get this message :.\
"The number is too large. Please buy the full version!"

So, We need to do some **Reverse Engineering**.For that we will need 3 tools :.\
#### 1. Apktool
#### 2. dex2jar
#### 3. jd-gui
Im very recommend to read about the tools before you continue to read :).\
So, After read and install the tools lets create directory of the tools with out apk.

<img width="360" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69642124-f702fc80-1069-11ea-9c9f-09dd7f9a29d7.PNG">

First thing , using dex2jar - ```d2j-dex2jar WeirdCalculator.apk```.\
We will get jar file of our apk.
Now using jd-gui to read the code, Load ""WeirdCalculator-dex2jar.jar"".\
After some exploring the code we can notice two things:
1. If the input is above 100 we get the message - ""The number is too large. Please buy the full version!""
<img width="592" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69642835-0afb2e00-106b-11ea-9c1c-37c0af63b371.PNG">


2. We can notice an **array with 41** numbers that each value of the **xor with 0x539**.\
Ok , This is very strange ! Why a calculator need an array of 41 values and in addition xor this values with **permanent value** ?!.\
<img width="403" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69643062-6b8a6b00-106b-11ea-89ac-2a3b233c4a5e.PNG">

So its pretty obvious with found somthing **jucy** ! Now we have two ways of soltuion ! 

### 1. Python script
Writing a simple python script that will execute the Suspicious code.


<img width="834" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69644098-e1430680-106c-11ea-9078-cae8776da195.PNG">






Flag : ```FLAG{APK_4nalys1s_1s_r4th3r_3asy_1snt_1t}```

