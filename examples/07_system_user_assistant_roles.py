# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a system user assistant role prompt example.
# Task: support ticket tagging
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt = """
You are a financial advisor.

I earn ₹40,000 per month and spend ₹25,000.
Calculate my monthly savings and suggest a simple plan.

Let's think step by step.
"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)