# Setup

## Create a Python Virtual Environment

This project works with Python v3.10.11.

To create a local python environment, run:
```python -m venv venv```

To activate it, you can run:

```.\venv\Scripts\activate```

## Install dependencies

```pip install -r requirements.txt```

## Download first FastAPI version. DO NOT REPLICATE

Inside the Python Virtual Environment:

```pip install fastapi uvicorn```

Optional: If you want automatic reload while developing:

```pip install "uvicorn[standard]"```

# Update requirements.txt

Make sure you have installed:

```pip install pipreqs```

Then run:

```pipreqs .```
