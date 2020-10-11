#!/bin/bash

if [ ! "$BASH_VERSION" ]
    then
        echo "This script does not support being explicitly run via sh."
        exit 1
    fi

echo "Checking if all core files are up to date.."
git pull
echo "Done"

echo "Checking if RaspTank dependencies and virtual environment is installed.."
if [ -d env ]
    then
        echo "RaspTank is installed."
        echo "Executing server using python.."
        source env/bin/activate
        python3 server.py
    else
        read -n 1 -r -p "RaspTank is not installed. Do you want everything to be installed? [y/n]"
        if [[ $REPLY =~ ^[Yy]$ ]]
            then
                echo "Creating virtual environment.."
                python3 -m venv env
                source env/bin/activate
                echo "Done"
                echo "Installing apt and pip dependencies"
                yes | sudo apt-get update
                yes | sudo apt-get upgrade
                yes | sudo apt-get install python-setuptools
                yes | sudo apt-get install build-essential 
                yes | sudo apt-get install libssl-dev 
                yes | sudo apt-get install libffi-dev 
                yes | sudo apt-get install python3-dev
                pip install RPi.GPIO
                pip install Adafruit_PCA9685
                pip install playsound
                echo "Done"
                echo "Adding default folder structure.."
                mkdir tmp
                mkdir tmp/sound_files/
                mkdir tmp/recorded_voices/
                echo "Done [Exited with 0]"
            fi
    fi
