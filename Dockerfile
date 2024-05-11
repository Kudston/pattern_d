FROM python:3.9-slim-bullseye

RUN apt-get update -y
RUN apt-get install gcc -y

RUN mkdir /usr/src/pattern_d/
WORKDIR /usr/src/pattern_d/


RUN mkdir requirements/
COPY requirements.txt requirements/prod.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements/prod.txt

ADD . /usr/src/pattern_d/

EXPOSE 8500

# CMD ["uvicorn", "src.main:app" ,"--host","0.0.0.0","--port", "8500"]