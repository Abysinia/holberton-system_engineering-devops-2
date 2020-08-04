#create a file in /tmp.

file { '/tmp/holberton':
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  content => 'I love Puppet'
}
