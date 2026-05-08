# Loop in python (Used for something repet)
# 1. for loop : ranged based
# 2. while loop : condition based

# 1. for loop
# range (start, stop, step)
# range always works with integer number.
# end =" "  - output horizontally aayga

for i in range(10): # 10 digit hai ek hto stop bali rhti hai
    print("Hello")
    
    
for i in range(1, 8): # isme 1 start hai or 8 stop
    print(i)     
    
    
    
for i in range(1, 8, 2):
    print(i)    
    
for i in range(1,8,2):
    print(i, end=" ") # end use hua h horizontally output k liye
    
    
for i in range(1,20):
    if i==10: # 10 pe rok dega
        break
    print(i, end=" ")    
    
for i in range(1,20):
    if i==10:
        continue # skip kr dega 10 ko baki number aayge 1 to 19 but 10 ni hoga usme
    print(i, end=" ") 
    
    
for i in range(1,21):
    if i%2==0:
        print(i, end=",")  
        
        
        
for i in range(1,21):
    if i%2 !=0:
        print(i, end=",")
    else:
        print(f"Odd : {i}")    
        
        
for i in range(1,21):
    if i%2 !=0:
        print(f"Even : {i}")
    else:
        print(f"Odd : {i}")   
        
        
s=0
for i in range(1,5):
    s=s+i
    print(s, end=" ")     
    
s=10
for i in range(1,5):
    s=s+i
    print(s, end=" ")  
    
for r in range(10, 15, -1):
    print(r)            # no output 15 minus mai hota to aata output  
    
# 1. WAP to take start point and end_point from user input and print all number divsible by 2 and 3.   

# 2. WAP to take a number from user input and print formatted table.
# format :
# 3*1=3
# 3*2=6 

# 3. WAP to take a number from user input and print reversed formatted table.

# 1. WAP to take start point and end_point from user input and print all number divsible by 2 and 3. 

start_point=int(input("Enter the Start point - "))
end_point=int(input("Enter the End point - "))
for i in range(start_point, end_point):
    if i%2==0 and i%3==0:
        print(i, end=" ")
        
        
 #2. WAP to take a number from user input and print formatted table.
# format :
# 3*1=3
# 3*2=6 

num1=int(input("Enter the Number - "))
for i in range(1,11):
    result=num1*i
    print(f"{num1} X {i} = {result}")
    
# 3. WAP to take a number from user input and print reversed formatted table.

num1=int(input("Enter the Number - "))
for i in range(10,0,-1):
    result=num1*i
    print(f"{num1} X {i} = {result}")    
    

    