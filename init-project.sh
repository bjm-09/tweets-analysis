#!/bin/bash

# Check if virtual environment name is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <virtual_env_name>"
    exit 1
fi

# Step 1: Create virtual environment
echo "Creating virtual environment..."
python -m venv "$1"

# Check if virtual environment creation was successful
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment."
    exit 1
fi

# Step 2: Activate virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source "$1"/bin/activate
pip install -r requirements.txt

# Check if dependencies installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi

echo "Setup completed successfully."
