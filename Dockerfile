FROM python:3.11-alpine

WORKDIR /app
COPY requirements/run.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "./scripts/run-local.sh" ]