from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.contacts.interfaces import IOrganization

from jubin.site import siteMessageFactory as _

from plone.theme.interfaces import IDefaultPloneLayer


class IJubinSiteSpecific(IDefaultPloneLayer):
    """ A marker interface that defines a Zope 3 browser layer. """



class IJubinStationLocation(Interface):
    """Interface for Station with a 'geolocation' field."""



class IJubinSlide(Interface):
    """Jubin Slide type for banner"""
    
    # -*- schema definition goes here -*-


class IJubinAddressBook(Interface):
    """Jubin AddressBook type"""
    
    # -*- schema definition goes here -*-



class IBasePartner(IOrganization):
    """Base Partner type"""
    
    # -*- schema definition goes here -*-

    contactName = schema.TextLine(
        title=_(u"Contact"),
        required=False,
        description=_(u""),
    )

    privatePhone = schema.TextLine(
        title=_(u"Private phone"),
        required=False,
        description=_(u""),
    )


class IJubinStationPartner(IBasePartner):
    """Jubin Station type"""
    
    # -*- schema definition goes here -*-

    opening = schema.Text(
        title=_(u'''Horaires d'ouverture'''),
        required=False,
        description=_(u""),
    )

    sp95 = schema.Bool(
        title=_(u"SP 95"),
        required=False,
        description=_(u""),
    )

    sp98 = schema.Bool(
        title=_(u"SP 98"),
        required=False,
        description=_(u""),
    )

    diesel = schema.Bool(
        title=_(u"DESIEL"),
        required=False,
        description=_(u""),
    )

    gaz = schema.Bool(
        title=_(u"GAZ"),
        required=False,
        description=_(u""),
    )
    
    shop = schema.Bool(
        title=_(u"SHOP"),
        required=False,
        description=_(u""),
    )

    lavage = schema.Bool(
        title=_(u"LAVAGE"),
        required=False,
        description=_(u""),
    )
    
    
    
class IJubinRestaurantPartner(IBasePartner):
    """Description of the Example Type"""
    
    # -*- schema definition goes here -*-

class IJubinCommercialPartner(IBasePartner):
    """Description of the Example Type"""
    
    # -*- schema definition goes here -*-

    reduction = schema.TextLine(
        title=_(u"Reduction"),
        required=True,
        description=_(u""),
    )

    reductionConditions = schema.TextLine(
        title=_(u"Conditions"),
        required=False,
        description=_(u""),
    )



