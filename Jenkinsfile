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
                    bat '"C:\\Users\\ubale\\sonar-scanner-7.1.0.4889-windows-x64\\bin\\sonar-scanner.bat"'
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
                bat '''
                docker rm -f fastapi-conatiner || exit 0
                FOR /F "tokens=*" %%i IN ('docker ps -q --filter "publish=8500"') DO docker stop %%i
                '''
            }
        }
        
        stage('Docker Run') {
            steps {
                bat 'docker run -d -p 8000:8000 --name fastapi-conatiner %DOCKER_IMAGE%'
            }
        }
    }
}
