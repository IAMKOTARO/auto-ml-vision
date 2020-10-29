python3 -m venv env
source ./env/bin/activate
cat requirements.txt | xargs -I@ pip install @