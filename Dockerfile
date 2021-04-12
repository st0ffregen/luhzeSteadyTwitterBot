FROM python:3
WORKDIR /usr/src/app/bot
COPY ./bot /usr/src/app/bot
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install tweepy
CMD ["python", "/usr/src/app/bot/updateStatus.py"]