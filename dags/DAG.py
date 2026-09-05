from datetime import datetime
import init
from airflow import DAG
from airflow.operators.bash import BashOperator
PROJECT_PATH = init.home
# A Dag represents a workflow, a collection of tasks
with DAG(dag_id="NeoWS_pipeline", start_date=datetime(2026, 8, 24),
    schedule="0 0 * * *",
    catchup=False,) as dag:
    # Tasks are represented as operators
    extract = BashOperator(task_id="extract", bash_command=f"python {PROJECT_PATH}/extract.py")
    transform = BashOperator(task_id="transform", bash_command=f"python {PROJECT_PATH}/transform.py")
    load = BashOperator(task_id="load", bash_command=f"python {PROJECT_PATH}/load.py")

    # Set dependencies between tasks
    extract >> transform >> load