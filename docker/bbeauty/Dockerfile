FROM python:3.8

COPY ./src /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT [ "/entrypoint.sh" ]