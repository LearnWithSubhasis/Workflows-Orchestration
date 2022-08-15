from kfp import dsl

def deploy_model_op(model):

    return dsl.ContainerOp(
        name='Deploy Model',
        image='subhasiskhatua/subhasis-kubeflow-deploy-model-2:latest',
        arguments=[
            '--model', model
        ]
    )