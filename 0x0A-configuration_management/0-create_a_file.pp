#create a file in /tmp.

file { 'holberton_file':
  ensure  => 'file',
  path    => '/tmp/holberton',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
