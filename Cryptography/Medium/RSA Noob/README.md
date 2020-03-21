

# RSA Noob

* **Category:** Cryptography 
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/120)

> These numbers were scratched out on a prison wall. Can you help me decode them?  
>  https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

## Solution
As you can guess... , This challenge is about **RSA Encrption**.  
I extremely recommend to learn RSA Encrption as best as you can. I will give a short explantaion.  

## How we encrypt messege with RSA Encrption ?  

1.We need to choose the message and convert to a numberic format.   
Lets convert "attack at dawn" - > 1976620216402300889624482718775150  
M = 1976620216402300889624482718775150  

2.Chose 2 prime numbers - **p** and **q**  
p = 3 
q = 5

3. Calculate n -> n = pq -> n = 3*5 -> n = 15  

4. Calculate φ(n) = φ(p)*φ(q)= 2 * 4 = 8 (https://en.wikipedia.org/wiki/Euler%27s_totient_function) 




Flag : ```flag{d0nt_m3s5_w1th_th3_KGB} ```

