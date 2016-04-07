"""Search the UW Directory."""
try:
    import ldap3
    conn = ldap3.Connection('directory.washington.edu', auto_bind=True)
    ready = True
except ImportError:
    ready = False

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
