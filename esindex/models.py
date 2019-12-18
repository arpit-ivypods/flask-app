def user():
    mappings = {
        "mappings": {
            "properties": {
                "id": {
                    "type": "text"
                },
                "fullName": {
                    "type": "text"
                },
                "age": {
                    "type": "integer"
                },
                "college": {
                    "type": "text"
                },
                "qualification": {
                    "type": "text"
                },
                "company": {
                    "type": "text"
                },
                "coverPicture": {
                    "type": "nested",
                    "properties": {
                        "url": {
                            "type": "text"
                        }
                    }
                },
                "address": {
                    "type": "text"
                },
                "coordinates": {
                    "type": "geo_point"
                },
                "rent": {
                    "type": "nested",
                    "properties": {
                        "min": {
                            "type": "integer"
                        },
                        "max": {
                            "type": "integer"
                        }
                    }
                },
                "createdAt": {
                    "type": "date"
                }
            }
        }
    }
    return mappings

def rooms():
    mappings = {
        "mappings": {
            "properties": {
                
                "userId": {
                    "type": "text"
                },
                "id": {
                    "type": "text"
                },
                "houseId": {
                    "type": "text"
                },
                "fullName": {
                    "type": "text"
                },
                "age": {
                    "type": "integer"
                },
                "college": {
                    "type": "text"
                },
                "company": {
                    "type": "text"
                },
                "userCoverPicture": {
                    "type": "nested",
                    "properties": {
                        "url": {
                            "type": "text"
                        }
                    }
                },
                "roomCoverPicture": {
                    "type": "nested",
                    "properties": {
                        "url": {
                            "type": "text"
                        }
                    }
                },
                "coordinates": {
                    "type": "geo_point"
                },
                "rent": {

                    "type": "integer"

                },
                'genderPref': {
                    "type": "text"
                },
                "createdAt": {
                    "type": "date"
                },
                "title": {
                    "type": "text"
                }
            }
        }
    }
    return mappings
