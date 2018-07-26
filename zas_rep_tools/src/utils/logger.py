import os
import time
import datetime
import logging
import logging.handlers
#import coloredlogs
from zas_rep_tools.src.utils.debugger import p
from raven.conf import setup_logging
import threading
import types
import sys
import traceback
from collections import defaultdict



#coloredlogs.DEFAULT_DATE_FORMAT = "%H:%M:%S"
#coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s  [%(name)s]  %(levelname)s %(message)s'




from logutils.colorize import ColorizingStreamHandler

class RainbowLoggingHandler(ColorizingStreamHandler):
    """ A colorful logging handler optimized for terminal debugging aestetichs.

    - Designed for diagnosis and debug mode output - not for disk logs

    - Highlight the content of logging message in more readable manner

    - Show function and line, so you can trace where your logging messages
      are coming from

    - Keep timestamp compact

    - Extra module/function output for traceability

    The class provide few options as member variables you
    would might want to customize after instiating the handler.
    """



    date_format = "%H:%M:%S"

    #: How many characters reserve to function name logging
    who_padding = 22

    #: Show logger name
    show_name = True

    # Define color for message payload
    level_map = {
        logging.DEBUG: (None, 'cyan', False),
        logging.INFO: (None, 'white', True),
        logging.WARNING: ("yellow", 'white', True),
        logging.ERROR: ( 'red', "white", True),
        logging.CRITICAL: ('magenta', 'white', True),
    }



    def get_color(self, fg=None, bg=None, bold=False):
        """
        Construct a terminal color code

        :param fg: Symbolic name of foreground color

        :param bg: Symbolic name of background color

        :param bold: Brightness bit
        """
        params = []
        if bg in self.color_map:
            params.append(str(self.color_map[bg] + 40))
        if fg in self.color_map:
            params.append(str(self.color_map[fg] + 30))
        if bold:
            params.append('1')

        color_code = ''.join((self.csi, ';'.join(params), 'm'))

        return color_code

    def colorize(self, record):
        """
        Get a special format string with ASCII color codes.
        """

        # Dynamic message color based on logging level
        if record.levelno in self.level_map:
            fg, bg, bold = self.level_map[record.levelno]
        else:
            # Defaults
            bg = None
            fg = "white"
            bold = False

        # Magician's hat
        # https://www.youtube.com/watch?v=1HRa4X07jdE
        # template = [
        #     "[",
        #     self.get_color("black", None, True),
        #     "%(asctime)s",
        #     self.reset,
        #     "] ",
        #     self.get_color("white", None, True) if self.show_name else "",
        #     "%(name)s " if self.show_name else "",
        #     "%(padded_who)s",
        #     self.reset,
        #     " ",
        #     self.get_color(bg, fg, bold),
        #     "%(message)s",
        #     self.reset,
        # ]

        template = [
            "[",
            self.get_color("gray", None, False),
            "%(asctime)s",
            self.reset,
            "] ",
            #self.get_color("white", None, True) if self.show_name else "",
            self.get_color(bg, fg, bold),
            "%(name)s" if self.show_name else "",
            self.reset,
            self.get_color("green", None, False),
            " %(threadName)s:",
            self.reset,
            #"{%(process)d} ",
            "{%(sthread)s} ",
            #self.get_color("red", None, False),
            self.get_color(bg, fg, bold),
            "%(levelname)s",
            self.reset,
            self.get_color("yellow", None, False),
            " %(message)s",
            self.reset,
            self.get_color("blue", None, False),
            "  [%(padded_who)s]\n",
            self.reset,
        ]

        #'%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} %(levelname)5s %(message)s ' 




        format = "".join(template)

        who = [self.get_color("blue"),
               getattr(record, "funcName", ""),
               "()",
               #self.get_color("black", None, True),
               # ":",
               # self.get_color("cyan"),
               # str(getattr(record, "lineno", 0))
               ]

        who = "".join(who)

        # We need to calculate padding length manualy
        # as color codes mess up string length based calcs
        # unformatted_who = getattr(record, "funcName", "") + "()" + \
        #     ":" + str(getattr(record, "lineno", 0))

        # if len(unformatted_who) < self.who_padding:
        #     spaces = " " * (self.who_padding - len(unformatted_who))
        # else:
        #     spaces = ""

        record.padded_who = who #+ spaces
        #record.nasctime = 

        formatter = logging.Formatter(format, self.date_format)
        self.colorize_traceback(formatter, record)
        output = formatter.format(record)
        # Clean cache so the color codes of traceback don't leak to other formatters
        record.ext_text = None
        return output

    def colorize_traceback(self, formatter, record):
        """
        Turn traceback text to diff coloures.
        # """

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)

            output_list = []
            for line in formatter.formatException(record.exc_info).split("\n"):
                #p(line)
                if "Traceback" in line:
                    output_list.append(self.get_color("red", None, True))
                    output_list.append(line)
                    #output_list.append(self.reset)
                    output_list.append("\n")
                
                else:
                    if "File" in line:
                        new_line = []
                        for token in line.split(" "):
                            #p(repr(token))
                            if "file" in token.lower():
                                new_line.append("  ")
                                new_line.append(self.reset)
                                new_line.append(self.get_color("gray", None, True))
                                new_line.append(token)
                                #new_line.append(self.reset)
                                new_line.append(self.get_color("magenta", None, False))
                            elif "line" == token:
                                #p(repr(token))
                                new_line.append(self.reset)
                                #new_line.append("\t    ")
                                new_line.append(self.get_color("gray", None, True))
                                new_line.append(token)
                                new_line.append(self.get_color("magenta", None, False))
                            elif "in" == token:
                                #p(repr(token))
                                new_line.append(self.reset)
                                new_line.append(self.get_color("gray", None, True))
                                new_line.append(token)
                                new_line.append(self.get_color("magenta", None, False))
                            else:
                                new_line.append(token)
                        output_list.append(" ".join(new_line))
                    else:
                            #new_line.append()
                        #self.get_color("yellow", None, False)
                        output_list.append("\n     ")
                        output_list.append(self.get_color("magenta"))
                        output_list.append(line)
                        output_list.append("\n")
                        output_list.append(self.reset)
            

            record.exc_text = "".join(output_list)  + "\n\n\n\n"          #p(record.exc_text )

    def format(self, record):
        """
        Formats a record for output.

        Takes a custom formatting path on a terminal.
        """
        if self.is_tty:
            message = self.colorize(record)
        else:
            message = logging.StreamHandler.format(self, record)

        return message





