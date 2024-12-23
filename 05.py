# Arithmetic => + - * / %
print(4/2) # 2.0
print(5%2) # 1
print(4//2) # 2
print(2**3) # 8
print(5 + 2 * 3) # 11

# P E M D A S
# ()
# ** R->L
# * / // % L->R
# + - L->R

print(5 + 2 * 3 - 1 + 10 / 5)


# Calculate BMI
# weight/(height * height)
weight = int(input("Enter the weight: "))
height = float(input("Enter the height: "))
BMI = weight/(height**2)
print(BMI)