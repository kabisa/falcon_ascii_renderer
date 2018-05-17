projectId = "pablo-ascii-art-generator"

if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == null) {
  additionalBuildArgs = "--pull --no-cache"
} else {
  additionalBuildArgs = "--pull"
}

pipeline {
  agent none

  options {
    ansiColor("xterm")
  }

  stages {
    stage("Check out") {
      agent {
        label "webapps"
      }

      steps {
        checkout scm
      }
    }

    stage("Test") {
      agent {
        dockerfile {
          additionalBuildArgs "${additionalBuildArgs}"
          args "-u root"
          filename "dockerfiles/ci/Dockerfile"
        }
      }

      steps {
        sh "cd /app && pylint app tests && flake8 && pytest --cov=app"
      }
    }
  }
}
