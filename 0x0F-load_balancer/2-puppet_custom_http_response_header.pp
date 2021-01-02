#  custom HTTP header with Puppet
exec { 'Custom_header_response':
    command  => 'apt-get update;
    apt-get -y install nginx;
    sed -i "19i \\\\n\tadd_header X-Served-By $HOSTNAME;\n" /etc/nginx/sites-enabled/default;
    service nginx restart'
}
