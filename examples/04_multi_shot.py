# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a multi-shot prompt example.
# Task: support ticket tagging
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt = """
You are an AI that classifies support tickets into categories.

Categories: Billing, Technical Issue, Account Access, General Inquiry

Examples:
Ticket: I was charged twice for my subscription this month.
Category: Billing

Ticket: The app crashes every time I try to open it.
Category: Technical Issue

Ticket: I forgot my password and cannot log in.
Category: Account Access

Ticket: How can I upgrade my plan?
Category: General Inquiry

Ticket: My payment failed but money was deducted.
Category: Billing

Ticket: Website is not loading on my laptop.
Category: Technical Issue

Now classify:

Ticket: Unable to reset my password using the link sent to email.
Category:
"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)