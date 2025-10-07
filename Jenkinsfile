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
                sh 'pwd && ls -la' // DEBUG: Shows where we are and what files exist
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
