"""A plugin to lookup numbers against the OpenCNAM API."""
try:
    import requests
    ready = True
    ready_reason = None
except ImportError:
    ready = False
    ready_reason = "Requires the requests library"


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


def isReady():
    """Return the status of the plugin."""
    return ready, ready_reason
