
# Weird Android Calculator

* **Category:** Programming 
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/290)

> I've found this very weird android application.Seems to be some kind of calculator, but there is something strange with it. Can you find out what it is?
> https://mega.nz/#!qXIAgSKZ!u2QBlLV-3G8kmsr6yR0wqpQOFyv89e0WvBt45alBIRY
> Flag is in Format: FLAG{...}
> Note: You don't really need an android device to solve this. But it might be helpful :)

## Solution
First lets run the app in android eumulator. I am using  **BlueStacks** emulator.\
As you can see its simple calculator...

<img width="184" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69641316-a8a12e00-1068-11ea-8daa-02a9944d019e.PNG">

After few some inputs in the calculator get nothing , But in some cases i get this message : "the number is large"

So, We need to do some **Reverse Engineering**.For that we will need 3 tools :.\
**1.Apktool**.\
**2.dex2jar**.\
**3.jd-gui**.





Flag : ```stCTF{h34p_6ump5_r_c00l!11!!}```

