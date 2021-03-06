FROM python:3.8

WORKDIR /src/mockservice

COPY requirements.txt .

RUN apt-get update && apt-get install -y python python-pip
RUN pip3 install --cache-dir=/cache -r requirements.txt

COPY . .

# CMD ["uvicorn", "app:app", "--port", "5000"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]