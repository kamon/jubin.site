"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinAddressBook
from jubin.site.config import PROJECTNAME

#from jubin.site.content import base as jubinbase

from collective.contacts.content.addressbook import AddressBook
from collective.contacts.content.addressbook import AddressBookSchema



# Partners Container / AddressBook type

class JubinAddressBook(AddressBook):
    """Jubin AddressBook type"""
    implements(IJubinAddressBook)

    meta_type = "JubinAddressBook"
    schema = AddressBookSchema.copy()

    # Here i will list the fields that should be shown by default in
    # the table view for organizations
    show_on_organizations_view = [('title', True),
                                  #('sector', True),
                                  #('sub_sector', True),
                                  ('phone', True),
                                  ('fax', True),
                                  ('email', True),
                                  #('web', True),
                                  ('address', True),
                                  ('city', True),
                                  #('country', True),
                                  ('state', False),
                                  ('zip', False),
                                  #('extraAddress', False),
                                  #('email2', False),
                                  #('email3', False),
                                  #('text', False),
                                  ]



atapi.registerType(JubinAddressBook, PROJECTNAME)

