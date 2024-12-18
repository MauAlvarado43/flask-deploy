FROM python:3.7.2

ADD . /flask-deploy

WORKDIR /flask-deploy

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn[gevent]

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info