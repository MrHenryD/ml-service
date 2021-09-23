FROM python:3.9

WORKDIR "/opt/mlservice"
COPY . /opt/mlservice/requirements.txt

RUN pip install -r /opt/mlservice/requirements.txt

CMD ["python3", "/opt/mlservice/server.py"]