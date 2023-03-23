FROM python:3.10.6

COPY . ./backend
WORKDIR /backend

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD cd app && gunicorn -b 0.0.0.0:8000 app:app