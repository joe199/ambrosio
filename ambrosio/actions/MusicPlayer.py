from Action import Action

class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music", "audio"]

    def do(self, command):
        print "Will play music ", " ".join(command)
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
