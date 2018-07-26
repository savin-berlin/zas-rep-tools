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


#import codecs
import sure
#import inspect
import copy
#from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import random
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN
import json
#import glob

from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.classes.reader import Reader

from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, LenGen, path_to_zas_rep_tools, get_number_of_streams_adjust_cpu
#from zas_rep_tools.src.utils.recipes_test_db import *
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import *



import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama





class TestZAScorpusCorpus(unittest.TestCase):
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




    ##### xx :0== ######


    @attr(status='stable')
    #@wipd
    def test_initialization_of_the_corpus_instance_000(self):
        corp = Corpus(mode="test")
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


###################  Corpus Initialization :500############################################ 
    @attr(status='stable')
    #@wipd
    def test_new_plaintext_corpus_initialization_500(self):

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


        corp = Corpus(mode="test")
        #corp = Corpus(logger_level=logging.DEBUG,mode="test")
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
    @attr(status='stable')
    #@wipd
    def test_new_encrypted_corpus_initialization_501(self):

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


        corp = Corpus(mode="test")
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name, encryption_key=encryption_key, source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
        
        

    @attr(status='stable')
    #@wipd
    def test_open_plaintext_blogger_corpus_502(self):

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


        corp = Corpus(mode="test")
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
  
    
        corp.db.get_all_attr()['name'].should.be.equal(name)
        corp.db.get_all_attr()['language'].should.be.equal(language)
        corp.db.get_all_attr()['visibility'].should.be.equal(visibility)
        corp.db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        corp.db.get_all_attr()['typ'].should.be.equal(typ)
        corp.db.get_all_attr()['id'].should.be.equal(corpus_id)
        corp.db.get_all_attr()['license'].should.be.equal(license)
        corp.db.get_all_attr()['version'].should.be.equal(version)
        corp.db.get_all_attr()['template_name'].should.be.equal(template_name)
        corp.db.get_all_attr()['source'].should.be.equal(source)

        assert corp.exist()
   
    @attr(status='stable')
    #@wipd
    def test_open_encrypted_twitter_corpus_503(self):

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
        #p(encryption_key)

        corp = Corpus(mode="test")
        corp.open(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_corp_de), encryption_key=encryption_key)
    

        corp.db.get_all_attr()['name'].should.be.equal(name)
        corp.db.get_all_attr()['language'].should.be.equal(language)
        corp.db.get_all_attr()['visibility'].should.be.equal(visibility)
        corp.db.get_all_attr()['platform_name'].should.be.equal(platform_name)
        corp.db.get_all_attr()['typ'].should.be.equal(typ)
        corp.db.get_all_attr()['id'].should.be.equal(corpus_id)
        corp.db.get_all_attr()['license'].should.be.equal(license)
        corp.db.get_all_attr()['version'].should.be.equal(version)
        corp.db.get_all_attr()['template_name'].should.be.equal(template_name)
        corp.db.get_all_attr()['source'].should.be.equal(source)

        assert corp.exist()
   





