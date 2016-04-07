import requests


def lookup(number):
    """Look up a given number against the OpenCNAM API."""
    res = requests.get("https://api.opencnam.com/v2/phone/%s" % number)
    return res.content.decode()


def getName():
    """Return the name of this plugin."""
    return "OpenCNAM"
