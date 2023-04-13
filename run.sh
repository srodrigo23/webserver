clear
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd src
clear
echo 'Start Web Server'
python main.py