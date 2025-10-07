pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'pwd'
                    sh 'ls -la'
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
