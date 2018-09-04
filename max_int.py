"""If users enters x number of positive integers.
Program goes through those integers and finds the maximum positive 
and updates the code. If a negative integer is inputed the progam stops the execution
"""
"""
num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print ("The maximum is", max_int)

"""
n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1 = 0
num2 = 0
num3 = 1
i = 1
for i in range(n):
    temp3 = num3
    num3 = num1 + num2 + num3
    if i > 1:
        num1 = num2
    num2 = temp3
    print(num3)
    
    

    

    


 