

# RSA Noob

* **Category:** Cryptography 
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/120)

> These numbers were scratched out on a prison wall. Can you help me decode them?  
>  https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

## Solution
Ok , From first look we dont have any idea from where to start. After trying set of tools still get nothing...\
In this case when we get stuck , I recommend to read again the challenge and his files.

![Screenshot from 2019-11-11 01-53-34](https://user-images.githubusercontent.com/57364083/68551491-284abe00-0416-11ea-9f10-82057866979d.png)


After reading the challenge again and again we can notice the word **KGB** may bay relate to stegnograpy by **RGB**.\
So after play with some tools with rgb values and lsb , I found the solution in relation of rgb **offsets**.\
I use the tool stegslove , One of his option is **Stereogram Solver** and in this option there are 1000 offsets possible.

![Screenshot from 2019-11-11 03-10-46](https://user-images.githubusercontent.com/57364083/68552506-6fd64780-0420-11ea-89de-a653d952e646.png)

After a liitel hard work i found the flag in offset **898**.

![Screenshot from 2019-11-11 03-11-36](https://user-images.githubusercontent.com/57364083/68552509-76fd5580-0420-11ea-8f81-f7ea90c5db00.png)

Flag : ```flag{d0nt_m3s5_w1th_th3_KGB} ```

