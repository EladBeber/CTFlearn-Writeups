

# TAKING LS

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/103)

> Just take the Ls. Check out this zip file and I be the flag will remain hidden.\
>  https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## Solution

We are getting in this ctf 2 hints:
1. In the title - TAKING **LS**
2. In the description - the flag will remain **hidden** So lets look for hiddent files with the help of ```ls-a```
```
strings 95f6edfb66ef42d774a5a34581f19052.jpg
```
![Screenshot from 2019-11-06 01-32-32](https://user-images.githubusercontent.com/57364083/68248342-4fc01600-0025-11ea-9b11-9bd37177a68e.png)

**scroll down and...**

![Screenshot from 2019-11-06 01-32-45](https://user-images.githubusercontent.com/57364083/68248429-7bdb9700-0025-11ea-9f35-ee46dd470be7.png)





Flag : ```flag{wow!_data_is_cool} ```

