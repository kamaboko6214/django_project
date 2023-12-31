FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /work
RUN pip install --upgrade pip
RUN pip install \
    Django
COPY . /work/