#!/bin/bash

# エラーが発生した時点でスクリプトを停止する
set -e

# 1. Dockerイメージをビルドする
echo "Building Docker image..."
docker build -t my-flask-app:latest .

# 2. Minikubeにイメージをロードする
echo "Loading image into Minikube..."
minikube image load my-flask-app:latest

# 3. Kubernetesマニフェストを適用する
echo "Applying Kubernetes manifests..."
kubectl apply -f k8s/

# 完了メッセージ
echo "Deployment initiated! It may take a moment for the pods to be up and running."
echo "Check status with: kubectl get pods"
