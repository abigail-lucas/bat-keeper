FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD .env /
ADD bot.py /
ADD db_connector.py /
CMD [ "python", "./bot.py" ]
