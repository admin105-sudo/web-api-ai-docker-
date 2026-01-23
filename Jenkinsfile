pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        EC2_HOST = "98.84.15.229"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/admin105-sudo/web-api-ai-docker-.git'
            }
        }

        stage('Build & Docker Compose') {
            steps {
                sh 'docker compose build'
                sh 'docker compose push'    // optional if using registry
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@$EC2_HOST "
                    cd /path/to/app
                    docker compose pull
                    docker compose up -d
                    "
                    '''
                }
            }
        }
    }
}
