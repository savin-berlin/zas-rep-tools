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

from zas_rep_tools.src.classes.DBHandler import DBHandler

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZAScorpusDBHandlerDBHandler(unittest.TestCase):
    def setUp(self):



        ######## Folders Creation ##############
        ########### Begin ######################
        abs_path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Logger))))
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
        self.path_to_temp_test_stats_encrypted = os.path.join(self.path_to_temp_testFolder, "stats_encrypted.db")
        self.path_to_temp_test_stats_plain_text = os.path.join(self.path_to_temp_testFolder, "stats_plain_text.db")
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




    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_initialisation_000(self):
        db = DBHandler()
        assert not db.get_db()
        #assert db._attachedDBs_config is False
        assert not db._attachedDBs_config 
        assert not db._tables_dict 
        assert not db._attributs_dict 
        assert not db.dbnames 



    ###### xxx: 000 ######
    #@attr(status='stable')
    @wipd
    def test_dbhandler_initialisation_of__corpus__001(self):
        stats = DBHandler().init("corpus",
                            self.path_to_temp_prjFolder, "streamed", "de",
                            "intern", "twitter")





    # ###### xxx: 000 ######
    # #@attr(status='stable')True
    # #@wipd
    # def test_initialisation_000(self):
    #     db = DBHandler( developingMode = True)
    #     #db = DBHandler()
    #     #db.init_corpus(self.path_to_temp_prjFolder, "twitter_streamed_de", "de", "twitter", "intern")
    #     #db.init_corpus(self.abs_path_to_test_prjFolder, "twitter_streamed_de", "de", "twitter", "intern")
    #     #p(db.rowsNumber("info"))
    #     # p(db.tables())
    #     # p(db.tableColumns("info"))
    #     #p(db.tableColumnsTypes("info"))
    #     #p(db.tableColumns("info"))
    #     #p(db.get_attribut(u"visibility"))
    #     # p(db.rowsNumber("info"))

        
    #     #db = DBHandler( )
    #     db = DBHandler( developingMode = True)
    #     db.init_stats(self.path_to_temp_prjFolder,  "twitter_streamed", "de", "intern","twrd")
    #     #db.init_stats(self.abs_path_to_test_prjFolder,  "twitter_streamed", "de", "intern","twrd")
    #     #p(db.tables())
    #     #p(db.tableColumns("info"))
    #     #p(db.get_all_attributs())
    #     #db.update_attribut("version","7")
    #     #p(db.get_all_attributs())



