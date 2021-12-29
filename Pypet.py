#Pypet 

#create a Tamagoshi

print('Welcome to Pypet!')

name = 'Fluffy'
age = 1 
weight = 5.4
hungry = True 
photo = '(=^o.o^=)__'

print('Hello ' + name)
print (photo)


# Python dictionary to tell Python all these varialbles are for 1 cat 

cat = {
	'name': 'Fluffy Kiki',
	'hungry': 'True',
	'weight': 5.4,
	'age': 1,
	'photo': '(=^o.o^=)__',
}

print('Hello ' + cat['name'])
print(cat['photo'])

print (cat)


#Feeding my Pet 
# First, define our function — feed — which changes our pypet’s hungry attribute to False to show that it is no longer hungry.

print('Welcome to Pypet!')

cat = {
	'name': 'Fluffy Kiki',
	'hungry': 'True',
	'weight': 5.4,
	'age': 1,
	'photo': '(=^o.o^=)__',
}

def feed(pet):
	pet['hungry'] = False
	pet['weight'] = pet['weight'] + 1


print (cat)
feed(cat)
print (cat)










