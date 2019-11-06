
# BINWALK

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/108)

> Here is a file with another file hidden inside it. Can you extract it?\
> https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

## Solution

We have a huge hint to use **Binwalk**.\
Binwalk is **very popular** tools for Forensics. Its a tool for searching a given binary image for embedded files and executable code.\
I am very recommend to read and investigate about file signatures, and also on png and jpeg structre.\
You can look here - [File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

Ok , so lets use Binwalk to see if there are any hiddend files.
We will use this command  ```binwalk -b PurpleThing.jpeg ```

![Screenshot from 2019-11-06 03-19-09](https://user-images.githubusercontent.com/57364083/68254775-2bb80100-0034-11ea-8768-325210db6ae5.png)


Binwalk recognize **two** Png files, But we only see **one** !?!?\
Lets use this command to extract the Png file - ```binwalk -D 'image:png' PurpleThing.jpeg ```

We are done ! , We get a folder and inside him the original png file and the hidden png file that contain the **flag**.

![Screenshot from 2019-11-06 03-23-49](https://user-images.githubusercontent.com/57364083/68254807-3d99a400-0034-11ea-8528-835f6d2ba80a.png)





Flag : ```ABCTF{b1nw4lk_is_us3ful} ```

