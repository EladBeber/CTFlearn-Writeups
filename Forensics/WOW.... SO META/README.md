
# WOW.... SO META

* **Category:** Forensics
* **Points:** 20
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/348)

> This photo was taken by our target. See what you can find out about him from it.\
> https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk

## Solution

We are have a clue from the title - ""WOW.... SO **META**"" the META may be a short for Metadata.\
Metadata is "data that provides information about other data".In short, it's data about data.\
So we will use the tool - "**ExifTool**" , this tool we help us reading meta info about the file.\
Use this command ```exiftool 3UWLBAUCb9Z2.jpg ``` and get the flag !.

![Screenshot from 2019-11-06 15-24-25](https://user-images.githubusercontent.com/57364083/68294419-cfd39380-0098-11ea-9487-39f49bc851d5.png)


Flag : ```flag{EEe_x_I_FFf} ```

