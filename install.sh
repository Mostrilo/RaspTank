#!/bin/sh

echo "Creating virtual environment.."
python3 -m venv env
echo "Done"
echo "Installing pip dependencies"
chmod u+x dependencies.sh
./dependencies.sh
echo "Done [Exited with 0]"