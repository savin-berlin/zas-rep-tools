import os
import time
import datetime
import logging
import coloredlogs
from zas_rep_tools.src.utils.debugger import p
from raven.conf import setup_logging



class Logger :
    coloredlogs.DEFAULT_DATE_FORMAT = "%H:%M:%S"
    coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s  %(name)s %(levelname)s %(message)s'
    def myLogger(self, logger_name, folder_for_log=False,  level=logging.INFO , use_logger=True, save_logs=False): # for classes
        coloredlogs.install(level=level)


        self.logger = logging.getLogger(logger_name)
        save_logs = True if folder_for_log else False

        ## coloring
        # logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        # logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
        # logging.addLevelName( logging.CRITICAL, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.CRITICAL))
        # logging.addLevelName( logging.INFO, "\033[1;95m%s\033[1;0m" % logging.getLevelName(logging.INFO))

        #p(self.logger.handlers)
        if len(self.logger.handlers): # to delete massage duplicates
            while self.logger.handlers:
                self.logger.handlers.pop()

        if use_logger:
            #p("fuck u 1.1")

            # logging.basicConfig(level=logging.DEBUG, # set up logging to file - see previous section for more details
            #         format='%(asctime)s %(levelname)s  %(name)-12s  %(message)s',
            #         datefmt='%m-%d %H:%M:%S',
            #         filename='/te##mp/myapp.log',
            #         filemode='w')

            
            ##### Logger Initialisation: #######
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(logging.DEBUG)

            # # create console handler and set level to info
            # handler = logging.StreamHandler()
            # handler.setLevel(level)
            # formatter = logging.Formatter("%(asctime)s,%(msecs)03d %(name)-12s: %(levelname)-8s %(message)s", "%H:%M:%S")
            # handler.setFormatter(formatter)
            # self.logger.addHandler(handler)
            # #setup_logging(handler)

            #! if folder_for_log :
            #!     if save_logs:
            #!         # create debug file handler and set level to debug
            #!         now = datetime.datetime.now()
            #!         fname = logger_name + "_" + now.strftime("%Y:%m:%d_%H-%M-%S-%f") +'.log'
            #!         handler=logging.FileHandler(os.path.join(folder_for_log,fname))
            #!         handler.setLevel(logging.DEBUG)
            #!         #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            #!         formatter = logging.Formatter("%(asctime)s.%(msecs)03d  %(name)-12s %(levelname)-8s %(message)s", "%H:%M:%S")
            #!         handler.setFormatter(formatter)
            #!         self.logger.addHandler(handler)
            #!         self.logger.propagate = False  
                #return self.logger

            #return self.logger
        else: 
            #p("fuck u 1.2")
            #self.logger = logging.getLogger()
            self.logger.disabled = True
            self.logger.propagate = False
            return self.logger

        return self.logger


    def myLogger2(self,  folder_for_log=False,  logger_name="",  level=logging.INFO, use_logger=True, save_logs=False): #for scripts 
        coloredlogs.install(level=level)



        self.logger = logging.getLogger(logger_name)
        save_logs = True if folder_for_log else False

        ## coloring
        # logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        # logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
        # logging.addLevelName( logging.CRITICAL, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.CRITICAL))
        # logging.addLevelName( logging.INFO, "\033[1;95m%s\033[1;0m" % logging.getLevelName(logging.INFO))


        self.logger.setLevel(logging.DEBUG)

        if not os.path.isdir(folder_for_log):
            os.makedirs(folder_for_log)

        if len(self.logger.handlers): # to delete massage duplicates
            while self.logger.handlers:
                self.logger.handlers.pop()

        if use_logger:
            #p("fuck u 2.1")
            # logging.basicConfig(level=logging.DEBUG, # set up logging to file - see previous section for more details
            #         format='%(asctime)s %(levelname)s  %(name)-12s  %(message)s',
            #         datefmt='%m-%d %H:%M:%S',
            #         filename='/temp/myapp.log',
            #         filemode='w')

            
            ##### Logger Initialisation: #######
            now = datetime.datetime.now()

            # create console handler and set level to info
            # handler = logging.StreamHandler()
            # handler.setLevel(level)
            # formatter = logging.Formatter("%(asctime)s,%(msecs)03d %(name)-12s: %(levelname)-8s %(message)s", "%H:%M:%S")
            # handler.setFormatter(formatter)
            # self.logger.addHandler(handler)
            #setup_logging(handler)

            if not folder_for_log:
                if save_logs:

                    # create error file handler and set level to error
                    handler = logging.FileHandler( "error.log","w", encoding=None, delay="true")
                    handler.setLevel(logging.ERROR)
                    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
                    handler.setFormatter(formatter)
                    self.logger.addHandler(handler)

                    # create debug file handler and set level to debug
                    handler = logging.FileHandler("all.log","w")
                    handler.setLevel(logging.DEBUG)
                    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
                    handler.setFormatter(formatter)
                    self.logger.addHandler(handler)



                    #self.logger.propagate = False
                return self.logger
            else:
                if save_logs:
                    # create error file handler and set level to error
                    fname_error = "error_logs"+ now.strftime("%Y:%m:%d_%H-%M-%S-%f") +'.log'
                    handler = logging.FileHandler( os.path.join(folder_for_log, fname_error) ,"w", encoding=None, delay="true")
                    handler.setLevel(logging.ERROR)
                    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
                    handler.setFormatter(formatter)
                    self.logger.addHandler(handler)

                    # create debug file handler and set level to debug
                    fname_all = "all_logs"+ now.strftime("%Y:%m:%d_%H-%M-%S-%f") +'.log'
                    handler = logging.FileHandler(os.path.join(folder_for_log, fname_all),"w")
                    handler.setLevel(logging.DEBUG)
                    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
                    handler.setFormatter(formatter)
                    self.logger.addHandler(handler)
                    self.logger.propagate = False

                    # create debug file handler and set level to debug
                    fname_all = "INFO_"+ now.strftime("%Y:%m:%d_%H-%M-%S-%f") +'.log'
                    handler = logging.FileHandler(os.path.join(folder_for_log, fname_all),"w")
                    handler.setLevel(logging.INFO)
                    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
                    handler.setFormatter(formatter)
                    self.logger.addHandler(handler)

                return self.logger
        else: 
            #p("fuck u 2.2")
            self.logger.propagate = False
            self.logger.disabled = True
            return self.logger

        #return self.logger

# s = Logger()
# m = s.myLogger()
# m2 = s.myLogger()
# m.info("Info1")
# m2.info("info2")