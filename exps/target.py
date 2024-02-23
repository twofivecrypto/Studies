import math

# Initial value
initial_value = 5000

# Target value
target_value = 1000000  # $1 million

# Calculate the number of times to double
num_doubles = math.ceil(math.log2(target_value / initial_value))

print("You need to double $100", num_doubles, "times to reach $1 million.")
