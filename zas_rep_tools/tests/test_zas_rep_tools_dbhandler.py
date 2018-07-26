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

#import json
#import codecs
import sure
#import inspect
import copy
#from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
#import glob
import random
import json

from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.configer import Configer
import  zas_rep_tools.src.utils.db_helper as db_helper
#from zas_rep_tools.src.utils.recipes_test_db import *

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import *
#from zas_rep_tools.src.utils.db_helper import *

#logger_save_logs = True

class TestZAScorpusDBHandlerDBHandler(unittest.TestCase):
    #_multiprocess_can_split_ = True
    _multiprocess_shared_  = True
    @classmethod 
    def setUp(self):
        #print "setup called" #called.append("setup")
        Configer(mode="test", rewrite=False).create_test_data(use_original_classes=True, corp_status_bar=True, corp_log_ignored=True,  corp_lang_classification=True)
        self.configer = Configer(mode="test")
        ######## Folders Creation ##############

        self.tempdir = TempDirectory()
        

        #####################
        #### Test DBs########
        #######Begin#########

        self.path_to_zas_rep_tools = self.configer.path_to_zas_rep_tools
        self.path_to_testdbs  =  self.configer.path_to_testdbs 
        self.db_blogger_plaintext_corp_en = self.configer.test_dbs["plaintext"]["blogger"]["en"]["corpus"]
        self.db_blogger_plaintext_corp_de = self.configer.test_dbs["plaintext"]["blogger"]["de"]["corpus"]
        self.db_blogger_plaintext_corp_test = self.configer.test_dbs["plaintext"]["blogger"]["test"]["corpus"]
        self.db_blogger_plaintext_stats_en = self.configer.test_dbs["plaintext"]["blogger"]["en"]["stats"]
        self.db_blogger_plaintext_stats_de = self.configer.test_dbs["plaintext"]["blogger"]["de"]["stats"]
        self.db_blogger_plaintext_stats_test = self.configer.test_dbs["plaintext"]["blogger"]["test"]["stats"]
          

        self.db_twitter_encrypted_corp_de = self.configer.test_dbs["encrypted"]["twitter"]["de"]["corpus"]
        self.db_twitter_encrypted_stats_de = self.configer.test_dbs["encrypted"]["twitter"]["de"]["stats"]


        ## TempDir
        self.tempdir.makedir('TestDBs')
        self.tempdir_testdbs  = self.tempdir.getpath('TestDBs')
        copy_tree(os.path.join(self.path_to_zas_rep_tools,self.path_to_testdbs ),self.tempdir_testdbs)

        #######End###########
        #### Test DBs########
        #####################



        #####################
        # Test Blogger Corpus#
        #######Begin#########

        self.path_to_test_sets_for_blogger_Corpus = "data/tests_data/Corpora/BloggerCorpus"
        
        #TXT
        self.txt_blogger_hightrepetativ_set = "txt/HighRepetativSubSet"
        self.txt_blogger_small_fake_set = "txt/SmallFakeSubset"
        #self.txt_blogger_small_sub_set = "txt/SmallSubset"

        #CSV
        self.csv_blogger_hightrepetativ_set = "csv/HighRepetativSubSet"
        self.csv_blogger_small_fake_set = "csv/SmallFakeSubset"
        # #self.csv_blogger_small_sub_set = "csv/SmallSubset"

        #XML
        self.xml_blogger_hightrepetativ_set = "xml/HighRepetativSubSet"
        self.xml_blogger_small_fake_set = "xml/SmallFakeSubset"
        #self.xml_blogger_small_sub_set = "xml/SmallSubset"

        #JSON
        self.json_blogger_hightrepetativ_set = "json/HighRepetativSubSet"
        self.json_blogger_small_fake_set = "json/SmallFakeSubset"
        # #self.json_blogger_small_sub_set = "json/SmallSubset"


        ## TempDir
        #self.path_to_test_corpora  = "data/tests_data/Corpora"
        self.tempdir.makedir('BloggerCorpus')
        self.tempdir_blogger_corp  = self.tempdir.getpath('BloggerCorpus')
        copy_tree(os.path.join(self.path_to_zas_rep_tools,self.path_to_test_sets_for_blogger_Corpus),self.tempdir_blogger_corp)

        #######End###########
        # Test Blogger Corpus#
        #####################



        #####################
        # Test Twitter Corpus#
        #######Begin#########

        self.path_to_test_sets_for_twitter_Corpus = "data/tests_data/Corpora/TwitterCorpus"
        self.json_twitter_set = "JSON/zas-rep-tool/"
        self.csv_twitter_set = "CSV/zas-rep-tool/"
        self.xml_twitter_set = "XML/zas-rep-tool/"

        ## TempDir
        #self.path_to_test_corpora  = "data/tests_data/Corpora"
        self.tempdir.makedir('TwitterCorpus')
        self.tempdir_twitter_corp  = self.tempdir.getpath('TwitterCorpus')
        copy_tree(os.path.join(self.path_to_zas_rep_tools,self.path_to_test_sets_for_twitter_Corpus),self.tempdir_twitter_corp)

        #######End###########
        # Test Twitter Corpus#
        #####################






        #####################
        #### Test Blogger ####
        #######Begin#########

        self.input_list_fake_blogger_corpus = [{'rowid':'1' ,'star_constellation': 'Capricorn', 'text': u'Well, the angel won. I went to work today....after alot of internal struggle with the facts. I calculated sick days left this year,', 'working_area': 'Consulting', 'age': '46', 'id': '324114', 'gender': 'female'}, {'rowid':'2' ,'star_constellation': 'Pisces', 'text': u"urlLink Drawing Game  It's PICTIONARY. It's very cool.", 'working_area': 'indUnk', 'age': '24', 'id': '416465', 'gender': 'male'}, {'rowid':'3' ,'star_constellation': 'Virgo', 'text': u'The mango said, "Hi there!!.... \n"Hi there!!.... \n"Hi there!!.... ', 'working_area': 'Non-Profit', 'age': '17', 'id': '322624', 'gender': 'female'}]
        self.input_list_blogger_corpus_high_repetativ_subset = [{'rowid':'1' ,'star_constellation': 'Capricorn', 'text': u'@lovelypig #direct_to_haven 67666 8997 -))) -) -P Neeeeeeeeeeeeeeeeiiiiiiinnnnn!!!!! Bitte nicht \U0001f602\U0001f602\U0001f602 \nTest Version von einem Tweeeeeeeeet=)))))))\nnoch einen Tweeeeeeeeet=))))))) \U0001f605\U0001f605', 'working_area': 'Consulting', 'age': '46', 'id': '324114', 'gender': 'female'}, {'rowid':'2' ,'star_constellation': 'Pisces', 'text': u'Einen weiteren Thread eingef\xfcgt!!! juHuuuuuuuu=) \U0001f49b\U0001f49b\U0001f49b\nden vierten Threadddddd!!! wooooowwwwww!!! \u263a\ufe0f \U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Quoted Tweet, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c h', 'working_area': 'indUnk', 'age': '24', 'id': '416465', 'gender': 'male'}, {'rowid':'3' ,'star_constellation': 'Virgo', 'text': u'Eine Teeeeeest Diskussion wird er\xf6ffnet!!! @zas-rep-tools \nEinen Test Retweet wird gepostet!!!!! Juhuuuuuu=) \U0001f600\U0001f600\U0001f600\U0001f600\nnoooooooch einen Tweeeeeeeeet=)))))))', 'working_area': 'Non-Profit', 'age': '17', 'id': '322624', 'gender': 'female'}]
        self.fieldnames = self.configer.columns_in_doc_table["blogger"] 

        #######End###########
        #### Test Blogger ####
        #####################


        #####################
        #### Test PrjFolder #
        #######Begin#########
        ## TempDir
        self.tempdir.makedir('ProjectFolder')
        self.tempdir_project_folder  = self.tempdir.getpath('ProjectFolder')

        #######End###########
       #### Test PrjFolder #
        #####################  

    @classmethod 
    def tearDown(self):
        #print "teardown called"# called.append(‘teardown’)
        self.tempdir.cleanup()





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
        db = DBHandler(mode="test")
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
        db = DBHandler(mode="test")
        
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility))
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_corpus_with_additional_columns_and_template_in_documents_501(self):
        db = DBHandler(mode="test")
        
        new_additional_columns = [
                        ("gender","TEXT"),
                        ("age","TEXT"),
                        ("eye_colour","TEXT"),
                        ]
        #p(new_additional_columns, "new_additional_columns")
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source,
                additional_columns_with_types_for_documents=new_additional_columns)


        col_and_types_for_twitter_docs = DBHandler.templates["twitter"]


        col_and_types_of_docs_tabel_in_the_current_db = db.colt("documents")
        default_col_and_typ_for_docs = [(u'blogger_id', u'INTEGER'), (u'text', u'BLOB')]
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
        db = DBHandler(mode="test")
        
        new_additional_columns = [
                        ("gender","TEXT"),
                        ("age","TEXT"),
                        ("eye_colour","TEXT"),
                        ]
        #p(new_additional_columns, "new_additional_columns")
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                version=version, source=source,
                additional_columns_with_types_for_documents=new_additional_columns)



        col_and_types_of_docs_tabel_in_the_current_db = db.colt("documents")
        default_col_and_typ_for_docs = [(u'blogger_id', u'INTEGER'), (u'text', u'BLOB')]
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
        db = DBHandler(mode="test")
        
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])


        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility))
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)

        #encryption
        db.encryption().should.be.equal("plaintext")


    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_encrypted_empty_corpus_with_general_init_504(self):
        db = DBHandler(mode="test")
        
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init(typ, self.tempdir_project_folder, name, language,
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
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility))
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_encrypted_empty_corpus_with_special_init_505(self):
        db = DBHandler(mode="test")
        
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
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
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility))
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)
   



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipdl
    def test_dbhandler_creation_of_empty_stats_with_general_init_as_plaintext_506(self):
        db = DBHandler(mode="test")
        

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"


        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, corpus_id=corpus_id,  version=version)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set(db_helper.default_tables["stats"].keys()))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr()['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("plaintext")



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipdl
    def test_dbhandler_creation_of_empty_stats_with_special_init_as_plaintext_507(self):
        db = DBHandler(mode="test")
        

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"

        db.init_stats(self.tempdir_project_folder, name, language,
                visibility, corpus_id=corpus_id,  version=version)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set(db_helper.default_tables["stats"].keys()))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr()['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("plaintext")






    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_encrypted_stats_with_general_init_508(self):
        db = DBHandler(mode="test")
        

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"


        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, corpus_id=corpus_id,  version=version,
                encryption_key = encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        db_helper.default_tables["stats"]
        set(db.tables()).should.be.equal(set(db_helper.default_tables["stats"].keys()))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr()['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    ###### xxx: 000 ######
    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_encrypted_stats_with_special_init_509(self):
        db = DBHandler(mode="test")
        

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"


        db.init_stats(self.tempdir_project_folder, name, language,
                visibility, corpus_id=corpus_id,  version=version,
                encryption_key=encryption_key)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set(db_helper.default_tables["stats"].keys()))
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        #db.get_all_attr()['id'].should.be.equal(create_id(name,language, typ, visibility, corpus_id=corpus_id))
        db.get_all_attr()['version'].should.be.equal(version)


        #encryption
        db.encryption().should.be.equal("encrypted")
        db.is_encrypted.should.be.equal(True)



    @attr(status='stable')
    #@wipd
    def test_dbhandler_creation_of_empty_DB_as_plaintext_510(self):
        db = DBHandler(mode="test")

        name= "testDB"


        db.initempty(self.tempdir_project_folder, name)

        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        db.tables().should.be.equal([])
        
        # check db names
        db.dbnames.should.be.equal([u'main'])

        #encryption
        db.encryption().should.be.equal("plaintext")




    @attr(status='stable')
    #@wipdl
    def test_dbhandler_creation_of_empty_DB_as_encrypted_511(self):
        db = DBHandler(mode="test")

        name= "testDB"
        encryption_key= "testDB"


        db.initempty(self.tempdir_project_folder, name, encryption_key=encryption_key)

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

    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_blogger_corpus_plaintext_515(self): 
        #db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")


        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


        db._db.should.be.a("pysqlcipher.dbapi2.Connection")
        db.get_db().should.be.a("pysqlcipher.dbapi2.Connection")

        # check tables
        set(db.tables()).should.be.equal(set([u'info', u'documents']))
        
        # check db names
        #p(db.dbnames)
        db.dbnames.should.be.equal([u'main'])
        #p(db.id())

        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        db.get_all_attr()['id'].should.be.equal(corpus_id)
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)

        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_twitter_corpus_encrypted_516(self):
        #db.init("corpus", ".", "streamed", "de", "intern", platform_name="twitter", license="MIT" , template_name="twitter", version="2", source="Twitter API", encryption_key="corpus", corpus_id="9588")


        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key=encryption_key)



        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['language'].should.be.equal(language)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        db.get_all_attr()['typ'].should.be.equal(typ)
        db.get_all_attr()['id'].should.be.equal(corpus_id)
        db.get_all_attr()['license'].should.be.equal(license)
        db.get_all_attr()['version'].should.be.equal(version)
        db.get_all_attr()['template_name'].should.be.equal(template_name)
        db.get_all_attr()['source'].should.be.equal(source)

        db.encryption().should.be.equal("encrypted")



    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_blogger_stats_plaintext_517(self):
        #db.init("stats", self.tempdir_project_folder, "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")

        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        version = self.configer.init_info_data["blogger"]["version"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"


        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        db.get_all_attr()['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr()['id'].should.be.equal(stats_id)
        db.get_all_attr()['version'].should.be.equal(version)

        db.encryption().should.be.equal("plaintext")


    @attr(status='stable')
    #@wipd
    def test_connection_with_plain_text_twitter_stats_encrypted_518(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"


        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ),  encryption_key=encryption_key)
        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )



        # check attributes names
        db.get_all_attr()['name'].should.be.equal(name)
        db.get_all_attr()['visibility'].should.be.equal(visibility)
        db.get_all_attr()['typ'].should.be.equal(typ)
        db.get_all_attr()['corpus_id'].should.be.equal(corpus_id)
        db.get_all_attr()['id'].should.be.equal(stats_id)
        db.get_all_attr()['version'].should.be.equal(version)

        db.encryption().should.be.equal("encrypted")





    ###### Attaching of DBs: 520 ######
   
    @attr(status='stable')
    #@wipd
    def test_attach_plaintext_corpus_db_520(self):
        #db.init("stats", ".", "streamed", "de", "intern", corpus_id="9588" , version="2", encryption_key="stats", stats_id="6361")
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        db.status().should.be.equal("manyDB")

        #p(db.dbnames)
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )[0])

        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


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
        db.get_all_attr(attached_db_name)['language'].should.be.equal(language)
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
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ),  encryption_key="stats")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ),  encryption_key="corpus")
        #p(db.status())
        db.status().should.be.equal("manyDB")


        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ))[0])

        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "corpus"

        # check attributes names
        db.get_all_attr(attached_db_name)['name'].should.be.equal(name)
        db.get_all_attr(attached_db_name)['language'].should.be.equal(language)
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
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        db.status().should.be.equal("manyDB")
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )[0])


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        version = self.configer.init_info_data["blogger"]["version"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"


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
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        db.status().should.be.equal("manyDB")
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ))[0])

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"] 
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"] 
        typ= "stats"

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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )[0])
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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ))[0])
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
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        attached_db_name_1 = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ))[0])
        attached_db_name_2 = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )[0])
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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ))[0])
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
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
        attached_db_name = "_"+os.path.basename(os.path.splitext(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )[0])
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
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        #db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        path_to_db1 = os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) 
        path_to_db2 = os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de )
        path_to_db3 = os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) 
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



    ###### Inserts of DBs: 560 ######






    @attr(status='stable')
    #@wipd
    def test_insert_many_values_with_insertdict_560(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False



    @attr(status='stable')
    #@wipd
    def test_insert_dict_with_many_values_with_lazyinsert_561(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.lazyinsert("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False
        #p(inp_dict)
        columns = inp_dict.keys()
        rows = inp_dict.values()

        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False




    @attr(status='stable')
    #@wipd
    def test_insert_one_value_with_insertdict_562(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=False)["blogger"]
        num_of_insertions = 1

        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False
   
        #[unicode(item) for item in db.getall("documents")[0]].should.be.equal([unicode(inp_dict[col]) for col in self.configer.columns_in_doc_table["blogger"] ])
        columns = inp_dict.keys()
        rows = inp_dict.values()

        #for i in xrange(num_of_insertions):
        for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[0]):
            if col != "text":
                if inp_dict[col] != value:
                    assert False
                else:
                    assert True
            else:
                if value != json.dumps(inp_dict[col]):
                    assert False


    @attr(status='stable')
    #@wipd
    def test_insert_dict_with_one_value_with_lazyinsert_563(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=False)["blogger"]
        num_of_insertions = 1

        db.lazyinsert("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False



        #[unicode(item) for item in db.getall("documents")[0]].should.be.equal([unicode(inp_dict[col]) for col in self.configer.columns_in_doc_table["blogger"] ])
        columns = inp_dict.keys()
        rows = inp_dict.values()

        #for i in xrange(num_of_insertions):
        for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[0]):
            if col != "text":
                if inp_dict[col] != value:
                    assert False
                else:
                    assert True
            else:
                if value != json.dumps(inp_dict[col]):
                    assert False





    @attr(status='stable')
    #@wipd
    def test_insert_one_row_with_insert_list_564(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_list = self.configer.docs_row_values(token=True, unicode_str=True)["blogger"][0]

        num_of_insertions = 1

        db.insertlist("documents", inp_list)

        if num_of_insertions != db.rownum("documents"):
           assert False

        for  item1,  item2 in zip(db.getall("documents")[0], inp_list):
            #print item1,item2
            if not isinstance(item2, (list,dict,tuple)):
                if item1 != item2:
                    assert False
            else:
                if item1 != json.dumps(item2):
                    assert False


    @attr(status='stable')
    #@wipd
    def test_insert_one_row_with_insert_lazyinsert_565(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_list = self.configer.docs_row_values(token=True, unicode_str=True)["blogger"][0]

        num_of_insertions = 1
        #p(db.col("documents"))
        db.lazyinsert("documents", inp_list)

        if num_of_insertions != db.rownum("documents"):
           assert False

        for  item1,  item2 in zip(db.getall("documents")[0], inp_list):
            #print item1,item2
            if not isinstance(item2, (list,dict,tuple)):
                if item1 != item2:
                    assert False
            else:
                if item1 != json.dumps(item2):
                    assert False





    @attr(status='stable')
    #@wipd
    def test_insert_many_rows_with_insertlist_566(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_list = self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]

        num_of_insertions = len(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"])
        #p(num_of_insertions)

        db.insertlist("documents", inp_list)

        if num_of_insertions != db.rownum("documents"):
           assert False

        for i in xrange(num_of_insertions):
            for  item1,  item2 in zip(db.getall("documents")[i], inp_list[i]):
                if not isinstance(item2, (list,dict,tuple)):
                    if item1 != item2:
                        assert False
                else:
                    if item1 != json.dumps(item2):
                        assert False





    @attr(status='stable')
    #@wipd
    def test_insert_many_rows_with_lazyinsert_567(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_list = self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]

        num_of_insertions = len(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"])
        #p(num_of_insertions)

        db.lazyinsert("documents", inp_list)

        if num_of_insertions != db.rownum("documents"):
           assert False

        for i in xrange(num_of_insertions):
            for  item1,  item2 in zip(db.getall("documents")[i], inp_list[i]):
                if not isinstance(item2, (list,dict,tuple)):
                    if item1 != item2:
                        assert False
                else:
                    if item1 != json.dumps(item2):
                        assert False




    ####### Work with JSON1: 570 #######

    @attr(status='stable')
    #@wipd
    def test_work_with_json_list_570(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")

        inp_list = self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]
        #p(inp_list)
        #p(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"])
        num_of_insertions = len(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"])
        #p(num_of_insertions)

        db.insertlist("documents", inp_list)

        if num_of_insertions != db.rownum("documents"):
           assert False

        for i in xrange(num_of_insertions):
            for  item1,  item2 in zip(db.getall("documents")[i], inp_list[i]):
                if not isinstance(item2, (list,dict,tuple)):
                    if item1 != item2:
                        assert False
                else:
                    if item1 != json.dumps(item2):
                        assert False

        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")

        #c = db.execute('SELECT * FROM documents WHERE json_extract("text", "$[1]") LIKE "%tt%";')
        #p(c.fetchall())
        #p((id_index, text_index), c="r")
        for row in inp_list:
            #p(row)
            input_id = row[id_index]
            text_element = row[text_index]
            c = db.execute('select json_extract("text", "$[0]") from documents WHERE id={};'.format(input_id))
            
            # p((c.fetchall(), len(c.fetchall())), c="r")
            # p((c.fetchall(), len(c.fetchall())), c="r")
            # p(c.fetchall()[0][0])
            #p((c.fetchall(), text_element[0]))
            # if c.fetchall()[0][0] != text_element[0]:
            #     assert False



    ###### Get rows from DB: 580 ######

    @attr(status='stable')
    #@wipdl
    def test_get_all_rows_from_db_with_intern_getter_580_1(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        ## test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db._intern_getter("documents").fetchall()[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False



    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_limit_and_offset_580_2(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        rows_with_intergetter =  list(db._intern_getter("documents", limit=3, offset=3))
        #p(rows_with_intergetter)
        rows_with_execute = db.execute("SELECT * FROM documents LIMIT 3 OFFSET 3;").fetchall()

        rows_with_intergetter.should.be.equal(rows_with_execute)



    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_where_condition_581(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")

        ##1. where as string
        #p(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"])
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            id_to_search = item[id_index]
            getted_item = db._intern_getter("documents", where="id = {}".format(id_to_search)).fetchall()[0] 
            #p((item, getted_item))
            for i1, i2 in zip(item, getted_item):
                #p((i1, i2))
                if isinstance(i1, (list, dict, tuple)):
                    i1= json.dumps(i1)
                #p((i1, i2))

                if i1 != i2:
                    assert False


        ##2.  where as list with one condition
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            id_to_search = item[id_index]
            getted_item = db._intern_getter("documents", where=["id = {}".format(id_to_search)]).fetchall()[0]
            #p((item, getted_item))
            for i1, i2 in zip(item, getted_item):
                #p((i1, i2))
                if isinstance(i1, (list, dict, tuple)):
                    i1= json.dumps(i1)
                #p((i1, i2))

                if i1 != i2:
                    assert False   

        ## 3. where as list with many conditions
        id_collector = []
        items_collector = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            id_to_search = item[id_index]
            if len(id_collector) >= 3:
                where_cond_list = ["id={}".format(doc_id) for doc_id in id_collector]
                #p(where_cond_list, "where_cond_list")
                getted_item = db._intern_getter("documents", where=where_cond_list, connector_where="OR").fetchall()
                #p(getted_item, "getted_item")
                for item1, item2 in zip(items_collector, getted_item):
                    for i1, i2 in zip(item1, item2):
                        #p((i1, i2))
                        if isinstance(i1, (list, dict, tuple)):
                            i1= json.dumps(i1)
                        #p((i1, i2))

                        if i1 != i2:
                           #p((i1, i2), c="r")
                            assert False    
            else:
                id_collector.append(id_to_search)
                items_collector.append(item)

        ## 4. where as list with json_extract condition
        #SELECT * FROM documents WHERE json_extract("text", "$[1]") LIKE '%ta%';
        
        ##########4.1. prepare ietem to compare
        elem_index_to_use = 0
        index_of_token_in_text_elemen_to_use = 0
        text_token_to_search = ""
        matched_items_to_compare = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            id_to_search = item[id_index]
            getted_item = db._intern_getter("documents", where=["id = {}".format(id_to_search)]).fetchall()[0]
            
            #p((item, getted_item))
            #p((item[text_index], getted_item[text_index]))

            
            text_elem_1 = item[text_index]
            text_elem_2 = json.loads(getted_item[text_index])
            #p((text_elem_1,text_elem_2))

            ### set_element_to_search
            if elem_index_to_use ==0:
                text_token_to_search = text_elem_1[index_of_token_in_text_elemen_to_use]
                item[text_index] = json.dumps(item[text_index]) if isinstance(item[text_index], list) else item[text_index]
                matched_items_to_compare.append(tuple(item))
            #p(text_token_to_search)
            else:
                if text_elem_1[index_of_token_in_text_elemen_to_use].lower() == text_token_to_search.lower():
                    item[text_index] = json.dumps(item[text_index]) if isinstance(item[text_index], list) else item[text_index]
                    matched_items_to_compare.append(tuple(item))

            elem_index_to_use+=1
        #p(matched_items_to_compare, "matched_items_to_compare")

        ##########4.2.  extract items with json_extract from the db
        if not isinstance(text_token_to_search, unicode):
            print "'text_token_to_search' is not an unicode string."
            assert False
        #print repr((text_token_to_search.encode("utf-8"))), type(text_token_to_search.encode("utf-8"))
        where_cond = 'json_extract("text", "$[{}]") LIKE "{}" '.format(index_of_token_in_text_elemen_to_use, text_token_to_search.encode("utf-8"))
        extracted_items_from_db = db._intern_getter("documents", where=where_cond).fetchall()
        #p(extracted_items_from_db)
        #p(text_token_to_search.encode("utf-8"), "text_token_to_search.encode('utf-8')")
        #p(matched_items_to_compare, "matched_items_to_compare")
        #p(extracted_items_from_db, "extracted_items_from_db")
        #p(matched_items_to_compare,"matched_items_to_compare")
        #p(extracted_items_from_db,"extracted_items_from_db")
        if matched_items_to_compare != extracted_items_from_db:
            assert False




    ## colums with and without json_extract condition!!! as new test case

    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_for_certain_columns_582(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")


        # ##1. columns as string
        getted_ids_from_db = db._intern_getter("documents", columns="id").fetchall()
        #p(getted_ids_from_db)
        extracted_ids_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_ids_from_input_data.append((item[id_index],))
        #p(extracted_ids_from_input_data)
        if getted_ids_from_db != extracted_ids_from_input_data:
            assert False



        # ##3. columns as list (one columns to search)
        getted_ids_from_db = db._intern_getter("documents", columns=["id"]).fetchall()
        #p(getted_ids_from_db)
        extracted_ids_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_ids_from_input_data.append((item[id_index],))
        #p(extracted_ids_from_input_data)
        if getted_ids_from_db != extracted_ids_from_input_data:
            assert False 



        # ##4. columns as list (with many columns to search)
        getted_ids_from_db = db._intern_getter("documents", columns=["id", "text"]).fetchall()
        #p(getted_ids_from_db)
        extracted_ids_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_ids_from_input_data.append((item[id_index],json.dumps(item[text_index])))
        #p(extracted_ids_from_input_data)
        if getted_ids_from_db != extracted_ids_from_input_data:
           assert False 




    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_additional_select_conditions_on_example_of_json1_583(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")

        #select json_extract("text", "$[0]") from documents;

        # ##1. select condition as string
        index_of_token_to_extract_from_text_element = 0
        getted_text_tokens_from_db = db._intern_getter("documents", select='json_extract("text", "$[{}]")'.format(index_of_token_to_extract_from_text_element)).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[text_index][index_of_token_to_extract_from_text_element],))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)




        # ##2. select condition as list (with one elemnt)
        index_of_token_to_extract_from_text_element = 0
        getted_text_tokens_from_db = db._intern_getter("documents", select=['json_extract("text", "$[{}]")'.format(index_of_token_to_extract_from_text_element)]).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[text_index][index_of_token_to_extract_from_text_element],))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)



        # ##3. select condition as list (with many elements)
        index_of_1_token_to_extract_from_text_element = 0
        index_of_2_token_to_extract_from_text_element = 1
        getted_text_tokens_from_db = db._intern_getter("documents", select=['json_extract("text", "$[{}]")'.format(index_of_1_token_to_extract_from_text_element),'json_extract("text", "$[{}]")'.format(index_of_2_token_to_extract_from_text_element)]).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item1, item2 in zip(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"],getted_text_tokens_from_db):
            #p(text_index,"text_index")
            #p(item, "item")
            extracted_text_tokens_from_input_data.append((item1[text_index][index_of_1_token_to_extract_from_text_element],item1[text_index][index_of_2_token_to_extract_from_text_element]))

        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)






    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_select_and_columns_combined_584(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")
        gender_index = self.configer.columns_in_doc_table["blogger"].index("gender")

        #select json_extract("text", "$[0]") from documents;

        # ##1. columns and select conditions (1 elem from each condition)
        index_of_token_to_extract_from_text_element = 0
        getted_text_tokens_from_db = db._intern_getter("documents",columns="id", select='json_extract("text", "$[{}]")'.format(index_of_token_to_extract_from_text_element)).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[id_index],item[text_index][index_of_token_to_extract_from_text_element]))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)



        # ##2. columns and select conditions (many elements from each condition)
        index_of_1_token_to_extract_from_text_element = 0
        index_of_2_token_to_extract_from_text_element = 1
        getted_text_tokens_from_db = db._intern_getter("documents", columns=["id","gender"], select=['json_extract("text", "$[{}]")'.format(index_of_1_token_to_extract_from_text_element),'json_extract("text", "$[{}]")'.format(index_of_2_token_to_extract_from_text_element)]).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[id_index],item[gender_index],item[text_index][index_of_1_token_to_extract_from_text_element],item[text_index][index_of_2_token_to_extract_from_text_element]))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)




    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_select_and_columns_combined_585(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")
        gender_index = self.configer.columns_in_doc_table["blogger"].index("gender")

        #select json_extract("text", "$[0]") from documents;

        # ##1. columns and select conditions (1 elem from each condition)
        index_of_token_to_extract_from_text_element = 0
        getted_text_tokens_from_db = db._intern_getter("documents",columns="id", select='json_extract("text", "$[{}]")'.format(index_of_token_to_extract_from_text_element)).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[id_index],item[text_index][index_of_token_to_extract_from_text_element]))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)



        # ##2. columns and select conditions (many elements from each condition)
        index_of_1_token_to_extract_from_text_element = 0
        index_of_2_token_to_extract_from_text_element = 1
        getted_text_tokens_from_db = db._intern_getter("documents", columns=["id","gender"], select=['json_extract("text", "$[{}]")'.format(index_of_1_token_to_extract_from_text_element),'json_extract("text", "$[{}]")'.format(index_of_2_token_to_extract_from_text_element)]).fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        

        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            extracted_text_tokens_from_input_data.append((item[id_index],item[gender_index],item[text_index][index_of_1_token_to_extract_from_text_element],item[text_index][index_of_2_token_to_extract_from_text_element]))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)






    @attr(status='stable')
    #@wipd
    def test_get_all_rows_from_db_with_intern_getter_with_columns_and_where_combined_586(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")
        gender_index = self.configer.columns_in_doc_table["blogger"].index("gender")

        #select json_extract("text", "$[0]") from documents;

        # ##1. columns where condition
        index_of_token_to_extract_from_text_element = 0
        getted_text_tokens_from_db = db._intern_getter("documents",columns="id", where="gender='m'").fetchall()
        #p(getted_text_tokens_from_db)
        #p(getted_text_tokens_from_db)
        extracted_text_tokens_from_input_data = []
        for item in self.configer.docs_row_values(token=True, unicode_str=True)["blogger"]:
            if item[gender_index] == "m":
                extracted_text_tokens_from_input_data.append((item[id_index],))
        #p(getted_text_tokens_from_db)
        #p(extracted_text_tokens_from_input_data)
        getted_text_tokens_from_db.should.be.equal(extracted_text_tokens_from_input_data)





    @attr(status='stable')
    #@wipd
    def test_getall_587(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        ## test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False



    @attr(status='stable')
    #@wipd
    def test_getlistlazy_588(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        ## test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],list(db.getlistlazy("documents"))[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False





    @attr(status='stable')
    #@wipd
    def test_getdictlazy_589(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        #p(list(db.getdictlazy("documents"))[0]["gender"])
        getted_output_from_db = list(db.getdictlazy("documents"))
        #p(getted_output_from_db)
        #p(inp_dict)
        ## test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col in self.configer.columns_in_doc_table["blogger"]:
                value_from_input = inp_dict[col][i]
                value_from_output=getted_output_from_db[i][col]
 
                #p((value_from_input, value_from_output))
                if col != "text":
                    if value_from_input != value_from_output:
                        assert False
                    else:
                        assert True
                else:
                    if value_from_output != json.dumps(value_from_input):
                        assert False






    @attr(status='stable')
    #@wipd
    def test_getdictlazy_for_certain_columns_and_select_590(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()


        #p(list(db.getdictlazy("documents", columns=["hhh", "id"]))[0])
        columns_to_get = ["id", "text"]
        select_to_get = ["gender"]
        getted_output_from_db = list(db.getdictlazy("documents", columns=columns_to_get, select=select_to_get ))
        #p(getted_output_from_db)
        #p(inp_dict)
        #test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col in columns_to_get +select_to_get:
                value_from_input = inp_dict[col][i]
                value_from_output=getted_output_from_db[i][col]
 
                #p((value_from_input, value_from_output))
                if col != "text":
                    if value_from_input != value_from_output:
                        assert False
                    else:
                        assert True
                else:
                    if value_from_output != json.dumps(value_from_input):
                        assert False







    @attr(status='stable')
    #@wipd
    def test_getlazy_591(self):
        ####code from "test_insert_many_values_with_insertdict_560"
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()



        # lazyget() -> dict
        #p(list(db.getdictlazy("documents", columns=["hhh", "id"]))[0])
        columns_to_get = ["id", "text"]
        select_to_get = ["gender"]
        getted_output_from_db = list(db.lazyget("documents", columns=columns_to_get, select=select_to_get, output="dict"))
        #p(getted_output_from_db)
        #p(inp_dict)
        #test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col in columns_to_get +select_to_get:
                value_from_input = inp_dict[col][i]
                value_from_output=getted_output_from_db[i][col]
 
                #p((value_from_input, value_from_output))
                if col != "text":
                    if value_from_input != value_from_output:
                        assert False
                    else:
                        assert True
                else:
                    if value_from_output != json.dumps(value_from_input):
                        assert False

        # lazyget() -> list
        ## test_get_all_rows_from_db_with_intern_getter Part
        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],list(db.lazyget("documents", output="list"))[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False






    ###### Role Back of DBs: 610 ######
    @attr(status='stable')
    #@wipd
    def test_roleback_changes_db_610(self):
        ####test_insert_many_values_with_insertdict_560
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        db.insertdict("documents", inp_dict)

        columns = inp_dict.keys()
        rows = inp_dict.values()

        ##### test roleback

        rowNum_bevore = 0
        #p((db.all_inserts_counter, db.number_of_new_inserts_after_last_commit, db.rollback()))
        if db.rollback() != num_of_insertions:
           assert False

        rowsNum_after_rollback = db.rownum("documents")

        if rowNum_bevore != rowsNum_after_rollback :
            assert False




    ###### Encryption/Decryption: 620 ######
    @attr(status='stable')
    #@wipd
    def test_uniq_DB_encryption_620(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )

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
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )

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
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats" )

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
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats")
        db.attach(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_corp_de ), encryption_key="corpus")
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )

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
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_twitter_encrypted_stats_de ), encryption_key="stats")
        newkey = "newkey"
        db.change_key(newkey)

        assert db._encryption_key == newkey




    ###### Attributs of DBs: 650 ######
    @attr(status='stable')
    #@wipd
    def test_get_attr_from_connected_db_625(self):
        #corpus:
        #    db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")
        #stats:
        #    db.init("stats", self.tempdir_project_folder, "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")


        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        # check attributes names
        db.get_attr('name').should.be.equal(name)
        db.get_attr('language').should.be.equal(language)
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
    def test_get_attr_from_attached_db_626(self):
        #corpus:
        #    db.init("corpus", self.tempdir_project_folder, "blogger", "de", "extern", platform_name="blogs", license="MIT" , template_name="blogger", version="2", source="LanguageGoldMine", corpus_id="7614")
        #stats:
        #    db.init("stats", self.tempdir_project_folder, "blogger", "de", "extern", corpus_id="7614" , version="2", stats_id="3497")

        db = DBHandler(mode="test")
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        #p(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


        fname = os.path.splitext(os.path.basename(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) ))[0]
        stats_db_name = "_"+fname
        db.attach(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_stats_en) )
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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )

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
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )
        #p(db.col("documents"))
        row1_bevore = db.getall("documents", where="rowid=1")
        db.update("documents", ["gender"], ["unknown"], where="rowid=1")
        row1_after = db.getall("documents", where="rowid=1")
        #p((row1_bevore,row1_after))
        if row1_after[0][3] != u"unknown":
           assert False
        db.close()


    @attr(status='stable')
    #@wipd
    def test_addNewtable_702(self):
        db = DBHandler(mode="test")
        #db = DBHandler(devmode=True)
        db.connect(os.path.join(self.tempdir_testdbs,  self.db_blogger_plaintext_corp_en) )

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




    ###### INDEXES: 750 ######

    @attr(status='stable')
    #@wipd
    def test_init_default_indexes_in_corpus_bevore_insertions_750(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))
        
        number_of_indexes_which_should_be_initialized = 0
        for table_name, index_query_list in db_helper.default_indexes["corpus"].iteritems():
            for index_query in index_query_list:
                number_of_indexes_which_should_be_initialized+=1


        number_of_indexes_bevor = len(db.indexes())
        db.init_default_indexes()
        #p(db.execute("SELECT * FROM sqlite_master WHERE type = 'index';").fetchall())
        number_of_indexes_after = len(db.indexes())
        if number_of_indexes_bevor+number_of_indexes_which_should_be_initialized != number_of_indexes_after:
            assert False
        #p(db.indexes())






    @attr(status='stable')
    #@wipd
    def test_init_default_indexes_in_corpus_after_insertions_751(self):
        #db = DBHandler(devmode=True)
        db = DBHandler(mode="test")
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"] 
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"] 
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"

        db.init_corpus(self.tempdir_project_folder, name, language,
                visibility, platform_name, license=license,
                template_name=template_name, version=version, source=source)
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))

        number_of_indexes_which_should_be_initialized = 0
        for table_name, index_query_list in db_helper.default_indexes["corpus"].iteritems():
            for index_query in index_query_list:
                number_of_indexes_which_should_be_initialized+=1


        number_of_indexes_bevor = len(db.indexes())



        db.insertdict("documents", inp_dict)

        if num_of_insertions != db.rownum("documents"):
            assert False

        columns = inp_dict.keys()
        rows = inp_dict.values()

        for i in xrange(num_of_insertions):
            for col, value in  zip(self.configer.columns_in_doc_table["blogger"],db.getall("documents")[i]):
                if col != "text":
                    if inp_dict[col][i] != value:
                        assert False
                    else:
                        assert True
                else:
                    if value != json.dumps(inp_dict[col][i]):
                        assert False


        db.init_default_indexes()
        #p(db.execute("SELECT * FROM sqlite_master WHERE type = 'index';").fetchall())
        number_of_indexes_after = len(db.indexes())
        if number_of_indexes_bevor+number_of_indexes_which_should_be_initialized != number_of_indexes_after:
            assert False
        #p(db.indexes())
     








    @attr(status='stable')
    #@wipd
    def test_init_default_indexes_in_stats_bevore_insertions_752(self):
        db = DBHandler(mode="test")
        

        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        version = self.configer.init_info_data["twitter"]["version"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"


        db.init(typ, self.tempdir_project_folder, name, language,
                visibility, corpus_id=corpus_id,  version=version)



        number_of_indexes_which_should_be_initialized = 0
        for table_name, index_query_list in db_helper.default_indexes["stats"].iteritems():
            for index_query in index_query_list:
                number_of_indexes_which_should_be_initialized+=1

        #p(db.indexes())

        number_of_indexes_bevor = len(db.indexes())
        db.init_default_indexes()
        #p(db.execute("SELECT * FROM sqlite_master WHERE type = 'index';").fetchall())
        number_of_indexes_after = len(db.indexes())

        if number_of_indexes_bevor+number_of_indexes_which_should_be_initialized != number_of_indexes_after:
            assert False
        #p(db.indexes())








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







