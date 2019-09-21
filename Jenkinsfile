pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing will be done'
        sh '''apt-get install -y python-pip
pytest'''
      }
    }
  }
}