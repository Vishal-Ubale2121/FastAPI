pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQubeServer'
        DOCKER_IMAGE = 'fastapi-app:latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Vishal-Ubale2121/FastAPI.git'
            }
        }

        stage('Verify Python & pip') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version'
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe" install -r requirements.txt'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    bat 'sonar-scanner'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Docker Cleanup') {
            steps {
                bat 'docker rm -f fastapi-container || exit 0'
            }
        }

        stage('Docker Run') {
            steps {
                bat 'docker run -d -p 8000:8000 --name fastapi-container %DOCKER_IMAGE%'
            }
        }
    }
}
