# GandiCertbotAcmeV2AutoRenew

#### Use to automatically renew [Let's Encrypt](https://letsencrypt.org/) wildcard SSL certificates with [Certbot](https://certbot.eff.org/) for [Gandi](https://doc.rpc.gandi.net/domain/usage.html) hosted domains.


Manually issue initial Let's Encrypt certificate using Certbot (assumes installed to /opt/certbot/):
```
certbot-auto certonly --manual --preferred-challenges=dns --email your@email.com --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.domain.com -d domain.com
```

Edit **config-updatednskey** with relevant information:
- Gandi API key
- Domain
- Gandi Production API
- Acme-Challenge path

Automatically renew certificates with **renew-letsencrypt-cert** script:
```
certbot-auto renew --manual-auth-hook authenticator.sh --manual-cleanup-hook cleanup.sh
```
