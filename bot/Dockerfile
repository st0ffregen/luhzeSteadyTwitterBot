FROM python:3.7
WORKDIR /usr/src/app/bot
COPY . /usr/src/app/bot
RUN pip install tweepy
CMD ["python", "/usr/src/app/bot/updateStatus.py"]