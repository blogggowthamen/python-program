n=input("Enter the Number")
if n>1:
for i in range(2,num):
     if(num % i) == 0:
       print(num,"is not a prime number")
       print(i,"times",num//i,"is",num)
     break
     else:
        print("Given is a prime number")
else:
    print("Given is not a prime number")        
