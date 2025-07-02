# Real-Time Roadside Assistance (AWS - Serverless)

A scalable serverless data pipeline that ingests 50K roadside assistance events per second using Kinesis, processes them via Lambda, stores structured data in DynamoDB, and archives raw data to S3 with lifecycle policies (Glacier/IA).

## 📦 Architecture

- Kinesis Data Stream → Lambda → DynamoDB
- S3 archive bucket with lifecycle policy
- Terraform for IAC

## 🛠 Stack

- AWS Kinesis
- AWS Lambda (Python 3.9)
- AWS DynamoDB
- AWS S3 (IA & Glacier policies)
- Terraform

## 🚀 Deployment

```bash
chmod +x deploy.sh
./deploy.sh
```
