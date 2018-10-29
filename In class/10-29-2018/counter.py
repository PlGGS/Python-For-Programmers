class counter():
    value = 0

    def __str__(self):
        '''Replaces the default str conversion method for a counter'''
        return "counter : " + str(self.value)
    
    def __repr__(self):
        '''Replaces the default representation method for a counter'''
        return "counter(" + str(self.value) + ")"

    def __init__(self, initValue = 0):
        '''Constructor with default value of 0'''
        self.value = initValue
    
    def getValue (self):
        return self.value

    def setValue (self, newValue):
        self.value = newValue

    def increment(self):
        self.value += 1

    def decrement (self):
        self.value -= 1

    def resetValue (self):
        self.value = 0