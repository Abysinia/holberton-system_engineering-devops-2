#create a file in /tmp.

file { 'My file':
  ensure  => 'file',
  path    => '/tmp/holberton',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  content => 'I love Puppet'
}
