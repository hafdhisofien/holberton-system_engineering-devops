#!/usr/bin/env bash
# Configurating our nginx server using a puppet manifest

exec {'Install nginx':
command  => 'sudo apt update && sudo apt -y install nginx && echo "Holberton School" | sudo tee /usr/share/nginx/html/index.html && redirect="\\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n" && sudo sed -i "37i $redirect" /etc/nginx/sites-enabled/default && sudo service nginx restart',
listen_port => 80,
provider => shell,
}