pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        EC2_IP = "44.198.56.239"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/admin105-sudo/web-api-ai-docker-.git'
            }
        }

        stage('Run App on EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@${EC2_IP} '
                    cd /home/ec2-user &&
                    git pull &&
                    docker stop myapp || true &&
                    docker rm myapp || true &&
                    docker build -t myapp . &&
                    docker run -d -p 80:80 --name myapp myapp
                    '
                    """
                }
            }
        }
    }
}
