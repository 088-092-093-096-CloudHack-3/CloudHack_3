# Follow Task-0 subtask-1
FROM python:3.8-alpine
WORKDIR /app
COPY ./app/requirements.txt ./app/app.py ./
EXPOSE 5004
RUN pip install -r requirements.txt 
CMD ["python","app.py"]
