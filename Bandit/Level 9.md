# Bandit Level 8 → Level 9

Level Goal  
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once  

Commands you may need to solve this level  
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd  

Helpful Reading Material  
Piping and Redirection  
***

Notes:  
`Sort` - command is a powerful Linux command that is used to sort lines of text in a file or stream. It has various options and features that allow you to fine-tune the sorting process, including sorting the text in a file according to the values in a specific column, changing the sort order, and more.

The basic syntax for the sort command is as follows:

sort [options] [files]

By default, the sort command sorts lines of text in ascending order based on the text itself. For example, if you have a file with the following content:
```
this
is
an
example
of
sort
```
When you use the sort command without any options, it will output the sorted text as follows:

```
an
example
is
of
sort
this
```  
`Uniq` - uniq command is a Linux command used to identify and display unique lines in a file or stream. The basic syntax for the command is as follows:

uniq [options] [files]  
By default, the uniq command displays all unique lines (i.e., lines that appear exactly once in the input). You can use the -c or --count switch to display the count of each unique line, like this:
```
cat
dog
cat
bird
dog
bird
```  
Using the uniq -c command will output:  
```
2 cat
2 dog
1 bird
```  
Additionally, the uniq command has other useful options, such as:

`-u` or --unique: Displays only unique lines (the default behavior if no options are specified).  
`-i` or --ignore-case: Ignores case while comparing lines.  
`-s` or --skip-fields: Skips a certain number of leading fields when comparing lines.  
`-w` or --width: Sets the width of fields to compare.  

To solve this challenge, combine these notes to get:  
![!\[Alt text\](image.png)](<Images/Level 9.png>)  
EN632PlfYiZbn3PhVK3XOGSlNInNE00t