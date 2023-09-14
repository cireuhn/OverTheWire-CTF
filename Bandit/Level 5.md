# Bandit Level 4 → Level 5  
Level Goal
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Commands you may need to solve this level  
ls , cd , cat , file , du , find  
***
I did the *man* file command and search for the keyword human using /human  
The output from this was:  
```markdown
     -i, --mime  
             Causes the file command to output mime type strings rather than the more traditional human readable ones.  
             Thus it may say ‘text/plain; charset=us-ascii’ rather than “ASCII text”.
```
Using this I was able to differentiate the files that were binary and ASCII text.  
![!\[Alt text\](image.png)](<Images/Level 5.png>)  
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR