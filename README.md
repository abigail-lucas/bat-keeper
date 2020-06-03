# PICKME

This is a simple bot for pulling a name out of a hat. It pulls a list of people based on their role and chooses the amount passed.

## Commands

```
?help                       - gives help on the uses of this bot
?pickme {number} {role}     - returns random members that has viewing permissions
?offline {role}             - returns all of the members that are offline
```

## Setup

A simple list of commands to build, and run the docker image. Make sure Docker and docker-compose is installed.

- `docker-compose up`

Please note that the build will fail if you do not have a `.env` file in the root directory of this project. This file should simply contain the token for the bot.

Example of how the `.env` should look like:

```
DISCORD_TOKEN=this-text-should-be-the-token
MYSQL_PASSWORD=password-to-access-mysql
```

## Softare Versions

Python
```
Python3
```

Docker and docker-compose
```
Docker version 19.03.6, build 369ce74a3c
docker-compose version 1.21.2, build a133471
```

MySQL
```
mysql:5.7
```

## TODO

- Implement authorized roles for commands
