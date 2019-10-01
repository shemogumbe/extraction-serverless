# Registration Extraction POC

# How to use this
## Setting up the environment
```bash
git clone https://gitlab.com/zignite/clients/royal-informatics/registration-extraction-poc.git
cd registration-extraction-poc

# make sure you have python 3.6 and virtualenv installed
virtualenv --python=python3.6 venv
source venv/bin/activate

pip install -r requirements.txt

# Add an environment variable as below
export GOOGLE_APPLICATION_CREDENTIALS='path to site'

# Start the API service (Flask app)
python app.py
# go to localhost:5000/front
# go to localhost:5000/rear
```

## Video link on how to set up Google Cloud Vision API:
https://www.youtube.com/watch?v=tqFk8bzv2ys
