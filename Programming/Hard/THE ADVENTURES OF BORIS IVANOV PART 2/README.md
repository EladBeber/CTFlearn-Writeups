
# THE ADVENTURES OF BORIS IVANOV PART 2

* **Category:** Programming
* **Points:** 80 
* **level:** Hard


## [Challenge](https://ctflearn.com/problems/382)

> The KGB agent Boris Ivanov found the place where one of the criminals was hiding for a long time. Unfortunately the criminal disappeared and more than that he shredded the piece of paper with important information. Help Boris to restore it. Here is a bin with the strips of paper: https://mega.nz/#!KLR3gaYD!6qvqvopHKjjzZZ0HC6pnWjXw0Pw5Z9kgKdGQCMXeUb0. Boris is an experienced agent and he instantly realized that the size of the sheet was 500x500

## Solution
Ok , So we have **500** PNG files, This amount of photos may be suspecious.\
In addition if you notice , each picture seems to be empty , Or with a thin line in some color.\
Lets look for more data , You can notice that the dimension of all the pictures is **500 X 1** and we have **500** pictures :)
Think about that , If we have **500** pictures with **widith=500 and height = 1** , The simple thought is to concatenate them vertically.

#### This is vertically concatenate  - 

![vertical](https://user-images.githubusercontent.com/57364083/69500145-2ba77480-0f01-11ea-9892-dd9d9543974d.png)

#### This is horizontally concatenate  - 

![vertical](https://user-images.githubusercontent.com/57364083/69500161-51cd1480-0f01-11ea-95b9-30c9f28f64c2.png)

So , We need to make vertically concatenate to all of the 500 pictures...
Using PIL , Its pretty simple.

<img width="771" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69500353-0582d400-0f03-11ea-8d6d-8d5edcb83871.PNG">

After finishing the concatenate of all the pictures we get the final picture - 

![concatenate](https://user-images.githubusercontent.com/57364083/69500306-9c02c580-0f02-11ea-9105-08f6b4fdc886.png)

The digits in the middle is a simple hex code, Convert to ascii...

<img width="711" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69500332-dec49d80-0f02-11ea-88d8-d2d04356f3d1.PNG">


Flag : ```flag{th3_KGB_l0v3s_CTF}```

