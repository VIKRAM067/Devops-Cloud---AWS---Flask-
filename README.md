# 🚀 Flask Application Deployment: End-to-End DevOps & Cloud Project

This repository documents a foundational **DevOps and Continuous Integration/Continuous Deployment (CI/CD)** project.

## 🎯 About the Project

This project uses a very small Flask application, but the **Flask app itself is NOT the focus**.

The real purpose is to demonstrate hands-on experience and understanding of how applications move from source code to a running service in the cloud. This project focuses entirely on DevOps practices, automation, and deployment—not application complexity. This practical implementation is highly valuable for anyone looking to gain real-world experience with cloud deployments and CI/CD workflows.

---

## 🛠️ Tools & Technologies Used

| Category | Tools | Purpose in this Project |
| :--- | :--- | :--- |
| **Code & App** | Python, Flask | The application source code. |
| **Containerization** | Docker | Packaging the application and its runtime environment. |
| **Automation (CI/CD)** | Jenkins | The central server for automating the build, test, and deployment process. |
| **Source Control** | Git & GitHub | Managing and versioning the source code. |
| **Cloud Infrastructure**| AWS EC2 (t3.micro, Ubuntu) | Hosting the entire environment (Jenkins + Dockerized App). |
| **OS** | Linux (Ubuntu) | The base operating system for the cloud host. |

---

## ☁️ Cloud Setup & Infrastructure Details

The entire environment is hosted on a single **AWS EC2 instance** (`t3.micro`, Ubuntu OS).

---
## 🛠️ Step-by-Step Deployment Guide

This guide walks through the infrastructure setup, software installation, and pipeline creation necessary to deploy the Flask application. 

### I. AWS Infrastructure Setup

1.  **Create an EC2 Instance:**
    * Launch a new AWS EC2 instance.
    * Select the **Ubuntu** Operating System.
    * Choose the **`t3.micro`** instance type (Free Tier eligible).
    * Ensure you generate or select a Key Pair (`.pem` file) for SSH access.

2.  **Set Security Group (Networking):**
    * Configure the Inbound Rules of the Security Group attached to the EC2 instance to allow traffic on the following required ports:
        * **22 (SSH):** For connecting to the instance from your local machine.
        * **8080 (Jenkins):** For accessing the Jenkins web interface.
        * **5000 (Flask App):** For accessing the deployed application.
     
  <img width="1595" height="409" alt="Screenshot 2025-12-13 233645" src="https://github.com/user-attachments/assets/86d90277-089e-4d78-97f4-4153aa7a6c36" />

### II. Connect and Install Dependencies (Git, Docker, Java)

1.  **Connect to the AWS Instance:**
    * Use the Key Pair file (`.pem`) and the EC2 instance's Public IP address to connect via SSH from your local machine:
        ```bash
        ssh -i /path/to/your-key.pem ubuntu@<ec2-public-ip>
        ```
        <img width="1734" height="867" alt="image" src="https://github.com/user-attachments/assets/3e01d01e-f682-4ecb-8474-76195f542d6d" />

2.  **Install Git and Docker:**
    * **Update System Packages:**
        ```bash
        sudo apt update && sudo apt upgrade -y
        ```
    * **Install Git, Docker, and Docker Compose:**
        ```bash
        sudo apt install git docker.io docker-compose-v2 -y
        ```
    * **Start and Enable Docker:**
        ```bash
        sudo systemctl start docker
        sudo systemctl enable docker
        ```
    * **Add User to Docker Group (to run docker without sudo):**
        ```bash
        sudo usermod -aG docker $USER
        newgrp docker
        ```

3.  **Install Java (OpenJDK 17):**
    * Java is required to run the Jenkins automation server.
    ```bash
    sudo apt install openjdk-17-jdk -y
    ```

---

### III. Jenkins Installation and Setup

1.  **Add Jenkins Repository and Install:**
    * These commands add the Jenkins repository key, register the repository, update packages, and install Jenkins:
        ```bash
        curl -fsSL [https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key](https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key) | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
        echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] [https://pkg.jenkins.io/debian-stable](https://pkg.jenkins.io/debian-stable) binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
        sudo apt update
        sudo apt install jenkins -y
        ```

2.  **Start and Enable Jenkins Service:**
    ```bash
    sudo systemctl start jenkins
    sudo systemctl enable jenkins
    ```

3.  **Initial Jenkins Setup:**
    * **Retrieve the initial admin password:**
        ```bash
        sudo cat /var/lib/jenkins/secrets/initialAdminPassword
        ```
    * **Access the Jenkins dashboard at** `http://<ec2-public-ip>:8080`.
    * Paste the password, install suggested plugins, and create an admin user.

4.  **Grant Jenkins Docker Permissions:**
    * This crucial step allows the Jenkins user (which executes your pipeline) to build and run Docker containers on the EC2 host:
        ```bash
        sudo usermod -aG docker jenkins
        sudo systemctl restart jenkins
        ```

5.  **Create Dockerfile and Jenkinsfile:**
    * The project requires two key files in the repository root:
        * **`Dockerfile`**: Defines how the Flask application is containerized.
        * **`Jenkinsfile`**: Defines the CI/CD pipeline steps (get code, build Docker image, run container).


### IV. Configure and Build the Jenkins Pipeline

Once Jenkins is installed and granted Docker permissions, you must define the automation workflow using the web interface. 

1.  **Access the Dashboard:** Open your browser and navigate to the Jenkins dashboard: `http://<ec2-public-ip>:8080`.
2.  **Create a New Item:**
    * Click **"New Item"** (or **"Create a job"**).
    * Select **"Pipeline"** as the item type and click **"OK"**.
3.  **Configure the Pipeline:**
    * In the configuration screen, navigate to the **"Pipeline"** section at the bottom.
    * **Definition:** Change the selection from "Pipeline script" to **"Pipeline script from SCM"** (Source Code Management).
    * **SCM:** Select **"Git"**.
    * **Repository URL:** Enter the URL of your GitHub repository
    * **Credentials:** If your repository is private, you must add your GitHub credentials here.
    * **Branch Specifier:** Set this to `*/main` or `*/master` (or your primary branch name).
    * **Script Path:** Ensure this is set to the name of your pipeline file, typically **`Jenkinsfile`**.
4.  **Save the Configuration:** Click **"Save"** at the bottom of the page.
5.  **Build the Pipeline:**
    * Navigate back to your new pipeline job page.
    * Click **"Build Now"** on the left-hand menu. 
6.  **Verify Execution:**
    * Monitor the build progress in the **"Build History"** section.
    * Click on the running build number and select **"Console Output"** to see the logs.
  
    <img width="1918" height="836" alt="Screenshot 2025-12-13 233703" src="https://github.com/user-attachments/assets/560dd31f-d299-4a39-bf51-d8a0b85d23ea" />

---

### IV. Access the Flask App

* Once the Jenkins pipeline build status is **SUCCESS**, the container is running and exposed via the EC2 instance's public IP on port 5000.

* Access the deployed application in your browser: `http://<ec2-public-ip>:5000`

<img width="1919" height="962" alt="Screenshot 2025-12-13 233550" src="https://github.com/user-attachments/assets/75bc738d-3eff-44d4-94ed-467930865086" />



