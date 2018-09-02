# GandiCertbotAcmeV2AutoRenew

### Use to automatically renew LetsEncrypt.org wildcard SSL certificates with Certbot for Gandi hosted domains


Issue initial [Let's Encrypt](https://letsencrypt.org/) certificate using [Certbot](https://certbot.eff.org/) manually:
```
certbot-auto certonly --manual --preferred-challenges=dns --email your@email.com --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.domain.com
```

Edit **config-updatednskey** with relevant information:
- Gandi API key
- Domain
- Gandi Production API
- Acme-Challenge path

Automatically renew certificates with **renew-letsencrypt-cert** script.
```
certbot-auto renew --manual-auth-hook authenticator.sh --manual-cleanup-hook cleanup.sh
```
