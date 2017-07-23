import time, random, urllib.request

wordList = urllib.request.urlopen("https://raw.githubusercontent.com/agiliq/Anagen/master/res/raw/wordlist.txt").read().decode("utf-8").splitlines()

presentTime = lambda: int(round(time.time() * 1000))
loadVerbs = lambda: [word for word in wordList if word.endswith("ing") and word.count("ing") == 1 and len(word) >= 6 and not "-" in word]
loadNouns = lambda: [word for word in wordList if not word.endswith(("ing", "al", "ly", "ed", "en", "le", "ke")) and len(word) >= 6]

rank = 1
money = 0

actionVerbs = loadVerbs()
actionNouns = loadNouns()
timeCounter = presentTime()

class MoneyAction:
    def __init__(self, rank):
        self.action = self.generateAction()
        _multiplier = 1 + len(self.action) / 40
        self.income = int(random.randint(10000, 100000) * (rank * _multiplier))

    def generateAction(self):
        global actionVerbs, actionNouns
        return "%s your %s" % (random.choice(actionVerbs), random.choice(actionNouns))

print("Welcome to the money simulator! This is how rich people earn money.")
print("You currently have: $%s, and are presently Rank %s.\n" % (money, rank))

while (True):
    try:
        if (presentTime() - timeCounter >= 1000):
            action = MoneyAction(rank)
            money += action.income

            print("You were %s, and earned $%s!" % (action.action, str(action.income)))
            print("You currently have: $%s, and are presently Rank %s." % (str(money), str(rank)))
            if (money - ((rank + 1) * 1000000) >= 0):
                print("As you had reached $%s, you paid $%s to become Rank %s!" % (str(money), str((rank + 1) * 1000000), str(rank + 1)))
                money -= rank * 1000000
                rank += 1
            print("")
            timeCounter = presentTime()
    except KeyboardInterrupt:
        print("And that is how rich people earn money.")
        break