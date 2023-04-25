FROM python:3.8

COPY . .

RUN apt update -y

RUN apt upgrade -y

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "application.py"]
