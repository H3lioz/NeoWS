# NeoWS ETL Pipeline

NeoWS is a containerized ETL pipeline that retrieves asteroid data from the NASA Near Earth Object Web Service (NeoWs) API and processes it using Apache Airflow.

## How it works

The pipeline consists of three main stages:

- **extract.py** — obtains asteroid data for the previous date from the NASA NeoWs API and saves it as a flattened JSON file. The file includes:
  - asteroid ID and name
  - absolute magnitude
  - minimum and maximum estimated diameter
  - potentially hazardous asteroid status
  - close approach data
  - relative velocity
  - miss distance
  - orbiting body
  - Sentry object status

- **transform.py** — processes the extracted JSON using pandas and produces two CSV files:
  - `Asteroid_DB.csv` — general information about asteroids
  - `Observing_params.csv` — observation parameters for each asteroid for the download date

- **load.py** — connects to PostgreSQL and loads the generated CSV files into the corresponding database tables.

The entire ETL pipeline is orchestrated by a single Apache Airflow DAG that runs daily.

# Tech stack

- Apache Airflow 3.3.1
- Python 3.13 (pandas, psycopg3, requests)
- PostgreSQL 16
- Docker & Docker Compose
