pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        EC2_IP = "98.84.15.229"
        GIT_REPO = "https://github.com/admin105-sudo/web-api-ai-docker-.git"
    }

    stages {

        stage('Build & Docker Compose') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@$EC2_IP "
                    cd /home/ubuntu/web-api-ai-docker-
                    docker compose down
                    docker compose up -d
                    "
                    '''
                }
            }
        }
    }
}
