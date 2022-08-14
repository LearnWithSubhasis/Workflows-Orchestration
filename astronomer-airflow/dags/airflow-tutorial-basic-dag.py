
from datetime import datetime, timedelta
from pprint import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from simple import print_simple

with DAG(
    'airflow-tutorial-basic-dag',
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
    description='Subhasis - Sample DAG for demonstrating a simple DAG',
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
        task_id='print_simple_using_python_op',
        provide_context=True,
        python_callable=print_simple,
        dag=dag)

    run_task_3 = BashOperator(
        task_id='echo_task_using_bash_op',
        depends_on_past=False,
        bash_command='echo "Message from echo_task_using_bash_op"',
    )

    run_this = print_context()
    run_this >> run_this_2 >> run_task_3