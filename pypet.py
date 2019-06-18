print('Welcome to Pypet!')

cat = {
    'name': 'Saffy Jr.',
    'age': 1,
    'weight': 35.5,
    'hungry': True,
    'photo' : '(=^o.o^=)__'
}

mouse = {
    'name': 'Mousey',
    'age': 2,
    'weight': 9.7,
    'hungry': True,
    'photo': '<:3 )~~~~'
}

pets = [cat, mouse]

def feed(pet):
    if pet['hungry']== True:
        pet['hungry']= False
        pet['weight']= pet['weight'] + 1
    else:
        print (pet['name'] + ' is not hungry')
    
for pet in pets:
    print ('Hello ' + pet['name'])
    print (pet['photo'])
    feed(pet)
    print (pet)
    feed(pet)
    print (pet)