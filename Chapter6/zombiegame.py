import zombiedice


class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollresult = zombiedice.roll()
        brains = 0
        while diceRollresult is not None:
            brains += diceRollresult['brains']

            if brains < 2:
                diceRollresult = zombiedice.roll()

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='luke'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='leader'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='stop at 1 shottie', minShotguns=1),
    MyZombie(name='Biffatron')

)
zombiedice.runWebGui(zombies=zombies, numGames=1000)