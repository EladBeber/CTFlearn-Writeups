

# TAKING LS

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/103)

> Just take the Ls. Check out this zip file and I be the flag will remain hidden.\
>  https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## Solution

While download the challenge we are getting a rar file and inside him a pdf file with the name "The Flag.pdf"\
But the pdf is protect by a password, So lets think.

We are getting in this ctf 2 hints:
1. In the title - TAKING **LS**
2. In the description - the flag will remain **hidden** So lets look for hiddent files with the help of ```ls-a```

![Screenshot from 2019-11-06 02-06-46](https://user-images.githubusercontent.com/57364083/68250796-65840a00-002a-11ea-958c-03798d5beade.png)

Ok we are seeing a strange file start with a dot , with the name "the password".
Hidden files and folder have names that start with a **.** (dot character). 
To toggle show/hide hidden files or folders use the keyboard shortcut Ctrl+H.




Flag : ```flag{wow!_data_is_cool} ```

