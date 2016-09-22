###1.2 Computing the second largest number
###This is a program that calculates the second largest number among integers
###users entered.

#INITIALIZATION
Largest=0
secondLargest=0

#MAIN 
n=int(input("How many integers would you like to enter?"))
for i in range (0,n):
        num=int(input("Integer%d:" %(i+1)))
        if(num>Largest and num>secondLargest):
                secondLargest=Largest
                Largest=num
        if(num<Largest and num>secondLargest):
                secondLargest=num

#OUTPUT                
print ("The second largest number is",secondLargest)
