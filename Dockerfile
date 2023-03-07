FROM python:3.9.2

RUN useradd ruan

WORKDIR /home/project

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY luxury_rents.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP luxury_rents.py

RUN chown -R ruan:ruan ./
USER ruan

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
