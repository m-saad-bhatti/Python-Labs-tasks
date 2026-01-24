# Take input from user
number = int(input("Enter a number: "))

# Print the multiplication table
print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")