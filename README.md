# PICKME

This is a simple bot for pulling a name out of a hat. It pulls a list of people based on their role and chooses the amount passed.

## Setting this up

This project is built using `Python3` and the discord bot library. I have included two guides on launching this project. The first is aimed at developers familiar with Python environments. The second is aimed at students and developers new to Python environments.

### Quick setup guide

This is a quick guide on launching the project, assuming you know the basics of venv and hooking up Discord's bot API keys.

- `pip install -r requirements.txt`
- Add your API key in `.env`
- `python bot.py`

### Guide on how to launch and build this

This is a step-by-step guide on building this project. It is aimed at new developers and students.

- Make sure Python 3 is installed if you are using Windows
- Install the `venv` package with Python 3 like this: `pip3 install venv` - if you encounter an error, make sure to give it sudo permissions
- Create your virtual environment. If you are using `venv` then do `python3 -m venv venv` (the first `venv` invokes the package, the last `venv` is the virtual environment's name)
- Activate your virtual environment by going into `venv/bin/` activating the python. `cd venv/bin/` and then `source activate`
- Install dependencies with pip once your virtual environment is up. Do this with `pip install -r requirements.txt`
- Once it is installed you are ready to boot the project. Although you will need the bot API key and you can do that by making your own bot on Discord' developer portal and putting that in a `.env` file.

## TODO

- Move duplicate code to methods
- Restrict bot commands to only certain roles
