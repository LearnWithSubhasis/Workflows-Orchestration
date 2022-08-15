import kfp
from kfp import dsl
from kfp_preprocess_component import preprocess_op
from kfp_train_component import train_op
from kfp_test_component import test_op
from kfp_deploy_model_component import deploy_model_op

@dsl.pipeline(
   name='Subhasis - California Housing Pipeline',
   description='An example pipeline.'
)
def california_housing_pipeline():
    _preprocess_op = preprocess_op()

    _train_op = train_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_train']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_train'])
    ).after(_preprocess_op)

    _test_op = test_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_test']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_test']),
        dsl.InputArgumentPath(_train_op.outputs['model'])
    ).after(_train_op)

    _deploy_model_op = deploy_model_op(
        dsl.InputArgumentPath(_train_op.outputs['model'])
    ).after(_test_op)


client = kfp.Client()
client.create_run_from_pipeline_func(california_housing_pipeline, arguments={})

def call_kubeflow_pipeline():
    client = kfp.Client()
    client.create_run_from_pipeline_func(california_housing_pipeline, arguments={})

