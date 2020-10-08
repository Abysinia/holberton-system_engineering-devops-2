#  Sky is the limit, let's bring that limit higher
exec { '/usr/bin/env sed -i s/500/4096/ /etc/default/nginx': }
exec { '/usr/bin/env service nginx restart': }
