FROM python:alpine3.19

WORKDIR /app

COPY . .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN chmod +x cli.py
COPY cli.py /usr/local/bin/twitter-cli

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]