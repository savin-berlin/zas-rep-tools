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
from zas_rep_tools.src.utils.TestDBrecipes import *

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger
from zas_rep_tools.src.utils.db_helper import *





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

        self.path_to_temp_test_blogger_corpus_plaintext = os.path.join(self.path_to_temp_testFolder, "7614_corpus_blogs_blogger_de_extern_plaintext.db")
        self.path_to_temp_test_blogger_stats_plaintext = os.path.join(self.path_to_temp_testFolder, "7614_3497_stats_blogger_de_extern_plaintext.db")
        self.path_to_temp_test_fakeDB = os.path.join(self.path_to_temp_testFolder, "fakeDB.db")
        self.path_to_temp_test_twitter_corpus_encrypted = os.path.join(self.path_to_temp_testFolder, "9588_corpus_twitter_streamed_de_intern_encrypted.db")
        self.path_to_temp_test_twitter_stats_encrypted = os.path.join(self.path_to_temp_testFolder, "9588_6361_stats_streamed_de_intern_encrypted.db")
        ######## Folders Creation ##############
        ########### End #####################
        



    def tearDown(self):
        self.tempdir.cleanup()
        #print ">>>TempDirectory was cleaned<<<"


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
        db = DBHandler(logger_level=logging.ERROR)
        assert not db.get_db()
        #assert db._attachedDBs_config is False
        assert not db._attachedDBs_config 
        assert not db._tables_dict 
        assert not db._attributs_dict 
        assert not db.dbnames 





#################################Beginn##############################################
############################INTERN METHODS###########################################
#####################################################################################

