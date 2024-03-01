# Define the name of the virtual environment
VENV = izr_desktop_venv

all:
    izr_desktop_venv/bin/python3 app.py
# Target to create the virtual environment
create:
	python3 -m venv $(VENV)

# Target to activate the virtual environment
act:
    . $(VENV)/bin/activate

# Target to deactivate the virtual environment
deact:
    deactivate

# Target to run the Python script using the virtual environment
run: $(VENV)/bin/activate
    . $(VENV)/bin/activate && python3 app.py


load:
    pip install -r requirements.txt
create:
    pip freeze > requirements.txt
compile:
    pip install pyinstaller
    pyinstaller IZRScreen.py
