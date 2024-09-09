FROM ubuntu:24.10

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip 

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r lib.txt

CMD ["python3", "app.py"]

