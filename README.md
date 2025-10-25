# DICOM-Toolkit
RapidAPI. Manage DICOM data, extracting info from each volume or converting them to new formats such as NIfTI.

# Render
Default Start Command:
```gunicorn your_application.wsgi```

I updated it to (yet to test):
```uvicorn main:app --host 0.0.0.0 --port $PORT```

# Unit tests

Unit tests can be run in the lcoal machine with:
```make test_unit```

Or can be run in a dockerized container:
```make docker_test_unit```

NOTE: Not all test data can be stored i the GitHub. Any msissing data can be found at Google Drive. As per now, the files not added in google Drive are:
- anonimized_dicom
  - CT
    - ThoraxRoutine--10.0--B70f.zip
  - MR
    - AX-DWI.zip 
    - T1-SAG-SE.zip
  - PT
    - PET_0mmol_1LC-Patlak-Intercept.zip
    - PET_FET_Cerebral.zip
  - RANO
    - DEMO_1.zip
  - US
    - 1.2.826.0.1.3680043.8.1055.1.20131219224620253.58545162.94269574.zip
    - Ultrasound.zip
- non_anonimized_dicom
  - TAC.zip


# Docker

Be very carfull with filling the computer's space with the docker images/containers and the build time + final size (GCP).

If any issue happens while pulling images, tr to upgrade the docker CLI. To delete any existing docker image/container, run:

```docker system prune -a```

# Package management

Two requirements.txt are being used in this project:
- requirements.txt: Necessary libraries to run the backend in a docker container
- requirements-dev.txt: Extra libraries in order to run the backend locally or run test over the backend
