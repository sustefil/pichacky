pipeline {
    agent { dockerfile true }

    stages {
        stage('Test') {
            steps {
                sh '''
                python -m unittest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker-compose down && docker-compose up -d
                '''
            }
        }
    }
}
