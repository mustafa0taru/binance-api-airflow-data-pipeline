# dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from binance_trade import extract_trade_data

# Binance API credentials
api_key = 'api_key'
api_secret = 'api_secret'

# Binance trading pairs to extract
symbols = ['BTCUSDT', 'SOLUSDT', 'ETHUSDT', 'BNBUSDT', 'USDTUSDC']

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'binance_trade_extraction',
    default_args=default_args,
    description='Extract trade data from Binance API',
    schedule_interval=timedelta(days=1), 
)

def run_extraction(**kwargs):
    extract_trade_data(api_key, api_secret, symbol, '/path/to/save/trade_data.json')

extract_task = PythonOperator(
    task_id='run_extraction',
    python_callable=run_extraction,
    provide_context=True,
    dag=dag,
)

extract_task
