class robot():
    position = (0, 0)
    directions = {'up':('U', 'u'), 
                  'down':('D', 'd'), 
                  'left':('L', 'l'), 
                  'right':('R', 'r')}
    direction = 'R'

    def __init__(self, initX = 0, initY = 0, initDirection = 'R'):
        self.position = (initX, initY)
        self.direction = initDirection

    def __str__(self):
        return (str(self.getPosition()) + ':' + str(self.getDirecton()))

    def runProgram(self, runString):
        runString = str(runString).upper()

        for char in runString:
            if char == 'A':
                self.advance()
            elif char == 'L':
                self.turnLeft()
            elif char == 'R':
                self.turnRight()
            elif char == 'a':
                self.turnAround()
            pass
        pass

    def getDirecton(self):
        '''What I would call getFacing'''
        return str(self.direction).upper()

    def getFacing(self):
        return str(self.direction).upper()

    def getPosition(self):
        return self.position

    def turnLeft(self):
        print('turning left')
        
        if self.direction == self.directions['up'][0] or self.direction == self.directions['up'][1]:
            self.direction = self.directions['left'][0]
            print(self.getFacing())
        elif self.direction == self.directions['down'][0] or self.direction == self.directions['down'][1]:
            self.direction = self.directions['right'][0]
        elif self.direction == self.directions['left'][0] or self.direction == self.directions['left'][1]:
            self.direction = self.directions['down'][0]
        elif self.direction == self.directions['right'][0] or self.direction == self.directions['right'][1]:
            self.direction = self.directions['up'][0]
        pass

    def turnRight(self):
        print('turning right')
        
        if self.direction == self.directions['up'][0] or self.direction == self.directions['up'][1]:
            self.direction = self.directions['right'][0]
        elif self.direction == self.directions['down'][0] or self.direction == self.directions['down'][1]:
            self.direction = self.directions['left'][0]
        elif self.direction == self.directions['left'][0] or self.direction == self.directions['left'][1]:
            self.direction = self.directions['up'][0]
        elif self.direction == self.directions['right'][0] or self.direction == self.directions['right'][1]:
            self.direction = self.directions['down'][0]
        pass

    def turnAround(self):
        print('turning around')
        
        if self.direction == self.directions['up'][0] or self.direction == self.directions['up'][1]:
            self.direction = self.directions['down'][0]
        elif self.direction == self.directions['down'][0] or self.direction == self.directions['down'][1]:
            self.direction = self.directions['up'][0]
        elif self.direction == self.directions['left'][0] or self.direction == self.directions['left'][1]:
            self.direction = self.directions['right'][0]
        elif self.direction == self.directions['right'][0] or self.direction == self.directions['right'][1]:
            self.direction = self.directions['left'][0]
        pass

    def advance(self):
        print('advancing')
        
        if self.direction == self.directions['up'][0] or dir == self.directions['up'][1]:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.direction == self.directions['down'][0] or dir == self.directions['down'][1]:
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == self.directions['left'][0] or dir == self.directions['left'][1]:
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == self.directions['right'][0] or dir == self.directions['right'][1]:
            self.position = (self.position[0] + 1, self.position[1])