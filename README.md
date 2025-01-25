# 🌟 End-to-End ML Project (Visa-Approval-Prediction)

## 🛠️ Tech Stack
✨ **Technologies Used**:  
- 🐍 **Python**  
- 🐋 **Docker**  
- 🤖 **GitHub Actions**  
- ☁️ **AWS (EC2, ECR)**  
- 🍃 **MongoDB**  
- 📊 **Evidently**  
- ⚡ **FastAPI**  
- 📈 **Scikit-learn**

---

## 🛠️ Git Commands
```bash
git add .
git commit -m "Updated"
git push origin main
```
---

## 🚀 How to run
```bash
conda create -p visa python=3.8 -y
conda activate visa
pip install -r requirements.txt
python app.py
```
---

## 🔄 Workflow
- *📝 constant*
- *⚙️ config_entity*
- 📦 artifact_entity
- 🛠️ component
- 🔗 pipeline
- 🚀 app.py / demo.py

## 🌐 Export Environment Variables

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```
---

## 📦 AWS-CICD-Deployment-with-Github-Actions

### 🏁 Steps:

1️⃣ **Login to AWS Console**  
   Navigate to your AWS account and sign in.  


2️⃣ **Create IAM User for Deployment**  
   **Permissions Needed:**  
   - 🖥️ **EC2 Access**: For managing virtual machines.  
   - 📦 **ECR**: Elastic Container Registry to store Docker images.

3️⃣ **Create ECR Repository**  
   Create a repository in ECR to store your Docker images.  

4️⃣ **Create EC2 Machine (Ubuntu)**  
   Launch an EC2 instance with Ubuntu as the operating system.  

5️⃣ **Install Docker in EC2 Machine**  
   Install Docker on the EC2 machine to manage containerized applications.  


```bash
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
6️⃣ **Configure EC2 as Self-Hosted Runner**
- Navigate to: Settings > Actions > Runners > New self-hosted runner
- Choose OS and follow the commands step-by-step.
  
7️⃣ **Setup GitHub Secrets**
Add the following secrets in your repository:

-🔑 AWS_ACCESS_KEY_ID
-🔑 AWS_SECRET_ACCESS_KEY
-🌍 AWS_DEFAULT_REGION
-📦 ECR_REPO

## 💡 Deployment Workflow Overview
- 1. 🛠️ Build the Docker image of the source code.
- 2. 📤 Push the Docker image to ECR.
- 3. 🖥️ Launch the EC2 instance.
- 4. 📥 Pull the image from ECR on EC2.
- 5. 🚀 Run the Docker container on EC2.
 
## 🔐 IAM Policies Required:
- 📦 AmazonEC2ContainerRegistryFullAccess
- 🖥️ AmazonEC2FullAccess

