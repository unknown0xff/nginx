#!/bin/sh
docker cp ./nginx.conf nginx:/etc/nginx/nginx.conf
docker exec -it nginx nginx -s reload
