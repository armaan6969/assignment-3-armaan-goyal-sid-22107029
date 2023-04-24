#ques6
side1 = input("Enter length of side 1: ")
side2 = input("Enter length of side 2: ")
side3 = input("Enter length of side 3: ")

# Converting the entered sides to integers
side1 = int(side1)
side2 = int(side2)
side3= int(side3)

# Checking if the entered sides can form a triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Yes")
else:
    print("No")