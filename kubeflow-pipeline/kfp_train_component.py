from kfp import dsl

def train_op(x_train, y_train):

    return dsl.ContainerOp(
        name='Train Model',
        image='subhasiskhatua/subhasis-kubeflow-train-2:latest',
        arguments=[
            '--x_train', x_train,
            '--y_train', y_train
        ],
        file_outputs={
            'model': '/app/model.pkl'
        }
    )