pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Satishmahakalkar/ML_Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary Python packages
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your test suite (adjust to your test framework)
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image for deployment
                sh 'docker build -t ml_project_image .'
            }
        }

        stage('Deploy') {
            steps {
                // Stop any existing container and deploy the new one
                sh '''
                docker stop ml_project_container || true
                docker rm ml_project_container || true
                docker run -d --name ml_project_container -p 5000:5000 ml_project_image
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
