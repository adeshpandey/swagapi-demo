pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('test') {
      steps {
        echo 'Testing will be done'
        sh '''pip install -r requirements\\
pytest'''
      }
    }
  }
}