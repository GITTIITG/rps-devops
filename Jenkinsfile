pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'pwd && ls -la'
                sh 'docker-compose build'
            }
        }
        stage('Run Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
