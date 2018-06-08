import random

bidders = {}
b = 0
while b < 16:
	b+=1
	bidders[b] = {'oppCost': random.randint(10,100), 
	'epsilon': random.randint(-5,5)}
	bidders[b]['estCost'] = bidders[b]['oppCost'] + bidders[b]['epsilon']
print('Bidders:', bidders)

counter = 0
participators = {}
protentialProfits = {}
scores = {}
for b in bidders:		#participate function will need to be refined
	if bidders[b]['estCost'] >= bidders[b]['oppCost']:
		counter+=1
		print(b, "Yes", 'estCost:', bidders[b]['estCost'], 
			'oppCost:', bidders[b]['oppCost'])
		bidders[b]['offer'] = bidders[b]['estCost']
		participators[b] = bidders[b]['offer']
		protentialProfits[b] = bidders[b]['estCost'] - bidders[b]['oppCost']
		bidders[b]['bid'] = random.randint(bidders[b]['oppCost'], bidders[b]['estCost'] + 5)
		bidders[b]['Score']= bidders[b]['bid']/bidders[b]['estCost'] + bidders[b]['estCost']/50
		scores[b] = bidders[b]['Score']
	else: 
		print(b, "No")
print('Bidders:', bidders)
print('Participation rate:', counter, 'out of 16 =', counter/16*100,'%')
print('Partipators:', participators)
print('Potential profits:', protentialProfits)
print('Scores:', scores)

'''
for i in bidders:
	bidders[i]['bid'] = random.randint(bidders[i]['oppCost'], bidders[i]['estCost'] + 5)
print(bidders)

for n in bidders: 
	bidders[n]['Score']= bidders[n]['bid']/bidders[n]['estCost'] + bidders[n]['estCost']/50
print(bidders)
'''
