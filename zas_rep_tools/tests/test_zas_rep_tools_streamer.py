#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Tests for XXX Module
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#





import unittest
import os
import logging

import sure
import sys
import inspect
import copy
from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import glob
import signal
import subprocess
#import multiprocessing

from zas_rep_tools.src.classes.Streamer import Streamer
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.test_helpers import exit_after





class TestZASStreamerStreamer(unittest.TestCase):
    def setUp(self):



        ######## Folders Creation ##############
        ########### Begin ######################
        self._path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Streamer))))
        #p(self._path_to_zas_rep_tools)


        #test-API-Data: it is just a test account! Please dear peeps, don't use it for another goals! 
        self.test_consumer_key = "97qaczWSRfaaGVhKS6PGHSYXh"
        self.test_consumer_secret = "mWUhEL0MiJh7FqNlOkQG8rAbC8AYs4YiEOzdiCwx26or1oxivc"
        self.test_access_token = "1001080557130932224-qi6FxuYwtvpbae17kCjAS9kfL8taNT"
        self.test_access_token_secret = "jCu2tTVwUW77gzOtK9X9svbdKUFvlSzAo4JfIG8tVuSgX"


        self.tempdir = TempDirectory()
        self.tempdir.makedir('TwitterStream')
        self.path_to_output = self.tempdir.getpath("TwitterStream")
        #p(self.path_to_output)
        ######## Folders Creation ##############
        ########### End #####################
        
        



    def tearDown(self):
        #copy_tree(self.path_to_output,os.path.join(self._path_to_zas_rep_tools, "temp"))
        self.tempdir.cleanup()
        #p("Every-thing was cleaned")


####################################################################################################
####################################################################################################
###################### START STABLE TESTS #########################################################
####################################################################################################
####################################################################################################


###################INITIALISATION:000############################################



    ###### xxx: 000 ######




    ##### xx :0== ######


    @attr(status='stable')
    #@wipd
    def test_streamer_initialisation_000(self):
        stream = Streamer(self.test_consumer_key,self.test_consumer_secret,self.test_access_token,self.test_access_token_secret,self.path_to_output, language="de")

        assert  isinstance(stream, Streamer)
        #stream.stream_twitter()
        #BloggerCorp = Converter(self.small_subset)

        

    ##### throws_exceptions:050  ######




#################################Beginn##############################################
############################INTERN METHODS###########################################
#####################################################################################

###################    :100############################################ 

    ###### ***** ######

    #@attr(status='stable')
    #@wipd
    #def test_XXX_name_100(self):
    ##self.logger_initialisation()
    #   pass

    ###### ***** ######


    ###### ***** ######






#################################END#################################################
############################INTERN METHODS###########################################
#####################################################################################



#################################Beginn##############################################
############################EXTERN METHODS###########################################
#####################################################################################


###################    :500############################################ 
    ###### ***** ######
   
    #@attr(status='stable')
    @wipd
    def test_stream_twitter_500(self):
        stream = Streamer(self.test_consumer_key,self.test_consumer_secret,self.test_access_token,self.test_access_token_secret,self.path_to_output, use_logger=False, language="de")

        #assert  isinstance(stream, Streamer)
        #stream.stream_twitter()
        #print "fghjk"
        try:
            @exit_after(5)
            def run_streamer():
                stream.stream_twitter()

            run_streamer()
        except SystemExit:
            assert  True

        # try:
        #     run_streamer()
        # except SystemExit:
        #     assert  True  
        # except:
        #     assert False  



        # Start bar as a process
        # p = multiprocessing.Process(target=stream.stream_twitter())
        # p.start()

        #     # Wait for 10 seconds or until process finishes
        # p.join(10)

        #  # If thread is still active
        # if p.is_alive():
        #     print "running... let's kill it..."

        #     # Terminate
        #     p.terminate()
        #     p.join()



        # def timeout(func, args=(), kwargs={}, timeout_duration=5, default=None):
        #     import signal

        #     class TimeoutError(Exception):
        #         pass

        #     def handler(signum, frame):
        #         raise TimeoutError()

        #     # set the timeout handler
        #     signal.signal(signal.SIGINT, handler) 
        #     signal.alarm(timeout_duration)
        #     try:
        #         result = func(*args, **kwargs)
        #     except TimeoutError as exc:
        #         result = default
        #     finally:
        #         signal.alarm(0)

        #     return result


        # timeout(stream.stream_twitter())


            #exit(signal.SIGINT)

        # signal.signal(signal.SIGINT, stream.stream_twitter())
        # signal.alarm(10)



        # def handler():
        #     stream.stream_twitter()

        # # Set the signal handler and a 5-second alarm
        # signal.signal(signal.SIGINT, handler)
        # signal.alarm(5)

        # # This open() may hang indefinitely
        # #fd = os.open('/dev/ttyS0', os.O_RDWR)

        # signal.alarm(0)

        # handler()

            # signal.SIGINT
            # process = subprocess.Popen(..)
        # process.send_signal()


        

   



#################################END##################################################
############################EXTERN METHODS############################################
######################################################################################





####################################################################################################
####################################################################################################
###################### STOP STABLE TESTS #########################################################
####################################################################################################
####################################################################################################


























####################################################################################################
####################################################################################################
###################### START WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################











####################################################################################################
####################################################################################################
###################### STOP WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################







