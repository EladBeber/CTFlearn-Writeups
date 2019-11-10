

# UP FOR A LITTLE CHALLENGE?

* **Category:** Forensics
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/problems/142)

> https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0 You Know What To Do ...\

## Solution

As you probably know , The first thing we will check is **strings**.\
When using strings we can notice to four suspecious strings:
1. **Url address -  https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg**
2. **Mp real_unlock_key: Nothing Is As It SeemsU**
3.  **password: Really? Again**
4. **flag{Not_So_Simple...}**

As you can assume... the flag is not correct :).\
So , after trying few more tools we dont find something special, So lets use the URL.\
We get rar file , after extracting him and get inside the folder - "Did I Forget Again?" We see a jpeg file.
After trying a lot of tools that not bring nothing , lets think... , Maybe there is a hidden file that we forgot to check !?\
Lets use ```ls -a```. YeS ! there is so lets use ```ctrl+h```

Flag : ```ABCTF{T3Rm1n4l_is_C00l} ```

