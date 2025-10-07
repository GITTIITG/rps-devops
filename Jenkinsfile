pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Run Application') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
    }
}
