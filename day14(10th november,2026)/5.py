alien_0 = {'x_position':0 , 'y_position': 25, 'speed':'medium'}
print(f"Original position is {alien_0['x_position']}")

#determining the position based of it's speed
if alien_0['speed'] == 'slow':
    x_increament = 1
elif alien_0['speed'] == 'medium':
    x_increament = 2
else:
    #this means it's very fast
    x_increament = 3

alien_0['x_position'] = alien_0['x_position'] + x_increament

print(f"New position: {alien_0['x_position']}")
