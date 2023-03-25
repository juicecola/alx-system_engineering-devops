#making changes to configuration file
file_line { 'turnoff passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   =>  'PasswordAuthetication no', 
}

file_line { 'declare the identity file':
  ensure => 'present',
  path   =>  '~/ssh/school',
  line   =>  '    identity file ~/ssh/school',
}

