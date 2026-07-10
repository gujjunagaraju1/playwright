pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }

        }
        stage('Install dependencies'){
            steps {
        sh '''
            python3 -m venv ev
            . ev/bin/activate
            pip install -r requirements.txt
            playwright install
            pytest -v test.py
        '''
    }
        }


    }
    post{
        success{
            echo 'Build passed'
        }
        failure{
            echo 'build failure'
        }
    }
}