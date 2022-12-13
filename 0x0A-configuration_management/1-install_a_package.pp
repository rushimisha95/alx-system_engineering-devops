# Install flask 2.1.0 modified
package { 'flask':
  ensure   => '2.1.0',
  provider =>  pip3
}
