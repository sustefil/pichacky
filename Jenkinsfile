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
            sh '''
            docker-compose down && docker-compose up -d
            '''
        }
    }
}
