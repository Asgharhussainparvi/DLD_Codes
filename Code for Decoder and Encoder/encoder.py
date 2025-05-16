def encoder(data):
  for i in range(len(data)):
    if data & (1 << i) != 0:  # Check if bit at position i is active using bitwise AND
      return i
  return -1  # No active bit found

# Example usage
data = 8  # Input data (binary 1000)
position = encoder(data)
print(position)  # Output: 3 (position of the active MSB)
