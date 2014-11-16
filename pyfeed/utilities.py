#!/venv/bin/env python
#Copyright Melvin me@melvinphilips.com
def getlistitem(listitems, item):
    ''' returns the desired item of a list if available otherwise return None'''
    if item in listitems:
        return listitems[item]
    else:
        return None
