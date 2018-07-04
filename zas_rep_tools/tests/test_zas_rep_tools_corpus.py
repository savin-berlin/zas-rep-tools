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

from zas_rep_tools.src.classes.Corpus import Corpus

from zas_rep_tools.src.utils.recipes_test_db import *
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZAScorpusCorpus(unittest.TestCase):
    def setUp(self):


        create_all_test_dbs_if_not_exist()
        ######## Folders Creation ##############

        self.tempdir = TempDirectory()
        

        #####################
        #### Test DBs########
        #######Begin#########

        self.path_to_zas_rep_tools = path_to_zas_rep_tools
        self.path_to_testdbs  =  path_to_testdbs 
        self.db_blogger_plaintext_corp = db_blogger_plaintext_corp
        self.db_twitter_encrypted_corp = db_twitter_encrypted_corp
        self.db_blogger_plaintext_stats = db_blogger_plaintext_stats
        self.db_twitter_encrypted_stats = db_twitter_encrypted_stats 

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
        self.txt_blogger_hightrepetativ_set = "txt/HighRepetativSubSet"
        self.txt_blogger_small_fake_set = "txt/SmallFakeSubset"
        #self.txt_blogger_small_fake_set = "txt/SmallSubset"

        # self.csv_blogger_hightrepetativ_set = "csv/HighRepetativSubSet"
        # self.csv_blogger_small_fake_set = "csv/SmallFakeSubset"
        # #self.csv_blogger_small_fake_set = "csv/SmallSubset"


        # self.xml_blogger_hightrepetativ_set = "xml/HighRepetativSubSet"
        # self.xml_blogger_small_fake_set = "xml/SmallFakeSubset"
        # #self.xml_blogger_small_fake_set = "xml/SmallSubset"


        # self.json_blogger_hightrepetativ_set = "json/HighRepetativSubSet"
        # self.json_blogger_small_fake_set = "json/SmallFakeSubset"
        # #self.json_blogger_small_fake_set = "json/SmallSubset"


        ## TempDir
        #self.path_to_test_corpora  = "data/tests_data/Corpora"
        self.tempdir.makedir('BloggerCorpus')
        self.tempdir_blogger_corp  = self.tempdir.getpath('BloggerCorpus')
        copy_tree(os.path.join(self.path_to_zas_rep_tools,self.path_to_test_sets_for_blogger_Corpus),self.tempdir_blogger_corp)

        #######End###########
        # Test Blogger Corpus#
        #####################





        #####################
        #### Test Blogger ####
        #######Begin#########

        self.input_list_fake_blogger_corpus = [{'star_constellation': 'Capricorn', 'text': u'Well, the angel won. I went to work today....after alot of internal struggle with the facts. I calculated sick days left this year,', 'working_area': 'Consulting', 'age': '46', 'id': '324114', 'gender': 'female'}, {'star_constellation': 'Pisces', 'text': u"urlLink Drawing Game  It's PICTIONARY. It's very cool.", 'working_area': 'indUnk', 'age': '24', 'id': '416465', 'gender': 'male'}, {'star_constellation': 'Virgo', 'text': u'The mango said, "Hi there!!.... \n"Hi there!!.... \n"Hi there!!.... ', 'working_area': 'Non-Profit', 'age': '17', 'id': '322624', 'gender': 'female'}]
        self.input_list_blogger_corpus_high_repetativ_subset = [{'star_constellation': 'Capricorn', 'text': u'Neeeeeeeeeeeeeeeeiiiiiiinnnnn!!!!! Bitte nicht \U0001f602\U0001f602\U0001f602 \nTest Version von einem Tweeeeeeeeet=)))))))\nnoch einen Tweeeeeeeeet=))))))) \U0001f605\U0001f605', 'working_area': 'Consulting', 'age': '46', 'id': '324114', 'gender': 'female'}, {'star_constellation': 'Pisces', 'text': u'Einen weiteren Thread eingef\xfcgt!!! juHuuuuuuuu=) \U0001f49b\U0001f49b\U0001f49b\nden vierten Threadddddd!!! wooooowwwwww!!! \u263a\ufe0f \U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Quoted Tweet, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c h', 'working_area': 'indUnk', 'age': '24', 'id': '416465', 'gender': 'male'}, {'star_constellation': 'Virgo', 'text': u'Eine Teeeeeest Diskussion wird er\xf6ffnet!!! @zas-rep-tools \nEinen Test Retweet wird gepostet!!!!! Juhuuuuuu=) \U0001f600\U0001f600\U0001f600\U0001f600\nnoooooooch einen Tweeeeeeeeet=)))))))', 'working_area': 'Non-Profit', 'age': '17', 'id': '322624', 'gender': 'female'}]
        self.fieldnames = blogger_columns 

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

    def tearDown(self):
        self.tempdir.cleanup()


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
    def test_initialization_of_the_corpus_instance_000(self):
        corp = Corpus()
        corp.should.be.a(Corpus)

        

    ##### throws_exceptions:050  ######




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
    @attr(status='stable')
    #@wipd
    def test_new_plaintext_corpus_initialization_500(self):

        name = init_data_blogger["name"]
        language = init_data_blogger["language"]
        visibility = init_data_blogger["visibility"]
        platform_name = init_data_blogger["platform_name"]
        license = init_data_blogger["license"]
        template_name = init_data_blogger["template_name"]
        version = init_data_blogger["version"]
        source = init_data_blogger["source"]
        encryption_key = init_data_blogger["encryption_key_corp"]
        corpus_id = init_data_blogger["corpus_id"]
        stats_id = init_data_blogger["stats_id"]
        typ= "corpus"


        corp = Corpus(logger_level=logging.ERROR)
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
    @attr(status='stable')
    #@wipd
    def test_new_encrypted_corpus_initialization_501(self):

        name = init_data_blogger["name"]
        language = init_data_blogger["language"]
        visibility = init_data_blogger["visibility"]
        platform_name = init_data_blogger["platform_name"]
        license = init_data_blogger["license"]
        template_name = init_data_blogger["template_name"]
        version = init_data_blogger["version"]
        source = init_data_blogger["source"]
        encryption_key = init_data_blogger["encryption_key_corp"]
        corpus_id = init_data_blogger["corpus_id"]
        stats_id = init_data_blogger["stats_id"]
        typ= "corpus"


        corp = Corpus(logger_level=logging.ERROR)
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name, encryption_key=encryption_key, source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
        
        

    @attr(status='stable')
    #@wipd
    def test_open_plaintext_blogger_corpus_502(self):

        name = init_data_blogger["name"]
        language = init_data_blogger["language"]
        visibility = init_data_blogger["visibility"]
        platform_name = init_data_blogger["platform_name"]
        license = init_data_blogger["license"]
        template_name = init_data_blogger["template_name"]
        version = init_data_blogger["version"]
        source = init_data_blogger["source"]
        encryption_key = init_data_blogger["encryption_key_corp"]
        corpus_id = init_data_blogger["corpus_id"]
        stats_id = init_data_blogger["stats_id"]
        typ= "corpus"


        corp = Corpus(logger_level=logging.ERROR)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp))
  
    
        corp.db.get_all_attr('main')['name'].should.be.equal(name)
        corp.db.get_all_attr('main')['language'].should.be.equal(language)
        corp.db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        corp.db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        corp.db.get_all_attr('main')['typ'].should.be.equal(typ)
        corp.db.get_all_attr('main')['id'].should.be.equal(corpus_id)
        corp.db.get_all_attr('main')['license'].should.be.equal(license)
        corp.db.get_all_attr('main')['version'].should.be.equal(version)
        corp.db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        corp.db.get_all_attr('main')['source'].should.be.equal(source)

        assert corp.exist()
   
    @attr(status='stable')
    #@wipd
    def test_open_encrypted_twitter_corpus_503(self):

        name = init_data_twitter["name"]
        language = init_data_twitter["language"]
        visibility = init_data_twitter["visibility"]
        platform_name = init_data_twitter["platform_name"]
        license = init_data_twitter["license"]
        template_name = init_data_twitter["template_name"]
        version = init_data_twitter["version"]
        source = init_data_twitter["source"]
        encryption_key = init_data_twitter["encryption_key_corp"]
        corpus_id = init_data_twitter["corpus_id"]
        stats_id = init_data_twitter["stats_id"]
        typ= "corpus"
        #p(encryption_key)

        corp = Corpus(logger_level=logging.ERROR)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_corp), encryption_key=encryption_key)
    

        corp.db.get_all_attr('main')['name'].should.be.equal(name)
        corp.db.get_all_attr('main')['language'].should.be.equal(language)
        corp.db.get_all_attr('main')['visibility'].should.be.equal(visibility)
        corp.db.get_all_attr('main')['platform_name'].should.be.equal(platform_name)
        corp.db.get_all_attr('main')['typ'].should.be.equal(typ)
        corp.db.get_all_attr('main')['id'].should.be.equal(corpus_id)
        corp.db.get_all_attr('main')['license'].should.be.equal(license)
        corp.db.get_all_attr('main')['version'].should.be.equal(version)
        corp.db.get_all_attr('main')['template_name'].should.be.equal(template_name)
        corp.db.get_all_attr('main')['source'].should.be.equal(source)

        assert corp.exist()
   






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







