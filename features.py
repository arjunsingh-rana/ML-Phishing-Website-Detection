from urllib.parse import urlparse
import re


# Common phishing-related words
SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "bank",
    "account",
    "paypal",
    "signin",
    "password",
]


# Frequently abused TLDs
SUSPICIOUS_TLDS = [
    "xyz",
    "top",
    "club",
    "online",
    "live",
    "click",
    "shop",
]


def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()

    # Normalize hostname: prepend 'www.' if it does not start with it and is not an IP address
    if hostname and not hostname.startswith("www."):
        if not re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname):
            hostname = "www." + hostname
            parsed = parsed._replace(netloc=hostname)
            url = parsed.geturl()

    path = parsed.path.lower()

    features = {}

    # 1 URL Length
    features["url_length"] = len(url)

    # 2 Hostname Length
    features["hostname_length"] = len(hostname)

    # 3 Number of Dots
    features["dot_count"] = url.count(".")

    # 4 Number of Hyphens
    features["hyphen_count"] = url.count("-")

    # 5 Number of Digits
    features["digit_count"] = sum(c.isdigit() for c in url)

    # 6 HTTPS
    features["https"] = 1 if parsed.scheme == "https" else 0

    # 7 Number of Subdomains
    features["subdomain_count"] = max(hostname.count(".") - 1, 0)

    # 8 Contains IP Address
    features["has_ip"] = (
        1
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname)
        else 0
    )

    # 9 Suspicious Keywords
    features["suspicious_keyword"] = (
        1
        if any(word in url.lower() for word in SUSPICIOUS_WORDS)
        else 0
    )

    # 10 Suspicious TLD
    tld = hostname.split(".")[-1]

    features["suspicious_tld"] = (
        1
        if tld in SUSPICIOUS_TLDS
        else 0
    )

    return features