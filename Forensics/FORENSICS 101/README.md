
# FORENSICS 101

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## Challenge

> Think the flag is somewhere in there. Would you help me find it?\
> https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c

## Solution

The solution here is pretty easy. We are hit the flag in initial and basic check in Forensics , **Strings !!!**
```
strings 95f6edfb66ef42d774a5a34581f19052.jpg
```
![Screenshot from 2019-11-06 01-32-32](https://user-images.githubusercontent.com/57364083/68248342-4fc01600-0025-11ea-9b11-9bd37177a68e.png)

**scroll down and...**

![Screenshot from 2019-11-06 01-32-45](https://user-images.githubusercontent.com/57364083/68248429-7bdb9700-0025-11ea-9f35-ee46dd470be7.png)





Flag : ```flag{wow!_data_is_cool} ```

