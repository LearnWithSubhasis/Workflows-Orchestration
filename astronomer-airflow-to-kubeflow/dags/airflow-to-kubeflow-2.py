
from datetime import datetime, timedelta
from pprint import pprint
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from simple import print_simple
from complex.complex import print_complex
from kfp_pipeline import call_kubeflow_pipeline

with DAG(
    'airflow-to-kubeflow',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        # 'depends_on_past': False,
        # 'email': ['airflow-practice@example.com'],
        # 'email_on_failure': False,
        # 'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='Subhasis - Sample DAG for demonstrating call from airflow to kubeflow',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['example', 'airflow', 'kubeflow'],
) as dag:

    @task(task_id="print_the_context")
    def print_context(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        pprint(kwargs)
        print(ds)
        return 'Whatever you return gets printed in the logs'


    run_this_2 = PythonOperator(
        task_id='print_simple',
        provide_context=True,
        python_callable=print_simple,
        dag=dag)


    run_this_3 = PythonOperator(
        task_id='print_complex',
        provide_context=True,
        python_callable=print_complex,
        dag=dag)


    run_this_4 = PythonOperator(
        task_id='run_kubeflow_pipeline',
        provide_context=True,
        python_callable=call_kubeflow_pipeline,
        dag=dag)


    # kubeflow_task = BashOperator(
    #     task_id="call_kubeflow_pipeline",
    #     bash_command='python ./simple.py'
    #     #bash_command='python ~/airflow/dags/kubeflow_pipelines/kfp_pipeline.py'
    #     #bash_command='echo "Here is the message: \'{{ dag_run.conf["message"] if dag_run else "" }}\'"',
    # )

    run_this = print_context()
    run_this >> run_this_2 >> run_this_3 >> run_this_4