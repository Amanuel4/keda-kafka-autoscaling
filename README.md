# Kubernetes Event-Driven Autoscaling (KEDA) with Apache Kafka (KRaft)

This repository provides a complete proof-of-concept for **event-driven autoscaling in Kubernetes using KEDA and Apache Kafka (KRaft mode)**.

Instead of relying on CPU or memory metrics, this system scales workloads dynamically based on **Kafka consumer lag**, enabling true event-driven elasticity for streaming workloads.

---

## 🏗️ Architecture Overview

This solution uses:

- **Apache Kafka (KRaft mode via Strimzi 4.2.0)** as the event backbone
- **KEDA (Kubernetes Event-Driven Autoscaler)** as the scaling controller
- **Kafka consumer lag** as the scaling signal
- Kubernetes **Horizontal Pod Autoscaler (HPA)** integration for scaling consumer workloads

### How it works

1. Producers publish messages to Kafka topics.
2. Consumers process messages in a consumer group.
3. KEDA continuously monitors consumer lag using Kafka metrics.
4. When lag exceeds a threshold:
   - KEDA triggers HPA
   - Kubernetes scales up consumer pods
5. When lag decreases:
   - Pods are scaled down automatically

This enables scaling based on **real workload demand**, not infrastructure metrics.

---

## ⚙️ Prerequisites

Before deploying, ensure you have:

- A running Kubernetes cluster (Tanzu, OpenShift, kind, etc.)
- `kubectl` configured with cluster-admin access
- Docker or compatible container runtime
- **Strimzi Kafka Operator installed**
- **KEDA installed in the cluster**

---

## 📦 Clone the Repository

```bash
git clone https://github.com/Amanuel4/keda-kafka-autoscaling.git
cd keda-kafka-autoscaling