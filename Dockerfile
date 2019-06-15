FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3

COPY boston_analysisa.py .

CMD ["python3","-u","boston_analysisa.py"]