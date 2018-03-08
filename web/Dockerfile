FROM python:3.6-alpine
MAINTAINER Sujay Kundu "sujay@skillenza.com"
COPY . /app
WORKDIR /app
RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
