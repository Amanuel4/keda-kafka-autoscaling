#!/bin/bash
set -e

# Replace with your own docker container registry namespace
REGISTRY="<YOUR_REGISTRY>"

echo "Building components..."
docker build -t $REGISTRY/notification-generator:main ../producer
docker build -t $REGISTRY/notification-worker:main ../consumer

echo "Pushing images..."
docker push $REGISTRY/notification-generator:main
docker push $REGISTRY/notification-worker:main

echo "Applying manifests..."
kubectl apply -f ../k8s/infrastructure/kafka-nodepool.yaml
kubectl apply -f ../k8s/infrastructure/kafka-cluster.yaml
kubectl apply -k ../k8s/overlays/dev