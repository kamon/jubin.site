﻿# -*- coding: utf-8 -*-

"""Common configuration constants
"""

PROJECTNAME = 'jubin.site'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'JubinCommercialPartner': 'jubin.site: Add CommercialPartner',
    'JubinRestaurantPartner': 'jubin.site: Add RestaurantPartner',
    'JubinStationPartner': 'jubin.site: Add StationPartner',
    'JubinAddressBook': 'jubin.site: Add AddressBook',

    'JubinSlide': 'jubin.site: Add Slide',
}


JUBIN_STATES = [
   ('CH-BE', u'Berne'), 
   ('CH-FR', u'Fribourg'), 
   ('CH-GE', u'Genève'), 
   ('CH-JU', u'Jura'), 
   ('CH-NE', u'Neuchâtel'), 
   ('CH-TI', u'Tessin'), 
   ('CH-VS', u'Valais'), 
   ('CH-VD', u'Vaud'),
]

JUBIN_CITIES = [

('aigle', u'Aigle'),
('alle', u'Alle'),
('arconciel', u'Arconciel'),
('asuel', u'Asuel'),
('beurnevesin', u'Beurnevesin'),
('boecourt', u'Boecourt'),
('boncourt', u'Boncourt'),
('bonfol', u'Bonfol'),
('bourg-st-pierre', u'Bourg-St-Pierre'),
('carouge', u'Carouge'),
('carrouge', u'Carrouge'),
('chailly-montreux', u'Chailly-Montreux'),
('chalais', u'Chalais'),
('champex', u'Champex'),
('champex-lac', u'Champex-Lac'),
('chatel-st-denis', u'Chatel-St-Denis'),
('chatonnaye', u'Chatonnaye'),
('chene-bourg', u'Chêne-Bourg'),
('chermignon', u'Chermignon'),
('chevenez', u'Chevenez'),
('chippis', u'Chippis'),
('collombey', u'Collombey'),
('corban', u'Corban'),
('corcelles-payerne', u'Corcelles-Payerne'),
('cornol', u'Cornol'),
('cottens', u'Cottens'),
('courchapoix', u'Courchapoix'),
('courfaivre', u'Courfaivre'),
('courgenay', u'Courgenay'),
('courrendlin', u'Courrendlin'),
('courtemaiche', u'Courtemaiche'),
('courtetelle', u'Courtetelle'),
('crissier', u'Crissier'),
('cully', u'Cully'),
('damvant', u'Damvant'),
('delemont', u'Delémont'),
('develier', u'Develier'),
('dombresson', u'Dombresson'),
('estavayer-le-lac', u'Estavayer-le-lac'),
('fahy', u'Fahy'),
('farvagny', u'Farvagny'),
('ferreyres', u'Ferreyres'),
('fontenais', u'Fontenais'),
('fully', u'Fully'),
('geneve', u'Genève'),
('givisiez', u'Givisiez'),
('glovelier', u'Glovelier'),
('goppenstein', u'Goppenstein'),
('grandvaux', u'Grandvaux'),
('granges', u'Granges'),
('haute-nendaz', u'Haute-Nendaz'),
('la-chaux-de-fonds', u'La Chaux-de-Fonds'),
('la-chaux-du-milieu', u'La Chaux-du-Milieu'),
('le-noirmont', u'Le Noirmont'),
('les-bois', u'Les Bois'),
('les-breuleux', u'Les Breuleux'),
('les-paccots', u'Les Paccots'),
('les-ponts-de-martel', u'Les Ponts-de-Martel'),
('lucelle', u'Lucelle'),
('lully', u'Lully'),
('lully-estavayer-le-lac', u'Lully - Estavayer-le-lac'),
('martigny', u'Martigny'),
('mase', u'Mase'),
('meinier', u'Meinier'),
('miecourt', u'Miécourt'),
('montbrelloz', u'Montbrelloz'),
('moudon', u'Moudon'),
('oron-la-ville', u'Oron-la-ville'),
('orsieres', u'Orsieres'),
('payerne', u'Payerne'),
('peney-vuiteboeuf', u'Peney-Vuiteboeuf'),
('pleujouse', u'Pleujouse'),
('porrentruy', u'Porrentruy'),
('prayon', u'Prayon'),
('rarogne', u'Rarogne'),
('rebeuvelier', u'Rebeuvelier'),
('rennaz', u'Rennaz'),
('riddes', u'Riddes'),
('rossens', u'Rossens'),
('saignelegier', u'Saignelegier'),
('saillon', u'Saillon'),
#('saint-martin', u'Saint-Martin'),
('st-martin', u'St-Martin'),
('saint-ursanne', u'Saint-Ursanne'),
('saulcy', u'Saulcy'),
('sierre', u'Sierre'),
('soyhieres', u'Soyhieres'),
('tatroz', u'Tatroz'),
('tramelan', u'Tramelan'),
('vallorbe', u'Vallorbe'),
('vermes', u'Vermes'),
('vers-chez-perrin', u'Vers-chez-Perrin'),
('villars-sur-fontenais', u'Villars-sur-Fontenais'),
('villeneuve', u'Villeneuve'),
('vuarrens', u'Vuarrens'),
('vuisternens-dt-romont', u'Vuisternens-devant-Romont'),

]


