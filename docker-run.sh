#!/bin/sh

docker run -d -p443:443 --name nginx \
    -v /etc/letsencrypt:/etc/letsencrypt \
    nginx

./docker-sync.sh
