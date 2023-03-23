FROM python:3.10.6

ADD . /backend
WORKDIR /backend
COPY . ./backend

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0