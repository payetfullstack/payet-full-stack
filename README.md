# Multi-API SaaS Hub & DICOM Toolkit API

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![pydicom](https://img.shields.io/badge/pydicom-3.0+-205280?style=flat)](https://pydicom.github.io/)
[![Google Cloud](https://img.shields.io/badge/GCP-Kubernetes_Autopilot-4285F4?style=flat&logo=googlecloud&logoColor=white)](https://cloud.google.com/)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Monetized-0052CC?style=flat&logo=rapidapi&logoColor=white)](https://rapidapi.com/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-yellow?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)

A production-ready, stateless multi-API backend platform designed to deploy, monetize, and scale pay-per-use developer utilities on **RapidAPI**. The initial flagship module hosted on this platform is the **DICOM Toolkit API**—a high-performance medical imaging pipeline for processing, inspecting, and converting DICOM datasets.

---

## 📌 Portfolio Context & Public Release Note

> **Note for Hiring Managers & Engineering Recruiters:**
> This repository was originally architected and deployed as a commercial multi-API SaaS microservice platform. It has been made public to demonstrate software engineering standards, cloud-native architecture, and security-first development practices.
>
> **Key Engineering & Architectural Principles Demonstrated:**
> * **Multi-API Platform Architecture:** Designed as an extensible API hub using isolated FastAPI `APIRouter` modules capable of hosting multiple distinct SaaS products under unified security and logging layers.
> * **Zero-Storage Security (HIPAA/GDPR Compliance):** Memory-only processing models (`tempfile`) with instant buffer cleanup to ensure no sensitive data or Protected Health Information (PHI) is persisted.
> * **Hardened API Defenses:** Mitigation of Zip Bomb and Zip Slip vulnerabilities (`os.path.realpath` boundary enforcement) alongside constant-time HMAC secret validation to block timing attacks.
> * **Cloud-Native Infrastructure:** Automated CI/CD build definitions (`cloudbuild.yaml`) deploying containerized workloads to **Google Cloud Kubernetes Engine (GKE) Autopilot**.

---

## 🏗️ Platform Architecture & Monetization Pipeline

The core framework acts as a central hub where independent API services share middleware, authentication, and deployment
definitions while maintaining domain isolation.

```text
 ┌────────────────────────────────────────────────────────┐
 │                  RapidAPI Marketplace                  │
 │  - Manages API Subscriptions & Usage Metering          │
 │  - Integrates directly with Stripe for User Billing    │
 └──────────────────────────┬─────────────────────────────┘
                            │ Proxied HTTP Requests +
                            │ RapidAPI Proxy Secret Headers
                            ▼
 ┌────────────────────────────────────────────────────────┐
 │            GCP GKE Autopilot (FastAPI Core)            │
 └───────────────┬────────────────────────────┬───────────┘
                 │                            │
                 ▼                            ▼
  ┌─────────────────────────┐  ┌──────────────────────────┐
  │   /dicom-toolkit        │  │  /future-saas-service    │
  │ (Medical Data Pipeline) │  │ (Extensible SaaS Module) │
  └─────────────────────────┘  └──────────────────────────┘
```

## DICOM Toolkit API

### 💡 Business Objective & Core Features

The project addresses the need for light, developer-friendly cloud utilities in medical imaging without requiring heavy
local software installations.

* **Metadata Extraction:** Parse, validate, and search DICOM header attributes (e.g., Modality detection across CT, MR, PT, US) in memory.
* **Format Conversion (In Progress):** Transform complex DICOM series into NIfTI format for medical AI/ML research pipelines.
* **Data Visualization & Analytics (Planned):** On-the-fly slice rendering and series metadata correlation studies.
* **Pay-Per-Use Monetization:** Integrated with RapidAPI header verification and Stripe payment processing for automated subscription management.

---

### 🔒 Security, HIPAA & GDPR Compliance Strategy

Handling Protected Health Information (PHI) requires strict privacy boundaries, which are being taken into consideration
during the development of the project:

* **Zero-Storage Architecture:** DICOM datasets are processed strictly in memory (`tempfile`) and immediately purged upon request completion. No medical images or metadata are persisted to disk or database storage.
* **PHI Protection:** System-level boundaries prevent sensitive patient data exposure, keeping operations focused solely on technical metadata and image arrays.
* **Zip Bomb & Path Traversal Defenses:** Robust archive validation enforces strict file count (`MAX_FILES`) and uncompressed size (`MAX_TOTAL_SIZE_MB`) caps alongside `os.path.realpath` checks to mitigate Zip Slip attacks.
* **Timing-Attack Proof Authentication:** RapidAPI proxy headers are verified using constant-time `hmac.compare_digest` checks.

---

### 🛠️ Infrastructure & Tech Stack

* **Backend Engine:** Python 3.11, FastAPI, Pydantic, PyDICOM
* **Cloud Infrastructure:** Google Cloud Platform (GCP) — Kubernetes Engine (GKE) Autopilot for auto-scaling and cost efficiency
* **Distribution & Monetization:** RapidAPI, Stripe
* **Testing & Quality Control:** Pytest, Custom TestClient fixtures, Docker, GNU Make

---

### 📂 Project Structure

```text
├── app/
│   ├── dependencies.py          # Security & RapidAPI auth dependencies
│   ├── main.py                  # App entrypoint & GKE health check endpoints
│   ├── routers/                 # Modular APIRouters (DICOM Toolkit, Metadata)
│   └── utils/                   # Memory-safe DICOM, ZIP, and logging helpers
│   └── tests/                   # Unit, integration (to be done), and security test suite
├── Dockerfile                   # Production container definition for GKE
├── cloudbuild.yaml              # YAML to specify build steps for GCP
├── Makefile                     # Automation tasks (local execution, docker, tests)
├── requirements.txt             # Production dependencies
└── requirements-dev.txt         # Development & test environment libraries
