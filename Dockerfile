FROM python:3.10
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python helpers.py;python run.py