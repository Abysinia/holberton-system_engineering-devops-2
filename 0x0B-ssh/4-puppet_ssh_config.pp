# ssh_config 

file_line { 'ssh config: NO password':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => 'PasswordAuthentication no',
    match              => '^PasswordAuthentication',
    append_on_no_match => true,
  }

file_line { 'ssh config: New Place for priv key':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => 'IdentityFile ~/.ssh/holberton',
    match              => '^IdentityFile',
    append_on_no_match => true,
  }
