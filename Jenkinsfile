pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_REPO = "silviacaser/example-voting-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', credentialsId: 'github-credentials', url: 'https://github.com/SilviaCaser1/VotingApp.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_REPO .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push $DOCKER_REPO'
            }
        }
    }
}
