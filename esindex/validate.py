def user(data):
    if data.get('fullName') == None:
        data['fullName'] = None
    if data.get('age') == None:
        data['age'] = None
    if data.get('college') == None:
        data['college'] = None
    if data.get('author') == None:
        data['author'] = None
    if data.get('company') == None:
        data['company'] = None
    if data.get('company') == None:
        data['company'] = None
    if data.get('coverPicture') == None:
        data['coverPicture'] = {
            "url": None
        }
    return data

def house(data):
    if data.get('locality') == None:
        data['locality'] = {'name':None}
    if data.get('genderPref') == None:
        data['genderPref'] = None
    if data.get('city') == None:
        data['city'] = {'name': None}
    if data.get('genderPref') == None:
        data['genderPref'] = None
    if data.get('genderPref') == None:
        data['genderPref'] = None
    if data.get('location') == None:
        data['location'] = {
            'coordinates': {
                'lat': 28.507241,
                'lng': 77.064048
            }
        }
    if data.get('location') != None:
        if data['location'].get('coordinates') == None:
            data['location'] = {
                'coordinates': {
                    'lat': 28.507241,
                    'lng': 77.064048
                }
            }
    return data

def room(data):
    if data.get('coverPicture') == None:
        data['coverPicture'] = {
        "url": None
    }
    if data.get('rent') == None:
        data['rent'] = None
    if data.get('title') == None:
        data['title'] = None
    if data.get('createdAt') == None:
        data['createdAt'] = None
    return data

def dUser(data):
    if data.get('fullName') == None:
        data['fullName'] = None
    if data.get('age') == None:
        data['age'] = None
    if data.get('college') == None:
        data['college'] = None
    if data.get('company') == None:
        data['company'] = None
    if data.get('author') == None:
        data['author'] = None
    if data.get('coverPicture') == None:
        data['coverPicture'] = {
            "url": None
        }
    if data.get('createdAt') == None:
        data['createdAt'] = None
    return data

def dUserAttr(data):
    if data.get('dPrefBudget') == None:
            data['dPrefBudget'] = {'min': 0, 'max': 100000}
    if data.get('dPrefLocality') == None:
            data['dPrefLocality'] = {'name': None}
    if data.get('dPrefLocation') == None:
        data['dPrefLocation'] = {
        'coordinates': {
            'lat': 28.507241,
            'lng': 77.064048
        }
    }
    if data.get('dPrefLocation') != None:
       if data['dPrefLocation'].get('coordinates') == None:
            data['dPrefLocation'] = {
                'coordinates': {
                    'lat': 28.507241,
                    'lng': 77.064048
                }
            }
    return data
