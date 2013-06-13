# -*- coding: utf-8 -*-

def reindexCatalog(context):
    """
    This method will reindex the new indexes added to the catalog
    """
    from Products.CMFCore.utils import getToolByName
    site = context.getSite()
    cat = getToolByName(site, 'portal_catalog')
    cat.reindexIndex('state', site.REQUEST)
    cat.reindexIndex('zip', site.REQUEST)
    cat.reindexIndex('city', site.REQUEST)
