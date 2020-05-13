# LAB: Create A Pipeline For A Java App
In this lab, we are building a continuous delivery (CD) pipeline. We are using a very simple application written in Go. For the sake of simplicity, we are going to run only one type of test against the code. The prerequisites for this lab are as follows:

This repo consists of a Java Hello World application. It shows:

Run & test the application from CLI

Create a Docker image, run the container and test it

Create Kubernetes deployment and test it

Let’s get started!

A running Jenkins instance. This could be a cloud instance, a virtual machine, a bare metal one, or a docker container. It must be publicly accessible from the internet so that the repository can connect to Jenkins through web-hooks.
Image registry: you can use Docker Registry, a cloud-based offering like ECR or GCR, or even a custom registry.
An account on GitHub. Although we use GitHub in this example, the procedure can work equally with other repositories like Bitbucket with minor changes.
The pipeline can be depicted as follows:

Create a CI/CD pipeline with Kubernetes and Jenkins

Step 01: The Application Files
Our sample application will respond with ‘Hello World’ to any GET request. Create a new file called App.java and Since we are building a CD pipeline, we should have some tests in place. Our code is so simple that it only needs one test case which is AppTest.java = Source code can be found in src.

Step 02: By following this repository the pre-requisite of tools to be installed and available.
Git
Jenkins
Maven
Ansible
Docker &
Kubernetes

Jenkins runs with jenkins user /home/jenkins/.kube/config kube config file is placed in above path.jenkins user have access to kubernetes cluster where it will deploy the apps

kubernetes cluster creation Please follow cluster creation steps mentioned in the file kubernetes_cluster

Horizontal pod auto scaler deployment kubectl apply -f hpa.yaml

It will autoscale number of pods based on memory utilization

pod distrution budget deployment kubectl apply -f pdb.yaml

application service deployment kubectl apply -f app_service.yaml
