Introduction to software development. 
Coursework 1

1 Processing a sequence of numbers
The tasks of this section are related to processing a sequence of numbers. 
In all of these tasks, the program gets from the user the number n of numbers 
to be entered and then asks the user to enter n more numbers. 
The speci?c tasks to perform with this sequence of numbers are outlined below. 

1.1 Printing the extremal points
Write a program that prints all elements a of the sequence satisfying 
the following two conditions. 
? a is not the ?rst nor the last element of the sequence. 
? a is either greater than both its immediate successor and predecessor 
or smaller than both of them.
For example, if the sequence is 3,4,10,8,6,2,21,15 then the elements to be printed 
are 10,2,21.

1.2 Computing the second largest number
Write a program that computes the second largest element of the sequence. 
For example, in the sequence above, the second largest element is 15. 
You can assume that all the elements are di?erent.

1.3 Finding two elements in a sequence
Write a program that prints ÅgYESÅh if the considered sequence of numbers 
contains both 1 and 2 so that 2 appears after 1 
(they do not need to be consecutive, simply 2 should appear somewhere after 1). 
If the sequence does not satisfy the above property, the program should print ÅgNOÅh. 
For example, the program should print ÅgYESÅh for the sequences 10,1,3,4,5,2,47,15 
or 2,3,5,2,1,2,10 but should print ÅgNOÅh for sequences 2,2,2,3,1,5 or 1,1,1,1,6.

2 Processing of strings
2.1 Finding two elements in a string
This task is a version of the last question in the previous section 
applied to strings. Write a program that gets from the user a string 
and prints ÅgYESÅh if the string contains letters a and b 
so that b is located after a. Otherwise, the program should print ÅgNOÅh.

2.2 Processing a sequence of strings
Write a program that gets from the user a sequence of strings and counts the number 
of strings for which the condition in the previous section is true. 
In order to get a sequence of strings, the programs should ask the user 
for the number n of strings to be entered and then prompt the user to enter 
n strings.