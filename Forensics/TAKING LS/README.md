

# TAKING LS

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/103)

> Just take the Ls. Check out this zip file and I be the flag will remain hidden.\
>  https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## Solution

After download the challenge we are getting a rar file, and inside him a pdf file with the name "The Flag.pdf".\
But the pdf is protect by a password, So lets think.

We are getting in this ctf 2 hints:
1. In the title - TAKING **LS**
2. In the description - the flag will remain **hidden** So lets look for hidden files with the help of ```ls-a```


![Screenshot from 2019-11-06 02-06-46](https://user-images.githubusercontent.com/57364083/68250796-65840a00-002a-11ea-958c-03798d5beade.png)

Ok we are seeing a strange file start with a dot , with the name "ThePassword".\
Hidden files and folder have names that start with a **.** (dot character). \
To toggle show/hide hidden files or folders use the keyboard shortcut **Ctrl+H**.

We are getting a folder and inside txt file - "ThePassword.txt".\
When openning him we get the password for the pdf - ```Nice Job!  The Password is "Im The Flag".```


![Screenshot from 2019-11-06 02-07-19](https://user-images.githubusercontent.com/57364083/68251412-b8aa8c80-002b-11ea-87cd-c17fa42117a0.png)

Lets use the password to open unlock pdf and get the flag !

![Screenshot from 2019-11-06 02-11-43](https://user-images.githubusercontent.com/57364083/68251515-fdcebe80-002b-11ea-9f39-61da7fdc27b0.png)



Flag : ```ABCTF{T3Rm1n4l_is_C00l} ```

