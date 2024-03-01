#!/usr/bin/puppet

# Install a specific version of flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],  # Ensure python3-pip is installed before installing Flask with pip3
}