#encoding problem
        # p(db.get_attribut("name"),c="r")
        # db.update_attribut("name", "4567890ß")
        # p(db.get_attribut("name"),c="r")



 
    # @wipd
    # def test_initialisation_corpus_001(self):
    #     db = DBHandler(developingMode = True)
    #     #db = DBHandler()
    #     #p(self.path_to_temp_test_corpus)
        
    #     #db.connect(self.path_to_temp_test_corpus)
    #     #p(db.tables())
    #     #p(db.tables())
    #     #db.connect(self.path_to_temp_test_fakeDB)
    #     db.init_corpus(self.path_to_temp_testFolder, "twitter_streamed", "de", "intern", "twitter" )
    #     #db.init_corpus(self.path_to_temp_prjFolder, "twitter_streamed", "de", "intern", "twitter", template_name="twitter")
        

    #     #db.init_corpus(self.path_to_temp_prjFolder, "twitter_streamed_de",
    #     #    "de", "intern", "twitter",
    #     #    template_name="twitter",
    #     #    additional_columns_with_types_for_documents=[("kaka","TEXT"), ("koko","BLOB")])
    #     #additional_columns_with_types
    #     p(db.dbnames)
    #     db.attach(self.path_to_temp_test_stats)
    #     #db.attach(self.path_to_temp_test_stats_encrypted, "stats")
    #     p(db.dbnames)
    #     db.attach(self.path_to_temp_test_stats_plain_text)
    #     p(db.dbnames)
    #     #db.detach()
    #     db.reattach()
    #     #p(db.dbnames)
    #     p(db._attributs_dict)
    #     p(db.get_attribut("name"))
    #     db.update_attribut("name", "4567890")
    #     p(db.get_attribut("name"))
    #     p(db.get_all_attributs("main"), "567890")

        #db._validation_DBfile(self.path_to_temp_test_stats_plain_text)
        #db._validation_DBfile(self.path_to_temp_test_stats_encrypted, "stats")
        #db._validation_DBfile(self.path_to_temp_test_corpus)

        # # p(db.tables("stats"))
        # #p(db.tables())
        # # p(db.tableColumns("documents"))
        # # # p(db.get_all_attributs(), c="m")
        # # # p(db.tableColumns("documents"), c="r")
        # # db.insertCV("documents", [u'docs_id', u'text'], ["1","h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # # # db.insert_row("documents", [u'docs_id', u'text'], ["2","hjk"])
        # # # db.insert_row("documents", [u'docs_id', u'text'], ["3","hj😀😀😀😀😀😀k"])
        # # # db.insert_row("documents", [u'docs_id', u'text'], ["4","h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # # #db.insert_values("documents", [None,"ghj"])
        # # #db.insert_values("documents", [None,"ghj"])
        # # p(db.rowsNumber("documents"))
        # p(db.rowsNumber("documents"))
        # db.lazy_writer("documents", "cv", [ u'text'], ["h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # db.lazy_writer("documents", "v", values= [None,"h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # db.lazy_writer("documents", "v", values= [None,"h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # db.lazy_writer("documents", "v", values= [None,"h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # p(db.rowsNumber("documents"))
        # #db.commit()
        # db.rollback()
        # p(db.rowsNumber("documents"))

        # p(db._attachedDBs, c="r")
        # p(db.dbnames)
        # p(db.tables("stats"))
        # #db.encrypte("new")
        # # p(db._attachedDBs, c="m")
        # # p(db.dbnames)
        # # db.decrypte()
        # # p(db._attachedDBs, c="b")
        # # p(db.dbnames)
        # # #db.lazy_writer("documents", "v", values= ["hjk","h😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀jk"])
        # #db._reattach_dbs()
        # # #db.update("documents", ["text"], ["xxx"], "docs_id=3")
        # # #db.commit()
        
        # # # p(db.lazy_getter("documents", size_to_get=6))

        # # # for item in db.lazy_getter("documents"):
        # # #     p(item)


        # # # for item in db.getlimit(3,"documents"):
        # # #     p(item)

        # # # #db.drop_table("info", "stats")
        # # # p(db.tables(,"stats"))
        # # # p(db.tables("stats"))
        # # # p(db.rowsNumber("info"))
        # # # p(db.rowsNumber("info", "stats"))
        # # # p(db.tableColumnsTypes("info"))
        # # # p(db.tableColumnsTypes("info", "stats"))
        # # # p(db.tableColumns("info"))
        # # # p(db.tableColumns("info","stats"))
        # # # p(db.path("main"))
        # # # p(db.fname("stats"))
        # # # p(db.fname())
        # # # p(db.path())
        # # # p(db.attachedDBs())
        # # # p(db.attachedDBs())
        # # # p(db.fnameAttachedDBs())
        # # # p(db.pathAttachedDBs())
        # # # p(db.dbsNames())

        # #p(db.id())




    # #@wipd
    # def test_initialisation_stats_001(self):
    #     db = DBHandler( developingMode = True)
    #     #p(db.tables())
    #     db.init_stats(self.path_to_temp_prjFolder, "fghj", "twitter_streamed", "intern", "de")
    #     p(db.get_all_attributs(), c="m")
    #     p(db.tableColumns("baseline"), c="r")
    #     p(db.tableColumns("reduplications"), c="r")
    #     db.commit()





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





####################################################################################################
####################################################################################################
###################### STOP WORK_IN_PROGRESS (wipd) TESTS #########################################
####################################################################################################
####################################################################################################







