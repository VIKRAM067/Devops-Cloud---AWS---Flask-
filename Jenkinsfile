pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VIKRAM067/Devops-Cloud---AWS---Flask-.git'
            }
        }

        stage('Deploy with Docker') {
            steps {
                sh 'docker stop flask_app || true'
                sh 'docker rm flask_app || true'
                sh 'docker build -t flask_app .'
                sh 'docker run -d -p 5000:5000 --name flaskApp_Container flask_app'
            }
        }

    }
}

