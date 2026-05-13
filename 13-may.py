# WAP to sum of the indices of string : "python"

name="python"
for i in range(len(name)):
    i+=i
    print(i)
    
# WAP to print the factorial from 1 to 8

fact=1
for i in range(1, 9):
    fact=fact*i
    print(i, "=",fact)  
    
# WAP to print only prime number from 1 to 15

for num in range (1, 16):
    if num>1:
        for i in range(2, num):
            if num%i==0:
             break
        else:
          print(num)  
        
        
      