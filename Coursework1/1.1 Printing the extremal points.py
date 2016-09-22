###1.1 Printing the extremal points.
###This is a program that inputs a sequence of integers from a user and
###prints all numbers greather or smaller than both the predecessor and
###the successor except the first and the last integer.

#INITIALIZATION
list=[]
listresult=[]
n=int(input("How many integers would you like to enter?"))
for i in range (0,n):
        num=int(input("Integer%d:" %(i+1)))
        list.append(num)

#MAIN
for i in range(1, n-1):
        if(list[i]<list[i-1] and list[i]<list[i+1]):
                listresult.append(list[i])
        if(list[i]>list[i-1] and list[i]>list[i+1]):
                listresult.append(list[i])

#OUTPUT                
print ("The result is",listresult)
                
            
        
        
    
