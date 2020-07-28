#!/bin/sh
docker cp ./nginx.conf niginx:/etc/nginx/nginx.conf
docker exec -it nginx nginx -s reload
