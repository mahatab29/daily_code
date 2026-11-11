favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
friend = ['phil','sarah']

for name in favorite_language:
    print(f"Hi, {name.title()}")

    if name in friend :
        language = favorite_language[name].title()
        print(f"\t{name} favorite languae is {language}")

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")
    