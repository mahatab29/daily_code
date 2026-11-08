yoyo=[]
yoyo.append("i")
yoyo.append('mount')
yoyo.append('everest')
print(yoyo)
#when you append , you can't control the position of the element . That's why we use "insert" operation.
yoyo.insert(1, 'am')
print(yoyo)
yoyo.insert(2,"big")
print(yoyo)
#in remove method you don't need to know the position of the element, but in del method you must.
yoyo.remove('big')
print(yoyo)
del yoyo[2]
print(yoyo)
#pop method . controlling the position
hello=['honda', 'yamaha', 'suzuki']
hello_poped=hello.pop(0)
print(hello)
print(hello_poped)
#pop methond default 
hello_poped=hello.pop()
print(hello_poped)
print(hello)


