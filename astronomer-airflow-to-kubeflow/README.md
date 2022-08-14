# Steps for complex DAG, calling kubeflow pipeline from airflow DAG

## 1. Create a Kubernetes cluster
> brew install kind
> 
> kind create cluster
> 
> kubectl cluster-info --context kind-kind

## 2. Setup Kubeflow
> kubeflow-setup.sh
> 
> kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8081:80

## 3. Build Docker images for inidividual steps in the kubeflow pipeline
> docker login

#### Build, tag, push docker image to DockerHub
Step 1 = PreProcess
> docker build . -t subhasis-kubeflow-preprocess-2:latest
> 
> docker tag subhasis-kubeflow-2 subhasiskhatua/subhasis-kubeflow-preprocess-2
> 
> docker push -a subhasiskhatua/subhasis-kubeflow-preprocess-2

Step 2 = Train
> docker build . -t subhasis-kubeflow-train-2:latest -f Dockerfile-train
> 
> docker tag subhasis-kubeflow-train-2 subhasiskhatua/subhasis-kubeflow-train-2
> 
> docker push -a subhasiskhatua/subhasis-kubeflow-train-2

Step 3 = Test
> docker build . -t subhasis-kubeflow-test-2:latest -f Dockerfile-test
> 
> docker tag subhasis-kubeflow-test-2 subhasiskhatua/subhasis-kubeflow-test-2
> 
> docker push -a subhasiskhatua/subhasis-kubeflow-test-2

Step 4 = Deploy
> docker build . -t subhasis-kubeflow-deploy-2:latest -f Dockerfile-deploy
> 
> docker tag subhasis-kubeflow-deploy-2 subhasiskhatua/subhasis-kubeflow-deploy-2
> 
> docker push -a subhasiskhatua/subhasis-kubeflow-deploy-2

#### References

https://towardsdatascience.com/machine-learning-pipelines-with-kubeflow-4c59ad05522

https://www.kubeflow.org/docs/components/pipelines/installation/localcluster-deployment/

https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker

https://www.kubeflow.org/docs/components/pipelines/overview/caching/

https://docs.min.io/docs/minio-client-quickstart-guide.html

https://valohai.com/blog/kubeflow-vs-airflow/

----------------------
#### MinIO 
kubectl -n minio-operator  get secret $(kubectl -n minio-operator get serviceaccount console-sa -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode && echo ""

kubectl -n minio-operator port-forward svc/console 9090


