from kfp import dsl

def test_op(x_test, y_test, model):

    return dsl.ContainerOp(
        name='Test Model',
        image='subhasiskhatua/subhasis-kubeflow-test-2:latest',
        arguments=[
            '--x_test', x_test,
            '--y_test', y_test,
            '--model', model
        ],
        file_outputs={
            'mean_squared_error': '/app/output.txt'
        }
    )