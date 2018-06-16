print('''
PRICE CAP GAME
	''')
mu = 1 # mu in {1, 3, 5, 8, 12, 15}
import random

bidders = {}
oppCostDict = {}
b = 0
while b < 16:
	b+=1
	bidders[b] = {'oppCost': random.randint(10,100), 
	'epsilon': random.randint(-5,5)}
	bidders[b]['estCost'] = bidders[b]['oppCost'] + bidders[b]['epsilon']
	bidders[b]['capCost'] = bidders[b]['estCost'] + mu
	oppCostDict[b] = bidders[b]['oppCost']
#print('Bidders:', bidders)
counter = 0
participators = {}
for b in bidders:		#participate function will need to be refined
	if bidders[b]['capCost'] >= bidders[b]['oppCost'] and int(0.9*bidders[b]['oppCost']) + 7 >= bidders[b]['oppCost']:
		counter+=1
		#print(b, "Yes", 'capCost:', bidders[b]['capCost'], 
			#'oppCost:', bidders[b]['oppCost'])
		bidders[b]['offer'] = min(bidders[b]['capCost'], int(0.9*bidders[b]['oppCost']) + 7)
		participators[b] = {'offer': bidders[b]['offer'], 
		'expProfit': bidders[b]['offer'] - bidders[b]['oppCost']}
	else: 
		#print(b, "No")
		bidders[b]['offer'] = 999
#print('Bidders:', bidders)
#print('Partipators:', participators)
#print(bidders)
orderedBidders = sorted(participators.items(), key = lambda i: i[1]['offer'])
#print(participators, orderedBidders)
orderedOppCosts = sorted(oppCostDict.items(), key = lambda i: i[1])
winningBids = []
profits = []
oppCostList = []
i = 0
while i < min(8, len(orderedBidders)):
	winningBids.append(orderedBidders[i][1]['offer'])
	profits.append(orderedBidders[i][1]['expProfit'])
	oppCostList.append(orderedOppCosts[i][1])
	i +=1 
print('BIDS:', winningBids)
print('COSTS:', oppCostList)
averageProfit = sum(profits)/len(profits)
averageWinner = sum(winningBids)/len(winningBids)
overcost = sum(winningBids)/sum(oppCostList) - 1
print('Allowed markup: mu =', mu)
print('Participation rate:', counter, 'out of 16 =', counter/16*100,'%')
print('Total expenditure:', sum(winningBids))
print('Average winning offer:', round(averageWinner,2))
print('Average profit:', round(averageProfit,2))
print('Overcost:', round(overcost,4))

#ALLOCATIVE EFFICIENCY

bidsAll = []
lowestBids = {}
highestBids = {}
oppCostsAll = []
lowestCosts = {}
highestCosts = {}
for b in bidders:
	oppCostsAll.append(bidders[b]['oppCost'])
	bidsAll.append(bidders[b]['offer'])
SortedCosts = sorted(oppCostsAll)
SortedBids = sorted(bidsAll)
#print(SortedCosts, SortedCosts[7], SortedCosts[8])
#print(SortedBids, SortedBids[7], SortedBids[8])
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
#print('>>lowest costs', lowestCosts)
#print('>>highest costs', highestCosts)
#print('>>lowest bids', lowestBids)
#print('>>highest bids', highestBids)
effCounter = 0
for b in bidders:
	if b in lowestCosts and b in lowestBids:
		effCounter += 1
	if b in lowestCosts and not b in lowestBids:
		effCounter += 0
	if b in highestCosts and b in highestBids:
		effCounter += 1
	if b in highestCosts and not b in highestBids:
		effCounter += 0
print('Allocative efficiency:', effCounter/16)
		
'''
participation
winning offers
allocative efficiency
overcost
profit
'''














