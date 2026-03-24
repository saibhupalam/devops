pipeline {
    agent any

    stages {
        stage('Build Frontend') {
            steps {
                sh 'docker build -t saibhupalam/devops_frontend ./frontend'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t saibhupalam/devops_backend ./backend'
            }
        }
    }
}