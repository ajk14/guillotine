class Color:
	GREY = "Grey"
	RED = "Red"
	GREEN = "Green"
	BLUE = "Blue"
	PURPLE = "Purple"

class Noble:
	def __init__(self, name, value, color, description):
		self.name=name 
		self.value=value
		self.color=color
		self.description=description

	def __str__(self):
		return self.name + " " + str(self.value) + " " + self.color + " " + str(self.description)

nobleDeck = [
	Noble("Tragic Figure", None, Color.GREY, "*worth -1 per Gray in your pile"),
	Noble("Hero of the People", -3, Color.GREY, None),
	Noble("The Clown", -2, Color.GREY, "place it in another's score pile"),
	Noble("Innocent Victim", -1, Color.GREY, "must discard an action card"),
	Noble("Martyr", -1, Color.GREY, None),
	Noble("Martyr", -1, Color.GREY, None),
	Noble("Martyr", -1, Color.GREY, None),
	Noble("Palace Guard", None, Color.RED, None),
	Noble("Palace Guard", None, Color.RED, None),
	Noble("Palace Guard", None, Color.RED, None),
	Noble("Palace Guard", None, Color.RED, None),
	Noble("Palace Guard", None, Color.RED, None),
	Noble("Master Spy", 4, Color.RED, "moves to the end of the line when action card played"),
	Noble("General", 4, Color.RED, "add another noble from the deck to end of the line"),
	Noble("Colonel", 3, Color.RED, None),
	Noble("Captain of the Guard", 2, Color.RED, "add another noble from the deck to end of the line"),
	Noble("Lieutenant", 2, Color.RED, None),
	Noble("Lieutenant", 2, Color.RED, None),
	Noble("Governor", 4, Color.GREEN, None),
	Noble("Mayor", 3, Color.GREEN, None),
	Noble("Councilman", 3, Color.GREEN, None),
	Noble("Unpopular Judge", 2, Color.GREEN, "Can't PLay action card"),
	Noble("Unpopular Judge", 2, Color.GREEN, "Can't PLay action card"),
	Noble("Tax Collector", 2, Color.GREEN, None),
	Noble("Land Lord", 2, Color.GREEN, None),
	Noble("Rival Executioner", 1, Color.GREEN, "also collects top noble on deck"),
	Noble("Sheriff", 1, Color.GREEN, None),
	Noble("Sheriff", 1, Color.GREEN, None),
	Noble("Cardinal", 5, Color.BLUE, None),
	Noble("Archbishop", 4, Color.BLUE, None),
	Noble("Bad Nun", 3, Color.BLUE, None),
	Noble("Bishop", 2, Color.BLUE, None),
	Noble("Heretic", 2, Color.BLUE, None),
	Noble("Wealthy Priest", 1, Color.BLUE, None),
	Noble("Wealthy Priest", 1, Color.BLUE, None),
	Noble("King Louis XVI", 5, Color.PURPLE, None),
	Noble("Marie Antoinette", 5, Color.PURPLE, None),
	Noble("Regent", 4, Color.PURPLE, None),
	Noble("Robespierre", 3, Color.PURPLE, "day ends after collection"),
	Noble("Duke", 3, Color.PURPLE, None),
	Noble("Baron", 3, Color.PURPLE, None),
	Noble("Lady", 2, Color.PURPLE, "draw an additional action card"),
	Noble("Lord", 2, Color.PURPLE, "draw an additional action card"),
	Noble("Countess", 2, Color.PURPLE, "worth +2 if holding Count"),
	Noble("Count", 2, Color.PURPLE, "worth +2 if holding Countess"),
	Noble("Fast Noble", 2, Color.PURPLE, "collect additional from front of line"),
	Noble("Lady in Waiting", 1, Color.PURPLE, "draw an additional action card"),
	Noble("Royal Cartographer", 1, Color.PURPLE, None),
	Noble("Coiffeur", 1, Color.PURPLE, None),
	Noble("Piss Boy", 1, Color.PURPLE, None)
]

