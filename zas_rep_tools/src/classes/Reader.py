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
import codecs


#from collections import defaultdict
from raven import Client
from cached_property import cached_property
from encodings.aliases import aliases


from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.helpers import get_file_list



class Reader(object):
    #supported_encodings_types = ["utf-8"]
    supported_encodings_types = set(aliases.values())
    def __init__(self, inpdata, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("Reader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of Reader()')



        #Input: Incaplusation:
        self._inpdata = inpdata

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization
        #self._



        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})


        ### Error Tracking #3
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})




        self.logger.debug('An instance of Reader() was created ')




class PlainTextCorpusReader(Reader):
    def __init__(self, path_to_corp, encoding="utf_8",
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):


        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("PlainTextCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of PlainTextCorpusReader()')


        ## Error-Tracking:Initialization #1
        if error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        #Input: Encapsulation:
        self._path_to_corp = path_to_corp
        self._encoding = encoding
        self._error_tracking = error_tracking

        #p(path_to_corp)

        self.logger.debug('Input was encapsulated')


        #InstanceAttributes: Initialization
        self._paths_list = get_file_list(path_to_corp, ".txt")
        self._readed_data = self._read_data()
        #p( self._readed_data )


        self.logger.debug('Intern InstanceAttributes was initialized')

        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('An instance of PlainTextCorpusReader() was created ')


    def _read_data(self):
        if self._paths_list:
            readed_data = {file:codecs.open(os.path.join(self._paths_list[0],file), encoding=self._encoding).read() for file in self._paths_list[1]}
            return (self._paths_list[0], readed_data)
            
        else:
            self.logger.error("Any *.txt wasn't find in the given path.")
            sys.exit()






class XMLCorpusReader(Reader):
    def __init__(self, inpdata, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("XMLCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of XMLCorpusReader()')



        #Input: Incaplusation:
        self._inpdata = inpdata

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization



        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})


        ### Error Tracking #3
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})




        self.logger.debug('An instance of XMLCorpusReader() was created ')


class CSVCorpusReader(Reader):
    def __init__(self, inpdata, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("CSVCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of CSVCorpusReader()')



        #Input: Incaplusation:
        self._inpdata = inpdata

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization



        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})


        ### Error Tracking #3
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})




        self.logger.debug('An instance of CSVCorpusReader() was created ')




class JSONCorpusReader(Reader):
    def __init__(self, inpdata, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self.logger = logger.myLogger("JSONCorpusReader", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

        self.logger.debug('Beginn of creating an instance of JSONCorpusReader()')



        #Input: Incaplusation:
        self._inpdata = inpdata

        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization



        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')



        ### Error Tracking #2
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})


        ### Error Tracking #3
        if self._error_tracking:
            self.client.context.merge({'tags': self.__dict__})




        self.logger.debug('An instance of JSONCorpusReader() was created ')




