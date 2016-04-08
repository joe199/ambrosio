
class Action(object):
    """Action to be carried on by ambrosio"""
    def __init__(self):
        super(Action, self).__init__()

    def do(self):
        pass

    def is_for_you(self, word):
        pass



class MusicPlayer(Action):
    """MusicPlayer for MusicPlayer"""
    def __init__(self, arg):
        super(MusicPlayer, self).__init__()

    def do(self):
        print "will play music"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
