# luhzeSteadyTwitterBot
Publishes a tweet on a daily base to advertise steady support and deletes the same tweet at midnight

# Build
```
docker build -t python-steady-twitter-bot ./bot
```

# Staging & Deployment
```
cp .env-example .env
docker run -it -v "$(pwd)/bot:/usr/src/app" --rm --env-file .env --name python-steady-twitter-bot-running python-steady-twitter-bot
```