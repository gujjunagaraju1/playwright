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
            pytest -v
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