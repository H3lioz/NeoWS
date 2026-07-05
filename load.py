import psycopg
import init
from pathlib import Path
from datetime import datetime
import pandas as pd

logging_path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/logs.txt')


try:
    with psycopg.connect(
        dbname=init.DB_name,
        user=init.DB_User,
        password=init.DB_password,
        host=init.DB_HOST,
        port=init.DB_PORT
    ) as conn:
        with logging_path.open('a') as logger :
            logger.write(f"\n✅ Подключение успешно    {datetime.now()}")
        with conn.cursor() as cur:
            df1 = pd.read_csv('/home/He1ioz/Документы/python/NeoWs/ignore/Asteroid_DB.csv')
            astr_val = df1.to_records(index=False).tolist()
            cur.executemany(
            "INSERT INTO asteroids (id, name, size, size_category, magnitude, latest_research_date) values (%s, %s, %s, %s, %s, %s)",
            astr_val)
            with logging_path.open('a') as logger :
                logger.write(f"\n✅ Данные астероидов записаны    {datetime.now()}")

            
            
            with Path('/home/He1ioz/Документы/python/NeoWs/ignore/Oberving_params.csv').open('r') as data:
                with cur.copy("COPY observed_parameters FROM STDIN WITH CSV HEADER") as copy:
                        copy.write(data.read())

            with logging_path.open('a') as logger :
                logger.write(f"\n✅ Данные о пареметрах астероидов записаны    {datetime.now()}")


except Exception as e:
    with logging_path.open('a') as logger :
            logger.write(f"\n❌ Ошибка: {e}    {datetime.now()}")