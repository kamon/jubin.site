"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinStationPartner
from jubin.site.interfaces import IJubinStationLocation
from jubin.site.config import PROJECTNAME

from jubin.site.content import base as jubinbase

# Maps imports
from Products.Maps.field import LocationField, LocationWidget
from Products.Maps import interfaces as mapfaces

from Products.Maps.adapters import GeoLocation

#from Products.Maps.content.Location import Location
#from Products.Maps.content.Location import LocationSchema

# Station Partner content type

JubinMapSchema = atapi.Schema((

    LocationField(
            'geolocation',
            languageIndependent = True,
            required=False,
            validators=('isGeoLocation',),
            widget = LocationWidget(
                label='Location',
                label_msgid='label_geolocation',
                description_msgid='help_geolocation',
                i18n_domain='maps',
            ),
        ),

     atapi.StringField(
             'markerIcon',
             languageIndependent = True,
             vocabulary="getMarkerIconVocab",
             enforceVocabulary=True,
             widget = atapi.SelectionWidget(
                 format="select",
                 label='Marker icon',
                 label_msgid='label_markericon',
                 description_msgid='help_markericon',
                 i18n_domain='maps',
             ),
         ),

))

JubinStationPartnerSchema = jubinbase.BasePartnerSchema + atapi.Schema((

    atapi.TextField(
        'opening',
        storage=atapi.AnnotationStorage(),
        widget = atapi.TextAreaWidget(
                label=u'''Horaires d'ouverture''',
            ),
        ),

    # no display
    atapi.BooleanField(
            'sp95',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='SP 95',
            ),
        ),

    # no display
    atapi.BooleanField(
            'sp98',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='SP 98',
            ),
        ),

    # no display
    atapi.BooleanField(
            'diesel',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='DIESEL',
            ),
        ),

    # no display
    atapi.BooleanField(
            'gaz',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='GAZ',
            ),
        ),

    atapi.BooleanField(
            'shop',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='SHOP',
            ),
        ),

    atapi.BooleanField(
            'lavage',
            storage=atapi.AnnotationStorage(),
            required = False,
            widget = atapi.BooleanWidget(
                label='LAVAGE',
            ),
        ),

)) + JubinMapSchema

JubinStationPartnerSchema.addField(jubinbase.JubinPhotoField.copy())
jubinbase.finalizeJubinPartnerSchema(JubinStationPartnerSchema, 
                              noSectorUsage=True, 
                              noDisplay=['text', 'sp95', 'sp98', 'diesel', 'gaz', 'privatePhone']
                              )

class JubinStationPartner(jubinbase.BasePartner):
    """Jubin Station Partner type"""
    implements(IJubinStationPartner,  
               IJubinStationLocation,         
               mapfaces.IMapEnabled, 
               )   # Enable map support for stations

    schema = JubinStationPartnerSchema

    #title = atapi.ATFieldProperty('title')
    #description = atapi.ATFieldProperty('description')
    
    opening = atapi.ATFieldProperty('opening')

    sp95 = atapi.ATFieldProperty('sp95')
    sp98 = atapi.ATFieldProperty('sp98')
    diesel = atapi.ATFieldProperty('diesel')
    gaz = atapi.ATFieldProperty('gaz')
    shop = atapi.ATFieldProperty('shop')
    lavage = atapi.ATFieldProperty('lavage')
    
    meta_type = "JubinStationPartner"
    
    security = ClassSecurityInfo()

    # Taken from Products.Maps

    security.declarePublic("getMarkerIconVocab")
    def getMarkerIconVocab(self):
        config = getMultiAdapter((self, self.REQUEST), name="maps_configuration")
        marker_icons = config.marker_icons
        result = atapi.DisplayList()
        for icon in marker_icons:
            result.add(icon['name'], icon['name'])
        return result

    security.declarePublic("getDefaultLocation")
    def getDefaultLocation(self):
        config = getMultiAdapter((self, self.REQUEST), name="maps_configuration")
        return config.default_location

atapi.registerType(JubinStationPartner, PROJECTNAME)



class LocationMarker(GeoLocation):
    implements(mapfaces.IRichMarker)
    adapts(IJubinStationLocation)

    @property
    def title(self):
        return self.context.Title()

    @property
    def description(self):
        return self.context.Description()

    @property
    def layers(self):
        return self.context.Subject()

    @property
    def icon(self):
        return self.context.getMarkerIcon()

    @property
    def url(self):
        return self.context.absolute_url()

    @property
    def related_items(self):
        related = self.context.computeRelatedItems()
        result = []
        for obj in related:
            result.append({'title': obj.Title(),
                           'url': obj.absolute_url(),
                           'description': obj.Description()})
        return tuple(result)

    @property
    def contents(self):
        context = self.context

        zip = context.zip
        
        city_vocab = context.getField('city').Vocabulary()
        city = city_vocab.getValue(context.city)   # fix the infamous UnicodeDecodeError bug
        city = city.encode('utf8')
        
        url = context.absolute_url()
        
        html = """<div style="padding-left: 0; margin-left: -38px" >
                        <strong>%s %s</strong>
                      </div>
                   """ % (zip, city)

        #photo = context.getImage()
        #if photo.get_size():
        html = html + """<div class="stationPhotoContainer" style="padding-left: 0; margin-left: -38px" > 
                              <a href="%s" >
                               <img src="%s" alt="%s" />
                              </a>
                             </div>""" % (url + '/image/image_view_fullscreen',
                                          url + '/image_googlemap',
                                          self.title)

        if html:
            return ({'title': _("Info"),
                     'text' : html,},)

