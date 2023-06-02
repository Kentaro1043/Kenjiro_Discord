FROM python:3.9.16-bullseye

WORKDIR /root/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
