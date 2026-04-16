# Import operating system module for path operations
import os

# Import system module for system-specific operations
import sys

# Add parent directory to Python path to import helper module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the helper function that sends prompts to the model.
from helper import get_completion

# This is a few-shot prompt example.
# Task: Sentiment classification
# We provide a few examples to demonstrate the pattern, then ask for a new classification

prompt = """Classify the sentiment of the following texts as positive, negative, or neutral.

Text: "I love this product! It works perfectly."
Sentiment: positive

Text: "This is the worst purchase I've ever made."
Sentiment: negative

Text: "The item arrived on time."
Sentiment: neutral

Text: "I'm really disappointed with the customer service."
Sentiment:"""

# Call the helper with the prompt and store the model's response.
response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)