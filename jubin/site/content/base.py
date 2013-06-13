"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.document import ATDocumentBase

from Products.validation import V_REQUIRED

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinAddressBook, IBasePartner, IJubinStationPartner
from jubin.site.config import PROJECTNAME

## Maps imports
#from Products.Maps.field import LocationField, LocationWidget
#from Products.Maps import interfaces as mapfaces 

from Products.AddRemoveWidget import ComboBoxWidget

from collective.contacts.content.addressbook import AddressBook
from collective.contacts.content.addressbook import AddressBookSchema

from collective.contacts.content.organization import Organization
from collective.contacts.content.organization import OrganizationSchema



## Utility functions #############################################

def finalizeJubinPartnerSchema(schema, noSectorUsage=True, noDisplay=[]):
    """Finalizes an type schema to alter some fields
    """

    if noSectorUsage:
        for f in ('sector', 'sub_sector'):
            schema[f].default = u'??NA'
            schema[f].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

    # Switzerland
    schema['country'].default = 'CH'

    # Modify 'text' field
    schema["text"].widget = atapi.TextAreaWidget(label=u"Notes diverses")

    # Fields to hide
    toHide = ['email2', 'email3', 
              #'web',
              'country', ]
    for f in toHide:
        schema[f].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

    # Fields to not display
    for f in noDisplay:
        schema[f].widget.visible['view'] = 'invisible'

    # Display state on base_view
    schema['state'].widget.visible['view'] = 'visible'

    # Other
    schema['zip'].widget.label = u'NPA'

    schema['web'].widget.label = u'URL du site ou page web'
    schema['web'].widget.description = u'''URL d'un site ou page web pour en savoir plus'''

    return schema


# Base fields, schemas, and class definitions

JubinPhotoField = atapi.ImageField('image',
                                   required = False,
                                   storage = atapi.AnnotationStorage(migrate=True),
                                   languageIndependent = True,
                                   #max_size = zconf.ATNewsItem.max_image_dimension,
                                   sizes= {'large'       : (768, 768),
                                           'preview'     : (400, 400),
                                           'googlemap'   : (320, 320),
                                           'mini'        : (200, 200),
                                           'thumb'       : (128, 128),
                                           'tile'        :  (64, 64),
                                           'icon'        :  (32, 32),
                                           'listing'     :  (16, 16),
                                          },
                                   validators = (('isNonEmptyFile', V_REQUIRED),),
                                   widget = atapi.ImageWidget(
                                                description = "",
                                                label= u'Photo',
                                                show_content_type = False)
                                            )


JubinAddressSchema = atapi.Schema((

    # redefining State / Canton field (selection)
    atapi.StringField(
        'state',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=u"Canton",
        ),
        vocabulary_factory='jubin.states',
        required=True,
        #searchable=1,
    ),

    # redefining City field (selection)
    atapi.StringField(
        'city',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=u"Ville",
        ),
        vocabulary_factory='jubin.cities',
        required=True,
        #searchable=1,
    ),

))

JubinExtraSchema = atapi.Schema((

    atapi.StringField(
            'contactName',
            storage=atapi.AnnotationStorage(),
            widget = atapi.StringWidget(
                label=u"Contact",
            ),
        ),

    # no display // TODO : Hide that in edit mode for Station 
    atapi.StringField(
        'privatePhone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Private phone"),
            description=_(u""),
        ),
    ),


))


BasePartnerSchema = OrganizationSchema.copy() \
                      + JubinAddressSchema \
                      + JubinExtraSchema

# Re-enable 'description' field for Jubin base schema - Optional but may be useful for all partner types
BasePartnerSchema['description'].widget.visible = {'edit': 'visible',
                                                    'view': 'visible'}
BasePartnerSchema['description'].widget.label = u'''Description de l'entreprise'''


class BasePartner(Organization):
    """Partner base type"""
    implements(IBasePartner)

    schema = BasePartnerSchema

    #title = atapi.ATFieldProperty('title')
    #description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    contactName = atapi.ATFieldProperty('contactName')
    privatePhone = atapi.ATFieldProperty('privatePhone')


    security = ClassSecurityInfo()

    # Jubin specifics


