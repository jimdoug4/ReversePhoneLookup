#!/usr/bin/env python
"""A took to find information about phone numbers."""
import os
import imp
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('settings.ini')


def lookup(number):
    """Look up a phone number against all providers."""
    providers_dir = "./providers"
    if "providers" in config and "folder" in config['providers']:
        providers_dir = config['providers']['folder']
    providers = os.listdir(providers_dir)
    for provider_name in providers:
        location = os.path.join(providers_dir, provider_name)
        if not os.path.isdir(location) or "__init__.py" not in os.listdir(location):
            continue
        info = imp.find_module("__init__", [location])
        provider = imp.load_module("__init__", *info)
        if provider_name in config:
            provider.configure(config[provider_name])
        if number is None:
            name = provider.getName()
            ready, reason = provider.isReady()
            msg = "* %s" % name
            if not ready:
                msg = "%s (Not ready: %s)" % (msg, reason)
            print(msg)
        else:
            ready, reason = provider.isReady()
            if ready:
                result = provider.lookup(number)
                if result is not None:
                    print("%s: %s" % (provider.getName(), result))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lookup(sys.argv[1])
    else:
        print("Usage: %s <number>\nLooks up <number> against the following sources:\n" %
              sys.argv[0])
        lookup(None)
