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
                dir("${WORKSPACE}") { // Ensure we are in Jenkins workspace
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Application') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
