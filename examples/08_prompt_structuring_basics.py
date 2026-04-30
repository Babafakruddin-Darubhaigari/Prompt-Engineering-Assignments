# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a prompt structuring basics example.
# Task: support ticket tagging
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt = """
Role:
You are a financial advisor who explains things in a simple and clear way.

Task:
Calculate monthly savings and suggest a basic savings plan.

Context:
A person earns ₹45,000 per month and spends ₹28,000.

Constraints:
- Keep the explanation simple
- Use step-by-step reasoning
- Do not include complex financial terms

Output Format:
- Monthly Savings: <amount>
- Explanation: step-by-step calculation
- Savings Plan: 2-3 simple bullet points
"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)