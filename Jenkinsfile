
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Kaustubhrd/student-complaint-register.git'
            }
        }

        stage('Check Project Files') {
            steps {
                sh 'test -f Dockerfile'
                sh 'test -f requirements.txt'
                sh 'test -f app.py'
                echo 'Project files verified successfully.'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t kaustubhrd26/student-complaint-register:v1 .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login \
                          -u "$DOCKERHUB_USER" --password-stdin
                        docker push kaustubhrd26/student-complaint-register:v1
                        docker logout
                    '''
                }
            }
        }
    }
}
