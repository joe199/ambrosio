from Action import Action
import subprocess

class SensorActions(Action):
    """SensorActions for Ambrosio"""
    def __init__(self, cfg):
        super(SensorActions, self).__init__(cfg)
        self.triggers = ["Temperature"]

    def do(self, command):
        print "Will mesure temperature ", " ".join(command)
        th = subprocess.check_output(['sudo','AdafruitDHT.py','11','4'])
        return th

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
