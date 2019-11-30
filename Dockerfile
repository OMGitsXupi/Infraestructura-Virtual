FROM python:3.7
WORKDIR /usr/src/wikirandom

RUN apt-get install libjpeg-dev \
                       zlib1g-dev \
                       libfreetype6-dev \
                       liblcms2-dev 
                      
                       
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/wikirandom

CMD fab gunicornPaaS
