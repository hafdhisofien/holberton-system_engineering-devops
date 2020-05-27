#fix the server limitation and set it to 1000
exec { 'increase the limit':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx; service nginx \
restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}