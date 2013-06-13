"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinRestaurantPartner
from jubin.site.config import PROJECTNAME

from jubin.site.content import base as jubinbase

# Maps imports
from Products.Maps.field import LocationField, LocationWidget
from Products.Maps import interfaces as mapfaces


# Restaurant Partner content type

JubinRestaurantPartnerSchema = jubinbase.BasePartnerSchema + atapi.Schema((



))

#JubinRestaurantPartnerSchema['image'].widget.visible = {'edit': 'invisible',
#                                                        'view': 'invisible'}
jubinbase.finalizeJubinPartnerSchema(JubinRestaurantPartnerSchema, 
                              noSectorUsage=True, 
                              noDisplay=['text', 'privatePhone'],
                              )

class JubinRestaurantPartner(jubinbase.BasePartner):
    """Jubin Restaurant Partner type"""
    implements(IJubinRestaurantPartner)

    schema = JubinRestaurantPartnerSchema
    meta_type = "JubinRestaurantPartner"
    
    #security = ClassSecurityInfo()


atapi.registerType(JubinRestaurantPartner, PROJECTNAME)


