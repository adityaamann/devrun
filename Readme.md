# devrun

Automatically set up any GitHub repository with one command.

No more wasting hours reading READMEs, installing wrong versions,
or missing environment variables. devrun clones any repo, figures
out what it needs, and sets it up for you automatically.

## What it does

- Clones the repo
- Detects the project type (Node.js, Python, etc.)
- Installs all dependencies automatically
- Creates .env file if environment variables are needed
- Tells you exactly how to start the project

## Requirements

- Python 3.8 or higher
- Git
- Node.js (for running Node.js projects)
- A free Groq API key from console.groq.com

## Installation

### 1. Clone devrun
git clone https://github.com/adityaamann/devrun
cd devrun

### 2. Install dependencies
pip3 install -r requirements.txt

### 3. Get your free Groq API key
Go to https://console.groq.com, sign up, and create an API key.

### 4. Create your .env file
Create a file called .env inside the devrun folder and add:
GROQ_API_KEY=your_key_here

### 5. Install devrun
pip3 install -e .

## Usage

devrun https://github.com/anyone/anyrepo

## Examples

devrun https://github.com/expressjs/express
devrun https://github.com/pallets/flask

## Supported project types

- Node.js (npm and yarn)
- Python (pip, poetry, setup.py, pyproject.toml)
- More coming soon

## Built with

- Python
- Groq API (free)
- LLaMA 3.3 70B