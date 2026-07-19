import psycopg
import init
from pathlib import Path
from datetime import datetime
import pandas as pd
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

try:
    with psycopg.connect(
        dbname=init.DB_name,
        user=init.DB_User,
        password=init.DB_password,
        host=init.DB_HOST,
        port=init.DB_PORT
    ) as conn:
        logger.info(f"✅ Подключение успешно")

        with conn.cursor() as cur:

            df1 = pd.read_csv(init.home/'ignore/Asteroid_DB.csv')
            astr_val = df1.to_records(index=False).tolist()
            cur.executemany(
            "INSERT INTO asteroids (id, name, size, size_category, magnitude, latest_research_date) \
            values (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO UPDATE SET size = EXCLUDED.size, size_category = EXCLUDED.size_category, magnitude = EXCLUDED.magnitude, latest_research_date = EXCLUDED.latest_research_date",
            astr_val)

            logger.info(f"✅ Данные астероидов записаны")

            
            
            with (init.home/'ignore/Oberving_params.csv').open('r') as data:
                with cur.copy("COPY observed_parameters FROM STDIN WITH CSV HEADER") as copy:
                        copy.write(data.read())

            logger.info(f"✅ Данные о пареметрах астероидов записаны")


except Exception as e:
    logger.error(f"❌ Ошибка: {e}")