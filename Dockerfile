FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY assessment.py assessment.py

RUN mkdir -p /output

CMD ["python", "assessment.py"]

