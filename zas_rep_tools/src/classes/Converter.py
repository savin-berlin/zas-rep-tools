#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : XXX{Information about this code}XXX
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#



import os
import copy
import sys
import regex
import logging


#from collections import defaultdict
from raven import Client
from cached_property import cached_property


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation



class Converter(object):

    def __init__(self, inpdata, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("Converter", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of Converter()')



        #Input: Incaplusation:
        self._inpdata = inpdata

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization




        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'InstanceAttributes': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'InstanceAttributes': self.__dict__})


        ### Error Tracking #3
        if self._error_tracking:
            self.client.context.merge({'InstanceAttributes': self.__dict__})




        self.logger.debug('An instance of Converter() was created ')


