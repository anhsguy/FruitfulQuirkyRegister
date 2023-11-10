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
                    // sh 'pip3 install -r requirements.txt'
                    sh 'python3 your_python_script.py'
                }
            }
        }
    }
}
