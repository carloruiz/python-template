FROM alpine:3.9

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY requirements.txt ./
RUN pip3 install -r requirements.txt 
ARG DEPENDENCYCACHE

ARG CODECASH 
COPY * ./
EXPOSE 80
EXPOSE 443
VOLUME ["/tmp"]
#for development, uncomment the next two lines, and comment out the last one. 
#WORKDIR /slideshare-backend-local
ENTRYPOINT ["gunicorn"]
#CMD ["gunicorn", "--bind=0.0.0.0:80", "-w", "3", "-k", "aiohttp.worker.GunicornWebWorker", "APP:aioapp"]
