FROM python:3.9-alpine

#Environment variables
ENV GOOGLE_API_KEY="<PUT YOUR GOOGLE MAPS API KEY HERE>"

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . /gravelfinder
WORKDIR /gravelfinder

#CREATE geojson files
RUN python3 ./geojson.py

EXPOSE 5000
EXPOSE 9090

RUN mkdir -p /tmp/metrics
ENV PROMETHEUS_MULTIPROC_DIR="/tmp/metrics"

#ENTRYPOINT ["gunicorn","--chdir","/gravelfinder","gravelfinder:app", "-w", "2", "--threads","2","-b","0.0.0.0:5000","-b","0.0.0.0:9090"]
ENTRYPOINT ["gunicorn","--chdir","/gravelfinder","-c","gunicorn_config.py","gravelfinder:app"]

