#!/bin/bash
set -e

# Choice menu
echo "1. Open keygen"
echo "2. Open telegram bot"
read -p "Choose action (1 or 2): " choice

# Choose handler
if [ "$choice" == "2" ]; then
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        export PYTHONPATH=../telegram-key-system
        python3 src/telegram/main.py
    else
        source venv/bin/activate
        export PYTHONPATH=../telegram-key-system
        python3 src/telegram/main.py
    fi
elif [ "$choice" == "1" ]; then
    if [ ! -d "node_modules" ]; then
        npm install -g yarn
        yarn install
        yarn tsc
        yarn keygen
    else
        yarn tsc
        yarn keygen
    fi
else
    echo "Invalid choice! Please select 1 or 2."
fi
