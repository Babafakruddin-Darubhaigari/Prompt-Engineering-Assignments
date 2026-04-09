# Prompt Engineering Practice

## Project title
Prompt Engineering Practice

## Topics covered
- Zero-shot prompting
- Prompt formulation for AI models
- Working with a Python virtual environment
- Dependency management using `requirements.txt`
- Organizing examples, prompts, and assignments

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
2. Run an example file with Python, for example:
   ```powershell
   python examples\01_zero_shot.py
   ```
3. Check the output in the terminal.

## Folder structure
- `assignments/` — prompt engineering exercises and task descriptions
- `examples/` — runnable Python examples for prompt techniques
- `prompts/` — prompt templates and explanations in Markdown
- `.venv/` — local virtual environment (ignored by Git)
- `requirements.txt` — project dependencies
- `README.md` — project overview and setup instructions
- `helper.py` — helper code used by example scripts
- `.gitignore` — files and folders excluded from Git
