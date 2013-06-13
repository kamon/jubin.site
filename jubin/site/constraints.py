# -*- coding: utf-8 -*-
#import datetime
import re

# Functions we need for our specific constraints, for fields validation

def is_digit(value):
    return value.isdigit()

def is_ch_zip(value):
    if re.compile("^\d{4}$").match(value):
        return True
    return False

def is_not_novalue(value):
    if value:
        if str(value) != '--NOVALUE--':
            return True
    return False     
