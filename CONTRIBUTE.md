# Setup

## Create a Python Virtual Environment

This project works with Python v3.12.3.

To create a local python environment, run:
```python3 -m venv venv```

To activate it, you can run:

```source venv/bin/activate```

## Install dependencies

```make install```

or

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
