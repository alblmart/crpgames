import random
print('''
	EXOGENEOUS REFERENCE PRICE GAME
	''')

bidders = {}
b = 0
while b < 16:
	b+=1
	bidders[b] = {'oppCost': random.randint(10,100), 
	'epsilon': random.randint(-5,5)}
	bidders[b]['estCost'] = bidders[b]['oppCost'] + bidders[b]['epsilon']
#print('Bidders:', bidders)

counter = 0
participators = {}
protentialProfits = {}
scores = {}
for b in bidders:		#participate function will need to be refined
	if bidders[b]['estCost'] >= bidders[b]['oppCost'] and int(0.9*bidders[b]['oppCost']) + 7 >= bidders[b]['oppCost']:
		counter+=1
		#print(b, "Yes", 'estCost:', bidders[b]['estCost'], 
			#'oppCost:', bidders[b]['oppCost'])
		bidders[b]['offer'] = min(bidders[b]['estCost'], int(0.9*bidders[b]['oppCost'] + 7))
		#participators[b] = bidders[b]['offer']
		protentialProfits[b] = bidders[b]['offer'] - bidders[b]['oppCost']
		bidders[b]['Score']= bidders[b]['offer']/bidders[b]['estCost'] + bidders[b]['estCost']/50
		scores[b] = bidders[b]['Score']
	else: 
		#print(b, "No")
		bidders[b]['offer'] = 999
		bidders[b]['Score'] = 999
#print('Bidders:', bidders)
print('Participation rate:', counter, 'out of 16 =', counter/16*100,'%')

bidsAll = []
lowestBids = {}
highestBids = {}
oppCostsAll = []
lowestCosts = {}
highestCosts = {}
scoresAll = []
lowestScores = {}
highestScores = {}
for b in bidders:
	oppCostsAll.append(bidders[b]['oppCost'])
	bidsAll.append(bidders[b]['offer'])
	scoresAll.append(bidders[b]['Score'])
SortedCosts = sorted(oppCostsAll)
SortedBids = sorted(bidsAll)
SortedScores = sorted(scoresAll)
#print(SortedCosts, SortedCosts[7], SortedCosts[8])
#print(SortedBids, SortedBids[7], SortedBids[8])
#print(SortedScores, SortedScores[7], SortedScores[8])
#print('COST LOOP')
for b in bidders:
	if bidders[b]['oppCost'] <= SortedCosts[7]:
		#print('yes', b, bidders[b]['oppCost'])
		lowestCosts[b] = bidders[b]
	else:
		#print('no', b, bidders[b]['oppCost'])
		highestCosts[b] = bidders[b]
#print('BID LOOP')
for b in bidders:
	if bidders[b]['offer'] <= min(SortedBids[7], 110):
		#print('yes', b, bidders[b]['offer'])
		lowestBids[b] = bidders[b]
	else:
		#print('no', b, bidders[b]['offer'])
		highestBids[b] = bidders[b]
#print(SCORE LOOP)
for b in bidders:
	if bidders[b]['Score'] <= min(SortedScores[7], 100):
		lowestScores[b] = bidders[b]
	else:
		highestScores[b] = bidders[b]
#print(lowestCosts)
#print(lowestScores) # lowestScores = winners
effCounter = 0
for b in bidders:
	if b in lowestCosts and b in lowestScores:
		effCounter += 1
	if b in lowestCosts and not b in lowestScores:
		effCounter += 0
	if b in highestCosts and b in highestScores:
		effCounter += 1
	if b in highestCosts and not b in highestScores:
		effCounter += 0
print('Allocative efficiency:', effCounter/16)

profitsAll = []
for b in bidders:
	if b in lowestScores:
		profitsAll.append(bidders[b]['offer'] - bidders[b]['oppCost'])
averageProfit = sum(profitsAll)/len(profitsAll)
print('Average profit:', round(averageProfit,2))

lowestCostList = []
winningOffers = []
for b in bidders:
	if b in lowestScores:
		winningOffers.append(bidders[b]['offer'])
	if b in lowestCosts:
		lowestCostList.append(bidders[b]['oppCost'])
averageWinningOffer = sum(winningOffers)/len(winningOffers)
print('Average winning offer:', averageWinningOffer)

paymentObserved = sum(winningOffers)
paymentEfficient = sum(lowestCostList)
print('Overcost:', paymentObserved/paymentEfficient - 1)





'''
participation rate *
average winning offer *
allocative efficiency *
over-cost *
average profit *
'''
