"""A plugin to lookup numbers against the Data 24/7 API."""
try:
    import requests
    ready = False
    ready_reason = "Not yet configured"
except ImportError:
    ready = False
    ready_reason = "Requires the requests library"

import json
user = None
passwd = None


def configure(config):
    """Configure the plugin."""
    global user, passwd, ready, ready_reason
    if "user" in config and "passwd" in config:
        user = config['user']
        passwd = config['passwd']
        ready = True
        ready_reason = None
    else:
        ready_reason = "Config needs both user and passwd"


def lookup(number):
    """Look up a gi`ven number against the Data 24/7 API."""
    global user, passwd
    url = "https://api.data24-7.com/v/2.0?api=I&user=%s&pass=%s&p1=%s&out=json" % (user, passwd,
                                                                                   number)
    res = requests.get(url).json()
    return res['response']['results'][0]['name']


def getName():
    """Return the name of this plugin."""
    return "Data 24/7"


def isReady():
    """Return the status of the plugin."""
    global user, passwd, ready, ready_reason
    url = "https://api.data24-7.com/v/2.0?api=B&user=%s&pass=%s&out=json" % (user, passwd)
    if ready:
        res = requests.get(url)
        try:
            data = res.json()
            if data['response']['results'][0]['status'] == "OK":
                ready_reason = "Balance: $%s" % data['response']['results'][0]['balance']
        except json.decoder.JSONDecodeError:
            ready = False
            ready_reason = res.content.decode()
    return ready, ready_reason
