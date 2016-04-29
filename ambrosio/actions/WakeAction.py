from Action import Action
import subprocess

class WakeAction(Action):
    """Wakes the computer"""
    def __init__(self, cfg):
        super(WakeAction, self).__init__(cfg)
        self.triggers = ["wake"]

    def do(self, command):
        print "Will wake up a computer ", " ".join(command)
        return "ok"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
