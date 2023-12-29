pipeline {
    agent none

    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh '''
                python -m unittest
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                sh '''
                docker-compose down && docker-compose up -d
                '''
            }
        }
    }
}
