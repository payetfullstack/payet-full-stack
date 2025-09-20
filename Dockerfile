# Dockerfile is Multi-Stage to minimize junk
# Use a .dockerignore to minimize files to copy

# Stage 1: Build
# Python version is -alpine since is smaller that -slim (from 184MB to 259MB)
# In case of using a C extended library, it will be necessary to upgrade to -slim
FROM python:3.12-alpine AS builder
WORKDIR /app
RUN apk add --no-cache build-base
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Testing stage
# Only for local debugging
FROM python:3.12-alpine AS test
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
CMD ["pytest", "app/tests/unit/"]

# Stage 3: Final production image.
# Used for CI/CD
FROM python:3.12-alpine AS final
WORKDIR /app
COPY --from=builder /install /usr/local
# Do not copy everything. Removing after copying doesn't save space
COPY app/routers ./app/routers
COPY app/utils ./app/utils
COPY app/dependencies.py ./app
COPY app/main.py ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
