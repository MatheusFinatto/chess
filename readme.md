back:
cd back
pip install -r requirements.txt
python3 app.py

front:
cd front
npm i
npm run dev


lichess bot:

python3 -m venv venv # If this fails you probably need to add Python3 to your PATH.
virtualenv venv -p python3
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
