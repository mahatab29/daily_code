# Dictionary in Dictionary
users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },

}

for username,userinfo in users.items():
    print(f"\nUsername:{username.title()}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
    
