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
        stage('Test random image') {
            agent {
                docker { image 'node:20.11.0-alpine3.19' }
            }

            steps {
                sh 'node --version'
            }
        }
    }
}
