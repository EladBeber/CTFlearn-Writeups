

# 07601

* **Category:** Forensics
* **Points:** 60
* **level:** Medium

## [Challenge](https://ctflearn.com/problems/97)

> I think I lost my flag in there. Hopefully, it won't get attacked...\
>  https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ

## Solution

With a quick use of strings command we get the flag **ABCTF{fooled_ya_dustin}** but its wrong flag...
So lets use one of the famoust tools - **binwalk**.\
By using this command ```binwalk -b AGT.png ```  we see alot of zip files hidden in the image.

![Screenshot from 2019-11-08 03-29-41](https://user-images.githubusercontent.com/57364083/68436639-4a023600-01c7-11ea-8947-9fbe8122dc94.png)

Lets extract hidden data from the image using the command  ```binwalk -e AGT.png ```\
After extract the hidden data we see a folder with the name **Secret Stuff...**  interesting..\
When getting into this folders we meet **Don't Open This...** , enter to this folder we see image.\
Using a simple strings command on the new image and we get the flag :

![Screenshot from 2019-11-08 03-24-47](https://user-images.githubusercontent.com/57364083/68436430-a9ac1180-01c6-11ea-9d3a-161f989ed316.png)


Flag : ```ABCTF{Du$t1nS_D0jo}1r ```

