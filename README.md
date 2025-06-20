## This is Network Security Project for phishing data. This project is end-to-end

### This project includes pipeline, data ingestion from MongoDB, data validation, data tranformation and model training and creating simple frontend using fastapi

### Aim of this project is not to get best model, but to create end-to-end project with MLflow experiment tracking and deploying it on AWS using github actions for CI/CD

### push.py pushes update data to MongoDB before data ingestion

### This also includes github actions workflows and pushing final models to s3 and creating image on ECR and hosting on EC2 instance (However, github action might fail as buckets, ecr and ec2 instance has bee deleted after testing for cost contraint)

### Before deployment, github repo was also linked to dagshub for MLflow experiment tracking

### Network data folder has original data. "networksecurity" has all core files. "app.py" has frontend part. "main.py" has entire workflow for model experimentation