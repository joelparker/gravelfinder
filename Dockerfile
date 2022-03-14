FROM python:3.8

#Environment variables
ENV GOOGLE_API_KEY="<PUT YOUR GOOGLE MAPS API KEY HERE>"

COPY requirements.txt /
RUN pip3 install -r ./requirements.txt

COPY . /gravelfinder
WORKDIR /gravelfinder

#CREATE geojson files
RUN python3 ./geojson.py

EXPOSE 5000

ENTRYPOINT ["python3", "./gravelfinder.py"]

