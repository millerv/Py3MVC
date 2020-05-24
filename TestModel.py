class MyModel:
    '''
    The MyModel class holds all the functions/methods that do the work.

    Args:

    Attributes:
        arg (feet): number of feet we're working with as float.
        arg (meters): number of meters we're working with as float.
    '''
    def __init__(self):
        self.feet = 0.0
        self.meters = 0.0

    def calculate(self, feet):
        try:
            self.meters = (0.3048 * feet * 10000.0 + 0.5)/10000.0
            return self.meters
        except ValueError:
            pass
