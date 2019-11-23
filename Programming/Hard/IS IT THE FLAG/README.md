
# IS IT THE FLAG? (JAVA)

* **Category:** Programming
* **Points:** 90
* **level:** Hard

## [Challenge](https://ctflearn.com/problems/197)

> Pedro was disappointed because he didn't speak Python well enough to capture some of the flags on CTFLearn. His plan for revenge was to create one in his native language (Java). The flag is a String of 6 alphanumeric characters. Capture it. https://mega.nz/#!SHp1xCAL!I9-Zy4kwu_JY019MiYZ6CzGey8sJ6UvqE-ML2idmkrs


## Solution
The java file contain simple code the check a flag hash and compare the hash to a specific hash.\
Using the java funcion hashCode.We need to find the correct flag that will give us the output **"You found it!"**.

<img width="487" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69483630-6098c600-0e32-11ea-8967-78447cac2528.PNG">

Ok, By looking the hashCode we can see that is not a complicated mathematical function.\

<img width="532" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69483667-b66d6e00-0e32-11ea-8d17-4e75a646937b.PNG">

Now when we understand the code , We have two option :\
#### 1. Brutefuce - You can notice that the flag is 6 alphanumeric characters so we have (26+26+10)^6 = 62^6 options.
#### 2. Mathematical way  - In this option we think about a more efficient way to get the flag.

## Mathematical Solution 
As you can notice , The isFlag function check the flag with some hash **but** check also the **lowercase flag** with some hash.
So maybe the second check may some hint for the way of thinking...
## Moment to think...
Lets take an example - We know that **flag.hashCode()==1471587914** so lets check from the start.\
Out option for each letter is : list=[alphanumeric](0-9 A-Z a-z).\
<img width="1089" alt="Capture" src="https://user-images.githubusercontent.com/57364083/69483799-74452c00-0e34-11ea-939f-d896bdc1e264.PNG">

So lets assume that the first letter is '0' , this mean that we need to **ensure** two things:
1.That by sum this letter with all the next letter at **maximum** value the hashcode be **bigger or equal to 1471587914**.
By that we can play with the next characters and to the same algorithm we just did.\
2.That by sum this letter with all the next letter at **minimum** value the hashcode be **smaller or equal to 1472541258**.
By that we can play with the next characters and to the same algorithm we just did.






Flag : ```flag{AFlagInPCAP} ```

