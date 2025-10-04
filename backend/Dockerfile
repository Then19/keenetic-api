FROM python:3.12-slim

COPY requirements.txt .

RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.main:application", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info", "--proxy-headers", "--forwarded-allow-ips=*", "--root-path", "/api"]