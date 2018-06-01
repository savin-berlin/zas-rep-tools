
from __future__ import print_function


import sys
import threading
from time import sleep
try:
    import thread
except ImportError:
    import _thread as thread



try:
    range, _print = xrange, print
    def print(*args, **kwargs): 
        flush = kwargs.pop('flush', False)
        _print(*args, **kwargs)
        if flush:
            kwargs.get('file', sys.stdout).flush()            
except NameError:
    pass


def quit_function(fn_name):
    # print to stderr, unbuffered in Python 2.
    #print('{0} took too long'.format(fn_name), file=sys.stderr)
    sys.stderr.flush() # Python 3 stderr is likely buffered.
    thread.interrupt_main() # raises KeyboardInterrupt

def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer



def get_file_list(path, extention):
    if os.path.isdir(path):
        txt_files = [file for file in os.listdir(path) if extention in file]
        if txt_files:
            return  (path,txt_files)
        else:
            False
    else:
        return False

