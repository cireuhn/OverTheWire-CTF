# Bandit Level 6 → Level 7
Level Goal  
The password for the next level is stored somewhere on the server and has all of the following properties:  

owned by user bandit7  
owned by group bandit6  
33 bytes in size  
Commands you may need to solve this level  
ls , cd , cat , file , du , find , grep  
***

I used the command:
```markdown
find -type f -user bandit7 -group bandit6 -size 33c
```
- *-type f*: This option specifies that you want to find only files, not directories.  
- *-user bandit7*: This option checks if the file is owned by the user bandit7.  
- *-group bandit6*: This option checks if the file is owned by the group bandit6.  
- *-size 33c*: This option checks if the file size is exactly 33 bytes. The c indicates that the size is in bytes.  

![Alt text](<Images/Level 7.png>)

After finding the interesting file, I performed *cat* to retrieve the password

![!\[Alt text\](image.png)](Images/Level7_2.png)  
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S