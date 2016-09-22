###2.2 Processing a sequence of strings
###This is a program that prints a number of strings that has "b" after "a"
###in the sequence of strings users entered.

        
#INITIALIZATION
found=0
n=int(input("How many strings do you want to enter? "))

for i in range (0,n):
    count=0
    s=input("Enter string %d:"%(i+1))
    for j in range(0, len(s)-1):
        for k in range (j+1, len(s)):
            if(s[j]=="a" and s[k]=="b"):
                count=count+1
    if(count>=1):
        found=found+1

#OUTPUT
if(found>1):
    print("It appears in",found,"strings.")
else:
    print("None")
