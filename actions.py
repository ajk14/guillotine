import readline
import random

class Action:
	def __init__(self, name, description, actionFunction):
		self.name=name
		self.description=description
		self.actionFunction=actionFunction

	def play(self, game):
		self.actionFunction(game)

	def __str__(self):
		return self.name + " " + self.description


def moveForward(game, nobleIndex, spaces):
	for i in range(spaces):
		moveForwardOne(game, nobleIndex)
		nobleIndex -= 1

def moveBackward(game, nobleIndex, spaces):
	for i in range(spaces):
		moveBackwardOne(game, nobleIndex)
		nobleIndex += 1

def moveForwardOne(game, nobleIndex):
	temp = game.currentLineup[nobleIndex]
	game.currentLineup[nobleIndex] = game.currentLineup[nobleIndex - 1]
	game.currentLineup[nobleIndex - 1] = temp

def moveBackwardOne(game, nobleIndex):
	temp = game.currentLineup[nobleIndex]
	game.currentLineup[nobleIndex] = game.currentLineup[nobleIndex + 1]
	game.currentLineup[nobleIndex + 1] = temp

def move(game, nobleIndex, spaces, forward):
	if forward:
		moveForward(game, nobleIndex, spaces)
	moveBackward(game, nobleIndex, spaces)

def fixedMove(game, cardName, spaces, forward=True):
	direction = "forward" if forward else "backward"
	nobleIndex = raw_input("Playing card '%s'. Move which noble %s %s? " % (cardName, direction, spaces))
	move(game, int(nobleIndex), spaces, forward)

def flexibleMove(game, cardName, maxSpaces, forward=True):
	direction = "forward" if forward else "backward"
	nobleIndex = raw_input("Playing card '%s'. Move which noble %s up to %s spaces? " % (cardName, direction, maxSpaces))
	chosenSpaces = raw_input("Move how many spaces? ")
	while (int(chosenSpaces) > maxSpaces or int(chosenSpaces) < 0):
		chosenSpaces = raw_input("Please enter a valid value, %s or fewer spaces: " % maxSpaces)
	move(game, int(nobleIndex), int(chosenSpaces), forward)

def colorMove(game, cardName, color, maxSpaces):
	nobleIndex = raw_input("Playing card '%s'. Move which %s noble forward up to %s spaces? " % (cardName, color, maxSpaces))
	while(game.currentLineup[int(nobleIndex)].color is not color):
		nobleIndex = raw_input("You must choose a %s noble! Try again: " % s)
	chosenSpaces = raw_input("Move how many spaces? ")
	while (int(chosenSpaces) > maxSpaces or int(chosenSpaces) < 0):
		chosenSpaces = raw_input("Please enter a valid value, %s or fewer spaces: " % maxSpaces)

def moveToFront(game, card):
	moveToIndex(game, card, 0)

def moveToBack(game, card):
	moveToIndex(game, card, len(game.currentLineup) - 1)

def moveToIndex(game, card, index):
	game.currentLineup.remove(card)
	game.currentLineup.insert(index, card)

def ignobleNoble(game):
	fixedMove(game, "Ignoble Noble", 4)

def tisAFarBetter(game):
	fixedMove(game, "Tis a Far Better Thing", 3)

def pushed(game):
	fixedMove(game, "Pushed", 2)

def wasThatMyName(game):
	flexibleMove(game, "Was that My Name", 3)

def idiot(game):
	flexibleMove(game, "L'idiot", 2)

def militaryMight(game):
	colorMove(game, "Military Might", Color.RED, 2)

def civicPride(game):
	colorMove(game, "CivicPride", Color.GREEN, 2)

def majesty(game):
	colorMove(game, "Majesty", Color.PURPLE, 2)

def stumble(game):
	fixedMove(game, "Stumble", 1, False)

def faintingSpell(game):
	flexibleMove(game, "Fainting Spell", 3, False)

def friendOfQueen(game):
	flexibleMove(game, "Friend of the Queen", 2, False)

def trip(game):
	fixedMove(game, "Trip", 1, False)
	game.playAction()

def eatCake(game):
	for noble in game.currentLineup:
		if noble.name is "Marie Antoinette":
			moveToFront(game, noble)

