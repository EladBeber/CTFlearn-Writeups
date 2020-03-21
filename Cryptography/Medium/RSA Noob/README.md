

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
p = 5 
q = 11

3. Calculate n -> n = pq -> n = 5*11 -> n = 55 

4. Calculate φ(n) = φ(p)*φ(q)= 4 * 10 = 4 (https://en.wikipedia.org/wiki/Euler%27s_totient_function) 

5. Chose e -> 0 <e <φ(n) and e is coprime to φ(n) ---> e = 7 (https://en.wikipedia.org/wiki/Coprime_integers)

6. Calculate d ---> d = modulo inverse(e,φ(n)) = 23  (https://www.dcode.fr/modular-inverse) (I also add a script in python)   




Flag : ```flag{d0nt_m3s5_w1th_th3_KGB} ```

