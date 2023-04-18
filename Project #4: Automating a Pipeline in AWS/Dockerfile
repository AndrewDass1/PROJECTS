FROM python:3.9.16

COPY . .

RUN apt update

RUN apt upgrade

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "flask_file.py"]