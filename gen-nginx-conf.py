#!/usr/bin/python3
#coding=utf-8

import sys
import os

template = '''\
user nginx;
worker_processes auto;
worker_rlimit_nofile 100000;

events {
    worker_connections 2048;
}

http {   
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    keepalive_timeout 65;
    include /etc/nginx/conf.d/*.conf;

    server {
        server_name %s;
        listen 443 ssl;

        ssl_certificate /etc/letsencrypt/live/%s/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/%s/privkey.pem;

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        #ssl_dhparam /etc/ssl/certs/dhparam.pem;

        #ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';

        ssl_session_timeout 1d;
        ssl_session_cache shared:SSL:50m;
        ssl_stapling on;
        ssl_stapling_verify on;
        add_header Strict-Transport-Security max-age=15768000;

        location / {
            proxy_pass http://localhost:%s;
            proxy_pass_header Server;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass_header Server;
            proxy_connect_timeout 3s;
            proxy_read_timeout 10s;
        }
    }
}
'''

def main():
    if len(sys.argv) > 2:
        domain = sys.argv[1]
        forward_port = sys.argv[2]

        with open('nginx.conf', 'w') as f:
            f.write(template % (domain, domain, domain, forward_port))

    else:
        print("command error.")

if __name__ == '__main__':
    main()