# SWISS_CITIES_BY_STATES = {
#
#    'CH-AG' : {'name': u'Aargau',
#               'cities': []},
#    'CH-AR' : {'name': u'Appenzell Ausser-Rhoden',
#               'cities': []},
#    'CH-AI' : {'name': u'Appenzell Inner-Rhoden',
#               'cities': []},
#    'CH-BL' : {'name': u'Basel-Landschaft',
#               'cities': []},
#    'CH-BS' : {'name': u'Basel-Stadt',
#               'cities': []},
#    'CH-BE' : {'name': u'Bern',
#               'cities': [u'Bévilard', u'Court', u'Perrefitte', u'Tramelan',]},
#    'CH-FR' : {'name': u'Fribourg',
#               'cities': [u'Arconciel', u'Châtel-St-Denis', u'Châtonnaye', u'Estavayer-le-Lac', u'Givisiez',
#                          u'Les Paccots', u'Lully',
#                          u'Montbrelloz', u'Rossens', u'Saint-Martin',
#                          u'Vuisternens-dt-Romont', u'Treyvaux']},
#    'CH-GE' : {'name': u'Genève',
#               'cities': [u'Genève',]},
#    'CH-GL' : {'name': u'Glarus',
#               'cities': []},
#    'CH-GR' : {'name': u'Graubünden',
#               'cities': []},
#    'CH-JU' : {'name': u'Jura',
#               'cities': [u'Alle', u'Asuel', u'Beurnevésin', u'Boncourt', u'Bonfol',
#                          u'Chevenez', u'Corban', u'Cornol', u'Courchapoix',
#                          u'Courfaivre', u'Courgenay', u'Courtemaîche',
#                          u'Damvant', u'Delémont', u'Develier', u'Fahy',
#                          u'Grandfontaine',
#                          u'Le Noirmont', u'Les Bois', u'Les Breuleux', u'Lucelle',
#                          u'Miécourt', u'Pleujouse', u'Porrentruy', u'Rebeuvelier', u'Reconvilier',
#                          u'Saignelégier', u'Saint-Ursanne', u'Saulcy', u'Soyhières',
#                          u'Vellerat', u'Vermes', ]},
#    'CH-LU' : {'name': u'Luzern',
#               'cities': []},
#    'CH-NE' : {'name': u'Neuchâtel',
#               'cities': [u'Brot-Plamboz', u'Dombresson',
#                          u'La Chaux-de-Fonds', u'La Chaux-du-Milieu',
#                          u'Les Ponts-de-Martel', ]},
#    'CH-NW' : {'name': u'Nidwalden',
#               'cities': []},
#    'CH-OW' : {'name': u'Obwalden',
#               'cities': []},
#    'CH-SG' : {'name': u'Sankt Gallen',
#               'cities': []},
#
#    'CH-SH' : {'name': u'Schaffhausen',
#               'cities': []},
#    'CH-SZ' : {'name': u'Schwyz',
#               'cities': []},
#    'CH-SO' : {'name': u'Solothurn',
#               'cities': []},
#    'CH-TG' : {'name': u'Thurgau',
#               'cities': []},
#
#    'CH-TI' : {'name': u'Ticino',
#               'cities': []},
#    'CH-UR' : {'name': u'Uri',
#               'cities': []},
#    'CH-VS' : {'name': u'Valais',
#               'cities': [u'Bourg-St-Pierre', u'Chalais', u'Champex', u'Champex-Lac',u'Chermignon', u'Chippis',
#                          u'Fully', u'Goppenstein', u'Granges', u'Haute-Nendaz',
#                          u'Martigny', u'Mase', u'Orsières', u'Prayon',
#                          u'Rarogne', u'Riddes', u'Saillon', u'Sierre', ]},
#    'CH-VD' : {'name': u'Vaud',
#               'cities': [u'Aigle', u'Carrouge', u'Chailly-Montreux', u'Corcelles-Payerne',
#                          u'Cottens', u'Crissier', u'Cully', u'Echallens', u'Ferreyres', u'Grandvaux',
#                          u'Le Pont-Vallorbe', u'Moudon',
#                          u'Oron-la-Ville', u'Peney-Vuiteboeuf', u'Rennaz',
#                          u'Vallorbe', u'Vers-chez-Perrin', u'Villeneuve', u'Vuarrens',]},
#    'CH-ZG' : {'name': u'Zug',
#               'cities': []},
#    'CH-ZH' : {'name': u'Zürich',
#               'cities': []},
# }



