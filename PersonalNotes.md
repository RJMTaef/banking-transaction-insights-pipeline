# what is python interpreter:
Actual Engine that runs python code

When you write print("Hello"), the code does not run by itself, so the interpreter reads it and executes it line by line.

# Why VS code asks you to select the interpreters:

your system can have multiple pythons installed, e.g. python 3.10, 3.11, Anaconda python or virtual environments, so vs code needs to understand which python to install.

# what happens if you ignore this interpreter selection in VS code?

-> You install pandas and vs code would say module not found
-> code runs in terminal but not in editor.
-> random version conflicts.
-> you waste hours debugging it.

# Libraries
Pre-built tools written by other developers
Instead of writing everythin from scratch you just reuse them

Eg
**PANDAS**
pandas
reads CSV, clean messy data, filter rows, transform columns and handle missing values.

**Matplotlib**
matplotlib
plot graph, plot transactionsal trends, show top customers, and visualize insights.

# Virtual environments
A private python workspace just for the project

**Why use it**
Your computer has one global python environment by default
If you install a library globally, all projects share the same libraries's version.

It sounds good, however, one project would need pandas version 1.5 but other projects might need version version 2.0. So if you install one, the other would break.

Therefore a virtual environment gives one isolated python +  packages for each individual project. So that it does not interfare with each other.

**How to create venv**
python3 -m venv venv

To activate - source venv/bin/activate

your inside when you see - (venv)

# .gitignore
it tells git to ignore these files/folder. Don't track them, don't upload them in github

# Why venv/ should be ignored?
venv/ contains python binaries, installed libraries and system specific files.
venv/ folder can be huge, different on every machine and easily be recreated.

If you upload venv/ to github, your repo becomes bloated, messy and unprofessional.

**In .gitignore file put**
venv/  ---- ignores your virtual environment
__pycache__/ ---- ignore python cache file
*.pyc ---- ignore compile python files

# python3 -c

runs a quick piece of python file directly into the terminal.

python3 -c "import pandas; import matplotlib; print('Packages working')"

You are not using ".py" file rather just executing one liner.

# Imports (why we use them)
os
→ Create/manage folders (ensure data/raw exists before saving files)
random
→ Generate fake values (names, countries, amounts, etc.)
datetime, timedelta
→ Create realistic dates (signup dates, transaction timelines)
pandas (pd)
→ Store data in tables and export to CSV easily
Other setup
random.seed(42)
→ Keep generated data consistent every run (helps debugging)
RAW_DATA_PATH = "data/raw"
→ Store folder path once instead of repeating it everywhere
os.makedirs(..., exist_ok=True)
→ Create folder if missing, avoid errors if it already exists

# 