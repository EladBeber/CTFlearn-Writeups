
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







Flag : ```flag{AFlagInPCAP} ```

