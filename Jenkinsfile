pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing will be done'
        sh '''yum install -y python-pip
pytest'''
      }
    }
  }
}