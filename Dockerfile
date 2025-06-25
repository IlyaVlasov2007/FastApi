FROM python:3.13-slim

WORKDIR /app

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "src/run.py"] 