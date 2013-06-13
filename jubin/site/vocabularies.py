# -*- coding: utf-8 -*-

import operator

from zope.interface import Interface, implements, implementer, alsoProvides
from zope.schema.interfaces import IVocabulary, IVocabularyFactory
from zope.app import zapi
from os import path

from zope.schema import vocabulary
from zope.schema import Iterable

#from Products.CMFCore.utils import getToolByName

import Products.CMFPlone.interfaces

import collective.contacts
from collective.contacts.iso3166 import CountriesStatesParser
from collective.contacts.vocabularies import TitledVocabulary

from jubin.site import siteMessageFactory as _

import config


# Utility functions

def normalize_name(cityname):
    # cityname is an unicode string : strip accents, turn spaces into '-', and lower.
    import unicodedata
    return unicodedata.normalize('NFKD', cityname).encode('ASCII', 'ignore').replace(' ', '-').lower()

def safe_decode(value):
    # Making sure we have unicode strings
    if isinstance(value, unicode):
        return value

    return unicode(value, 'utf-8')


# Swiss States

class ISwissStates(Interface):

    states = Iterable(
        title = _(u"Cantons"),
        description=_(u"Cantons suisses")
        )


class SwissStatesFromFile(object):
    """Countries utility that reads data from a file
    """
    implements(ISwissStates)

    # Commented out since e finlly use the config module to get the dt from 'JUBIN_STATES'
    #def __init__(self):
    #    iso3166_path = path.join(path.dirname(collective.contacts.vocabularies.__file__), 'iso3166')
    #    self.csparser = CountriesStatesParser(iso3166_path)
    #    self.csparser.parse()

    def states(self):
        #states = self.csparser.getStatesOf('CH')
        states = config.JUBIN_STATES
        #print states
        return states


@implementer(IVocabulary)
def SwissStates( context ):
    utility = zapi.getUtility(ISwissStates)
    return TitledVocabulary.fromTitles(utility.states())
alsoProvides(SwissStates, IVocabularyFactory)


# Swiss Cities

class ISwissCities(Interface):

    cities = Iterable(
        title = _(u"Villes"),
        description=_(u"Villes suisses")
        )


class SwissCitiesFromConfig(object):
    """Cities utility
    """
    implements(ISwissCities)

    def cities(self):
        # Augmenting the parametized_cities list with newly added cities (via the catalog)
        
        root = zapi.getUtility(Products.CMFPlone.interfaces.IPloneSiteRoot)
        propstool = root.portal_properties
        props = None
        if 'jubin_properties' in propstool.objectIds():
            props = propstool.jubin_properties

        config_cities = []
        results = []
        
        if props is not None:
            config_cities = props.getProperty('cities')

        for city in config_cities:
            city_id, city_name = tuple(city.split(':'))
            results.append((city_id, safe_decode(city_name)))
            
        #results = config.JUBIN_CITIES

        results = sorted(results,key=operator.itemgetter(0))
        #print results
        return results


@implementer(IVocabulary)
def SwissCities( context ):
    utility = zapi.getUtility(ISwissCities)
    return TitledVocabulary.fromTitles(utility.cities())
alsoProvides(SwissCities, IVocabularyFactory)


# Swiss Cities for search form

class ISwissCitiesForSearch(Interface):

    cities = Iterable(
        title = _(u"Villes"),
        description=_(u"Villes suisses")
        )

class SwissCitiesForSearchFromConfig(object):
    """Cities utility for search form - the list of cities here is contextual.
    """
    implements(ISwissCitiesForSearch)

    def cities(self, context):

        root = zapi.getUtility(Products.CMFPlone.interfaces.IPloneSiteRoot)
        cat = root.portal_catalog
        results = []
        keys = []
        
        ## All cities
        
        allcities_util = zapi.getUtility(ISwissCities)
        allcities = allcities_util.cities()
        #print allcities
        allcities_dict = dict(allcities)
        
        # Contextualize the list
        brains = cat({'portal_type': ['JubinStationPartner','JubinRestaurantPartner','JubinCommercialPartner',],
                      'path': '/'.join(context.getPhysicalPath())
                      })
                      
        for brain in brains:
            obj = brain.getObject()
            city_key = obj.city
            if city_key in keys:
                continue
            keys.append(city_key)
        
        # Now build the list of key/value pairs
        for k in keys:
            v = allcities_dict.get(k, '')
            if v:
                results.append((k, v))

        results = sorted(results,key=operator.itemgetter(0))
        return results


@implementer(IVocabulary)
def SwissCitiesForSearch( context ):
    utility = zapi.getUtility(ISwissCitiesForSearch)
    return TitledVocabulary.fromTitles(utility.cities(context))
alsoProvides(SwissCitiesForSearch, IVocabularyFactory)


