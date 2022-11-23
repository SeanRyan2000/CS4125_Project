pipeline {
    agent any
    triggers {
        // Minutes Hours Day Month Day-week
        // 2pm any day of the month Monday-Friday  
        cron('0 14 * * 1-5') 
    }

    stages {        
        stage('Build') {
            steps {
                // Will likely need to install flask on the docker and run it from that 
                // inside the docker container running jenkins I may need to set up a new docker container to run the flask and perfrom the test cases
                echo 'Building..'

                // sh '$ pip install -r requirements.txt'

                dir('routes') {
                    sh 'flask shell'
                    // sh 'exit()'
                }                
            }
        }
        stage('Test') {
            steps {
                // may need to set up sone CLI features to make the testing easier than trying to figure out gui testing features
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }


        node {
            stage('SCM') {
                git 'https://github.com/foo/bar.git'
            }
            stage('SonarQube analysis') {
                def scannerHome = tool 'SonarScanner 4.0';
                withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
                sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }

    }
        // guide https://medium.com/@gustavo.guss/jenkins-sending-email-on-post-build-938b236545d2
    
        post {
            always {
                echo 'Send email'
                // emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
            }
        }
        
    
}
