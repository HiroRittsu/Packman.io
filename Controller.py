# Helper to define an enum
def enum(**enums):
    return type('Enum', (), enums)

class Controller:
    # Input of the Controller
    Input = enum(Null=0, Left=1, Right=2, Launch=3)

    def __init__(self):
        pass

    def get_input(self, game):
        return Controller.Input.Null

    def event(self, game, event):
        pass

    def draw(self, game):
        pass
