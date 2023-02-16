from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pydantic import BaseModel
import requests
import csv

class User(BaseModel):
    username: str
    salary: int

args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 2, 14),
}

def fetch_data():
    response = requests.get("http://localhost:5000/getusers")
    mydata = [User(**data) for data in response.json()]
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for user in mydata:
            writer.writerow([user.username,user.salary])

dag = DAG(
    'fetch_data_from_api',
    default_args=args,
    schedule=timedelta(hours=10),
    catchup=False,
)

task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)

task
