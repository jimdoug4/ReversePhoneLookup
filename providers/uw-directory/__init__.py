"""Search the UW Directory."""
try:
    import ldap3
    SERVER_ADDRESS = 'directory.washington.edu'
    conn = ldap3.Connection(SERVER_ADDRESS, auto_bind=True)
    ready = True
    ready_reason = None
except ImportError:
    ready = False
    ready_reason = "Requires the ldap3 library"
except ldap3.core.exceptions.LDAPSocketOpenError:
    ready = False
    ready_reason = "Unable to connect to %s" % SERVER_ADDRESS

BASE_DN = 'ou=People,o=University of Washington,c=US'


def lookup(number):
    """Look for any entires in the UW directory with the given number."""
    if not ready:
        return None
    number = "+%s %s %s-%s" % (number[0], number[1:4], number[4:7], number[7:11])
    query = "(|(telephoneNumber=%s)(homePhone=%s))" % (number, number)
    conn.search(BASE_DN,  query, attributes=['cn', 'mail'])
    if len(conn.entries) > 0:
        return "%s <%s>" % (conn.entries[0]['cn'], conn.entries[0]['mail'])
    else:
        return None


def getName():
    """Return the name of this plugin."""
    return "UW Directory"


def isReady():
    """Return the status of the plugin."""
    return ready, ready_reason
