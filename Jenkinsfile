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

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pytest.exe" tests/main_test.py --disable-warnings'
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

        stage('Docker Run') {
            steps {
                bat 'docker run -d -p 8000:8000 --name fastapi-container %DOCKER_IMAGE%'
            }
        }
    }
}
