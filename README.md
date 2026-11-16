# AWS DevOps Platform

A hands-on DevOps project that packages a Flask application with
PostgreSQL, automates build and deployment with Jenkins, publishes the
container image to Docker Hub, and deploys the application to a local
Kubernetes cluster.

> **Deployment scope:** The application and Kubernetes environment were
> run locally using Docker Desktop and kind. This project has not been
> deployed to AWS.

## Project Overview

This project demonstrates an end-to-end local CI/CD workflow:

1.  Develop a Flask application with health-check endpoints.
2.  Run the application and PostgreSQL using Docker Compose.
3.  Trigger a Jenkins pipeline from GitHub using a webhook.
4.  Build a Docker image and push it to Docker Hub.
5.  Deploy the image to Kubernetes.
6.  Expose the application through a Kubernetes Service and NGINX
    Ingress.

## Architecture

``` text
Developer
   |
   v
GitHub repository
   |
   | GitHub Webhook
   v
Jenkins Pipeline
   |
   +--> Checkout source
   +--> Build Docker image
   +--> Push image to Docker Hub
   +--> Deploy / update application
   |
   v
Docker Hub
   |
   v
Kubernetes (Docker Desktop / kind)
   |
   +--> Deployment (3 replicas)
   +--> Service
   +--> NGINX Ingress
   |
   v
http://aws-devops.local
```

## Technology Stack

-   **Application:** Python, Flask
-   **Database:** PostgreSQL
-   **Containers:** Docker, Docker Compose
-   **CI/CD:** Jenkins, GitHub Webhooks
-   **Image Registry:** Docker Hub
-   **Orchestration:** Kubernetes (local kind cluster)
-   **Ingress:** NGINX Ingress Controller
-   **Configuration:** YAML, Kubernetes ConfigMaps and Secrets
-   **Storage:** Kubernetes PersistentVolumeClaim
-   **Source Control:** Git, GitHub

## Implemented Features

-   Flask application endpoints:
    -   `/` --- application status
    -   `/health` --- application health check
    -   `/db-health` --- PostgreSQL connectivity check
-   Dockerfile-based application image build.
-   Docker Compose setup for Flask and PostgreSQL.
-   Jenkins pipeline for source checkout, image build, Docker Hub push,
    deployment and health check.
-   GitHub webhook integration to trigger Jenkins builds.
-   Kubernetes Deployment configured with three replicas.
-   Kubernetes Service to expose the application inside the cluster.
-   NGINX Ingress host routing using `aws-devops.local`.
-   ConfigMap and Secret environment-variable injection.
-   PersistentVolumeClaim (PVC) storage test.
-   Liveness and readiness probes.
-   Kubernetes self-healing and rolling-update practice.

## Run Locally with Docker Compose

Prerequisites:

-   Docker Desktop with Docker Compose
-   Git

Clone the repository:

``` bash
git clone https://github.com/yashwadakte/aws-devops-platform.git
cd aws-devops-platform
```

Start the application and database:

``` bash
docker compose up -d --build
```

Check running services:

``` bash
docker compose ps
```

Test the application:

``` bash
curl http://localhost:5002/
curl http://localhost:5002/health
curl http://localhost:5002/db-health
```

Stop the services:

``` bash
docker compose down
```

> If your local Compose file uses different host ports, use the port
> mappings shown by `docker compose ps`.

## Jenkins CI/CD

The Jenkins pipeline is configured to:

1.  Check out the `main` branch from this GitHub repository.
2.  Build the application Docker image.
3.  Verify the built image.
4.  Authenticate to Docker Hub using a Jenkins credential.
5.  Push the image to Docker Hub.
6.  Deploy the application container.
7.  Run an HTTP health check.

Docker Hub image:

``` text
yashwadakte/aws-devops-app:v1
```

**Credential safety:** Store Docker Hub credentials in Jenkins
Credentials. Do not commit passwords, access tokens, `.env` files
containing secrets, or kubeconfig files to Git.

## Kubernetes

The application was deployed to a local Kubernetes cluster using Docker
Desktop / kind.

Implemented Kubernetes resources and capabilities:

-   Deployment with 3 replicas
-   Service
-   NGINX Ingress
-   ConfigMap
-   Secret
-   PersistentVolumeClaim
-   Liveness and readiness probes

Useful verification commands:

``` bash
kubectl get nodes
kubectl get deployments,pods,services,ingress,pvc
kubectl get ingress
kubectl rollout status deployment/aws-devops-app
```

The Ingress host configured for local testing is:

``` text
aws-devops.local
```

For local hostname resolution on Windows, add this line to the hosts
file (administrator permissions required):

``` text
127.0.0.1 aws-devops.local
```

Test the application:

``` bash
curl http://aws-devops.local/
curl http://aws-devops.local/health
```

## Repository

GitHub: https://github.com/yashwadakte/aws-devops-platform

Docker Hub image: https://hub.docker.com/r/yashwadakte/aws-devops-app

## Limitations and Next Steps

-   This is a local hands-on implementation; no AWS infrastructure
    deployment is claimed.
-   The Kubernetes cluster runs locally, not on Amazon EKS.
-   Terraform-based AWS provisioning and deployment to AWS services can
    be added when an active AWS account is available.
-   Add screenshots of successful Jenkins builds, Docker Hub image tags,
    Kubernetes resources and health-check responses if you want visual
    evidence in the repository.

## Author

Yash Wadakte
