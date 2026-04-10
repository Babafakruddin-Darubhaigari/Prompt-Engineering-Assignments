# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a one-shot prompt example.
# Task: Convert informal sentences to professional tone
# We provide ONE example to demonstrate the pattern
prompt = """Example:
Informal: "Hey, just wanted to touch base about the project. It's gonna be done by Friday, no worries."
Professional: "I wanted to inform you about the project status. The deliverables will be completed by Friday."

Now convert this informal sentence to professional tone:
Informal: "The meeting was a total mess and nobody knew what was going on."
Professional:"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)





print("PROMPT:")

print("-" * 50)

print(prompt)

print("\nRESPONSE:")

print("-" * 50)

print(response)