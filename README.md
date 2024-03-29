# Binance Trade Data Pipeline
A streamlined data pipeline designed to extract cryptocurrencies (BTC, SOL, ETH, BNB, USDT, USDC) trade data from Binance, orchestrate the process using Apache Airflow, and efficiently store the data on Amazon EC2 and S3 for processing and archiving.
## Tools used;
- Python
- Apache Airflow
- Binance API key and secret
- Amazon EC2 Instance
- Amazon S3 Bucket
## The Architecture
![Untitled (6)](https://github.com/mustafa0taru/binance-api-airflow-data-pipeline/assets/81088966/0f22cd74-bf9d-4e21-9ee1-7c1f247e7518)
## Features
- **Binance Trade Data Extraction**: Utilizes the Binance API to fetch cryptocurrency trade data.
- **Airflow Orchestration**: Apache Airflow DAG schedules and manages the data extraction process.
- **Amazon EC2 Storage**: Stores processed data on an Amazon EC2 instance.
- **Amazon S3 Archiving**: Efficiently archives and backs up data on Amazon S3 for scalability.
