###2.1 Finding two elements in a string
###This is a program that prints YES if "b" is placed after "a" in one of
###the string given by users. If none, it prints NO.

#INITIALIZATION
s=input("Enter a string:")
Found=0

#MAIN
for i in range(0, len(s)):
    for j in range (i+1, len(s)):
        if(s[i]=="a" and s[j]=="b"):
            Found=1

#OUTPUT
if(Found==1):
    print("YES")
else:
    print("NO")
