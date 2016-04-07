"""A plugin to lookup numbers against the OpenCNAM API."""
try:
    import requests
    ready = True
except ImportError:
    ready = False


def lookup(number):
    """Look up a given number against the OpenCNAM API."""
    if not ready:
        return None
    res = requests.get("https://api.opencnam.com/v2/phone/%s" % number)
    cnam = res.content.decode()
    if cnam != "":
        return cnam
    else:
        return None


def getName():
    """Return the name of this plugin."""
    return "OpenCNAM"
