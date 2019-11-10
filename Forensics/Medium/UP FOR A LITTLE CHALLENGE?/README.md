

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

As you can see :

![Screenshot from 2019-11-10 23-57-25](https://user-images.githubusercontent.com/57364083/68550072-309bfc80-0408-11ea-8b50-b9e87ccdf0df.png)

![Screenshot from 2019-11-10 23-57-38](https://user-images.githubusercontent.com/57364083/68550088-47425380-0408-11ea-9615-7cd1928648ac.png)


As you can assume... the flag is not correct :).\
So , after trying few more tools we dont find something special, So lets use the URL.\
We get a rar file , after extracting him and get inside the folder - "Did I Forget Again?"  We see a jpeg file.
After trying a lot of tools that not bring nothing , lets think... , Maybe there is a hidden file that we forgot to check !?\
Lets use ```ls -a```. YeS ! there is , So lets use ```ctrl+h```\
We get a rar with a locked jpeg file inside , We need the password to unlock the jpeg.

## Moment to think...

Where we can find this password ???. You remember the four strings we found from the original image ?.
After try all of them we got a **hit** !!! **Nothing Is As It SeemsU**  , but remove the last **U**.\
The Password is - ```Nothing Is As It Seems```
Unlock the jpeg file and if you notice we see a red string in the **bottom right corner**.


![Screenshot from 2019-11-11 00-18-40](https://user-images.githubusercontent.com/57364083/68550122-a43e0980-0408-11ea-94e6-667e8f422352.png)


Flag : ```flag{hack_complete} ```

