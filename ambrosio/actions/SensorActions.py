from Action import Action

class SensorActions(Action):
    """SensorActions for Ambrosio"""
    def __init__(self):
        super(SensorActions, self).__init__()
        self.triggers = ["music", "audio"]

    def do(self, command):
        print "Will play music ", " ".join(command)
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
