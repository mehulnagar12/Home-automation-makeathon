#!/bin/bash
#######################################################
# Copies py into a temp directory to run it
# This way, __pycache__ is not created
# and the dir stays clean
# doing this since .gitignore is not working properly
#######################################################

if [ ! -d "./../home_temp" ]; then
	mkdir ./../home_temp
fi

cp -R ./* ./../home_temp/
sudo python3 ./../home_temp/app/main.py
