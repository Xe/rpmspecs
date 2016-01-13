Caddy
=====

This packages [Caddy](https://caddyserver.com) for use in Fedora and Centos. 
Usage of this package is simple:

1. Put your caddy configuration in `/etc/caddy/Caddyfile`. The default example 
   configuration will automatically include each site in `/etc/caddy/sites`.
2. `systemctl enable caddy && systemctl start caddy`
3. Enjoy your SSL.
