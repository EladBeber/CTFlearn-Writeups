
# A CAPTURE OF A FLAG

* **Category:** Forensics
* **Points:** 30
* **level:** Easy

## [Challenge](https://ctflearn.com/problems/356)

> This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark.\
> https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4

## Solution

We have a wireshark file with a lot of data.\
In this case lets search for post and get request to find passwords or flags hidden.\
Lets sort the file by the Protocol column, by a quick glance we noitce about somthing interesting.
You can see a get request with a msg and after that probably base64 encryption.

<img width="1280" alt="Desktop Screenshot 2019 11 07 - 12 50 30 27" src="https://user-images.githubusercontent.com/57364083/68383238-f4457380-015d-11ea-9e43-3f0f962d16aa.png">


So lets get in the packet with folow tcp stream ,Copy the message and try to decrypt the base64 encryption.


<img width="1280" alt="Desktop Screenshot 2019 11 07 - 12 53 35 68" src="https://user-images.githubusercontent.com/57364083/68383217-eb54a200-015d-11ea-8390-f13d618b5038.png">


<img width="667" alt="Capture" src="https://user-images.githubusercontent.com/57364083/68383180-d710a500-015d-11ea-95c3-090c5b49dd66.PNG">


Flag : ```flag{AFlagInPCAP} ```

