pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'python3 --version'
                    sh 'python3 -m venv venv' // Create a virtual environment named 'venv'
                    sh 'source venv/bin/activate' // Activate the virtual environment
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 testCSV_data_reading.py'
                    sh 'deactivate' // Deactivate the virtual environment
                }
            }
        }
    }
}
