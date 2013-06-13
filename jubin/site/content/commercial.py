"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinCommercialPartner
from jubin.site.config import PROJECTNAME

from jubin.site.content import base as jubinbase

# Maps imports
from Products.Maps.field import LocationField, LocationWidget
from Products.Maps import interfaces as mapfaces


# Commercial Partner content type

JubinCommercialPartnerSchema = jubinbase.BasePartnerSchema + atapi.Schema((

    atapi.StringField(
            'reduction',
            storage=atapi.AnnotationStorage(),
            required = True,
            widget = atapi.StringWidget(
                label=u"Reduction",
            ),
        ),

    atapi.StringField(
            'reductionConditions',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.StringWidget(
                label=u"Conditions",
            ),
        ),


))

#JubinCommercialPartnerSchema.addField(jubinbase.JubinPhotoField.copy())
jubinbase.finalizeJubinPartnerSchema(JubinCommercialPartnerSchema, 
                              noSectorUsage=True, 
                              noDisplay=['text', 'privatePhone' ],
                              )

class JubinCommercialPartner(jubinbase.BasePartner):
    """Jubin Commercial Partner type"""
    implements(IJubinCommercialPartner)

    schema = JubinCommercialPartnerSchema
    meta_type = "JubinCommercialPartner"
    
    #security = ClassSecurityInfo()

    reduction = atapi.ATFieldProperty('reduction')
    reductionConditions = atapi.ATFieldProperty('reductionConditions')

atapi.registerType(JubinCommercialPartner, PROJECTNAME)


