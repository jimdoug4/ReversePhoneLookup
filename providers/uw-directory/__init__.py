"""Search the UW Directory."""
import ldap3

conn = ldap3.Connection('directory.washington.edu', auto_bind=True)
BASE_DN = 'ou=People,o=University of Washington,c=US'


def lookup(number):
    """Look for any entires in the UW directory with the given number."""
    number = "+%s %s %s-%s" % (number[0], number[1:4], number[4:7], number[7:11])
    query = "(|(telephoneNumber=%s)(homePhone=%s))" % (number, number)
    conn.search(BASE_DN,  query, attributes=['cn'])
    if len(conn.entries) > 0:
        return conn.entries[0]['cn']
    else:
        return None


def getName():
    """Return the name of this plugin."""
    return "UW Directory"
