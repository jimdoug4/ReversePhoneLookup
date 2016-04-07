#!/usr/bin/env python
"""A took to find information about phone numbers."""
import os
import imp
import sys

PROVIDERS_FOLDER = "./providers"


def lookup(number):
    """Look up a phone number against all providers."""
    providers = os.listdir(PROVIDERS_FOLDER)
    for provider in providers:
        location = os.path.join(PROVIDERS_FOLDER, provider)
        if not os.path.isdir(location) or "__init__.py" not in os.listdir(location):
            continue
        info = imp.find_module("__init__", [location])
        provider = imp.load_module("__init__", *info)
        if number is None:
            print("  * %s" % provider.getName())
        else:
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
