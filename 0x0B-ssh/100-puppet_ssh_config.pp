include stdlib
# set up your client SSH configuration file so that you can connect to a server without typing a password.
file { '/root/.ssh/config':
  ensure => 'file',
  mode   => '0600',
  content => "Host ubuntu\n\tHostName 54.172.10.124\n\tUser root\n\tIdentityFile /root/.ssh/school\n",
}

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
