
node {
  checkout scm
  def myImage = docker.build('registry.digitalocean.com/my-container-hub/pichacky:by_jenkins')
  stage('Test image') {
    myImage.inside {
      sh 'python -m unittest'
    }
  }

  stage('Publish image to DO') {
    docker.withRegistry('https://registry.digitalocean.com', 'do-registry-creds') {
      myImage.push()
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
