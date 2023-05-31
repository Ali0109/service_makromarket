FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR loyalty_service
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt