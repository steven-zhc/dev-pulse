#!/bin/bash

# Script to set up the development environment for DevPulse

# Step 1: Install Python (if not installed)
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, installing..."
    brew install python
else
    echo "Python3 is already installed."
fi

# Step 2: Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv .venv

# Step 3: Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

# Step 4: Install necessary dependencies
echo "Installing necessary dependencies..."
pip install requests flask pytest

# Step 5: Create the directory structure (if not already present)
echo "Setting up the directory structure..."
mkdir -p src tests
touch src/__init__.py src/cli.py src/github_api.py tests/test_github_api.py

# Step 6: Create a requirements.txt file
echo "Creating requirements.txt..."
pip freeze > requirements.txt

# Step 7: Add and commit changes to Git
echo "Committing initial setup to Git..."
git add .
git commit -m "Initial project setup"

echo "Setup complete. Your project is ready!"

