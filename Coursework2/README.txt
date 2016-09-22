Coursework 2

Question 1
You are asked to write a function called ReplaceCS that can replace words 
in a string where the words are comma separated. 
It has 3 parameters, the ?rst is the string to be altered 
and the remaining two parameters are lists of words. 
The ?rst list contains the words to be replaced and the second list contains 
the replacement words, for example:

ReplaceCS(txt,["yes"],["no"])
	Replaces all instances of the word "yes" with the word "no" in the string txt.
ReplaceCS(txt,["yes","the"],["no","a"])
	Replaces all instances of the word "yes" with the word "no" 
	and all instances of "the" with the word "a" in the string txt. 
	The function returns a list containing the updated string, 
	a boolean ?ag which is set to true of the updates are successful 
	and a summary of the number of replacements for each word. For the following script:

txt = "yes,the,answer,is,yes" 
[s,flag,description] = ReplaceCS(txt,["yes"],["no"]) 
print(s) 
print(flag) 
print(description) 
print("-----") 
txt = "yes,the,answer,is,yes" 
[s,flag,description] = ReplaceCS(txt,["yes","the","twelve"],["no","a","thirteen"]) 
print(s) 
print(flag) 
print(description) 
print("-----") 
txt = "yes,the,answer,is,yes" 
[s,flag,description] = ReplaceCS(txt,["yes","the"],["no"]) 
print(s) 
print(flag) 
print(description)

Your output should be:

no,the,answer,is,no 
True 
yes :replaced 2 times 
----
no,a,answer,is,no 
True 
yes :replaced 2 times 
the :replaced 1 time 
twelve :replaced 0 times 
----
yes,the,answer,is,yes 
False 
List lengths do not match

Note: if the word is replaced only once the description should say Åe1 timeÅf, 
all other values it should say ÅetimesÅf. 
If the lengths of the two input lists are not equal, 
your function should return the original input string, 
a value of false for the ?ag and a description stating ÅeList lengths do not matchÅf. 
In all other cases set the ?ag to true. 


Question 2
Read the document called ÅeNetwork DisplayÅf. 
This document describes a program that we will eventually write for coursework 3. 
We shall build this program slowly, adding functionality as we learn about it 
in the lectures. To begin, write a function called ValidJunctions(lines) 
that raises a LookupError if a junction name has been de?ned twice, 
or a junction name has been used but not de?ned. 1) For the script:

1) For the script:

try:
	inf = open("network1.txt", "r") 
	lines = inf.readlines() 
	ValidJunctions(lines) 
	print("Successful") 
except LookupError as exceptObj: 
	print("Error:", str(exceptObj))

The output is:
Successful

2) For the script:

try:
	inf = open("networkFail1.txt", "r") 
	lines = inf.readlines() 
	ValidJunctions(lines) 
	print("Successful") 
except LookupError as exceptObj: 
	print("Error:", str(exceptObj))

The output is:

Error: A junction has been defined twice

3) For the script:

try:
	inf = open("networkFail2.txt", "r") 
	lines = inf.readlines() 
	ValidJunctions(lines) 
	print("Successful") 
except LookupError as exceptObj: 
	print("Error:", str(exceptObj))

The output is:

Error: There is an undefined junction