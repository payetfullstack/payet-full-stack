# Google Cloud Platform (GCP) Infrastructure & FinOps Architecture

This document outlines the cloud infrastructure design, security access controls, CI/CD pipeline strategies, and FinOps
(Cost Optimization) policies governing the multi-API SaaS microservice deployment on **Google Cloud Platform (GCP)**.
The project was created for a personal project, so cost zero was a must at the begining.

---

## Infrastructure Overview

The application is deployed on **Google Cloud Kubernetes Engine (GKE) Autopilot**, providing containerized
orchestration with automatic cluster management and pay-per-pod resource allocation.

```text
 ┌─────────────────┐       ┌───────────────────────┐       ┌───────────────────────────┐
 │ Cloud Build     │ ────> │ Artifact Registry     │ ────> │ GKE Autopilot Cluster     │
 │                 │ Build │ (Retention: Max 2 img)│ Deploy│ (Region: us-central1)     │
 └─────────────────┘       └───────────────────────┘       └───────────────────────────┘
```

## FinOps & Cost Optimization Strategy

To ensure zero cost overhead during operation and stay strictly within GCP Free Tier / Monthly Credit boundaries
($74.40/month GKE Autopilot credit), strict resource constraints and quota limits are enforced:
1. Compute & GKE Constraints
- Deployment Mode: GKE Autopilot (Region: us-central1).
- Resource Quotas: Constrained to 1 vCPU and 1 GB RAM per pod instance.
- Cluster Cap: Restricted to 1 single cluster (autopilot-cluster-my-free-plan).

2. CI/CD & Cloud Build Optimization
- Free Tier Allowance: 2,500 build-minutes/month (e2-standard-2).
- Lean Build Pipeline (cloudbuild.yaml): Unit testing and linting are executed locally and during pre-commit hooks—never inside Cloud Build. This keeps image build times minimal and conserves build-minutes.
- Concurrency Cap: Concurrent builds restricted to 1 parallel build (Non-regional Default Pool) to eliminate accidental parallel build burn-rate.

3. Container Image Retention (Artifact Registry)
- Storage Limit: 0.5 GB per month limit (my-artifacts-registry).
- Cleanup Strategy: Enforced maximum of 2 active container images with automated pruning for images older than 7 days.

## Security & Identity Access Management (IAM)

Principle of Least Privilege (PoLP) is enforced across service accounts to avoid granting administrative broad permissions:

Custom Service Account: cloudbuild-deploy-trigger-sa@adria-personal-project.iam.gserviceaccount.com

Assigned IAM Roles (Minimal Required):
- `roles/artifactregistry.writer` — For pushing container images.
- `roles/container.developer` — For deploying manifests to GKE.
- `roles/logging.logWriter` — For writing build execution logs.

 Security Policy: Avoids using the default Compute Engine SA (...-compute@developer.gserviceaccount.com) due to over-privileged default scopes.

## Cluster Management Shortcuts

For developers or operators managing the cluster locally via gcloud and kubectl (project name kept secret, please check the private documentation for more info):

```Bash
# Set GCP Project and Region
gcloud config set project adria-personal-project
gcloud config set compute/region us-central1

# Fetch GKE Autopilot Credentials
gcloud container clusters get-credentials autopilot-cluster-my-free-plan \
    --region us-central1 \
    --project adria-personal-project

# Verify Pod Health
kubectl get pods
```
