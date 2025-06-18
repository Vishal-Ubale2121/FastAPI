pipeline{
    agent any

    environment{
        SONARQUBE = 'SonarQubeServer' // Name from Jenkins > Configure System
        DOCKER_IMAGE = 'fastapi-app:latest'
    }

    stages{
        stage('Clone Repository'){
            steps{
                git 'https://github.com/Vishal-Ubale2121/FastAPI.git'
            }
        }

        stage('Install Dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube Analysis'){
            steps{
                withSonarQubeEnv('SonarQubeServer'){
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Docker Build'){
            steps{
                sh 'docker build -t $Docker_IMAGE .'
            }
        }

        stage('Docker Run'){
            steps{
                sh 'docker run -d -p 8000:8000 --name fastapi_container $DOCKER_IMAGE'
            }
        }

    }

    post{
        always{
            sh 'docker rm -f fastapi_container || true'
        }
    }
}
