# 1. Get input from user
    # Note: input() always returns a String, so we must convert it to an int
from py_compile import main


mass = int(input("m: "))
    
    # 2. Calculate energy
    # Speed of light constant
c = 300000000
    
    # Calculate E = m * c^2
    # In Python, ** is the exponent operator
energy = mass * (c ** 2)
    
# 3. Output the result
print(energy)

if __name__ == "__main__":
  main()