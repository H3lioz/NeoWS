FROM python:3.14.5
WORKDIR /usr/src/NeoWs

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY init.py .
COPY extract.py .
COPY transform.py .
COPY load.py .
COPY etl_script .

RUN chmod +x etl_script

CMD ["bash", "./etl_script"]
