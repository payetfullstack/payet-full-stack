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

# Stage 2: Run
FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
