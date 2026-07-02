#!/bin/bash
cd ..
if [ ! -f "venv/bin/activate" ]; then
    echo "VENV not found. Please run scripts/install.sh first!"
    exit 1
fi

source venv/bin/activate
echo "Loading..."
python enchanter.py
