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

        '''
    }
        }
        stage('Run Tests'){
            steps{
                sh '''
                . ev/bin/activate
                mkdir -p allure-results
                pytest -v test.py --alluredir=allure-results
                '''
            }
        }


    }
    post{
        always{
            allure(
                includeProperties:false,
                jdk:'',
                results :[[path:'allure-results']]
            )

            }
        }
        success{
            echo 'Build passed'
        }
        failure{
            echo 'build failure'
        }
    }
