### Usage


```shell
ansible-playbook -i inventory site.yml
# specify user, limit to a host in inventory
ansible-playbook -i inventory site.yml -u USER -l HOST

```

### Ansible commands

```bash
# ping
ansible all -u debian -i inventory -m ping

#reboot the hosts
ansible all -u debian -i inventory -become -m reboot
```


### Troubleshooting caddy config

- 502 error means it can't route hostname in a wildcard configuration block
- routines:ST_CONNECT:tlsv1 alert means a SNI error, the wildcard certificate can't be used and a TLS certificate should be generated for the FQDN
- ansible issue at docker starting containers can be caused by missing apps/.../compose.yml. this is because docker wants to include all composes defined in the root .env file, remove the corresponding line (KEYCLOAK_COMPOSE_PATH=...)