def lackOfFaith(game):
	nobleIndex = raw_input("Playing card 'Lack of Faith'. Move which blue noble to front? ")
	while (game.currentLineup[int(nobleIndex)].color != Color.BLUE):
		nobleIndex = raw_input("You must choose only a blue card. Try again: ")
	moveToFront(game, game.currentLineup[int(nobleIndex)])

def forwardMarch(game):
	nobleIndex = raw_input("Playing card 'Forward March'. Move which palace guard to front? ")
	while (game.currentLineup[int(nobleIndex)].name != "Palace Guard"):
		nobleIndex = raw_input("You must choose only a palace guard. Try again: ")
	moveToFront(game, game.currentLineup[int(nobleIndex)])

def doubleFeature(game):
	game.collectNoble() 

def makeSelection(game, prompt, lowerBound, upperBound):
	index = raw_input(prompt)
	while (int(index) < lowerBound or int(index) > upperBound):
		index = raw_input("Invalid selection. Try again: ")
	return int(index)

def afterYou(game):
	playerIndex = makeSelection(game, "Playing card 'After You'. Move first noble into which player's pile? ", 0, game.playerCount() - 1)
	game.collectNobleFor(game.players[playerIndex])

def publicDemand(game):
	nobleIndex = makeSelection(game, "Playing card 'Public Demand'. Move which card to front? ", 0, len(game.currentLineup) - 1)
	moveToFront(game, game.currentLineup[int(nobleIndex)])

def fledToEngland(game):
	nobleIndex = makeSelection(game, "Playing card 'Fled To England'. Remove which card? ", 0, len(game.currentLineup) - 1)
	game.currentLineup.pop(int(nobleIndex))

def opinionated(game):
	first = makeSelection(game, "Playing card 'Opinionated Guards' to rearrange first 4 cards. Move which card to front? ", 0, 3)
	second = makeSelection(game, "Move which card second? ", 0, 3)
	third = makeSelection(game, "Move which card third? ", 0, 3)
	firstNoble = game.currentLineup[first]
	secondNoble = game.currentLineup[second]
	thirdNoble = game.currentLineup[third]
	moveToIndex(game, firstNoble, 0)
	moveToIndex(game, secondNoble, 1)
	moveToIndex(game, thirdNoble, 2)

def bribed(game):
	print "Playing card 'Bribed Guards'. Moving noble at front to end. "
	moveToBack(game, game.currentLineup[0])

def clothingSwap(game):
	nobleIndex = makeSelection(game, "Playing card 'Clothing Swap'. Replace which card? ", 0, len(game.currentLineup) - 1)
	game.currentLineup.remove(game.currentLineup[int(nobleIndex)])
	game.currentLineup.insert(nobleIndex, game.nobleDeck.deal())

def milling(game, number):
	print "Playing card 'Milling in Line. Randomly re-arranging first %s cards." % str(number)
	copy = game.currentLineup[:number]
	random.shuffle(copy)
	game.currentLineup[:number] = copy

def milling5(game):
	milling(game, 5)

def milling6(game):
	milling(game, 6)

def escape(game):
	print "Playing card 'Escape'. Shuffling line and removing 2. "
	random.shuffle(game.currentLineup)
	game.currentLineup.pop()
	game.currentLineup.pop()

def longWalk(game):
	print "Playing card 'The Long Walk'. Reversing order of line. "
	game.currentLineup.reverse()

def empty(game):
	pass

def massConfusion(game):
	print "Playing card 'Mass Confusion'. Dealing a new lineup. "
	nobleCount = len(game.currentLineup)
	newLineup = []
	for i in range(0, nobleCount):
		newLineup.append(game.nobleDeck.deal())
	game.currentLineup = newLineup

def extraCart(game):
	print "Playing card 'Extra Cart'. Adding 3 nobles. "
	for i in range(0, 3):
		game.currentLineup.append(game.nobleDeck.deal())

