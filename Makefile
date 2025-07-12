# Path to local venv
VENV=venv/bin/activate


run_backend:
	echo "Running FastAPI with Uvicorn..."
	. $(VENV) && uvicorn app.main:app --reload --log-level debug

test_unit:
	echo "Running unit tests..."
	. $(VENV) && pytest app/tests/unit/

install:
	echo "Installing dependencies..."
	. $(VENV) && pip install -r requirements.txt

update_requirements_txt:
	echo "Checking if pipreqs is installed..."
	bash -c "source $(VENV) && (pip show pipreqs > /dev/null 2>&1 || pip install pipreqs)"
	echo "Running pipreqs to update requirements.txt..."
	bash -c "source $(VENV) && pipreqs . --force"
