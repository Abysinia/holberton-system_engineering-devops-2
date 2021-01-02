#  custom HTTP header with Puppet
exec { '/usr/bin/env sed -i "19i '\\\\n\tadd_header X-Served-By $HOSTNAME;\n" /etc/nginx/sites-enabled/default': }
