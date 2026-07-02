#!/bin/bash
cd ..
echo "Installing HyperOS Enchanter Requirements..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Install Complete! You can now use scripts/start.sh to launch the app."