class MultiHandler(logging.Handler):
    def __init__(self, dirname):
        super(MultiHandler, self).__init__()
        self.files = {}
        self.dirname = dirname
        if not os.access(dirname, os.W_OK):
            raise Exception("Directory %s not writeable" % dirname)

    def flush(self):
        self.acquire()
        try:
            for fp in self.files.values():
                fp.flush()
        finally:
            self.release()

    def _get_or_open(self, key):
        "Get the file pointer for the given key, or else open the file"
        self.acquire()
        try:
            if self.files.has_key(key):
                return self.files[key]
            else:
                fp = open(os.path.join(self.dirname, "%s.log" % key), "a")
                #fp.write("\n\n")
                self.files[key] = fp
                return fp
        finally:
            self.release()

    def emit(self, record):
        # No lock here; following code for StreamHandler and FileHandler
        try:
            fp = self._get_or_open(record.threadName)
            msg = self.format(record)
            fp.write('%s\n' % msg.encode("utf-8"))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)



class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.

    Rather than use actual contextual information, we just use random
    data in this demo.
    """

    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def filter(self, record):
        #record.sthread = choice(ContextFilter.IPS)
        record.sthread = str(record.thread)[10:] if len(
                        str(record.thread)) > 10 else str(record.thread)
        #p(record.sthread)
        #record.user = choice(ContextFilter.USERS)
        return True



class SmartBufferHandler(logging.handlers.MemoryHandler,ColorizingStreamHandler):
    def __init__(self, num_buffered, *args, **kwargs):
        kwargs["capacity"] = num_buffered + 2  # +2 one for current, one for prepop
        super(SmartBufferHandler,self).__init__(*args, **kwargs)
    
    # Define color for message payload
    level_map = {
        logging.DEBUG: (None, 'cyan', False),
        logging.INFO: (None, 'white', True),
        logging.WARNING: ("yellow", 'white', True),
        logging.ERROR: ( 'red', "white", True),
        logging.CRITICAL: ('magenta', 'white', True),
    }


    def get_color(self, fg=None, bg=None, bold=False):
        """
        Construct a terminal color code

        :param fg: Symbolic name of foreground color

        :param bg: Symbolic name of background color

        :param bold: Brightness bit
        """
        params = []
        if bg in self.color_map:
            params.append(str(self.color_map[bg] + 40))
        if fg in self.color_map:
            params.append(str(self.color_map[fg] + 30))
        if bold:
            params.append('1')

        color_code = ''.join((self.csi, ';'.join(params), 'm'))

        return color_code



    def emit(self, record):
        if len(self.buffer) == self.capacity - 1:
            self.buffer.pop(0)


        #super(SmartBufferHandler,self).emit(record)
        """
        Emit a record.

        Append the record. If shouldFlush() tells us to, call flush() to process
        the buffer.
        """
        self.buffer.append(record)
        if self.shouldFlush(record):
            #p(self.get_color("magenta",None,True))
            print "\n\n{}Last {} Records (bevore error occurred) will be printed:{}".format(self.get_color("magenta",None,True),self.capacity-1, self.reset)
            print "-----------------START of the CAPTURE--------------------"
            self.flush()
            print "-----------------END of the CAPTURE---------------------\n\n"

        




def extract_function_name():
    """Extracts failing function name from Traceback
    by Alex Martelli
    http://stackoverflow.com/questions/2380073/\
    how-to-identify-what-function-call-raise-an-exception-in-python
    """
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    fname = stk[0][3]
    return fname


def log_exception(logger, e, msg):
    logger.error(
    "Function '{function_name}' raised '{exception_class}' ({exception_docstring}): '{exception_message}'. Additional Info: '{msg}'. ".format(
    msg= msg,
    function_name = extract_function_name(), #this is optional
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
    exception_message = e.message))



class DuplicateFilter(logging.Filter):

    def filter(self, record):
        # add other fields if you need more granular comparison, depends on your app
        #p(current_log)
        current_log = (record.module, record.levelno, record.msg)
        #p(getattr(self, "last_log", None), c="r")
        if record.msg != getattr(self, "last_log", None):
            self.last_log = current_log
            return True
        return False


        # if current_log != getattr(self, "last_log", None):
        #     self.last_log = current_log
        #     return True
        # return False



# class Zas_logger(self):
#     def __init__(self):


# class MaxLevelFilter(Filter):
#     '''Filters (lets through) all messages with level < LEVEL'''
#     def __init__(self, level):
#         self.level = level

#     def filter(self, record):
#         return record.levelno < self.level # "<" instead of "<=": since logger.setLevel is inclusive, this should be exclusive


class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level




def get_logs_folder_for_current_event(folder_for_logs):
    if not  os.path.isdir(folder_for_logs):
        os.mkdir(folder_for_logs)

    
    daynow = datetime.date.today().strftime("%Y_%m_%d")
    day_folder = os.path.join(folder_for_logs,daynow)
    if not os.path.isdir(day_folder):
        os.mkdir(day_folder)


    timenow = time.strftime('%H_%M') # %H:%M:%S
    time_folder = os.path.join(day_folder,timenow)
    if not os.path.isdir(time_folder):
        os.mkdir(time_folder)

     
    # i=1
    # while True:
    #     event_folder_name = "{}_{}".format(i,timenow)
    #     path_to_event_folder = os.path.join(day_folder, event_folder_name)
    #     if not  os.path.isdir(path_to_event_folder):
    #         os.mkdir(path_to_event_folder)
    #         break
    #     i+=1
    path_to_event_folder = time_folder
    return path_to_event_folder


def get_logger_names_of_activ_loggers(handlers_list):
    # for logger in logger.handlers:
    #     p(type(logger))
    output= defaultdict(list )
    #return {type(logger).__name__:logger.level for logger in handlers_list}
    for logger in handlers_list:
        output[type(logger).__name__].append(logger.level)
    return output
    #return {type(logger).__name__:logger.level for logger in handlers_list}




def add_stream_handler(logger, current_handler):
    i = 0
    indexes_to_delete = []
    #print "befove", logger.handlers
    for hndlr in logger.handlers:
        if type(current_handler).__name__ == type(hndlr).__name__:
            indexes_to_delete.append(i)
        i+=0
    for indx in  indexes_to_delete:
        #print logger.handlers[indx]
        del logger.handlers[indx]
    #print "middle", logger.handlers
    logger.addHandler(current_handler)
    #print "after", logger.handlers



def add_file_handler(logger, current_handler):
    i = 0
    indexes_to_delete = []
    #print "befove", logger.handlers
    for hndlr in logger.handlers:
        if type(current_handler).__name__ == type(hndlr).__name__:
            if current_handler.level ==hndlr.level:
                indexes_to_delete.append(i)
        i+=0
    for indx in  indexes_to_delete:
        #print logger.handlers[indx]
        del logger.handlers[indx]
    #print "middle", logger.handlers
    logger.addHandler(current_handler)
    #print "after", logger.handlers




def main_logger(logger_name, level=logging.INFO,  folder_for_log="logs", use_logger=True, save_logs=False, num_buffered=5):
    folder_for_log = "logs" if not folder_for_log else folder_for_log

    # filters
    d = DuplicateFilter()
    f = ContextFilter()
    #p(level, c="r")
    logger = logging.getLogger(logger_name)
    #logger.setLevel(logging.DEBUG)
    if save_logs:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(level)
    logger.addFilter(d)
    logger.addFilter(f)


    # Create a logger, with the previously-defined handler
    handler = RainbowLoggingHandler(sys.stdout)
    handler.setLevel(level)
    if level == logging.ERROR:
        handler.addFilter(MyFilter(logging.ERROR))
    logger.addFilter(f)

    add_stream_handler(logger, handler)

    #logger.setLevel(level)
    #p(logger.handlers, c="r")
    #p(get_logger_names_of_activ_loggers(logger.handlers), c="r")
    # activ_handlers = get_logger_names_of_activ_loggers(logger.handlers)
    # if (type(handler).__name__ not in activ_handlers) or (logging.INFO not in  activ_handlers[type(handler).__name__] ):
    #     logger.addHandler(logger.handlers)
    # else:
    

    #p((logging.INFO, logging.DEBUG, logging.ERROR)) #-> (20, 10, 40)
    if not use_logger:
        logger.disabled = True
        logger.propagate = False
        return logger


    # coloredlogs.install(level=level, logger=logger)
    #p((save_logs,logger_name),"save_logs")
    if save_logs:
        path_to_logs_folder_current_event = get_logs_folder_for_current_event(folder_for_log)
        
        # create error file handler and set level to error
        handler = logging.FileHandler( os.path.join(path_to_logs_folder_current_event, "error.log") ,"a", encoding=None, delay="true")
        handler.setLevel(logging.ERROR)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()] %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        handler.setFormatter(formatter)
        handler.addFilter(MyFilter(logging.ERROR))
        add_file_handler(logger, handler)

        # create debug file handler and set level to debug
        handler = logging.FileHandler(os.path.join(path_to_logs_folder_current_event, "critical.log") ,"a")
        handler.setLevel(logging.CRITICAL)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()]  %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        handler.setFormatter(formatter)
        handler.addFilter(MyFilter(logging.CRITICAL))
        activ_handlers = get_logger_names_of_activ_loggers(logger.handlers)
        add_file_handler(logger, handler)

        # create debug file handler and set level to debug
        handler = logging.FileHandler(os.path.join(path_to_logs_folder_current_event, "warning.log") ,"a")
        handler.setLevel(logging.WARNING)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()]  %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        handler.setFormatter(formatter)
        handler.addFilter(MyFilter(logging.WARNING))
        activ_handlers = get_logger_names_of_activ_loggers(logger.handlers)
        add_file_handler(logger, handler)


        # create debug file handler and set level to debug
        handler = logging.FileHandler(os.path.join(path_to_logs_folder_current_event, "info.log"),"a")
        handler.setLevel(logging.INFO)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()]  %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        handler.setFormatter(formatter)
        #handler.addFilter(MyFilter(logging.INFO))
        #handler.addFilter(MyFilter(logging.INFO))
        add_file_handler(logger, handler)


        # create debug file handler and set level to debug
        handler = logging.FileHandler(os.path.join(path_to_logs_folder_current_event, "debug.log") ,"a")
        handler.setLevel(logging.DEBUG)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()]  %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        handler.setFormatter(formatter)
        activ_handlers = get_logger_names_of_activ_loggers(logger.handlers)
        add_file_handler(logger, handler)

        multi_handler = MultiHandler(path_to_logs_folder_current_event)
        multi_handler.setLevel(level)
        #p(handler.level, c="m")
        formatter = logging.Formatter('%(asctime)7s [%(name)s] %(threadName)11s:{%(sthread)s} [%(funcName)s()] %(levelname)5s \n %(message)s \n', "%H:%M:%S")
        multi_handler.setFormatter(formatter)
        #logging.getLogger().addHandler(multi_handler)
        add_file_handler(logger,multi_handler)
        #p(get_logger_names_of_activ_loggers(logger.handlers), c="b")

    return logger



    def errorLogger(self, logger_name, level=logging.INFO):
        
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        #coloredlogs.install(level=level, logger=logger)
        #p(logger.handlers)
        if len(logger.handlers): # to delete massage duplicates
            while logger.handlers:
                logger.handlers.pop()
        return logger




