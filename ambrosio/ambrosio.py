#!/usr/bin/env/python
# _*_ coding: utf-8 _*_

import time
class Ambrosio(object):
    '''Class for ambrosio personal digital butler

    Will run our ambrosio'''

    def __init__(self):
        super(Ambrosio, self).__init__()
        self.cl = CommandList()

    def next_command(self):
        try:
            return self.cl.next()
        except:
            return None

    def mainloop(self):
        #While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            try:
                command = self.next_comman()
                time.sleep(1)



    if __name__ == __main__:
        print "Here be dragons!"
