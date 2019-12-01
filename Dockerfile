FROM python:3.7-slim-buster
WORKDIR /usr/src/wikirandom
                       
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/wikirandom

CMD fab gunicornPaaS
