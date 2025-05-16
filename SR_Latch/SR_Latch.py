def sr_latch(current_state, S, R):

  # If both S and R are high, undefined behavior (illegal state)
  if S and R:
    raise ValueError("Invalid Inputs: S and R cannot be high simultaneously")
  
  # Set the latch if S is high and R is low
  if S and not R:
    return True
  # Reset the latch if R is high and S is low
  elif R and not S:
    return False
  # Otherwise, hold the current state
  else:
    return current_state

# Example usage
current_state = False
S = True
R = False

new_state = sr_latch(current_state, S, R)
print(f"Current state: {current_state}, S: {S}, R: {R} -> New state: {new_state}")
