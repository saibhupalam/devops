pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker build -t username/reg_roll_frontend ./frontend'
                sh 'docker build -t username/reg_roll_backend ./backend'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'docker push username/reg_roll_frontend'
                sh 'docker push username/reg_roll_backend'
            }
        }
    }
}