# Traversing bolte hai means loop chlana

#name="python"
#size=len(name)
#for i in range(size):
 #   print(name[i],i)
 
name="python"
for i in range(len(name)):
    print(name[i]) 
    
# without range

var1="Devops Engineer"
for i in var1:
    if i=="e":
        continue
    print(i, end=" ")    
    
# WAP to count all the voewls from give string : "this is devops batch" 

var1 = "this is devops batch" 
v_count=0
c_count=0
for i in var1:
    if i in"aeiou":
        v_count+=1
    else:
        c_count+=1
        
    print(v_count)
    print(c_count)  
    
# WAP to print your name in reverse format.

name = "sourabh"
rev = ""
for i in name:
    rev=i+rev
    print(rev)
    
# rev = i + rev
#  "" = "s" + ""
#  "s"= "o" + "s"
#  "os"= "u" + "os"
#  "uos"= "r" + "uos"   
#  "ruos"= "a" + "ruos" 
#  "aruos"= "b" + "aruos"
#  "baruos"= "h" + "baruos"

# WAP print

# P PYTHON 0
# Y PYTHON 1
# T PYTHON 2
# H PYTHON 3
# O PYTHON 4
# N PYTHON 5

str1="PYTHON"
size=len(str1)
for i in range(size):
    print(str1[i],str1, i)
        