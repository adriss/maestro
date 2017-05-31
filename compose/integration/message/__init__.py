from datetime import time

class Message:
    def __init__(self, payload):
        self.payload = payload 
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False
    
    def __str__(self):
        return '[id:' + str(self.id) + ']'