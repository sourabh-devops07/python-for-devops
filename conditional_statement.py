a=0
if a:
    print("Yes")
else:
    print("No")
    
if True:
    print("Yes")
else:
    print("No")

a=""
if a:
  print("yes")
else:
    print("No")


a=True
b=True
print(a+b)
print(type(a*b))

if 1*1*0:
    print("Yes")
else:
    print("No")
    
if True*0:
        print("Yes")
else:
    print("No")
  
 
    
a=int(input("Enter a Number :- "))
if a/2==0:
    print("Number is Even ")
else:
    print("Number is Odd")    
    
  
  
  
  # WRP to print a last digit number is 456735
  
last = 456735
print(last%10) 
print(last%100) 
    
 # WAP to find largest and smallest   
num1=3               # max number
num2=9
num3=12 
res=max(num1, num2, num3)
print(res)


num1=3              # min number
num2=9
num3=12 
res=min(num1, num2, num3)
print(res)


num1=3              
num2=9
num3=12 

if num1>=num2 and num1>=num3:
    print(F"{num1} is Greater ")


if num2>-num1 and num2>=num3:
    print(F"{num2} is Greater ")
    
if num3>-num1 and num3>=num2:    
    print(F"{num3} is Greater ")

# WAP to print grade obtained by a student in a test take marks obtained from the user and displaay grade?


marks=int(input("Enter the Marks :- "))
if 90<marks<=100:
    print("Grade - A")
elif 80<marks<=90:
    print("Grade - B")
elif 70<marks<=80:
    print("Grade - C")
elif 60<marks<=70:
    print("Grade - D")
elif 50<marks<=60:
    print("grade - E")
elif 0<marks<=50:
    print("Grade - F")
else:
    print("Invalid Marks")   
    
    
# sigle line ifelse 

# Write a python script to check whether a given number is positive or non positive ?

print("Enter a Number - ")
a=int(input())
print("Positive") if a>0 else print("non Positive")    

# Even or Odd

a=10
result="Even" if a%2==0 else "odd" 
print(result)
                    
   # Pass or fail example
    
marks=int(input("Enter Marks - "))
result = "Pass" if marks>=40 else "Fail" 
print(result)  


# Real life logic

age=int(input("Enter the Age :-  "))
status = "Adult😋" if age>=18 else "Minor😥" 
print(status)  


# Positive Negative Zero

num = int(input("Enter the Number :- "))
if num > 0:
    print("Number is POSITIVE😁")
elif num <0:
    print("Number is NEGATIVE😌")
else:
    print("Zero")    
    
    
    
    
    
    
    
        