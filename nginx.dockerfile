FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
VOLUME 
EXPOSE 443:443/tcp