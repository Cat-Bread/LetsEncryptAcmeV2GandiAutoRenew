#!/bin/bash
echo $CERTBOT_VALIDATION > /var/www/html/.well-known/acme-challenge/$CERTBOT_VALIDATION
python /opt/certbot/renew/updatenskey.py $CERTBOT_VALIDATION
