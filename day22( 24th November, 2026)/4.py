def person_info(first_name, last_name, age = None):
    person = {'first name': first_name, 'last name': last_name,}
    if age:
        person['age'] = age
    return person

a = person_info('Mahatab', 'islam', age= 21)
print(a)
