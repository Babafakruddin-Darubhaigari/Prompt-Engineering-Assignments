# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a chain-of-thought prompt example.
# Task: support ticket tagging
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt = """
You are an AI that solves business problems step by step.

Example:

Problem: A company sells a product for $50. The cost to produce it is $30. They sold 100 units. What is the total profit?

Step 1: Profit per unit = 50 - 30 = 20
Step 2: Total profit = 20 * 100 = 2000
Final Answer: $2000

Now solve:

Problem: A business sells a product for $80. The cost price is $50. They sold 60 units. What is the total profit?

Step 1:
Step 2:
Final Answer:
"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)