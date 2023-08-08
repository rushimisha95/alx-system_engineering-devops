# Using strace, find out why Apache is returning a
# 500 error. Once you find the issue, fix it and then
# automate it using Puppet (instead of using Bash as you were
# previously doing).

exec { 'fix-phpp':
  provider => shell,
  command  => 'sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
