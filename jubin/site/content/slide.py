# -*- coding: utf-8 -*-

"""Definition of the Jubin site content types
"""

from zope.interface import implements, directlyProvides
from zope.component import adapts, getMultiAdapter

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.validation import V_REQUIRED

from jubin.site import siteMessageFactory as _
from jubin.site.interfaces import IJubinSlide
from jubin.site.config import PROJECTNAME

from jubin.site.content import base as jubinbase


JubinSlideSchema = base.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField('category',
        required = True,
        default = 'News',
        widget = atapi.StringWidget(
            description = u'',
            label = u'Catégorie',)
        ),

    #atapi.StringField('text_ligne1',
    #    widget = atapi.StringWidget(
    #        description = u'',
    #        label = u'Texte - Ligne 1',)
    #    ),

    #atapi.StringField('text_ligne2',
    #    widget = atapi.StringWidget(
    #        description = u'',
    #        label = u'Texte - Ligne 2',)
    #    ),

    #atapi.StringField('text_ligne3',
    #    widget = atapi.StringWidget(
    #        description = u'',
    #        label = u'Texte - Ligne 3',)
    #    ),

    atapi.FileField('flash_file',
              required=False,
              primary=True,
              searchable=True,
              languageIndependent=True,
              storage = atapi.AnnotationStorage(migrate=True),
              validators = (('isNonEmptyFile', V_REQUIRED),),
              widget = atapi.FileWidget(
                        description = '',
                        label=u'Fichier Flash',
                        show_content_type = False,)),

    atapi.StringField('url',
        required = False,
        validators = ('isURL',),
        widget = atapi.StringWidget(
            description = u'',
            label = u'URL',
            size = 60)
        ),

), marshall = atapi.PrimaryFieldMarshaller()
)

JubinSlideSchema.addField(jubinbase.JubinPhotoField.copy())

schemata.finalizeATCTSchema(JubinSlideSchema)

class JubinSlide(base.ATCTContent):
    """Jubin Slide type"""
    implements(IJubinSlide)

    schema = JubinSlideSchema
    meta_type = "JubinSlide"
    
    #security = ClassSecurityInfo()


atapi.registerType(JubinSlide, PROJECTNAME)


