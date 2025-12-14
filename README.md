# 🚀 Flask Application Deployment: End-to-End DevOps & Cloud Project

This repository documents a foundational **DevOps and Continuous Integration/Continuous Deployment (CI/CD)** project. The goal is not to showcase complex Python code but to demonstrate practical, hands-on experience in moving a simple application from source code (GitHub) to a running service in the Cloud (AWS EC2) using an automated pipeline.

This project focuses on **process, automation, and deployment**—the core pillars of a modern Data Engineering and MLOps environment.

---

## 🎯 Project Objectives (The Big Learning)

This project is a tangible demonstration of the following real-world DevOps practices:

* **CI/CD Automation:** Understanding and building an end-to-end pipeline using **Jenkins**.
* **Containerization:** Using **Docker** to package the application and its dependencies for reliable deployment.
* **Infrastructure:** Learning how **AWS EC2** hosts both the automation server (Jenkins) and the final application container.
* **Networking & Security:** Configuring **AWS Security Groups** to expose specific services (SSH, Jenkins, Flask App) securely.
* **Linux Fundamentals:** Executing commands and managing services on an **Ubuntu** server.
* **Troubleshooting:** Gaining real experience debugging issues across the entire stack (network, Docker, Jenkins jobs).

---

## 🛠️ Tools & Technologies Used

| Category | Tools | Purpose in this Project |
| :--- | :--- | :--- |
| **Code & App** | Python, Flask | The simple application to be deployed. |
| **Containerization** | Docker | Packaging the application and its runtime environment. |
| **Automation (CI/CD)** | Jenkins | The central server for automating the build, test, and deployment process. |
| **Source Control** | Git & GitHub | Managing and versioning the source code and configuration files. |
| **Cloud Infrastructure**| AWS EC2 (t3.micro, Ubuntu) | Hosting the entire environment (Jenkins + Dockerized App). |
| **OS** | Linux (Ubuntu) | The base operating system for the cloud host and pipeline execution. |

---

## ☁️ Cloud Setup (AWS EC2)

The entire pipeline and application run on a single EC2 instance.

### Instance Details
* **Instance Type:** `t3.micro` (Suitable for cost-effective development/testing)
* **OS:** `Ubuntu`
* **Purpose:** Hosts the Jenkins CI/CD server and the final Docker application container.

### Security Group Configuration (Inbound Rules)
The Security Group must be configured to allow external access to the necessary services:

| Port | Protocol | Purpose |
| :---: | :---: | :--- |
| **22** | TCP | SSH access to the EC2 instance (for management). |
| **80** | TCP | HTTP access (optional, if using a proxy or web server). |
| **443** | TCP | HTTPS access (optional, for secure connections). |
| **8080** | TCP | Access to the **Jenkins UI** (the CI/CD server). |
| **5000** | TCP | Access to the final **Flask Application**. |

---

## 🐋 Local Docker Commands (Development Testing)

These commands are used to test the container locally before deploying via Jenkins.

| Command | Purpose |
| :--- | :--- |
| `docker build -t flask_app .` | Builds the Docker image from the `Dockerfile` and tags it as `flask_app`. |
| `docker run -d -p 5000:5000 --name flaskApp_Container flask_app` | Runs the container in detached mode (`-d`), mapping port 5000 on the host to port 5000 inside the container. |
| `docker ps` | Lists all currently running Docker containers. |
| `docker logs flaskApp_Container` | Displays the output and error logs from the running application container. |

---

## ⚙️ Jenkins Setup & CI/CD Pipeline

Jenkins is the automation engine for this project. It fetches the code, builds the container, and deploys it.

### Initial Setup on EC2

```bash
# Enable and start the Jenkins service
sudo systemctl enable jenkins
sudo systemctl start jenkins

# Check the status to ensure it's running
sudo systemctl status jenkins
