# if else

name = "Sourabh"
if name:
    print(f"Yes name😎 {name} is provided")
    address="Noida"
    if address:
        print(f"Yes address is  {address} provided")
else:
    print("Name is not Provided")
    
    # if address not provide
name = "Sourabh"
if name:
    print(f"Yes name😎 {name} is provided")
    address=""
    if address:
        print(f"Yes address is  {address} provided")
else:
    print("Name is not Provided")   
    
    # if name not provide
name = ""
if name:
    print(f"Yes name😎 {name} is provided")
    address=""
    if address:
        print(f"Yes address is  {address} provided")
else:
    print("Name is not Provided")    
    
    # nested if else
    
    name = "Dev"
if name:
    print(f"Yes name😎 {name} is provided")
    address="Noida"
    if address:
        print(f"Yes address is  {address} provided")
    else:
        print(f"address is not Provided")  
else:
    print("Name is not provided") 
    
# next programe

num1=20
if num1%2==0:
    print("Number iS Even")
    mob=int(input("Enter your Number📞 -"))
    if len(mob) >=10:
        print("Valid Number")
    else:
        print("Invalid Number")
else:
    print("Odd")        
    
    
# UPSC exam programme
pre=int(input("Enter your Pre-Marks ")) 
if pre >= 400:
    print("You are Qualified and Eligible to MAINS😊") 
else:
    print("Pre-Failed😥 - Better Luck Next Time")   
mains=int(input("Enter your Mains Mark "))  
if mains>=600:
    print("You are Qulaified Mains😎 - Eligible to Interview ")
else:
    print("You are Disqualified in MAINS😭 - Good luck next time")        