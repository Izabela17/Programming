n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1 = 0
num2 = 0
num3 = 1

for i in range(n):
    temp3 = num3
    num3 = num1 + num2 + num3
    if i > 1:
        num1 = num2
    num2 = temp3
    print(num3)

1 - 1+0+0
2 - 1+1+0
3 - 2+1+0
4 - 3+2+1  