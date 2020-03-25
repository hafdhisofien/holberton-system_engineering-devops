#!/usr/bin/env bash
# Configurating our nginx server using a puppet manifest

package { 'nginx':
  ensure => installed,
}

exec { 'Holberton':
  provider => shell,
  command  => 'sudo echo "Holberton School" | sudo tee  /usr/share/nginx/html/index.html',
}

file_line { 'redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
