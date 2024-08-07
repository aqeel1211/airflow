from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from slack_sdk import WebClient
import random as rn

def send_slack_message():
    """For airflow demonstrations, sends a message to slack channel"""
    slack_token = 'xoxb-515149146933-7273865651924-ojS8natB503pCOPqMsCDVheK'
    channel_id = 'C077WHPBXFX'

    # Initialize Slack client
    client = WebClient(token=slack_token)

   
    error_poss = 1/rn.randint(0, 5)  # 1 in 6 will fail

    if error_poss != 1:

        UTCtime = datetime.utcnow().strftime('%d-%m-%y %H:%M:%S')
        message = f"Airflow demo message by Safiii {error_poss} at - ({UTCtime} UTC)"

        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )

    else:
        UTCtime = datetime.utcnow().strftime('%d-%m-%y %H:%M:%S')
        message = f":red_circle: {error_poss} Airflow demo message failed because of error poss: {error_poss} at - ({UTCtime} UTC)"

        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print("Helloo")
    
    # if not response["ok"]:
    #     raise Exception(f"Failed to send message: {response['error']}")


# Define the DAG
dag = DAG(
    'send_slack_message_dag',
    description='Sends a message to Slack channel using Airflow',
    schedule_interval='*/2 * * * *',
    start_date=datetime(2023, 1, 1),
    catchup=False
)


send_message_task = PythonOperator(
    task_id='send_message_task',
    python_callable=send_slack_message,
    dag=dag
)
