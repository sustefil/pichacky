
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
}

node('jenkins-agent-node') {
    stage('Verify Kubernetes context') {
        sh '''
            CTX=$(kubectl config current-context)
            [[ "$CTX" == "do-fra1-pichacky-k8s-cluster" ]] || exit 1
        '''
    }
    stage('Redeploy Kubernetes') {
        sh 'kubectl rollout restart statefulset pichacky-set'
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
