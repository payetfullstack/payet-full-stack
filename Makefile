# Path to local venv
VENV=venv/bin/activate


run_backend:
	echo "Running FastAPI with Uvicorn..."
	. $(VENV) && uvicorn main:app --reload

test_integration:
	echo "Running integration tests..."
	. $(VENV) && pytest tests/integration/

install:
	echo "Installing dependencies..."
	. $(VENV) && pip install -r requirements.txt

update_requirements_txt:
	echo "Checking if pipreqs is installed..."
	bash -c "source $(VENV) && (pip show pipreqs > /dev/null 2>&1 || pip install pipreqs)"
	echo "Running pipreqs to update requirements.txt..."
	bash -c "source $(VENV) && pipreqs . --force"
