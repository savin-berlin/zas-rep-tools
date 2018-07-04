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

from zas_rep_tools.src.classes.DBHandler import DBHandler
from zas_rep_tools.src.classes.Reader import Reader
from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation



class Corpus(object):

    def __init__(self, 
                 folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



        ## Logger Initialisation 
        logger = Logger()
        self._folder_for_log_files = folder_for_log_files
        self._use_logger = use_logger
        self._logger_level = logger_level
        self.logger = logger.myLogger("Corpus", self._folder_for_log_files, use_logger=self._use_logger, level=self._logger_level)

        self.logger.debug('Beginn of creating an instance of Corpus()')



        #Input: Incaplusation:
        self._error_tracking = error_tracking

        #p(inpdata)

        #InstanceAttributes: Initialization
        self.db = False


        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')


        self.logger.debug('An instance of Corpus() was created ')



        ############################################################
        ####################__init__end#############################
        ############################################################


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################Extern########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################



###########################+++++++++############################


    def init(self, prjFolder, DBname, language,  visibility, platform_name,
                    encryption_key=False,fileName=False, source=False, license=False,
                    template_name=False, version=False,
                    additional_columns_with_types_for_documents=False, corpus_id=False):

        if self.db:
            self.logger.error("CorpusInitError: An active Corpus Instance was found. Please close already initialized/opened Corpus, before new initialization.")
            return False

        self.db = DBHandler(logger_level=self._logger_level)
        self.db.init("corpus", prjFolder, DBname, language, visibility,
            platform_name=platform_name,encryption_key=encryption_key, fileName=fileName,
            source=source, license=license, template_name=template_name, version=version,
            additional_columns_with_types_for_documents=additional_columns_with_types_for_documents,
            corpus_id=corpus_id)

        if self.db.exist():
            self.logger.info("CorpusInit: '{}'-Corpus was successful initialized.".format(DBname))
            return True
        else:
            self.logger.error("CorpusInit: '{}'-Corpus wasn't  initialized.".format(DBname))
            return False



    def open(self, path_to_corp_db, encryption_key=False):

        if self.db:
            self.logger.error("CorpusInitError: An active Corpus Instance was found. Please close already initialized/opened Corpus, before new initialization.")
            return False

        self.db = DBHandler(logger_level=self._logger_level)
        self.db.connect(path_to_corp_db, encryption_key=encryption_key)


        if self.db.exist():
            self.logger.info("CorpusOpener: '{}'-Corpus was successful opened.".format(os.path.basename(path_to_corp_db)))
            return True
        else:
            self.logger.error("CorpusOpener: Unfortunately '{}'-Corpus wasn't opened.".format(os.path.basename(path_to_corp_db)))
            return False





    def exist(self):
        return True if self.db else False




    def getdb(self):
        self.logger.debug("DBConnection was passed.")
        return self.db









####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################INTERN########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


























####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
###################################Other Classes#####################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

# class BloggerCorpus(Corpus):

#     def __init__(self, inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("BloggerCorpus", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of BloggerCorpus()')



#         #Input: Incaplusation:
#         self._inpdata = inpdata

#         self._error_tracking = error_tracking

#         #p(inpdata)

#         #InstanceAttributes: Initialization




#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of BloggerCorpus() was created ')


# class TwitterCorpus(Corpus):

#     def __init__(self, inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=True):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("BloggerCorpus", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of BloggerCorpus()')



#         #Input: Incaplusation:
#         self._inpdata = inpdata

#         self._error_tracking = error_tracking

#         #p(inpdata)

#         #InstanceAttributes: Initialization




#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})


#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of BloggerCorpus() was created ')


# class Document(object):
#     def __init__(inpdata, 
#                  folder_for_log_files=False,  use_logger=True, logger_level=logging.INFO, error_tracking=False):



#         ## Logger Initialisation 
#         logger = Logger()
#         self._folder_for_log_files = folder_for_log_files
#         self._use_logger = use_logger
#         self.logger = logger.myLogger("Document", self._folder_for_log_files, use_logger=self._use_logger, level=logger_level)

#         self.logger.debug('Beginn of creating an instance of Document()')



#         #Input: Incaplusation:
#         self._error_tracking = error_tracking



#         #InstanceAttributes: Initialization




#         ## Error-Tracking:Initialization #1
#         if self._error_tracking:
#             self.client = initialisation()
#             self.client.context.merge({'tags': self.__dict__})



#         self.logger.debug('Intern InstanceAttributes was initialized')



#         ### Error Tracking #2
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})


#         ### Error Tracking #3
#         if self._error_tracking:
#             self.client.context.merge({'tags': self.__dict__})




#         self.logger.debug('An instance of BloggerCorpus() was created ')



