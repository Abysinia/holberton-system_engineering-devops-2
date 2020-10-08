#  Delete the limits
exec { '/usr/bin/env sed -i "/holberton/d" /etc/security/limits.conf': }
