my=['pizza','cake']
#this does not copy the list
friend=my
my.append('lol')
friend.append('ko')
print(f"my foods are: {my}")
print(f"friends food are: {friend}")
