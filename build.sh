#!/bin/bash

# Install requirements from requirements.txt
pip install -r requirements.txt

# Check if installation was successful (optional)
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements."
    exit 1
fi

# Run the Python script
python gen.py

# Exit with the script's exit code (optional)
exit $?
