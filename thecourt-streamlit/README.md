# court-dashboard
Code base for court-app dashboard, which currently powered by Streamlit.

## Installation
### 1. Clone this repository
```bash
$ git clone https://github.com/thecourtstats/court-dashboard.git
```

### 2. Get all dependencies

If you're using pip3
```bash
$ pip3 install -r requirements.txt
```
If you're not using pip3
```bash
$ pip3 install -r requirements.txt
```

### 3. Make sure `secrets.toml` file is exactly right and in proper format. Request the service account key to Alief

### 4. Run Streamlit App locally
```bash
$ python3 -m streamlit run TheCourt.py
```
or
```bash
$ python -m streamlit run TheCourt.py
```

Don't use this command, because the module needs statically generated
```bash
$ streamlit run TheCourt.py
```

## Instruction
### 1. Always put your query in lib/query.py files for easy maintain
### 2. Perhaps the `secrets.toml` file is git ignored, do not let the secret pushed to repository