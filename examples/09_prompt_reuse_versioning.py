# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a prompt reuse and versioning example.
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt1 = """
Calculate the monthly savings.

A person earns ₹50,000 and spends ₹32,000.
"""

# Call the helper with the prompt and store the model's response.
response1 = get_completion(prompt1)

print("PROMPT:")
print("-" * 50)
print(prompt1)

print("\nRESPONSE:")
print("-" * 50)
print(response1)


prompt2 = """
Role:
You are a financial advisor.

Task:
Calculate monthly savings and suggest a simple savings plan.

Context:
A person earns ₹50,000 per month and spends ₹32,000.

Constraints:
- Keep explanation simple
- Use step-by-step reasoning

Output Format:
- Monthly Savings: <amount>
- Explanation: steps
- Savings Plan: 2-3 bullet points
"""

# Call the helper with the prompt and store the model's response.
response2 = get_completion(prompt2)

print("PROMPT:")
print("-" * 50)
print(prompt2)

print("\nRESPONSE:")
print("-" * 50)
print(response2)