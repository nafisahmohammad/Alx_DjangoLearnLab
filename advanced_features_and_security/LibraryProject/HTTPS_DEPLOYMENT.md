# HTTPS Deployment Configuration

To enable HTTPS in production, an SSL/TLS certificate must be configured on the web server.

Example (Nginx):

- Install SSL certificate (e.g. using Let's Encrypt)
- Configure server block to listen on port 443
- Add SSL certificate and key paths

HTTP traffic is redirected to HTTPS using Django setting:

SECURE_SSL_REDIRECT = True

HSTS headers are enforced using:

SECURE_HSTS_SECONDS
SECURE_HSTS_INCLUDE_SUBDOMAINS
SECURE_HSTS_PRELOAD
