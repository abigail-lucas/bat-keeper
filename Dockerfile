FROM python:3

ADD .env /
ADD bot.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]
