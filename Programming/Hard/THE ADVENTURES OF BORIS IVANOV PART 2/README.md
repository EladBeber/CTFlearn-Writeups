
# THE ADVENTURES OF BORIS IVANOV PART 2

* **Category:** Programming
* **Points:** 80 
* **level:** Hard


## [Challenge](https://ctflearn.com/problems/382)

> The KGB agent Boris Ivanov found the place where one of the criminals was hiding for a long time. Unfortunately the criminal disappeared and more than that he shredded the piece of paper with important information. Help Boris to restore it. Here is a bin with the strips of paper: https://mega.nz/#!KLR3gaYD!6qvqvopHKjjzZZ0HC6pnWjXw0Pw5Z9kgKdGQCMXeUb0. Boris is an experienced agent and he instantly realized that the size of the sheet was 500x500

## Solution
Ok , So we have **500** PNG files, This amount of photos may be suspecious.\
In addition if you notice , each picture seems to be empty , Or with a thin line in some color.\
Lets look for mor data , You can notice that the dimension of all the pictures is **500 X 1** and we have **500** pictures :).
Think about that , If we have **500** pictures with **widith=500 and height = 1** , The simple thought is to combine them vertically.

#### This is vertically paste - 

![vertical](https://user-images.githubusercontent.com/57364083/69500145-2ba77480-0f01-11ea-9892-dd9d9543974d.png)



Flag : ```stCTF{h34p_6ump5_r_c00l!11!!}```

