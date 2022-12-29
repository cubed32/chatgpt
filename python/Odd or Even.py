# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
  print(num, "is even")
else:
  print(num, "is odd")

# Find the divisors of the number
divisors = []
for i in range(1, num+1):
  if num % i == 0:
    divisors.append(i)

# Print the divisors
print("Divisors:", divisors)
