def logic_AND(a, b):
  """Performs a logical AND operation on two bits."""
  return a and b

def logic_OR(a, b):
  """Performs a logical OR operation on two bits."""
  return a or b

def logic_NOT(a):
  """Performs a logical NOT operation on a bit."""
  return not a

def logic_XOR(a, b):
  """Performs a logical XOR operation on a bit."""
  return a != b

class FlipFlop:
  """Base class for Flip-Flops."""
  def __init__(self):
    self.q = None  # Current output (Q)
    self.prev_q = None  # Previous output (needed for T Flip-Flop)

  def get_output(self):
    """Returns the current output (Q) of the flip-flop."""
    return self.q

class SRFlipFlop(FlipFlop):
  """Simulates an SR Flip-Flop."""
  def __init__(self, S, R):
    super().__init__()
    self.S = S
    self.R = R

  def update(self):
    """Updates the flip-flop output based on S and R inputs."""
    if self.S and not self.R:
      self.q = True
    elif not self.S and self.R:
      self.q = False
    # Indeterminate output when S and R are both 1 or 0

class JKFlipFlop(FlipFlop):
  """Simulates a JK Flip-Flop."""
  def __init__(self, J, K):
    super().__init__()
    self.J = J
    self.K = K

  def update(self):
    """Updates the flip-flop output based on J and K inputs."""
    next_q = logic_OR(self.J, logic_AND(self.q, logic_NOT(self.K)))
    self.q = next_q

class DFlipFlop(FlipFlop):
  """Simulates a D Flip-Flop."""
  def __init__(self, D):
    super().__init__()
    self.D = D

  def update(self):
    """Updates the flip-flop output based on D input."""
    self.q = self.D

class TFlipFlop(FlipFlop):
  """Simulates a T Flip-Flop."""
  def __init__(self, T):
    super().__init__()
    self.T = T

  def update(self):
    """Updates the flip-flop output based on T input (toggle behavior)."""
    self.q = logic_XOR(self.q, self.T)

# Example usage
srflipflop = SRFlipFlop(1, 0)  # Initially set to 1 (S=1, R=0)
jkflipflop = JKFlipFlop(1, 0)  # J=1 sets on next clock pulse
dflipflop = DFlipFlop(0)  # Initially set to 0
tflipflop = TFlipFlop(1)  # Initial state depends on previous state (unknown)

# Update flip-flops
srflipflop.update()
jkflipflop.update()
dflipflop.update()
tflipflop.update()

# Get flip-flop outputs
srflipflop_output = srflipflop.get_output()
jkflipflop_output = jkflipflop.get_output()
dflipflop_output = dflipflop.get_output()
tflipflop_output = tflipflop.get_output()

print("SR Flip-Flop output:", srflipflop_output)
print("JK Flip-Flop output:", jkflipflop_output)
print("D Flip-Flop output:", dflipflop_output)
print("T Flip-Flop output:", tflipflop_output)
