# Chain-of-Thought Prompting

## What It Means
Chain-of-thought prompting is a technique where you ask the AI model to think step by step before giving the final answer. Instead of directly answering, the model explains its reasoning process in multiple steps.

## When to Use It
Use chain-of-thought prompting when:

The task involves calculations or logic
You need step-by-step reasoning
The problem is complex and cannot be solved in one step
You want more accurate and explainable results

## Example
Task: Calculate total cost.

## Chain-of-thought prompt:
Solve the problem step by step.

Problem: A shop sells a notebook for $10. A customer buys 5 notebooks and also pays a delivery charge of $5. What is the total cost?

Step 1: Cost of notebooks = 10 * 5 = 50
Step 2: Add delivery charge = 50 + 5 = 55
Final Answer: $55

Now solve:

Problem: A store sells a pen for $3. A customer buys 10 pens and pays an additional $7 for shipping. What is the total cost?

Step 1:The model follows the reasoning steps and then produces the final answer.

## Key Takeaway

Chain-of-thought prompting improves accuracy by breaking problems into smaller steps, helping the model reason more effectively instead of guessing.