#nesting dictionary
a1 = {'color':'green','points':5}
a2 = {'color':'yellow','points':10}
a3 = {'color':'red','points': 15}

a = [a1 , a2 , a3]

print(a)

for alien in a:
    print(alien)
    