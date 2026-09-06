# Contributing Guidelines

Thank you for reviewing or contributing to the project.

---

## Local Development Setup

### Prerequisites
* **Python:** v3.11
* **Docker:** Required for containerized testing and GKE deployment simulation
* **GNU Make:** Recommended for executing automated task shortcuts

### Environment Setup

Clone the repository and set up a clean Python virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate the environment (Linux/macOS)
source venv/bin/activate

# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

Install both runtime and development/testing dependencies using make or pip:
```Bash

# Using Makefile shortcut
make install

# Or manually via pip
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Environment Variables Configuration

Create a .env file in the project root directory containing mock or valid authentication secrets:
```Bash

X_RAPIDAPI_PROXY_SECRET_NAME=X-RapidAPI-Proxy-Secret
X_RAPIDAPI_PROXY_SECRET_VALUE=default-secret-key
```

### 4. Running the Application Locally

Start the local Uvicorn development server with hot-reloading enabled:
```Bash

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Access the interactive API documentation at:
    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc

### 5. Testing & Code Quality Guidelines

Before submitting a pull request or committing changes, ensure all unit and security tests pass cleanly.
```Bash

# Run unit tests locally
make test_unit

# Run tests in an isolated Docker environment
make docker_test_unit
```

### 6. Dependency Management Policy

- Production Dependencies: Add runtime libraries to requirements.txt with explicitly pinned versions.
- Development Dependencies: Add testing, linting, or profiling tools to requirements-dev.txt.