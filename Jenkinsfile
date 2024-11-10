pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Satishmahakalkar/ML_Project.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add build commands here if any
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here if any
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                // Add deployment steps here
            }
        }
    }
}
