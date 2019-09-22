pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Testing will be done'
        sh 'pip install -r requirements.txt && pip install pytest && pip install pylint'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
  }
}