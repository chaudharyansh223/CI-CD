pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'echo "test"'
      }
    }

    stage('build') {
      parallel {
        stage('build') {
          steps {
            sh 'echo "build"'
          }
        }

        stage('parallel') {
          steps {
            sh 'echo "running parallel"'
          }
        }

      }
    }

    stage('deploy') {
      steps {
        sh 'echo "deploy to prod"'
      }
    }

  }
}