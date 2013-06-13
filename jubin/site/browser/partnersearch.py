# -*- coding: utf-8 -*-
## Copyright (C) 2009 Groupe IGS - all rights reserved
## No publication or distribution without authorization.

from Acquisition import aq_inner
import transaction

from zope.interface import Interface, implements
from zope.schema import Tuple, Choice, TextLine
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form import form, field, button
from plone.app.z3cform.layout import FormWrapper, wrap_form

from Products.Five.browser import BrowserView
from zope.app.pagetemplate import viewpagetemplatefile

from Products.CMFCore.utils import getToolByName
#from Products.statusmessages.interfaces import IStatusMessage

from jubin.site import siteMessageFactory as _

from jubin.site import constraints

#from zope.event import notify


## Zope Schema / z3c.form Fields

class IPartnerSearchForm(Interface):
    """The PartnerSearchForm schema.
    """

    search_zip = TextLine(title=_(u"par NPA"),
                            #description=_(u""),
                            required=False,
                            constraint=constraints.is_ch_zip,
                            )

    search_city = Choice(title=_(u"par ville"),
                            #description=_(u""),
                            vocabulary="jubin.searchcities",
                            required=False,
                            )
                            
    search_state = Choice(title=_(u"par canton"),
                            #description=_(u""),
                            vocabulary="jubin.states",
                            required=False,
                            )



## Trainers Form

class PartnerSearchForm(form.Form):
    """ Form for searching a partner
    """
    ignoreContext = True # don't need context to get widget data

    id = "partnersearch_form"

    label = u""

    template = viewpagetemplatefile.ViewPageTemplateFile('templates/partnersearch.pt')
    
    fields = field.Fields(IPartnerSearchForm)

        
    # Normal view methods
    
    @property
    def category(self):
    
        """ Get the category from the context or the request """
        
        request = self.request
        cat = self.context.getProperty('category','') or request.get('category','station')  # default is station
          
        return cat


    def getSearchQuery(self, zip="", city="", state=""):

        query = { 
                  'path':'/'.join(self.context.getPhysicalPath()),
                  'sort_on':'sortable_title',
                 }

        # Get portal_type param depending on category
        category = self.category
        if category == 'restaurant':
            query['portal_type'] = 'JubinRestaurantPartner'
        elif category == 'commerce':
            query['portal_type'] = 'JubinCommercialPartner'
        elif category == 'privilege':  # Is a commerce
            query['portal_type'] = 'JubinCommercialPartner'
        else:
            query['portal_type'] = 'JubinStationPartner'

        # Important: search with zip or city or state
        if zip:
            query['zip'] = zip  
        elif city:
            query['city'] = city
        elif state:
            query['state'] = state
            
        return query
        
    def getResults(self):
    
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        
        request = self.request           

        zip = request.get('search_zip', '')
        city = request.get('search_city', '')
        state = request.get('search_state', '')
        
        query = self.getSearchQuery(zip=zip, city=city, state=state)

        brains = portal_catalog(query)

        #print "%s results" % len(brains)

        # XXX: This getObject should be removed and done in a way
        # that we can ask the data from the catalog instead of getting
        # all the objects.
        results = [i.getObject() for i in brains]

        return results

    @button.buttonAndHandler(_(u'Rechercher'))
    def search(self, action):
        context = aq_inner(self.context)
        data, errors = self.extractData()

        if errors:
            self.status = u"Veuillez corriger les erreurs"
            return

        print data

        ## Redirect with query string
        
        # Get category
        category = self.category

        # Get other search criteria from the form data
        zip, city, state = "", "", ""
        qs = ""

        if data['search_zip']:
            zip = data['search_zip']
            qs = "category=%s&search_zip=%s" % (category, zip)
            
        elif data['search_city']:
            city = data['search_city']
            qs = "category=%s&search_city=%s" % (category, city)
            
        elif data['search_state']:
            state = data['search_state']
            qs = "category=%s&search_state=%s" % (category, state)

        #qs = "category=%s&search_zip=%s&search_city=%s&search_state=%s" % (category, zip, city, state)          
        self.request.RESPONSE.redirect(self.context.absolute_url() + '/partnersearch' + '?' + qs)


PartnerSearchFormView = wrap_form(PartnerSearchForm)



    
    
