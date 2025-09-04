# 🚗 Vehicle Insurance Fraud Detection: An End-to-End MLOps Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Cloud-AWS-orange.svg" alt="AWS">
  <img src="https://img.shields.io/badge/Database-MongoDB-green.svg" alt="MongoDB">
  <img src="https://img.shields.io/badge/CI/CD-GitHub_Actions-blueviolet.svg" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Containerization-Docker-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/Deployment-EC2-yellow.svg" alt="EC2">
</p>

---

An **industry-standard, end-to-end MLOps project** demonstrating a production-ready pipeline for detecting fraudulent vehicle insurance claims.  

This repository showcases **advanced MLOps practices**, including automated data pipelines, model lifecycle management, and CI/CD-driven cloud deployment.  

It is designed to highlight **proficiency in data engineering, machine learning automation, and cloud-native deployment** to industry recruiters and stakeholders.  

---

## 🏛️ High-Level System Architecture

This diagram illustrates the flow of data from ingestion to prediction, including the automated CI/CD pipeline for deployment.
<img width="889" height="840" alt="Workflow" src="https://github.com/user-attachments/assets/d14f7784-4fc4-422a-aa7a-5c2b5d30741e" />


## 🚀 Key Features & Technical Highlights
1. **End-to-End ML Pipeline Automation** – From data ingestion to model deployment, ensuring reproducibility and efficiency.
2. **Scalable Data Handling** – Uses MongoDB Atlas for robust and scalable data storage.
3. **Cloud-Native Model Management** – AWS S3 for centralized, versioned model registry.
4. **CI/CD for ML** – GitHub Actions + Docker for automated testing, building, and deployment.
5. **Infrastructure as Code** – Deployment codified in GitHub workflows for consistency.
6. **Robust Monitoring & Traceability** – Integrated logging and exception handling.
7. **Interactive Prediction API** – FastTAPI-based app for real-time fraud detection.
8. **Modular Codebase** – Clean separation for data, models, and application logic.

## 🛠️ Tech Stack & Tools

| Category                 | Technologies                                      |
|---------------------------|--------------------------------------------------|
| Programming               | Python 3.10                                      |
| Data & Model Storage      | MongoDB Atlas, AWS S3                            |
| ML Lifecycle              | Scikit-learn, Pandas, NumPy                      |
| CI/CD & Automation        | GitHub Actions, Docker, AWS ECR, Self-Hosted Runners |
| Cloud & Deployment        | AWS EC2, FastAPI                                 |
| Code Quality & Packaging  | pyproject.toml, setup.py                         |

## 📖 Project Workflow Breakdown
- **Data Ingestion** – Fetches data from MongoDB, validates, and splits into train/test.
- **Data Validation** – Enforces schema integrity (schema.yaml) to ensure clean inputs.
- **Data Transformation** – Feature engineering + preprocessing for ML training.
- **Model Training** – Trains ML model & logs metrics.
- **Model Evaluation** – Compares with production model and promotes only if better.
- **Model Pusher** – Pushes validated models to AWS S3 (Model Registry).
- **Prediction Service** – FastAPI app loads latest model for real-time predictions.

## ⚙️ Local Setup and Execution
✅ Prerequisites
1. Python 3.10
2. Conda
3. MongoDB Atlas account
4. AWS account with IAM user credentials

## 🔧 Installation
```
# Clone Repository
git clone https://github.com/your-username/Vehicle-Insurance-MLOPS-Project.git
cd Vehicle-Insurance-MLOPS-Project

# Create Conda Environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# Install Dependencies
pip install -r requirements.txt
```

## 🌍 Configure Environment Variables
```
# MongoDB
export MONGODB_URL="mongodb+srv://<username>:<password>@..."

# AWS
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

## ▶️ Run Pipelines
```
# Training Pipeline
python demo.py

# Launch Prediction API
python app.py
Access app at: http://127.0.0.1:5000
```

## 🔄 CI/CD and Deployment Automation
The CI/CD pipeline (.github/workflows/aws.yaml) automates deployment to AWS EC2.

- Trigger – Runs on git push to main branch.
- Self-Hosted Runner – EC2 instance listens for jobs.
- Build, Tag & Push – Docker image pushed to AWS ECR.
- Deployment – EC2 pulls the latest image & runs container on port 5080.

## 🔑 Required GitHub Secrets
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO (ECR Repository URI)

## 📈 Business Impact & Use Case
This project provides a scalable & automated solution for the insurance industry:
- 💰 Reduce Financial Losses – Avoid payouts on fake claims.
- ⚡ Improve Efficiency – Automates manual review process.
- 📊 Enhance Decisions – Data-driven insights for claims adjusters.

## 🌟 Future Enhancements
- 📉 Advanced Monitoring – Use Evidently AI or Grafana for drift detection.
- 🔁 Automated Retraining – Trigger retraining when performance drops.
- 🧪 A/B Testing – Safely deploy new models alongside production ones.
- 🏗️ Infrastructure as Code (IaC) – Use Terraform or AWS CDK for reproducible cloud infra.



