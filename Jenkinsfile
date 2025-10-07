pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose -f docker-compose.yml build'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
    }
}
