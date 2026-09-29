# Dockerizing FastAPI with Postgres, Uvicorn, and Traefik

### Development

Build the images and spin up the containers:

```sh
$ docker compose up -d --build
```

Test it out:

1. [http://fastapi.localhost:8008/](http://fastapi.localhost:8008/)
1. [http://fastapi.localhost:8081/](http://fastapi.localhost:8081/)



## Cloud Deployment

This project is deployed on AWS using Kubernetes (k3s) with full CI/CD automation.

**Live:** https://devops-luca.click

### Stack

| Area | Tool |
|---|---|
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Orchestration | k3s (Kubernetes) on AWS EC2 t3.small |
| Registry | AWS ECR |
| Proxy / TLS | Traefik + Let's Encrypt |
| Monitoring | CloudWatch + Fluent Bit |

### Prerequisites

- AWS CLI configured (`aws configure`)
- Terraform installed
- Docker installed

### Infrastructure setup

```sh
cd infra
terraform init
terraform apply
```

Provisions: EC2 t3.small with k3s auto-installed, S3 remote state backend, ECR repository, Security Groups.

### Environments

| Environment | Namespace | Deploy trigger |
|---|---|---|
| Staging | `staging` | Push to `staging` branch |
| Prod | `prod` | Manual `workflow_dispatch` on `main` |

### CI/CD Pipeline

Every push to `develop`, `staging` or `main` runs:

1. Run pytest tests (with PostgreSQL service container)
2. Build Docker image
3. Scan image with Trivy (HIGH/CRITICAL CVEs reported)
4. Push to AWS ECR

Deployment to staging triggers automatically on push to `staging`. Production deployment requires manual approval via GitHub Actions `workflow_dispatch`.

### Tear down

```sh
cd infra
terraform destroy
```