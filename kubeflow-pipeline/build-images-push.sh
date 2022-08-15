docker login

docker build . -t subhasis-kubeflow-preprocess-2:latest -f Dockerfile-preprocess
docker tag subhasis-kubeflow-preprocess-2 subhasiskhatua/subhasis-kubeflow-preprocess-2
docker push -a subhasiskhatua/subhasis-kubeflow-preprocess-2

docker build . -t subhasis-kubeflow-train-2:latest -f Dockerfile-train
docker tag subhasis-kubeflow-train-2 subhasiskhatua/subhasis-kubeflow-train-2
docker push -a subhasiskhatua/subhasis-kubeflow-train-2

docker build . -t subhasis-kubeflow-test-2:latest -f Dockerfile-test
docker tag subhasis-kubeflow-test-2 subhasiskhatua/subhasis-kubeflow-test-2
docker push -a subhasiskhatua/subhasis-kubeflow-test-2

docker build . -t subhasis-kubeflow-deploy-model-2:latest -f Dockerfile-deploy-model
docker tag subhasis-kubeflow-deploy-model-2 subhasiskhatua/subhasis-kubeflow-deploy-model-2
docker push -a subhasiskhatua/subhasis-kubeflow-deploy-model-2
