import os
import sys
import time

class Tail(object):
    ''' Represents a tail command. '''
    def __init__(self, tailed_file):
        ''' Initiate a Tail instance.
            Check for file validity, assigns callback function to standard out.
            
            Arguments:
                tailed_file - File to be followed. '''

        self.check_file_validity(tailed_file)
        self.tailed_file = tailed_file
        self.callback = sys.stdout.write

    def checkIfFileExists(self,mfile):
        try:
            with open(mfile) as f:
                return True
        except IOError as e:
            return False

    def follow(self, s=1):
        ''' Do a tail follow. If a callback function is registered it is called with every new line. 
        Else printed to standard out.
    
        Arguments:
            s - Number of seconds to wait between each iteration; Defaults to 1. '''

        with open(self.tailed_file) as file_:
            # Go to the end of file
            file_.seek(0,2)
            while True:
                if not self.checkIfFileExists(self.tailed_file):
                    self.follow(self.tailed_file)

                curr_position = file_.tell()
                line = file_.readline()
                if not line:
                    file_.seek(curr_position)
                    time.sleep(s)
                else:
                    self.callback(line)

    def register_callback(self, func):
        ''' Overrides default callback function to provided function. '''
        self.callback = func

    def check_file_validity(self, file_):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
