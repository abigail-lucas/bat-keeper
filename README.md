# PICKME

This is a simple bot for pulling a name out of a hat. It pulls a list of people based on their role and chooses the amount passed.

## Commands

```
?help                       - gives help on the uses of this bot
?pickme {number} {role}     - returns random members that has viewing permissions
?offline {role}             - returns all of the members that are offline
```

## Setup

This project is set up to run on Docker 19.03.6, it has not been tested with newer versions of Docker.

A simple list of commands to build, and run the docker image. Make sure Docker is installed.

- `docker build -t pickme-bot .`
- `docker run pickme-bot`

Please note that the build will fail if you do not have a `.env` file in the root directory of this project. This file should simply contain the token for the bot.

Example of how the `.env` should look like:
```
DISCORD_TOKEN=this-text-should-be-the-token
```

## TODO

- Set up docker-compose
- Implement authorized roles for commands
- Implement a database to store authorized roles
