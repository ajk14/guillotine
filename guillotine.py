import random
import readline
import nobles
import actions

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player:
	def __init__(self, name):
		self.name=name
		self.nobles=[]
		self.actions=[]
		self.playedActions=[]

	def playAction(self, game, actionIndex):
		action = self.actions[actionIndex]
		action.play(game)
		if action.playerRetains:
			self.playedActions.append(action)
		else:
			game.discardPile.append(action)
		self.actions.remove(action)

	def draw(self, action):
		self.actions.append(action)

	def collectNoble(self, noble):
		self.nobles.append(noble)

class Deck:
	def __init__(self, cards):
		self.deck = list(cards)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

	def peek(self):
		return self.deck[-1]

class Game:
	def __init__(self, players):
		self.nobleDeck = Deck(nobles.nobleDeck)
		self.actionDeck = Deck(actions.actionDeck)
		self.players = players
		self.currentLineup = []
		self.discardPile = []
		self.currentPlayer = players[0]

	def startGame(self):
		for player in self.players:
			for i in range(0, 5):
				player.draw(self.actionDeck.deal())
		self.startDay()

	def startDay(self):
		for i in range(0, 12):
			self.currentLineup.append(self.nobleDeck.deal())

	def playerCount(self):
		return len(self.players)

	def nextPlayer(self):
		newIndex = (self.players.index(self.currentPlayer) + 1) % len(self.players)
		self.currentPlayer = self.players[newIndex]

	def playAction(self):
		cardIndex = raw_input("Great. Play which action card number? ")
		self.currentPlayer.playAction(self, int(cardIndex))

	def collectNoble(self):
		self.collectNobleFor(self.currentPlayer)

	def collectNobleFor(self, player):
		player.collectNoble(self.currentLineup.pop(0))

	def collectAction(self):
		self.currentPlayer.draw(self.actionDeck.deal())

	def printGame(self):
		print("Current Players: ")
		for i in range(len(self.players)):
			print "Player %s: %s" % (i, self.players[i].name)
			print "\tNobles: "
			for noble in self.players[i].nobles:
				print "\t\t" + str(noble)
			print "\tActions: "
			for j in range(len(self.players[i].actions)):
				print "\t\tAction %s: %s, %s" % (j, self.players[i].actions[j].name, self.players[i].actions[j].description)
			print "\t Played Actions: "
			for j in range(len(self.players[i].playedActions)):
				print "\t\tAction %s: %s, %s" % (j, self.players[i].playedActions[j].name, self.players[i].playedActions[j].description)
		print("Current Lineup: ")
		print(bcolors.WARNING + "Next to be executed: " + bcolors.ENDC)
		for i in range(len(self.currentLineup)):
			print "\tNoble %s: %s" % (i, self.currentLineup[i])
		print(bcolors.GREEN + "End of the line" + bcolors.ENDC)


def main():
	print (bcolors.GREEN + "Welcome to Guillotine!" + bcolors.ENDC)
	playCount = raw_input("How many players will be playing? ")
	players = []
	for i in range(int(playCount)):
		name = raw_input("What is player %s's name? " % str(i))
		players.append(Player(name))
	currentGame = Game(players)
	currentGame.startGame()
	currentGame.printGame()

	while True:
		line = raw_input("%s's turn. Would you like to play an action? Y/N " % currentGame.currentPlayer.name)

		if line == "Y" or line == "N":
			if line == "Y":
				currentGame.playAction()
				
			print "Collecting your noble and drawing an action card..."
			currentGame.collectNoble()
			currentGame.collectAction()
			currentGame.nextPlayer()

		currentGame.printGame()
			

if (__name__ == "__main__"):
	main()
