arr = [2, 4, 6, 8, 10]
size = 5 # Current size of the array
new_position = 2
new_element = 7

# Append a placeholder for the new element
arr.append(0)
# Shift elements to the right
for i in range(size - 1, new_position - 1, -1):
 arr[i + 1] = arr[i]

# Insert the new element at the specified position
arr[new_position] = new_element

# Update the size of the array
size += 1

# Print the updated array
for i in range(size):
 print(arr[i], end=" ")