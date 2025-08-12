# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True

# Tell browsers to only access via HTTPS for the next year
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure session and CSRF cookies are sent only over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent clickjacking by disallowing the site in iframes
X_FRAME_OPTIONS = "DENY"

# Prevent the browser from guessing content types
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s built-in XSS protection
SECURE_BROWSER_XSS_FILTER = True

## 🔐 Deployment Security Configuration

To support HTTPS in production:

- An SSL/TLS certificate must be configured on the web server (e.g., Nginx, Apache).
- Example (Nginx config):
  ssl_certificate /etc/ssl/certs/yourdomain.crt;
  ssl_certificate_key /etc/ssl/private/yourdomain.key;

location / {
    proxy_pass http://127.0.0.1:8000;
}

- Ensure `ALLOWED_HOSTS` includes your live domain.
- Enable the Django security settings in `settings.py` (see Security section).

# 🔍 Security Review: Django HTTPS Configuration

## Implemented Security Features

- **HTTPS Redirection:** All HTTP requests are redirected to HTTPS via `SECURE_SSL_REDIRECT = True`.
- **HSTS:** Enforced with `SECURE_HSTS_SECONDS`, including subdomains and preloading.
- **Secure Cookies:** Both session and CSRF cookies are only transmitted over HTTPS.
- **Clickjacking Protection:** `X_FRAME_OPTIONS = "DENY"` blocks rendering in iframes.
- **Content-Type Sniffing Protection:** Enabled via `SECURE_CONTENT_TYPE_NOSNIFF`.
- **XSS Protection:** Browser filtering activated via `SECURE_BROWSER_XSS_FILTER`.

## Potential Improvements

- Use environment variables to switch security settings between development and production.
- Consider using a Content Security Policy (CSP) for advanced XSS mitigation.
