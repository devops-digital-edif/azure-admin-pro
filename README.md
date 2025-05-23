# Azure Admin App - Deployment Guide

This document outlines the steps to deploy the Azure Admin App on an **Azure Virtual Machine (VM)**. The app uses **PostgreSQL** as the database and **Azure Blob Storage** for storing profile and course images.

---

## 🚀 Application Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Storage**: Azure Blob Storage
- **Web Server**: Gunicorn + Nginx (recommended for production)

---

## ☁️ Azure VM Setup

### 1. Provision Azure VM

- Go to Azure Portal → Virtual Machines → Create a VM
- Recommended image: **Ubuntu 20.04 LTS**
- Open inbound ports: **22 (SSH), 80 (HTTP), 443 (HTTPS)**
- Select or create a public IP and network security group

---

## 🛠️ Deployment Steps on VM

### 2. SSH into your VM
```
ssh <your-user>@<your-vm-ip>
```
### 3. Install Dependencies
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv postgresql postgresql-contrib  -y
```
### 4. Clone the Repository
```
git clone https://muralialakuntla3/azure-admin-project.git
cd azure_admin_app
```
### 5. Set up Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 6. Configure Environment Variables
- Create a .env file in the root project directory:
```
touch .env
nano .env
#### Paste the following:

DATABASE_URL=postgresql://<db_user>:<db_password>@localhost:5432/azure_admin_db
AZURE_STORAGE_CONNECTION_STRING=<your_azure_blob_conn_str>
SECRET_KEY=supersecretkey
```
### 7. Configure PostgreSQL

- goto azure cloud and create database under database section - azure_admin_db
- Update your .env:
```
DATABASE_URL=postgresql://youruser:yourpassword@localhost:5432/azure_admin_db
```
### 8. Create Storage Account and update Connection String
- login to azure portal
- create storage account
- goto access key section and copy the connection string
- Update your .env:
```
AZURE_STORAGE_CONNECTION_STRING=<your_azure_blob_conn_str>
```
- For SECRET_KEY use this command to generate secret
```
openssl rand -hex 32
```
- copy the secret and update in .env
```
SECRET_KEY=7c5c3f07ed4a4b11efffad65c5ed45bfaea804ecbfcab0469fbb7cc226df2bb5
```
### 9. Initialize the Database
```
python db_init.py
```
### 10. Run Flask App (Dev)
```
python run.py
```
- To keep it running in background (optional):
```
nohup python run.py &
```
------------------------------------------------------------------------------
# Promt used to create

## i want to build application for my azure admin class - be my developer as well as deployment engg

- through my application i want to show case how the database integrated with application - like use case of database (take PostgreSql DB)
- i want to use the storage account in the same application to store some user profile and other images
- use python to develop the application - i am gonna deploy it in VM,
- guide me to develop the application and give me deployment steps as well


## Application Info: 
Note: i want to perform CRUD operations in all the areas in the application
- i want to save user data like - Name, Email, Phone Number and the Profile Picture
   --> In database i want to store User details and in storage account i want to store Profile Picture
- i want to create some courses in application, my courses are Azure, AWS, DevOps, Python etc..
  --> i should be able to assign this courses to users
  --> in courses i want fields like - courseName, courseDescription, courseFee, courseDuration, courseImage
  --> course Images should store in storage account
- i need admin console to manage Users, Courses and assigning courses to users and need Users console to see their courses
- The database schema need to create when ever i run the application automatically


### Give me everything in detailed manner, in first phase will see development and in phase will see the deployment.

- start with first phase - development




