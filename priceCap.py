mu = 15 # mu in {1, 3, 5, 8, 12, 15}
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
		bidders[b]['offer'] = 'N/A'
print('Bidders:', bidders)
#print('Partipators:', participators)
#print(bidders)

orderedBidders = sorted(participators.items(), key = lambda i: i[1]['offer'])
print(participators, orderedBidders)
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


'''
participation
winning offers
allocative efficiency
overcost
profit
'''













