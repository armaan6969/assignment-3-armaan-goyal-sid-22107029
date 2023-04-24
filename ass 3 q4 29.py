#ques4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
#using if else
if num1 > num2 and num1 > num3: #case1 num1 greatest
    max_num = num1
elif num2 > num1 and num2 > num3: #case2 num2 greatest
    max_num = num2
else:
    max_num =num3  #case3 only option lft i.e num3 greatest
print("The greatest number is:", max_num)