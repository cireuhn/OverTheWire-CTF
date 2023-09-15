# Bandit Level 5 → Level 6
Level Goal  
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:  

human-readable  
1033 bytes in size  
not executable  
Commands you may need to solve this level  
ls , cd , cat , file , du , find  
***
There were many directories and many files within each directory. A fast way to knock this out was:
```markdown
find /path/to/search -type f -readable ! -executable -size 1033c
```
Let's break down the command:

find: The command used to search for files and directories.  
/path/to/search: Replace this with the actual path to the folder you want to search in. In this challenge it is inhere.  
-type f: This option specifies that you want to find only files, not directories.  
-readable: This option checks if the file is human-readable.  
! -executable: This option checks if the file is not executable. The exclamation mark (!) is used to negate the condition, so it matches files that are not executable.  
-size 1033c: This option checks if the file size is 1033 bytes. The c indicates that the size is in bytes.  

When you run this command, it will search the specified directory and its subdirectories for files that meet all these criteria. It will then list the files that match these characteristics.

![!\[Alt text\](image.png)](<Images/Level 6.png>)  
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU