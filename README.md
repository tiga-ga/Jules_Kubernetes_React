# K8s React Flask App

This project is a simple Flask application designed to be deployed on a local Kubernetes cluster (Minikube).

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Deployment

A helper script is provided to automate the build and deployment process.

1.  **Make the script executable:**
    
    First, give the deployment script execution permissions.
    
    ```sh
    chmod +x deploy.sh
    ```

2.  **Run the deployment script:**
    
    This script will:
    - Build the Docker image (`my-flask-app:latest`).
    - Load the image into your Minikube cluster.
    - Apply the Kubernetes configurations from the `k8s/` directory.
    
    ```sh
    ./deploy.sh
    ```

## Verifying the Deployment

To check the status of your pods and ensure they are running:

```sh
kubectl get pods
```

You should see the `flask-app` pods with a `Running` status.

## Accessing the Service

To access the application from your browser, you can expose the service through Minikube:

```sh
minikube service flask-app-service
```

This command will automatically open the application in your default web browser.

## Cleaning Up

To delete all the resources created by this deployment:

```sh
kubectl delete -f k8s/
```
