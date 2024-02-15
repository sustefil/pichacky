
node {
  checkout scm
  def myImage = docker.build('registry.digitalocean.com/my-container-hub/pichacky:by_jenkins')
  stage('Run tests') {
    myImage.inside {
      sh 'python -m unittest'
    }
  }

  stage('Publish image to DigitalOcean') {
    docker.withRegistry('https://registry.digitalocean.com', 'do-registry-creds') {
      myImage.push()
    }
  }

  stage('Redeploy Kubernetes') {
    agent { label 'jenkins-agent-node' }
    sh 'kubectl version'
    }
  }
}

// pipeline {
//     agent { dockerfile true }
//
//     stages {
//         stage('Test') {
//             steps {
//                 sh '''
//                 python -m unittest
//                 '''
//             }
//         }
//     }
// }
