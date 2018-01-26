FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /mathemacode
WORKDIR /mathemacode
ADD requirements.txt /mathemacode/
RUN pip install -r requirements.txt
ADD . /mathemacode/