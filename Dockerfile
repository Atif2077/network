FROM python:3
COPY .  /Downloads/project4
WORKDIR /Downloads/project4
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]