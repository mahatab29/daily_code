responses = {}
polling_active = True
while polling_active:
    name = input("what's your name : ")
    response = input("what is favorite language: ")
    responses[name]=response
    repeat = input("wanna repeat again y/n :")
    if repeat == "n" :
        polling_active = False

print(responses)
