# env/platform-agnostic-pns hasn't been publically released, so you will install it from master
export PIPELINE_VERSION=1.8.3

# Disable cache (otherwise - previous runs will be re-used)
export NAMESPACE=kubeflow
kubectl get mutatingwebhookconfiguration cache-webhook-${NAMESPACE}
kubectl patch mutatingwebhookconfiguration cache-webhook-${NAMESPACE} --type='json' -p='[{"op":"replace", "path": "/webhooks/0/rules/0/operations/0", "value": "DELETE"}]'

#Enable cache
#kubectl patch mutatingwebhookconfiguration cache-webhook-${NAMESPACE} --type='json' -p='[{"op":"replace", "path": "/webhooks/0/rules/0/operations/0", "value": "CREATE"}]'

kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"

kubectl apply -k github.com/minio/operator/
