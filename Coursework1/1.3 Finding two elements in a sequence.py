###1.3 Finding two elements in a sequence
###This is a program that print YES if 2 is placed after 1 in the sequence of numbers
###users entered.
        
#INITIALIZATION
list=[]
n=int(input("How many integers would you like to enter?"))
for i in range (0,n):
        num=int(input("Integer%d:" %(i+1)))
        list.append(num)

#MAIN
Found=0

for i in range(0, n-1):
    for j in range(1,n):
        if(list.index(1)<list.index(2)):
            Found=1

#OUTPUT
if(Found==1):
    print("YES")
else:
    print("NO")
