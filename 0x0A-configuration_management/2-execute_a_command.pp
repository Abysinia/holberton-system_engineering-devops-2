# create a manifest that kills a process named killmenow

exec { 'killmenow':
  path     => '/usr/bin',
  provider => 'shell',
  command  => 'pkill -f ./killmenow'
}
