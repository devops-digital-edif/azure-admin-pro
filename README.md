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

```bash
ssh <your-user>@<your-vm-ip>
