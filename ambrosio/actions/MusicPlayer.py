from Action import Action
from mpd import (MPDClient, CommandError)



class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music", "audio"]
        self.mpd = MPDClient()
        self.mpd.connect("localhost", "6600")

    def _do_update(self, command):
        self.mpd.update()

    def _do_add(self, command):
        canco = " ".join(command[1:])
        return self.mpd.addid(canco)

    def _do_cua(self, command):
        return "llista: %s" %(self.mpd.playlist())

    def _do_play(self, command):
        return self.mpd.play()

    def _do_stop(self, command):
        return self.mpd.stop()

    def _do_songs(self, command):
        llista = self.mpd.list("file")
        print llista
        if len(llista) > 0:
            return "\n".join(llista)
        else:
            return "Llista buida"


    def do(self, command):
        print "Will play music ", " ".join(command)
        if command[0] == "update":
            self._do_update(command)
        elif command[0] == "songs":
            return self._do_songs(command)
        elif command[0] == "add":
            return self._do_add(command)
        elif command[0] == "play":
            return self._do_play(command)
        elif command[0] == "stop":
            return self._do_stop(command)
        elif command[0] == "cua":
            return self._do_cua(command)

        return "Not found music argument"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