###################    :550############################################ 
    @attr(status='stable')
    #@wipd
    def test_insert_without_preprocession_550(self):

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


        corp = Corpus(mode="test", preprocession=False)
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        #p(len(self.input_list_blogger_corpus_high_repetativ_subset))
        corp.insert(self.input_list_blogger_corpus_high_repetativ_subset)
        #p(list(corp.docs(output="dict")))
        #sys.exit()
        for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
            #del row_from_corp["id"]
            { unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})


    @attr(status='stable')
    #@wipd
    def test_insert_with_preprocession_from_json_in_one_thread_on_twitter_example_551(self):
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
        language="de"
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True, mode="test")
        corp = Corpus( preprocession=True,  sent_splitter="somajo", pos_tagger="someweta", language=language, logger_traceback=True, ext_tb=True, mode="test") #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   

        corp.insert(reader.getlazy())
        inserted_rows_into_db = len(list(corp.db.lazyget("documents")))
        corp.inserted_insertion_status_general
        #p((inserted_rows_into_db , corp.inserted_insertion_status_general))
        if inserted_rows_into_db != sum(corp.inserted_insertion_status_general.values()):
            assert False




    @attr(status='stable')
    #@wipd
    def test_insert_with_preprocession_from_json_in_many_thread_on_twitter_example_552(self):
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
        language="de"
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True, mode="test")
        corp = Corpus( sent_splitter="somajo", pos_tagger="someweta", language=language, logger_traceback=True, ext_tb=True, mode="test") #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   

        corp.insert(reader.getlazy(stream_number=-1, min_files_pro_stream=7))
        inserted_rows_into_db = len(list(corp.db.lazyget("documents")))

        if inserted_rows_into_db != sum(corp.inserted_insertion_status_general.values()):
            assert False


    @attr(status='stable')
    #@wipd
    def test_preprocessing_on_example_of_blogger_corp_553(self):
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
        preprocession = True
        tokenizer = "somajo"
        sent_splitter = "somajo"
        pos_tagger = "someweta"
        sentiment_analyzer = "textblob"
        lang_classification = True
        del_url = True
        del_punkt = True
        del_num = True
        del_html = True
        del_mention = True
        del_hashtag = True
        case_sensitiv = False
        typ= "corpus"
        language="de"

        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter, pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer, language=language,lang_classification=lang_classification, del_url=del_url, del_punkt=del_punkt, del_num=del_num, del_mention=del_mention, del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,logger_traceback=True, mode="test") #text_field_name=""
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        corp.insert(self.input_list_blogger_corpus_high_repetativ_subset,  status_bar=True)


        # check, if there rows was matched
        for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
            #p(row_from_corp, "row_from_corp")
            #p(row_from_input, "row_from_input")
            del row_from_corp["text"]
            del row_from_input["text"]
            { unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})


        # check if preprocessing was right
        for row_from_corp in  corp.docs(output="dict"):
            if row_from_corp["id"]==324114:
                output_text = u'[[[["-)))", "$("], ["-)", "$("], ["-p", "ADJA"], ["neeeeeeeeeeeeeeeeiiiiiiinnnnn", "NN"]], ["neutral", 0.0]], [[["bitte", "PTKANT"], ["nicht", "PTKNEG"], ["\\ud83d\\ude02", "EMOIMG"], ["\\ud83d\\ude02", "EMOIMG"], ["\\ud83d\\ude02", "EMOIMG"], ["test", "NN"], ["version", "NN"], ["von", "APPR"], ["einem", "ART"], ["tweeeeeeeeet", "NN"], ["=)", "EMOASC"], ["))))))", "$("], ["noch", "ADV"], ["einen", "ART"], ["tweeeeeeeeet", "NN"], ["=)", "EMOASC"], ["))))))", "$("], ["\\ud83d\\ude05", "EMOIMG"], ["\\ud83d\\ude05", "EMOIMG"]], ["positive", 1.0]]]'
                if row_from_corp["text"] != output_text:
                    assert False
            elif row_from_corp["id"]==416465:
                output_text = u'[[[["einen", "ART"], ["weiteren", "ADJA"], ["thread", "NN"], ["eingef\\u00fcgt", "VVPP"], ["ju", "NE"], ["huuuuuuuu", "NN"], ["=)", "EMOASC"], ["\\ud83d\\udc9b", "EMOIMG"], ["\\ud83d\\udc9b", "EMOIMG"], ["\\ud83d\\udc9b", "EMOIMG"], ["den", "ART"], ["vierten", "ADJA"], ["threadddddd", "NN"], ["wooooowwwwww", "VVFIN"], ["\\u263a", "EMOIMG"], ["\\ufe0f", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["teeeeest", "NN"], ["tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["positive", 0.7]], [[["weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["zeichen", "NN"], ["beinhalten", "VVINF"], ["sollte", "VMFIN"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["teeeeest", "NN"], ["tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["zeichen", "NN"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["teeeeest", "NN"], ["quoted", "NE"], ["tweet", "NN"], ["das", "PDS"], ["als", "APPR"], ["extended", "NN"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["zeichen", "NN"], ["beinhalten", "VVINF"], ["sollte", "VMFIN"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["teeeeest", "NN"], ["tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["zeichen", "NN"], ["\\ud83d\\ude1c", "EMOIMG"], ["\\ud83d\\ude1c", "EMOIMG"], ["h", "NN"]], ["neutral", 0.0]]]'
                if row_from_corp["text"] != output_text:
                    assert False
            elif row_from_corp["id"]==322624:
                output_text = u'[[[["eine", "ART"], ["teeeeeest", "NN"], ["diskussion", "NN"], ["wird", "VAFIN"], ["er\\u00f6ffnet", "VVPP"], ["-rep-tools", "NE"], ["einen", "ART"], ["test", "NN"], ["retweet", "NN"], ["wird", "VAFIN"], ["gepostet", "VVPP"]], ["neutral", 0.0]], [[["juhuuuuuu", "ITJ"], ["=)", "EMOASC"], ["\\ud83d\\ude00", "EMOIMG"], ["\\ud83d\\ude00", "EMOIMG"], ["\\ud83d\\ude00", "EMOIMG"], ["\\ud83d\\ude00", "EMOIMG"], ["noooooooch", "ADV"], ["einen", "ART"], ["tweeeeeeeeet", "NN"], ["=)", "EMOASC"], ["))))))", "$("]], ["neutral", 0.0]]]'
                if row_from_corp["text"] != output_text:
                    assert False









    #@attr(status='stable')
    #@wipd
    def test_insert_parallel_many_threads_on_example_of_blogger_corp_554(self):
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
        preprocession = True
        tokenizer = True
        pos_tagger = False
        sent_splitter = False
        sentiment_analyzer = True
        lang_classification = True
        del_url = True
        del_punkt = True
        del_num = True
        del_html = True
        del_mention = True
        del_hashtag = True
        case_sensitiv = False
        typ= "corpus"
        language="de"

        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter, pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer, language=language,lang_classification=lang_classification, del_url=del_url, del_punkt=del_punkt, del_num=del_num, del_mention=del_mention, del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,logger_traceback=True, mode="test") #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        corp.insert(self.input_list_blogger_corpus_high_repetativ_subset,  status_bar=True)
        #p(corp.db.col("info"))
        # p(corp.db.get_all_attr())
        # p(corp.db.update_attr("version", "55454"))
        # p(corp.db.get_all_attr())
        #corp.db.update_attrs({"version":"5678", "id":"5678"})
        #p(corp.db.get_all_attr())
        #corp.insert(self.input_list_blogger_corpus_high_repetativ_subset)
        #for rdict in reader.getlazy(stream_number=-1, min_files_pro_stream=5):
        #   p(list(rdict))
        #p(reader.getlazy(stream_number=-1, min_files_pro_stream=1), c="r")
        #for gen in reader.getlazy(stream_number=-1, min_files_pro_stream=1):
        #    for k in gen:
        #        p((gen,k))
        #corp.insert(reader.getlazy(stream_number=-1, min_files_pro_stream=1))

        #corp.insert(reader.getlazy(), status_bar=False)
        #p(corp.opened_gateways)
        # p(corp.check_status_gateways())
        # #sys.exit()
        # for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
        #     del row_from_corp["id"]
        #     { unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})


    #@attr(status='stable')
    #@wipd
    def test_insert_parallel_many_threads_on_example_of_twitter_corp_555(self):

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
        language="de"
        preprocession = True
        tokenizer = True
        pos_tagger = False
        sent_splitter = True
        del_url = True
        del_punkt = True
        del_num = True
        case_sensitiv = False
        typ= "corpus"
        language="de"
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True,mode="test")
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter, pos_tagger=pos_tagger, language=language,del_url=del_url, del_punkt=del_punkt, del_num=del_num, case_sensitiv=case_sensitiv,logger_traceback=True, mode="dev") #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        #corp.insert(self.input_list_blogger_corpus_high_repetativ_subset)
        #for rdict in reader.getlazy(stream_number=-1, min_files_pro_stream=5):
        #   p(list(rdict))
        #p(reader.getlazy(stream_number=-1, min_files_pro_stream=5), c="r")

        #p(reader.getlazy(stream_number=-1, min_files_pro_stream=100), c="r")

        #p(len(reader.getlazy(stream_number=-1, min_files_pro_stream=100)), c="r")
        #for gen in reader.getlazy(stream_number=-1, min_files_pro_stream=100):
        #    p((gen,len(gen), len(list(gen))))
          #for k in gen:
          #    p((gen,k))


        #corp.insert(reader.getlazy(stream_number=-1, min_files_pro_stream=100))
        #p(len(list(corp.db.lazyget("documents"))))
        corp.insert(reader.getlazy(), status_bar=True)
        #p(corp.opened_gateways)
        # p(corp.check_status_gateways())
        # #sys.exit()
        # for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
        #     del row_from_corp["id"]
        #     { unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})







    #### DOCs Getter 600############
    

    @attr(status='stable')
    #@wipd
    def test_get_docs_single_600(self):

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


        corp = Corpus(mode="test")
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
            
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))    

        columns = inp_dict.keys()
        rows = inp_dict.values()

        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")

        number_of_rows_in_db = corp.db.rownum("documents")
        docs_row_values = self.configer.docs_row_values(token=True, unicode_str=True,lang="en")
        number_of_values = len(docs_row_values["blogger"])
        number_of_rows_in_input  = len(docs_row_values["blogger"])
        #p((number_of_rows_in_db, number_of_rows_in_input))
        if number_of_rows_in_db != number_of_rows_in_input:
            assert False


        rows_from_db = []
        count = 0
        for row_from_db in corp.docs(stream_number=1,adjust_to_cpu=False):
            rows_from_db.append(row_from_db)
            count +=1

        assert count == number_of_rows_in_db

        for row_from_db, row_from_input in zip(rows_from_db, docs_row_values["blogger"]):
            i=0
            while i <number_of_values:
                if i == text_index:
                    pass
                    #for sent in row_from_db[i]:
                    #p(row_from_db[i])
                    #p( row_from_input[i])
                    #p((row_from_db[i],json.dumps(row_from_input[i])))
                    #assert row_from_db[i] == json.dumps(row_from_input[i])
                else:
                    assert row_from_db[i] == row_from_input[i]
                i+=1




    
    @attr(status='stable')
    #@wipd
    def test_get_docs_many_streams_601(self):

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


        corp = Corpus(mode="test")
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
            
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True,lang="en")["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))    

        columns = inp_dict.keys()
        rows = inp_dict.values()

        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")


        number_of_rows = corp.db.rownum("documents")
        docs_row_values = self.configer.docs_row_values(token=True, unicode_str=True,lang="en")
        
        #p((number_of_rows,len(docs_row_values["blogger"])))
        if number_of_rows != len(docs_row_values["blogger"]):
            assert False

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows+1)).should.be.equal(get_number_of_streams_adjust_cpu(number_of_rows+1, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows+1) for row in gen]).should.be.equal(number_of_rows)
        
        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows)).should.be.equal(get_number_of_streams_adjust_cpu(number_of_rows, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows-1)).should.be.equal(get_number_of_streams_adjust_cpu(number_of_rows-1, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=number_of_rows-1) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=4)).should.be.equal(get_number_of_streams_adjust_cpu(4, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=4) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=3)).should.be.equal(get_number_of_streams_adjust_cpu(3, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=3) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=2)).should.be.equal(get_number_of_streams_adjust_cpu(2, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=2) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=1)).should.be.equal(get_number_of_streams_adjust_cpu(1, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=1) for row in gen]).should.be.equal(number_of_rows)

        len(corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=0)).should.be.equal(get_number_of_streams_adjust_cpu(0, number_of_rows, 4))
        len([row for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=0) for row in gen]).should.be.equal(number_of_rows)

        


        rows_from_db = []
        for gen in corp.docs(stream_number=4,adjust_to_cpu=True, min_files_pro_stream=2):
            for row_from_db in gen:
                rows_from_db.append(row_from_db)
        #docs_row_values = self.configer.docs_row_values(token=True, unicode_str=True)
        assert len(rows_from_db) == len(docs_row_values["blogger"])
        number_of_values = len(docs_row_values["blogger"][0])
        for row_from_db, row_from_input in zip(rows_from_db, docs_row_values["blogger"]):
            i=0
            #p((row_from_db, row_from_input))
            
            while i <number_of_values:

                if i == text_index:
                    pass
                    #p((row_from_db[i], row_from_input[i]))
                    #p((row_from_db[i],json.dumps(row_from_input[i])))
                    #assert row_from_db[i] == json.dumps(row_from_input[i])
                else:
                    #p(i)
                    assert row_from_db[i] == row_from_input[i]
                i+=1




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







