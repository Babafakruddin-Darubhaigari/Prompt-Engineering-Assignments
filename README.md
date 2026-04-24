# Prompt Engineering Practice

This project is a beginner-friendly workspace for learning prompt engineering with simple notes, small Python examples, and short assignments.

## Topics covered
- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Multi-shot prompting
- Chain-of-thought prompting
- Zero-shot chain-of-thought prompting
- Prompt formulation for AI models
- Working with a Python virtual environment
- Dependency management using `requirements.txt`
- Organizing examples, prompts, and assignments

## What you will learn
- How to give a direct instruction with zero-shot prompting
- How to guide the model with one example using one-shot prompting
- How to provide multiple examples for complex tasks with few-shot prompting
- How to make the model reason step by step using chain-of-thought prompting
- How to improve reasoning without examples using zero-shot chain-of-thought prompting
- How better prompt structure can improve the model's output

## Learning flow
1. Read the topic note inside `prompts/`.
2. Run the matching example inside `examples/`.
3. Complete the short practice task inside `assignments/`.

## Setup steps
1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
2. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\activate
   ```
3. Upgrade pip (optional but recommended):
   ```powershell
   python -m pip install --upgrade pip
   ```
4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## How to run example files
1. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\activate
   ```
2. Run the zero-shot example:
   ```powershell
   python examples\01_zero_shot.py
   ```
3. Run the one-shot example:
   ```powershell
   python examples\02_one_shot.py
   ```
4. Run the few-shot example:
   ```powershell
   python examples\03_few_shot.py
   ```
5. Run the multi-shot example:
   ```powershell
   python examples\04_multi_shot.py
   ```
6. Run the chain-of-thought example:
   ```powershell
   python examples\05_chain_of_thought.py
   ```
7. Run the zero-shot chain-of-thought example:
   ```powershell
   python examples\06_zero_shot_cot.py
   ```

8. Check the output in the terminal.

## Current practice modules
- `01_zero_shot` teaches how to ask the model to perform a task using only a clear instruction.
- `02_one_shot` teaches how to give the model one example before the real task so it can follow the same pattern.
- `03_few_shot` teaches how to provide multiple examples to help the model understand complex patterns and tasks.
- `04_multi_shot` teaches how to use many examples to improve accuracy and consistency in model responses.
- `05_chain_of_thought` teaches how to make the model think step by step to solve problems more accurately.
- `06_zero_shot_cot` teaches how to improve reasoning by asking the model to think step by step without giving examples.

## Folder structure
- `assignments/` - prompt engineering exercises and task descriptions
- `examples/` - runnable Python examples for prompt techniques
- `prompts/` - simple topic notes and prompt explanations
- `.venv/` - local virtual environment used for development
- `requirements.txt` - project dependencies
- `README.md` - project overview and setup instructions
- `helper.py` - helper code used by example scripts
- `.gitignore` - files and folders excluded from Git