# ================================
# SECURITY BEST PRACTICES
# ================================

# Turn off debug in production
DEBUG = False  

# Prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME-type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies only sent via HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Redirect HTTP to HTTPS (recommended)
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
