#!/usr/bin/env python
# encoding: utf-8
boolean = str

def convert(value, type):
    """ Convert / Cast function """
    try:

        if issubclass(type,str) and not (value.upper() in ['FALSE','TRUE']):
            return str(value)
        elif issubclass(type,unicode):
            return unicode(value)
        elif issubclass(type,int):
            return int(value)
        elif issubclass(type,float):
            return float(value)
        elif issubclass(type,boolean) and (value.upper() in ['FALSE','TRUE']):
            if str(value).upper() == 'TRUE': return True
            elif str(value).upper() == 'FALSE': return False
        elif issubclass(type,list):
            # TODO
            value = value.strip('[]')
            return [ item for item in value.split(',') ]
        else:
            return value

    except:
        # may raise an error here
        pass
