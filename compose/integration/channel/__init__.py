class Channel(object):
    def __init__(self, parameters):
        self.id = parameters['id']
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False
    
    def __str__(self):
        return '[id:' + str(self.id) + ']'