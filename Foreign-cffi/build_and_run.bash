#!/bin/env bash

#apt install python3.10-venv python3.10-dev
#ls ~/PocsVenv/bin/activate || python3 -m venv ~/PocsVenv
#source ~/PocsVenv/bin/activate
#python3 -m pip install --upgrade pip wheel
#python3 -m pip install cffi

cc -fPIC -shared -o my_functions.so my_functions.c

python3 main.py
