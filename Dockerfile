FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD .env /
ADD models.py /
ADD db_connector.py /
ADD bot.py /
ADD main.py /

CMD [ "python", "./main.py" ]
