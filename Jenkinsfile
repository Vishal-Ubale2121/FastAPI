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
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe" install pytest pytest-cov flake8 black safety'
            }
        }

        stage('Check Code Formatting') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\black.exe" --check app tests'
            }
        }

        stage('Lint Code') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\flake8.exe" app tests || exit 0'
            }
        }

        stage('Security Scan') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\safety.exe" check || exit 0'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\ubale\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pytest.exe" --cov=app --cov-report=xml --junitxml=results.xml tests/test_main.py --disable-warnings'
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'results.xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    bat '"C:\\Users\\ubale\\sonar-scanner-7.1.0.4889-windows-x64\\bin\\sonar-scanner.bat"'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Docker Cleanup') {
            steps {
                bat 'docker rm -f fastapi-container || exit 0'
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

        stage('Notify') {
            steps {
                echo 'You can add Slack/email/Teams notifications here.'
            }
        }
    }
}
