#!/usr/bin/env bash
# puppet manifest to create a custom HTTP header response

exec { 'update':
  command => '/usr/bin/apt-get update',
}
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
-> file_line { 'custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By ${hostname};',
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}