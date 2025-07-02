#!/bin/bash

set -e

echo "Packaging Lambda..."
cd lambda
pip install -r ../requirements.txt -t .
zip -r ../lambda_function_payload.zip .
cd ..

echo "Initializing Terraform..."
terraform init

echo "Applying Infrastructure..."
terraform apply -auto-approve

echo "✅ Deployment Complete"
