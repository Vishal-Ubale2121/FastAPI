pipeline{
    agent any

    environment{
        SONARQUBE = 'SonarQubeServer' // Name from Jenkins > Configure System
        DOCKER_IMAGE = 'fastapi-app:latest'
    }

    stages{
        stage('Clone Repository'){
            steps{
                git branch: 'main', url: 'https://github.com/Vishal-Ubale2121/FastAPI.git'
            }
        }

        stage('Install Dependencies'){
            steps{
                bat 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube Analysis'){
            steps{
                withSonarQubeEnv('SonarQubeServer'){
                    bat 'sonar-scanner'
                }
            }
        }

        stage('Docker Build'){
            steps{
                bat 'docker build -t $Docker_IMAGE .'
            }
        }

        stage('Docker Run'){
            steps{
                bat 'docker run -d -p 8000:8000 --name fastapi-container $DOCKER_IMAGE'
            }
        }

    }

    post{
        always{
            bat 'docker rm -f fastapi_container || true'
        }
    }
}
