
class Process:

    def __init__(self,memory,priority):
        self.memory = memory
        self.priority = priority

    def __eq__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.priority == other.priority

    def __lt__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.priority < other.priority