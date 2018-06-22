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


import codecs
import sure
import inspect
import copy
from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import glob

from zas_rep_tools.src.classes.DB import DB

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZAScorpusDBDB(unittest.TestCase):
    def setUp(self):



        ######## Folders Creation ##############
        ########### Begin ######################
        abs_path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(DB))))
        #p(abs_path_to_zas_rep_tools)
        relativ_path_to_test_prjFolder = "data/tests_data/testDBs/prjFolder"
        self.abs_path_to_test_prjFolder = os.path.join(abs_path_to_zas_rep_tools,relativ_path_to_test_prjFolder)
        relativ_path_to_test_testFolder = "data/tests_data/testDBs/testFolder"
        self.abs_path_to_test_testFolder = os.path.join(abs_path_to_zas_rep_tools,relativ_path_to_test_testFolder)


        relativ_path_to_test_corpus = "data/tests_data/testDBs/test/corpus.db"
        relativ_path_to_test_stats = "data/tests_data/testDBs/test/stats.db"
        self.abs_path_to_test_corpus = os.path.join(abs_path_to_zas_rep_tools,relativ_path_to_test_corpus)
        self.abs_path_to_test_stats = os.path.join(abs_path_to_zas_rep_tools,relativ_path_to_test_stats)


        self.tempdir = TempDirectory()
        self.tempdir.makedir('PrjFolder')
        self.tempdir.makedir('TestFolder')
        self.path_to_temp_prjFolder  = self.tempdir.getpath('PrjFolder')
        self.path_to_temp_testFolder  = self.tempdir.getpath('TestFolder')
        copy_tree(self.abs_path_to_test_prjFolder,self.path_to_temp_prjFolder )
        copy_tree(self.abs_path_to_test_testFolder,self.path_to_temp_testFolder )

        self.path_to_temp_test_corpus = os.path.join(self.path_to_temp_testFolder, "corpus.db")
        self.path_to_temp_test_stats = os.path.join(self.path_to_temp_testFolder, "stats.db")
        self.path_to_temp_test_fakeDB = os.path.join(self.path_to_temp_testFolder, "fakeDB.db")
        ######## Folders Creation ##############
        ########### End #####################
        



    def tearDown(self):
        self.tempdir.cleanup()
        print ">>>TempDirectory was cleaned<<<"


####################################################################################################
####################################################################################################
###################### START STABLE TESTS #########################################################
####################################################################################################
####################################################################################################


###################INITIALISATION:000############################################



    # ###### xxx: 000 ######
    # #@attr(status='stable')True
    # #@wipd
    # def test_initialisation_000(self):
    #     db = DB( developingMode = True)
    #     #db = DB()
    #     #db.initialise_corpus(self.path_to_temp_prjFolder, "twitter_streamed_de", "de", "twitter", "intern")
    #     #db.initialise_corpus(self.abs_path_to_test_prjFolder, "twitter_streamed_de", "de", "twitter", "intern")
    #     #p(db.rowsNumber("info"))
    #     # p(db.tables())
    #     # p(db.tableColumns("info"))
    #     #p(db.tableColumnsTypes("info"))
    #     #p(db.tableColumns("info"))
    #     #p(db.get_attribut(u"visibility"))
    #     # p(db.rowsNumber("info"))

        
    #     #db = DB( )
    #     db = DB( developingMode = True)
    #     db.initialise_stats(self.path_to_temp_prjFolder, "twrd", "twitter_streamed", "intern", "de")
    #     #db.initialise_stats(self.abs_path_to_test_prjFolder, "twrd", "twitter_streamed", "intern", "de")
    #     #p(db.tables())
    #     #p(db.tableColumns("info"))
    #     #p(db.get_all_attributs())
    #     #db.update_attribut("version","7")
    #     #p(db.get_all_attributs())


 
    @wipd
    def test_initialisation_001(self):
        db = DB( developingMode = True)
        db.connect(self.path_to_temp_test_corpus )
        #db.connect(self.path_to_temp_test_fakeDB)
        db.attach(self.path_to_temp_test_stats)
        p(db.fname())
        p(db.path())
        #p(db.attachedDBs())
        p(db.attachedDBs())
        p(db.fnameAttachedDBs())
        p(db.pathAttachedDBs())
        p(db.dbsName())







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


    # #@attr(status='stable')True
    # @oldwipd
    # def test_025(self):
    #     additional_dbs = [

    #             "/Users/egoruni/Desktop/BA/Code/zas-rep-tools/zas_rep_tools/data/DB/testDBs/additionalDBs/bloggerDB.db", 
    #             "/Users/egoruni/Desktop/BA/Code/zas-rep-tools/zas_rep_tools/data/DB/testDBs/additionalDBs/twitterDB.db",
    #             "/Users/egoruni/Desktop/BA/Code/zas-rep-tools/zas_rep_tools/data/DB/testDBs/additionalDBs/facebookDB.db",
    #             "/Users/egoruni/Desktop/BA/Code/zas-rep-tools/zas_rep_tools/data/DB/testDBs/additionalDBs/fakeDB.db",
    #             ]

    #     #database = DB("/Users/egoruni/Desktop/BA/Code/test/PrjData", developingMode = True)
    #     database = DB("/Users/egoruni/Desktop/BA/Code/test/PrjData", additional_DBs=additional_dbs,  developingMode = True)
    #     #database.del_mainDB()
    #     database.create_project("twitter", "/Users/egoruni/Desktop/BA/Code/test/PrjData")
    #     database.create_project("blogger", "/Users/egoruni/Desktop/BA/Code/test/PrjData")
    #     database.create_project("facebook", "/Users/egoruni/Desktop/BA/Code/test/PrjData",
    #             documents_columns={
    #                 "age":"INTEGER",
    #                 "gender":"TEXT",
    #                 "post_data":"TEXT",
    #             })
    #     # p(database.get_attached_dbs("paths"), c="m")
    #     # p(database.get_attached_dbs("names"), c="m")
    #     # p(database.tables("main"), c="r")
    #     # p(database.tables("twitter"), c="r")
    #     # p(database.tables("blogger"), c="r")
    #     # #p(database.get_tableInfo("Projects"), c="r")
    #     # #p(database.get_tableInfo("Corpora", "blogger"), c="r") 
    #     # #p(database.get_fk("Corpora", "blogger"), c="r")
    #     # #p(database.get_ix_list("Corpora", "blogger"), c="r")
    #     # #p(database.get_ix_info("ix_corpora_template_corpus", "blogger"), c="r")
    #     # p(database._get_all_prjDBs_paths(), c="m")
        

    #     database._attach_all_existing_prjDBs()
    #     # p(database.get_tableInfo("Projects"), c="r")
    #     # p(database.supported_projects())
    #     # p(database.supported_projects_with_ids())
    #     # database.add_language_into_mainDB("german", "de")
    #     # database.add_language_into_mainDB("english", "en")
    #     # p(database.supported_lang())
    #     # p(database.supported_lang_with_ids())
    # ##### throws_exceptions:050  ######











####################################################################################################
####################################################################################################
###################### STOP WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################







