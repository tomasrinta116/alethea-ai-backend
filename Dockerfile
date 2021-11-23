FROM python:3.8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential postgresql-common libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app/
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]