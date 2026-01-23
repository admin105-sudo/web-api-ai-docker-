pipeline {
    agent any

    environment {
        EC2_IP = "98.84.15.229"
        SSH_KEY = "/home/abi/ec2-key.pem"
        APP_NAME = "webapp"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/admin105-sudo/web-api-ai-docker-.git'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@$EC2_IP << EOF
                  docker stop $APP_NAME || true
                  docker rm $APP_NAME || true
                  docker build -t $APP_NAME:latest .
                  docker run -d -p 80:80 --name $APP_NAME $APP_NAME:latest
                EOF
                '''
            }
        }
    }
}
