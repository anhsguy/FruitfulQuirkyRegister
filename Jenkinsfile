pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                script {
                    checkout scm
                }
            }
        }
        
        stage('Run Python Code') {
            steps {
                // Run Python code
                script {
                    sh 'python3 --version'
                    sh 'python3 main.py'
                    sh 'python3 testCSV_data_reading.py'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Python code execution successful!'
        }
        failure {
            echo 'Failed to run Python code!'
        }
    }
}
