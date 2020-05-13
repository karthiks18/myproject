node{
   stage('SCM Checkout'){
     git 'https://github.com/karthiks18/myproject.git'
   }
   stage('Compile-Package'){
    
      def mvnHome =  tool name: 'maven3', type: 'maven'   
      sh "${mvnHome}/bin/mvn clean package"
   }
   stage('Build Docker Imager'){
   sh 'docker build -t karthiks18/myweb:${env.BUILD_NUMBER} .'
   }
   stage('Docker Image Push'){
   withCredentials([string(credentialsId: 'dockerPass', variable: 'dockerPassword')]) {
   sh "docker login -u karthiks18 -p ${dockerPassword}"
   }
   sh 'docker push karthiks18/myweb:${env.BUILD_NUMBER}'
   }
      stage ('Deploy') {
           steps {
               script{
                   sh "ansible-playbook  playbook.yml --extra-vars \"image_id=${env.BUILD_NUMBER}\""
               }
           }
       }

   }
