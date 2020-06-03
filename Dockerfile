FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD .env /
ADD config.py /
ADD main.py /
ADD models.py /
ADD bot.py /

CMD [ "python", "./main.py" ]
