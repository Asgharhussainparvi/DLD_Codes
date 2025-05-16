def decoder(code):
  outputs = [0] * 2**len(code)  # Initialize outputs with all zeros (length depends on code length)
  outputs[code] = 1  # Set the corresponding output to 1 based on the code value
  return outputs

# Example usage
code = 2  # Input code (binary 10)
active_outputs = decoder(code)
print(active_outputs)  # Output: [0, 0, 1, 0] (only third output is active)
