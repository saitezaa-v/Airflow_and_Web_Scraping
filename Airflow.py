import airflow, pendulum
from airflow import DAG
from airflow.contrib.operators.dataproc_operator
import DataprocClusterCreateOperator,DataProcPySparkOperator, DataprocClusterDeleteOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 1, 28, 10, 15),
    'depends_on_past': False,
    'retries': 0
}

dag = DAG(
    dag_id='Data_Processing_1',
    description='Sample code to explain GCP automation using Airflow DAG',
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    schedule_interval="@daily",
)

show_date = BashOperator(
    task_id='print_date',
    bash_command='sleep 2',
    dag=dag)

data_processing_test = DataProcPySparkOperator(
    dag=dag,
    task_id='data_processing_test',  ##Change the name of the task_id according to task
    main='some_folder/code/hello_GCP.py',  ## This is your data processing code with location
)