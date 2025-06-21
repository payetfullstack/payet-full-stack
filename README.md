# DICOM-Toolkit
RapidAPI. Manage DICOM data, extracting info from each volume or converting them to new formats such as NIfTI.

# Render
Default Start Command:
```gunicorn your_application.wsgi```

I updated it to (yet to test):
```uvicorn main:app --host 0.0.0.0 --port $PORT```