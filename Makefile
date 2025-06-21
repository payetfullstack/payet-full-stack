# Makefile for FastAPI project

# Path to your venv
VENV=venv/Scripts/activate

# Default target
.PHONY: run
run:
	@echo "Running FastAPI with Uvicorn..."
	@. $(VENV) && uvicorn main:app --reload

.PHONY: test
test:
	@echo "Running unit tests..."
	@. $(VENV) && pytest tests

.PHONY: install
install:
	@echo "Installing dependencies..."
	@. $(VENV) && pip install -r requirements.txt

.PHONY: update_requirements_txt
freeze:
	@echo "Freezing dependencies to requirements.txt..."
	@. $(VENV) && pipreqs .
