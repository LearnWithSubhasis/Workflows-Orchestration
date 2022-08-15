from kfp import dsl

def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='subhasiskhatua/subhasis-kubeflow-preprocess-2:latest',
        arguments=[],
        file_outputs={
            'x_train': '/app/x_train.npy',
            'x_test': '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy',
        }
    )