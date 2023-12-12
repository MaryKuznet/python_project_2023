FROM python:3.10
# RUN apt-get update -y && apt-get install -y build-essential ffmpeg libsm6 libxext6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 5000
# RUN python run.py
CMD python /app/helpers.py
CMD python run.py
# ENTRYPOINT ['python3.10']
# CMD ['run.py']