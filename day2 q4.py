

a=0
b=0
def find_max(a,b):
    if(a>b):
         return a
    else: 
         return b
     
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2: "))
max1= find_max(num1,num2)
print("Max number:",max1)
    

    
  