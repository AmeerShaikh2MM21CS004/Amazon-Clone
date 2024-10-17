FROM python:3.13.0-slim

WORKDIR /docker_env 

COPY requirements.txt /docker_env/

RUN pip install -r requirements.txt

COPY . /docker_env/

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
