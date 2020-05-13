Jenkins server prerequsistes
maven, docker, kubectl is available

jenkins runs with jenkins user
/home/jenkins/.kube/config 
kube  config file is placed in above path.jenkins user have access to  kubernetes cluster where it will deploy the apps

kubernetes cluster creation 
Please follow cluster creation steps mentioned in the file kubernetes_cluster

Horizontal pod auto scaler deployment
kubectl apply -f hpa.yaml

It will autoscale number of pods based on memory utilization

pod distrution budget deployment
kubectl apply -f pdb.yaml

application service deployment
kubectl apply -f app_service.yaml
