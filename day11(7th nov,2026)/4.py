banned_user = ['andrew', 'carolina' , 'david']
user=input("enter your name: ")
if user in banned_user :
    print(f"{user.title()}, you can post a response if you wish")
else:
    print(f"{user.title()} welcome to the programme")
    