###################    :100############################################ 

    ###### ***** ######

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
    


    ###### CREATION of DBs: 500 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_corpus_with_general_init_as_plaintext_500(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"

        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility))
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_corpus_with_additional_columns_and_template_in_documents_501(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        new_additional_columns = [
                        ("gender","TEXT"),
                        ("age","TEXT"),
                        ("eye_colour","TEXT"),
                        ]
        #p(new_additional_columns, "new_additional_columns")
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"

        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source,
                additional_columns_with_types_for_documents=new_additional_columns)


        col_and_types_for_twitter_docs = DBHandler.templates["twitter"]


        col_and_types_of_docs_tabel_in_the_current_db = db.colt("documents")
        default_col_and_typ_for_docs = [(u'docs_id', u'INTEGER'), (u'text', u'BLOB')]
        input_col_and_types = col_and_types_for_twitter_docs + new_additional_columns + default_col_and_typ_for_docs

        copy_of_db_data = copy.deepcopy(col_and_types_of_docs_tabel_in_the_current_db)
        #p(new_additional_columns, "new_additional_columns")
        #p(col_and_types_for_twitter_docs, "col_and_types_for_twitter_docs")
        #p(copy_of_db_data,"copy_of_db_data")
        #p(input_col_and_types, "input_col_and_types")
        #p(col_and_types_of_docs_tabel_in_the_current_db)
        for item_from_db in col_and_types_of_docs_tabel_in_the_current_db:
            for  item_from_input in input_col_and_types:
                if (item_from_db[0] == item_from_input[0]) and (item_from_db[1]==item_from_input[1].split(" ")[0]):
                    #p(item_from_db)
                    copy_of_db_data.remove(item_from_db)

        if not copy_of_db_data:
            assert True




    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_corpus_just_with_additional_columns_in_documents_502(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        new_additional_columns = [
                        ("gender","TEXT"),
                        ("age","TEXT"),
                        ("eye_colour","TEXT"),
                        ]
        #p(new_additional_columns, "new_additional_columns")
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        version = "2"
        source = "Twitter API"

        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                version=version, source=source,
                additional_columns_with_types_for_documents=new_additional_columns)



        col_and_types_of_docs_tabel_in_the_current_db = db.colt("documents")
        default_col_and_typ_for_docs = [(u'docs_id', u'INTEGER'), (u'text', u'BLOB')]
        input_col_and_types = new_additional_columns + default_col_and_typ_for_docs

        copy_of_db_data = copy.deepcopy(col_and_types_of_docs_tabel_in_the_current_db)

        for item_from_db in col_and_types_of_docs_tabel_in_the_current_db:
            for  item_from_input in input_col_and_types:
                if (item_from_db[0] == item_from_input[0]) and (item_from_db[1]==item_from_input[1].split(" ")[0]):
                    #p(item_from_db)
                    copy_of_db_data.remove(item_from_db)

        if not copy_of_db_data:
            assert True



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_corpus_with_special_init_as_plaintext_503(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"

        db.init_corpus(self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility))
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)

        #encryption
        db.encryption().should.be.equal("plaintext")


    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_encrypted_empty_corpus_with_general_init_504(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"
        encryption_key = "corpus"

        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                template_name=template_name, version=version,
                source=source, encryption_key=encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility))
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_encrypted_empty_corpus_with_special_init_505(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"
        encryption_key = "corpus"

        db.init_corpus(self.path_to_temp_prjFolder, name, lang,
                visibility, platform_name, license=license,
                template_name=template_name, version=version,
                source=source, encryption_key=encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility))
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)
   



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_stats_with_general_init_as_plaintext_506(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = "qwer"


        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, corpus_id=corpus_id,  version=version)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'baseline', u'replications', u'reduplications']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr('main')['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("plaintext")



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_stats_with_special_init_as_plaintext_507(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = "qwer"


        db.init_stats(self.path_to_temp_prjFolder, name, lang,
                visibility, corpus_id=corpus_id,  version=version)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'baseline', u'replications', u'reduplications']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr('main')['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("plaintext")






    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_encrypted_stats_with_general_init_508(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = "qwer"
        encryption_key = "stats"


        db.init(typ, self.path_to_temp_prjFolder, name, lang,
                visibility, corpus_id=corpus_id,  version=version,
                encryption_key = encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'baseline', u'replications', u'reduplications']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr('main')['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_encrypted_stats_with_special_init_509(self):
        db = DBHandler(logger_level=logging.ERROR)
        
        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = "qwer"
        encryption_key = "stats"


        db.init_stats(self.path_to_temp_prjFolder, name, lang,
                visibility, corpus_id=corpus_id,  version=version,
                encryption_key=encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'baseline', u'replications', u'reduplications']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        #db.get_all_attr('main')['id'].should.be.equal(create_id(name,lang, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr('main')['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_DB_as_plaintext_510(self):
        db = DBHandler(logger_level=logging.ERROR)

        name= "testDB"


        db.init_emptyDB(self.path_to_temp_prjFolder, name)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        db.tables().should.be.equal([])
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        #encryption
        db.encryption().should.be.equal("plaintext")




    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_DB_as_encrypted_511(self):
        db = DBHandler(logger_level=logging.ERROR)

        name= "testDB"
        encryption_key= "testDB"


        db.init_emptyDB(self.path_to_temp_prjFolder, name, encryption_key=encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        db.tables().should.be.equal([])
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)




    ###### Connection of DBs: 515 ######


        #self.path_to_temp_test_blogger_corpus_plaintext 
        #self.path_to_temp_test_blogger_stats_plaintext 
        #self.path_to_temp_test_fakeDB 
        #self.path_to_temp_test_twitter_corpus_encrypted
        #self.path_to_temp_test_twitter_stats_encrypted 

    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_blogger_corpus_plaintext_515(self): 
        #db.init("corpus", ".", "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")


        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "corpus"
        name= "blogger"
        lang="de"
        visibility = "extern"
        platform_name = "blogs"
        license = "MIT"
        template_name = "blogger"
        version = "2"
        source = "LanguageGoldMine"
        corpus_id = 7614


        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        #p(db.dbnames)
        db.dbnames.should.be.equal([u'main'])
        #p(db.id())

        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        db.get_all_attr('main')['id'].should.be.equal(corpus_id)
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)

        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_twitter_corpus_encrypted_516(self):
        #db.init("corpus", ".", "streamed", "de", "intern", platform_name="twitter", license="MIT" , template_name="twitter", version="2", source="Twitter API", encryption_key="corpus", corpus_id="9588")


        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"
        encryption_key = "corpus"
        corpus_id = 9588

        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key=encryption_key)



        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['language'].should.be.equal(lang)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        db.get_all_attr('main')['id'].should.be.equal(corpus_id)
        db.get_all_attr('main')['license'].should.be.equal(license)
        db.get_all_attr('main')['version'].should.be.equal(version)
        db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        db.get_all_attr('main')['source'].should.be.equal(source)

        db.encryption().should.be.equal("encrypted")



    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_blogger_stats_plaintext_517(self):
        #db.init("stats", ".", "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")

        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_stats_plaintext)
        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "stats"
        name= "blogger"
        lang="de"
        visibility = "extern"
        version = "2"
        corpus_id = 7614
        stats_id = "7614_3497"


        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        db.get_all_attr('main')['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr('main')['id'].should.be.equal(stats_id)
        db.get_all_attr('main')['version'].should.be.equal(version)

        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_twitter_stats_encrypted_518(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")

        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = 9588
        stats_id = "9588_6361"
        encryption_key = "stats"


        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_stats_encrypted,  encryption_key=encryption_key)
        #p(self.path_to_temp_test_blogger_corpus_plaintext)



        # check attributes names
        db.get_all_attr('main')['name'].should.be.equal(name)
        db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        db.get_all_attr('main')['typ'].should.be.equal(typ)
        db.get_all_attr('main')['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr('main')['id'].should.be.equal(stats_id)
        db.get_all_attr('main')['version'].should.be.equal(version)

        db.encryption().should.be.equal("encrypted")





    ###### Attaching of DBs: 520 ######
   
    @attr(status='stable')
    #@wipd
    def test_attach_plaintext_corpus_db_520(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_stats_plaintext)
        db.attach(self.path_to_temp_test_blogger_corpus_plaintext)
        db.status().should.be.equal("manyDB")

        #p(db.dbnames)
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_blogger_corpus_plaintext)[0])

        #p(attached_db_name)
        typ = "corpus"
        name= "blogger"
        lang="de"
        visibility = "extern"
        platform_name = "blogs"
        license = "MIT"
        template_name = "blogger"
        version = "2"
        source = "LanguageGoldMine"
        corpus_id = 7614


        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        #p(set(db.tables(dbname=attached_db_name)))
        set(db.tables(dbname=attached_db_name)).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        #p(db.dbnames)
        db.dbnames.should.be.equal([u'main', attached_db_name])
        #p(db.id())

        # check attributes names
        db.get_all_attr(attached_db_name)['name'].should.be.equal(name)
        db.get_all_attr(attached_db_name)['language'].should.be.equal(lang)
        db.get_all_attr(attached_db_name)['visibility'].should.be.equal(visibility)
        db.get_all_attr(attached_db_name)['platform_name'].should.be.equal(platform_name)
        db.get_all_attr(attached_db_name)['typ'].should.be.equal(typ)
        db.get_all_attr(attached_db_name)['id'].should.be.equal(corpus_id)
        db.get_all_attr(attached_db_name)['license'].should.be.equal(license)
        db.get_all_attr(attached_db_name)['version'].should.be.equal(version)
        db.get_all_attr(attached_db_name)['template_name'].should.be.equal(template_name)
        db.get_all_attr(attached_db_name)['source'].should.be.equal(source)


  

    @attr(status='stable')
    #@wipd
    def test_attach_encrypted_corpus_db_521(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_stats_encrypted,  encryption_key="stats")
        db.attach(self.path_to_temp_test_twitter_corpus_encrypted,  encryption_key="corpus")
        db.status().should.be.equal("manyDB")


        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_twitter_corpus_encrypted)[0])

        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "corpus"
        name= "streamed"
        lang="de"
        visibility = "intern"
        platform_name = "twitter"
        license = "MIT"
        template_name = "twitter"
        version = "2"
        source = "Twitter API"
        encryption_key = "corpus"
        corpus_id = 9588

        # check attributes names
        db.get_all_attr(attached_db_name)['name'].should.be.equal(name)
        db.get_all_attr(attached_db_name)['language'].should.be.equal(lang)
        db.get_all_attr(attached_db_name)['visibility'].should.be.equal(visibility)
        db.get_all_attr(attached_db_name)['platform_name'].should.be.equal(platform_name)
        db.get_all_attr(attached_db_name)['typ'].should.be.equal(typ)
        db.get_all_attr(attached_db_name)['id'].should.be.equal(corpus_id)
        db.get_all_attr(attached_db_name)['license'].should.be.equal(license)
        db.get_all_attr(attached_db_name)['version'].should.be.equal(version)
        db.get_all_attr(attached_db_name)['template_name'].should.be.equal(template_name)
        db.get_all_attr(attached_db_name)['source'].should.be.equal(source)





    @attr(status='stable')
    #@wipd
    def test_attach_plaintext_stats_db_522(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        db.status().should.be.equal("manyDB")
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_blogger_stats_plaintext)[0])


        typ = "stats"
        name= "blogger"
        lang="de"
        visibility = "extern"
        version = "2"
        corpus_id = 7614
        stats_id = "7614_3497"


        # check attributes names
        db.get_all_attr(attached_db_name)['name'].should.be.equal(name)
        db.get_all_attr(attached_db_name)['visibility'].should.be.equal(visibility)
        db.get_all_attr(attached_db_name)['typ'].should.be.equal(typ)
        db.get_all_attr(attached_db_name)['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr(attached_db_name)['id'].should.be.equal(stats_id)
        db.get_all_attr(attached_db_name)['version'].should.be.equal(version)



    @attr(status='stable')
    #@wipd
    def test_attach_encrypted_stats_db_523(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        db.status().should.be.equal("manyDB")
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_twitter_stats_encrypted)[0])

        typ = "stats"
        name= "streamed"
        lang="de"
        visibility = "intern"
        version = "2"
        corpus_id = 9588
        stats_id = "9588_6361"
        encryption_key = "stats"

        # check attributes names
        db.get_all_attr(attached_db_name)['name'].should.be.equal(name)
        db.get_all_attr(attached_db_name)['visibility'].should.be.equal(visibility)
        db.get_all_attr(attached_db_name)['typ'].should.be.equal(typ)
        db.get_all_attr(attached_db_name)['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr(attached_db_name)['id'].should.be.equal(stats_id)
        db.get_all_attr(attached_db_name)['version'].should.be.equal(version)

 




    ###### Reattaching of DBs: 530 ######

    @attr(status='stable')
    #@wipd
    def test_reattaching_one_plaintext_db_530(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_blogger_stats_plaintext)[0])
        dbnames = db.dbnames

        #Reattach without set an dbname
        db.status().should.be.equal("manyDB")
        db.reattach()
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")

        #Reattach with dbname
        db.reattach(dbname=attached_db_name )
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")



    @attr(status='stable')
    #@wipd
    def test_reattaching_one_encrypted_db_531(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_twitter_stats_encrypted)[0])
        dbnames = db.dbnames

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False
        #Reattach without set an dbname
        db.status().should.be.equal("manyDB")
        db.reattach()
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False
        #Reattach with dbname
        db.reattach(dbname=attached_db_name )
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False



    @attr(status='stable')
    #@wipd
    def test_reattaching_many_attached_dbs_532(self):
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        attached_db_name_1 = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_twitter_stats_encrypted)[0])
        attached_db_name_2 = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_blogger_stats_plaintext)[0])
        dbnames = db.dbnames

        if len(db._attachedDBs_config)==2:
            assert True
        else:
            assert False

        #Reattach without set an dbname
        db.status().should.be.equal("manyDB")
        db.reattach()
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==2:
            assert True
        else:
            assert False

        #Reattach with dbname
        db.reattach(dbname=attached_db_name_1)
        db.reattach(dbname=attached_db_name_2)
        db.dbnames.should.be.equal(dbnames)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==2:
            assert True
        else:
            assert False






    ###### Detaching of DBs: 540 ######
    @attr(status='stable')
    #@wipd
    def test_detaching_one_encrypted_db_540(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_twitter_stats_encrypted)[0])
        #dbnames = db.dbnames


        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False

        # Detach all attached DB
        db.detach()
        db.status().should.be.equal("oneDB")

        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False

        if len(db.dbnames) == 1:
            assert True
        else:
            assert False


        # Detach one attached DB 
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False


        db.detach(dbname=attached_db_name)
        db.status().should.be.equal("oneDB")
        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False

        if len(db.dbnames) == 1:
            assert True
        else:
            assert False


    @attr(status='stable')
    #@wipd
    def test_detaching_one_plaintext_db_541(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        attached_db_name = "_"+os.path.basename(os.path.splitext(self.path_to_temp_test_blogger_stats_plaintext)[0])
        #dbnames = db.dbnames

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False
        # Detach all attached DB
        db.detach()
        db.status().should.be.equal("oneDB")

        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False

        if len(db.dbnames) == 1:
            assert True
        else:
            assert False


        # Detach one attached DB 
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==1:
            assert True
        else:
            assert False


        db.detach(dbname=attached_db_name)

        db.status().should.be.equal("oneDB")

        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False

        if len(db.dbnames) == 1:
            assert True
        else:
            assert False



    @attr(status='stable')
    #@wipd
    def test_detaching_many_attached_dbs_542(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        #db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        path_to_db1 = self.path_to_temp_test_blogger_stats_plaintext
        path_to_db2 = self.path_to_temp_test_twitter_corpus_encrypted
        path_to_db3 = self.path_to_temp_test_blogger_corpus_plaintext
        db.attach(path_to_db1)
        db.attach(path_to_db2, encryption_key="corpus")
        db.attach(path_to_db3)
        attached_db_name_1 = "_"+os.path.basename(os.path.splitext(path_to_db1)[0])
        attached_db_name_2 = "_"+os.path.basename(os.path.splitext(path_to_db2)[0])
        attached_db_name_3 = "_"+os.path.basename(os.path.splitext(path_to_db3)[0])

        #p(db.dbnames)
        #p(db._attachedDBs_config)

        if len(db._attachedDBs_config)==3:
            assert True
        else:
            assert False
        # Detach all attached DB
        db.detach()
        db.status().should.be.equal("oneDB")

        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False


        if len(db.dbnames) == 1:
            assert True
        else:
            assert False


        # Detach  attached DB with given  name
        db.attach(path_to_db1)
        db.attach(path_to_db2, encryption_key="corpus")
        db.attach(path_to_db3)
        db.status().should.be.equal("manyDB")

        if len(db._attachedDBs_config)==3:
            assert True
        else:
            assert False

        if len(db.dbnames) == 4:
            assert True
        else:
            assert False


        db.detach(dbname=attached_db_name_1)


        if len(db._attachedDBs_config)==2:
            assert True
        else:
            assert False

        db.status().should.be.equal("manyDB")
        db.detach(attached_db_name_2)
        db.detach(attached_db_name_3)

        db.status().should.be.equal("oneDB")

        if len(db._attachedDBs_config)==0:
            assert True
        else:
            assert False

        if len(db.dbnames) == 1:
            assert True
        else:
            assert False



    ###### Inserts of DBs: 570 ######
    @attr(status='stable')
    #@wipd
    def test_insertCV_into_db_570(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(db.col("documents"))
        #[u'docs_id', u'text', u'gender', u'age', u'working_area', u'star_constellation']
        columns = [ u'text', u'gender', u'age', u'working_area', u'star_constellation']
        values = [['schöööööönen',"taaaaaag", "dirrrrrr"], 'm', '27', 'IT', 'lion' ]
        
        num_of_insertions = 10
        rowNum_bevore = db.rownum("documents")

        for i in range(num_of_insertions):
            db.insertCV("documents", columns, values)

        rowsNum_after = db.rownum("documents")

        if (num_of_insertions + rowNum_bevore) != rowsNum_after:
            assert False


    @attr(status='stable')
    #@wipd
    def test_insertV_into_db_571(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(db.col("documents"))
        #[u'docs_id', u'text', u'gender', u'age', u'working_area', u'star_constellation']
        values = ["NULL", ['schöööööönen',"taaaaaag", "dirrrrrr"], 'm', '27', 'IT', 'lion' ]
        num_of_insertions = 10
        rowNum_bevore = db.rownum("documents")

        for i in range(num_of_insertions):
            db.insertV("documents",  values)

        rowsNum_after = db.rownum("documents")

        if (num_of_insertions + rowNum_bevore) != rowsNum_after:
            assert False




    @attr(status='stable')
    #@wipd
    def test_lazy_writer_cv_572(self):
        #db = DBHandler(developingMode=True, lazyness_border=1000)
        db = DBHandler(logger_level=logging.ERROR, lazyness_border=1000)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(db.col("documents"))
        #[u'docs_id', u'text', u'gender', u'age', u'working_area', u'star_constellation']
        columns = [ u'text', u'gender', u'age', u'working_area', u'star_constellation']
        values = [['schöööööönen',"taaaaaag", "dirrrrrr"], 'm', '27', 'IT', 'lion' ]
        
        num_of_insertions = 1002
        rowNum_bevore = db.rownum("documents")
        #p(rowNum_bevore)
        for i in range(num_of_insertions):
            db.insertlazy("documents", "cv", columns, values)

        if db.commit() != 2:
           assert False

        rowsNum_after = db.rownum("documents")
        #p(rowsNum_after)
        if (num_of_insertions + rowNum_bevore) != rowsNum_after:
            assert False



    @attr(status='stable')
    #@wipd
    def test_lazy_writer_v_573(self):
        #db = DBHandler(developingMode=True, lazyness_border=1000)
        db = DBHandler(logger_level=logging.ERROR, lazyness_border=1000)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(db.col("documents"))
        #[u'docs_id', u'text', u'gender', u'age', u'working_area', u'star_constellation']
        values = ["NULL", ['schöööööönen',"taaaaaag", "dirrrrrr"], 'm', '27', 'IT', 'lion' ]
        num_of_insertions = 1002
        rowNum_bevore = db.rownum("documents")
        #p(rowNum_bevore)
        for i in range(num_of_insertions):
            db.insertlazy("documents", "v",  values=values)

        if db.commit() != 2:
           assert False

        rowsNum_after = db.rownum("documents")
        #p(rowsNum_after)
        if (num_of_insertions + rowNum_bevore) != rowsNum_after:
            assert False




    ###### Get rows from DB: 580 ######

    @attr(status='stable')
    #@wipd
    def test_get_all_580(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents")


        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])

        row2 = list(rows[1])
        row2.pop(0)
        [unicode(item) for item in row2].should.be.equal([unicode(item) for item in blog_value2])


        row3 = list(rows[2])
        row3.pop(0)
        [unicode(item) for item in row3].should.be.equal([unicode(item) for item in blog_value3])


        row4 = list(rows[3])
        row4.pop(0)
        [unicode(item) for item in row4].should.be.equal([unicode(item) for item in blog_value4])


        row5 = list(rows[4])
        row5.pop(0)
        [unicode(item) for item in row5].should.be.equal([unicode(item) for item in blog_value5])


        row6 = list(rows[5])
        row6.pop(0)
        [unicode(item) for item in row6].should.be.equal([unicode(item) for item in blog_value6])


    @attr(status='stable')
    #@wipd
    def test_get_all_with_where_condition_581(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents", where="rowid = 1")

        #p(rows)
        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])


    @attr(status='stable')
    #@wipd
    def test_get_all_with_where_condition_and_dbname_582(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents", where="rowid = 1", dbname="main")

        #p(rows)
        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])



    @attr(status='stable')
    #@wipd
    def test_get_all_with_where_condition_and_dbname_and_columnsname_582(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents", where="rowid = 1", dbname="main", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)


    @attr(status='stable')
    #@wipd
    def test_get_all_with_where_condition_and_columnsname_583(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents", where="rowid = 1", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)





    @attr(status='stable')
    #@wipd
    def test_get_all_with_columnsname_584(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getall("documents", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        if len(rows)!=6:
            assert False

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)

        row2 = list(rows[1])
        output_row2 = [unicode(item) for item in blog_value2]
        output_row2.pop(0)
        [unicode(item) for item in row2].should.be.equal(output_row2)

        row3 = list(rows[2])
        output_row3 = [unicode(item) for item in blog_value3]
        output_row3.pop(0)
        [unicode(item) for item in row3].should.be.equal(output_row3)


        row4 = list(rows[3])
        output_row4 = [unicode(item) for item in blog_value4]
        output_row4.pop(0)
        [unicode(item) for item in row4].should.be.equal(output_row4)


        row5 = list(rows[4])
        output_row5 = [unicode(item) for item in blog_value5]
        output_row5.pop(0)
        [unicode(item) for item in row5].should.be.equal(output_row5)

        row6 = list(rows[5])
        output_row6 = [unicode(item) for item in blog_value6]
        output_row6.pop(0)
        [unicode(item) for item in row6].should.be.equal(output_row6)




    @attr(status='stable')
    #@wipd
    def test_get_one_585(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1,blog_value2,blog_value3,blog_value4,blog_value5, blog_value6]
        for row_db, row_output in zip(db.getone("documents"), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])



    @attr(status='stable')
    #@wipd
    def test_get_one_with_where_conditions_586(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getone("documents", where="rowid=1"), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])


    @attr(status='stable')
    #@wipd
    def test_get_one_with_where_conditions_and_dbname_587(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getone("documents", where="rowid=1", dbname="main"), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])


    @attr(status='stable')
    #@wipd
    def test_get_one_with_where_conditions_and_dbname_and_colnames_588(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getone("documents", where="rowid=1", dbname="main", columns=[ u'gender', u'age', u'working_area', u'star_constellation']), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)



    @attr(status='stable')
    #@wipd
    def test_get_one_with_where_conditions_and_colnames_589(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getone("documents", where="rowid=1", columns=[ u'gender', u'age', u'working_area', u'star_constellation']), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)



    @attr(status='stable')
    #@wipd
    def test_get_one_with_and_colnames_590(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1,blog_value2,blog_value3,blog_value4,blog_value5, blog_value6]
        for row_db, row_output in zip(db.getone("documents",  columns=[ u'gender', u'age', u'working_area', u'star_constellation']), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)






    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_591(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(3,"documents", )

        if len(rows)!=3:
            assert False

        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])

        row2 = list(rows[1])
        row2.pop(0)
        [unicode(item) for item in row2].should.be.equal([unicode(item) for item in blog_value2])


        row3 = list(rows[2])
        row3.pop(0)
        [unicode(item) for item in row3].should.be.equal([unicode(item) for item in blog_value3])




    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_with_where_condition_592(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(3,"documents", where="rowid = 1",connector_where="AND")
        #p(db.getall("documents", where=["rowid = 1", "gender = 'm'"]))
        #p(db.getall("documents", where=["age = 27", "gender = 'm'"], connector_where="OR"))

        #p(rows)
        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])


    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_with_where_condition_and_dbname_593(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(1,"documents", where="rowid = 1", dbname="main")

        #p(rows)
        row1 = list(rows[0])
        row1.pop(0)
        [unicode(item) for item in row1].should.be.equal([unicode(item) for item in blog_value1])



    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_with_where_condition_and_dbname_and_columnsname_594(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(1,"documents", where="rowid = 1", dbname="main", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)


    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_with_where_condition_and_columnsname_595(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(1,"documents", where="rowid = 1", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)





    @attr(status='stable')
    #@wipd
    def test_get_all_with_limit_with_columnsname_596(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        rows = db.getlimit(3,"documents", columns=[ u'gender', u'age', u'working_area', u'star_constellation'])

        if len(rows)!=3:
            assert False

        row1 = list(rows[0])
        output_row1 = [unicode(item) for item in blog_value1]
        output_row1.pop(0)
        [unicode(item) for item in row1].should.be.equal(output_row1)

        row2 = list(rows[1])
        output_row2 = [unicode(item) for item in blog_value2]
        output_row2.pop(0)
        [unicode(item) for item in row2].should.be.equal(output_row2)

        row3 = list(rows[2])
        output_row3 = [unicode(item) for item in blog_value3]
        output_row3.pop(0)
        [unicode(item) for item in row3].should.be.equal(output_row3)




    @attr(status='stable')
    #@wipd
    def test_getlazy_597(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1,blog_value2,blog_value3,blog_value4,blog_value5, blog_value6]
        for row_db, row_output in zip(db.getlazy("documents", size_to_get=3), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])



    @attr(status='stable')
    #@wipd
    def test_getlazy_with_where_conditions_598(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getlazy("documents", where="rowid=1", size_to_get=3), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])


    @attr(status='stable')
    #@wipd
    def test_getlazy_with_where_conditions_and_dbname_599(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getlazy("documents", where="rowid=1", dbname="main", size_to_get=3), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_db.pop(0)
            [unicode(item) for item in row_db].should.be.equal([unicode(item) for item in row_output])


    @attr(status='stable')
    #@wipd
    def test_getlazy_with_where_conditions_and_dbname_and_colnames_600(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getlazy("documents", where="rowid=1", dbname="main", columns=[ u'gender', u'age', u'working_area', u'star_constellation'], size_to_get=3), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)



    @attr(status='stable')
    #@wipd
    def test_getlazy_with_where_conditions_and_colnames_601(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1]
        for row_db, row_output in zip(db.getlazy("documents", where="rowid=1", columns=[ u'gender', u'age', u'working_area', u'star_constellation']), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)



    @attr(status='stable')
    #@wipd
    def test_getlazy_with_and_colnames_602(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        output_list_with_rows = [blog_value1,blog_value2,blog_value3,blog_value4,blog_value5, blog_value6]
        for row_db, row_output in zip(db.getlazy("documents",  columns=[ u'gender', u'age', u'working_area', u'star_constellation'], size_to_get=2), output_list_with_rows):
            #p((row_db, row_output))
            row_db = list(row_db)
            row_output = [unicode(item) for item in row_output]
            row_output.pop(0)
            #p((row_db, row_output))
            [unicode(item) for item in row_db].should.be.equal(row_output)



    ###### Role Back of DBs: 610 ######
    @attr(status='stable')
    #@wipd
    def test_roleback_changes_db_610(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(db.col("documents"))
        #[u'docs_id', u'text', u'gender', u'age', u'working_area', u'star_constellation']
        columns = [ u'text', u'gender', u'age', u'working_area', u'star_constellation']
        values = [['schöööööönen',"taaaaaag", "dirrrrrr"], 'm', '27', 'IT', 'lion' ]
        
        num_of_insertions = 10
        rowNum_bevore = db.rownum("documents")

        for i in range(num_of_insertions):
            db.insertCV("documents", columns, values)

        if db.rollback() != num_of_insertions:
            assert False

        rowsNum_after_rollback = db.rownum("documents")

        if rowNum_bevore != rowsNum_after_rollback :
            assert False




    ###### Encryption/Decryption: 620 ######
    @attr(status='stable')
    #@wipd
    def test_uniq_DB_encryption_620(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)

        tables_from_plaintextDB = db.tables()

        if not db.encrypte("corpus"):
            assert False

        if db.encryption() != "encrypted":
            assert False

        if db.is_encrypted != True:
            assert False

        tables_from_encryptedDB = db.tables()

        if tables_from_plaintextDB != tables_from_encryptedDB:
            assert False

    @attr(status='stable')
    #@wipd
    def test_DB_encryption_with_attachedDBs_621(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        db.attach(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)

        tables_from_plaintextDB = db.tables()
        dbname_bevore_encryption = db.dbnames
        if not db.encrypte("corpus"):
            assert False

        if db.encryption() != "encrypted":
            assert False

        if db.is_encrypted != True:
            assert False

        tables_from_encryptedDB = db.tables()
        dbname_after_encryption = db.dbnames

        if tables_from_plaintextDB != tables_from_encryptedDB:
            assert False

        #p((dbname_bevore_encryption,dbname_after_encryption))

        if dbname_bevore_encryption != dbname_after_encryption:
            assert False



    @attr(status='stable')
    #@wipd
    def test_uniq_DB_decryption_622(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats" )

        tables_from_plaintextDB = db.tables()

        if not db.decrypte():
            assert False

        if db.encryption() != "plaintext":
            assert False

        if db.is_encrypted != False:
            assert False

        tables_from_encryptedDB = db.tables()

        if tables_from_plaintextDB != tables_from_encryptedDB:
            assert False


    @attr(status='stable')
    #@wipd
    def test_DB_decryption_with_attachedDBs_623(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats")
        db.attach(self.path_to_temp_test_twitter_corpus_encrypted, encryption_key="corpus")
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)

        tables_from_plaintextDB = db.tables()
        dbnames_bevore_encryption = db.dbnames
        if not db.decrypte():
            assert False

        if db.encryption() != "plaintext":
            assert False

        if db.is_encrypted != False:
            assert False

        tables_from_encryptedDB = db.tables()
        dbnames_after_encryption = db.dbnames

        if tables_from_plaintextDB != tables_from_encryptedDB:
            assert False

        #p((dbnames_bevore_encryption,dbnames_after_encryption))

        if dbnames_bevore_encryption != dbnames_after_encryption:
            assert False




    @attr(status='stable')
    #@wipd
    def test_DB_change_encryption_key_624(self):
        #db = DBHandler(developingMode=True)
        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_twitter_stats_encrypted, encryption_key="stats")
        newkey = "newkey"
        db.change_key(newkey)

        assert db._encryption_key == newkey




    ###### Attributs of DBs: 650 ######
    @attr(status='stable')
    #@wipd
    def test_get_attr_from_connected_db_580(self):
        #corpus:
        #    db.init("corpus", ".", "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")
        #stats:
        #    db.init("stats", ".", "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")


        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "corpus"
        name= "blogger"
        lang="de"
        visibility = "extern"
        platform_name = "blogs"
        license = "MIT"
        template_name = "blogger"
        version = "2"
        source = "LanguageGoldMine"
        encryption_key = "corpus"
        corpus_id = 7614
        stats_id = "7614_3497"

        # check attributes names
        db.get_attr('name').should.be.equal(name)
        db.get_attr('language').should.be.equal(lang)
        db.get_attr('visibility').should.be.equal(visibility)
        db.get_attr('platform_name').should.be.equal(platform_name)
        db.get_attr('typ').should.be.equal(typ)
        db.get_attr('id').should.be.equal(corpus_id)
        db.get_attr('license').should.be.equal(license)
        db.get_attr('version').should.be.equal(version)
        db.get_attr('template_name').should.be.equal(template_name)
        db.get_attr('source').should.be.equal(source)



    @attr(status='stable') 
    #@wipd
    def test_get_attr_from_attached_db_581(self):
        #corpus:
        #    db.init("corpus", ".", "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")
        #stats:
        #    db.init("stats", ".", "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")

        db = DBHandler(logger_level=logging.ERROR)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)
        #p(self.path_to_temp_test_blogger_corpus_plaintext)
        typ = "corpus"
        name= "blogger"
        lang="de"
        visibility = "extern"
        platform_name = "blogs"
        license = "MIT"
        template_name = "blogger"
        version = "2"
        source = "LanguageGoldMine"
        encryption_key = "corpus"
        corpus_id = 7614
        stats_id = "7614_3497"


        fname = os.path.splitext(os.path.basename(self.path_to_temp_test_blogger_stats_plaintext))[0]
        stats_db_name = "_"+fname
        db.attach(self.path_to_temp_test_blogger_stats_plaintext)
        db.get_attr('name', stats_db_name).should.be.equal(name)
        db.get_attr('visibility', stats_db_name).should.be.equal(visibility)
        db.get_attr('typ', stats_db_name).should.be.equal("stats")
        db.get_attr('corpus_id', stats_db_name).should.be.equal(corpus_id)
        db.get_attr('id', stats_db_name).should.be.equal(stats_id)
        db.get_attr('version', stats_db_name).should.be.equal(version)
 




    ###### Other Small Functions of DBs: 700 ######

    @attr(status='stable')
    #@wipd
    def test_drop_table_from_db_db_700(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)

        tables_bevore = db.tables()
        db.drop_table(u"documents")
        #p(db.drop_table("documents"), c="r")
        tables_after = db.tables()
        #p((tables_bevore, tables_after ))

        if (len(tables_bevore) - len(tables_after)) != 1:
            assert False

        tables_bevore.remove(u"documents")

        if tables_bevore !=tables_after:
            assert False


    @attr(status='stable')
    #@wipd
    def test_update_value_701(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)

        row1_bevore = db.getall("documents", where="rowid=1")
        db.update("documents", ["gender"], ["unknown"], where="rowid=1")
        row1_after = db.getall("documents", where="rowid=1")
        #p((row1_bevore,row1_after))
        if row1_after[0][2] != u"unknown":
            assert False


    @attr(status='stable')
    #@wipd
    def test_addNewtable_701(self):
        db = DBHandler(logger_level=logging.ERROR)
        #db = DBHandler(developingMode=True)
        db.connect(self.path_to_temp_test_blogger_corpus_plaintext)

        newtableName = u"tempTables"
        attributs_names_with_types_as_str = [
                                ("text","TEXT"),
                                ("age", "TEXT")
                                ]

        tables_bevore = db.tables()
        db.addtable(newtableName, attributs_names_with_types_as_str, dbname="main")

        tables_after = db.tables()

        set(db.col(newtableName)).should.be.equal(set(["text", "age"]))

        if tables_bevore == tables_after:
            assert False

        tables_bevore.append(newtableName)

        if set(tables_bevore) != set(tables_after):
            assert False



        

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







