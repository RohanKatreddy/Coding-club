# Read in three weights
a, b, c = [int(input()) for i in range(3)]

# Sort the weights in ascending order
weights = sorted([a, b, c])

# Mama Bear's bowl is the medium weight
mama_bowl = weights[1]

# Print the weight of Mama Bear's bowl
print("Mama Bear's bowl weighs", mama_bowl, "units")
