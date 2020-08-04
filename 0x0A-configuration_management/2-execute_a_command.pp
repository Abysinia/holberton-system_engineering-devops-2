# kills a process named killmenow

exec { 'kill process':
  path    => '/usr/bin:/bin',
  command => 'pkill killmenow'
}
