

## Info

netbox app.

extra steps to create superuser, install plugins, use dc exec:
```shell
docker compose exec -u 1000 netbox /app/netbox/netbox/manage.py createsuperuser --username admin --email example.com

docker compose exec netbox pip install netboxlabs-netbox-branching
```