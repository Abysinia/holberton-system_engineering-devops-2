# install puppet-lint

package { 'puppet-lint install':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