actionDeck = [
	Action("Ignoble Noble", "Move Forward Exactly 4 Places.", ignobleNoble),
	Action("Ignoble Noble", "Move Forward Exactly 4 Places.", ignobleNoble),
    Action("Tis a Far Better Thing", "Move Forward Exactly 3 Places ", tisAFarBetter),
	Action("Was that My Name?", "Move Forward Up to 3 Places ", wasThatMyName),
	Action("Pushed", "Move Forward Exactly 2 Places ", pushed),
	Action("Pushed", "Move Forward Exactly 2 Places ", pushed),
	Action("L'Idiot", "Move Forward Up to 2 Places ", idiot),
	Action("L'Idiot", "Move Forward Up to 2 Places ", idiot),
	Action("Military Might", "Red Up to 2 Places ", militaryMight),
	Action("Civic Pride", "Green Up to 2 Places ", civicPride),
	Action("Majesty", "Purple Up to 2 Places ", majesty),
	Action("Stumble", "Move Backward Exactly 1 Place ", stumble),
	Action("Stumble", "Move Backward Exactly 1 Place ", stumble),
	Action("Fainting Spell", "Move Backward Up to 3 Places ", faintingSpell),
	Action("Friend of the Queen", "Move Backward Up to 2 Places ", friendOfQueen),
	Action("Friend of the Queen", "Move Backward Up to 2 Places ", friendOfQueen),
	Action("Trip", "Move Backward Exactly 1 Place and play an extra Action Card ", trip),
	Action("Trip", "Move Backward Exactly 1 Place and play an extra Action Card ", trip),
	Action("Let Them Eat Cake", "Marie Antoinette to front ", eatCake),
	Action("Lack of Faith", "Blue to front ", lackOfFaith),
	Action("Forward March", "Palace Guard to front ", forwardMarch),
	Action("Double Feature", "Take an extra noble", doubleFeature),
	Action("Double Feature", "Take an extra noble", doubleFeature),
	Action("After You....", "Put front into another's pile ", afterYou),
	Action("Public Demand", "Move any to front ", publicDemand),
	Action("Fled to England", "Discard any 1 ", fledToEngland),
	Action("Opinionated Guards", "Re-arrange the first 4 as you like ", opinionated),
	Action("Bribed Guards", "Move noble at front to end ", bribed),
    Action("Clothing Swap", "Discard any 1 and replace from deck ", clothingSwap),
	Action("Milling in Line", "Randomly re-arrange the first 5 ", milling5),
	Action("Milling in Line", "Randomly re-arrange the first 6", milling6),
	Action("Escape!", "Randomize and discard 2 ", escape),
	Action("The Long Walk", "Reverse the order ", longWalk),
	Action("Military Support", "Bonus of +1 per Red ", empty),
	Action("Civic Support", "Bonus of +1 per Green ", empty),
	Action("Church Support", "Bonus of +1 per Blue ", empty),
	Action("Indifferent Public", "Gray valued as +1 instead of normal ", empty),
	Action("Fountain of Blood", "Bonus of +2 ", empty),
	Action("Mass Confusion", "Return nobles to deck, shuffle and re-deal ", massConfusion),
	Action("Extra Cart", "Add 3 from the deck to the end of the line ", extraCart),
	Action("Extra Cart", "Add 3 from the deck to the end of the line ", extraCart)]
"""	Action("Late Arrival", "Examine top 3 from the deck and add one to end of the line "),
	Action("Rat Break", "Pick up card of your choice from discards "),
	Action("Political Influence", "Draw 3 extra without taking a noble "),
	Action("Political Influence", "Draw 3 extra without taking a noble "),
	Action("Rain Delay", "Deal completely new hands "),
	Action("Callous Guards", "Line-altering cards cannot be played "),
	Action("Missing Heads", "Lose a random noble "),
	Action("Missed!", "Last noble collected placed at end of line "),
	Action("Tough Crowd", "Penalty of -2 "),
	Action("Twist of Fate", "Discard a face up action card "),
	Action("Rush Job", "Cannot play action card on next turn "),
	Action("Clerical Error", "Trade a noble "),
	Action("Lack of Support", "Look through hand and remove a card "),
	Action("Forced Break", "All players discard a card randomly "),
	Action("Infighting", "Chose 2 action cards and discard "),
	Action("Information Exchange", "Exchange hands "),
	Action("Confusion in Line", "Randomly rearrange the line "),
	Action("Foreign Support", "Draw an action card whenever collecting a purple "),
	Action("Scarlet Pimpernel", "End the day after your turn ")
]
 """