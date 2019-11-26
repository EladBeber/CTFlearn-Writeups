
# PIN

* **Category:** Reverse Engineering
* **Points:** 60
* **level:** Medium


## [Challenge](https://ctflearn.com/challenge/379)

> Can you crack my pin?  
>https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ




## Solution
We get a ELF file as you can see :   
![Screenshot from 2019-11-26 19-38-39](https://user-images.githubusercontent.com/57364083/69648357-d3dd4a80-1073-11ea-851a-ab0c2e04786f.png)

We neet to guess the correct pin , The pin will be the flag.  
Lets change the extenesion to exe and run it in IDA , For those who dont familiar with IDA - https://www.hex-rays.com/products/ida/  


Flag : ```stCTF{h34p_6ump5_r_c00l!11!!}```

