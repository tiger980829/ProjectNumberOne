teams = {
	'iron':['one','two','three',4],
	'metal':['four','five',"six"]
}
teams2 = {
	'iron':['seven','two','three',5],
	'metal':['four','five',"six"]
}
print(teams['iron'])

print('seven' in teams2['iron'])

teams['iron'] = teams['iron'] + ['seven']

print('seven' in teams['iron'])

print(teams)
print(teams.values())

# print('iron')
print(teams["iron"][1])

friends = ['one','two','three','four','five','six']

def Find3Name(allName):
	three_names = []
	i = 0
	while(i < len(allName)):
		name = allName[i]
		if ( len(name) == 3):
			three_names.append(name)
		i += 1
	return three_names

def Find4Name(allName):
	four_names = []
	i = 0
	for name in allName:
		if ( len(name) == 4):
			four_names.append(name)
		i += 1
	return four_names

print( Find3Name(friends) )
print( Find4Name(friends) )

Lastwords = input("Any Lastword?")

print(Lastwords)