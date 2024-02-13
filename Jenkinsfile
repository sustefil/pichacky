
node {
  checkout scm
  def myImage = docker.build 'pichacky:${env.BUILD_ID}'
  myImage.inside {
    sh 'python -m unittest'
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
