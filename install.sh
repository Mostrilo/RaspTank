#!/bin/sh

echo "Creating virtual environment.."
python3 -m venv env
echo "Done"
echo "Installing requirements from requirements.txt.."
pip install -r requirements.txt
echo "Done [Exited with 0]"