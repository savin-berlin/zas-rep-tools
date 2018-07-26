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


#import codecs
import sure
#import inspect
import copy
#from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
#import glob

from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.classes.reader import Reader
#from zas_rep_tools.src.utils.recipes_test_db import *


from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import *
from zas_rep_tools.src.utils.helpers import LenGen, path_to_zas_rep_tools, get_number_of_streams_adjust_cpu





class TestZASreaderReader(unittest.TestCase):
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
    def test_reader_initialisation_000(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        reader.should.be.a(Reader)

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
  #{'text': u"urlLink Drawing Game  It's PICTIONARY. It's very cool.", 'stern': 'Pisces', 'working_area': 'indUnk', 'age': '24', 'number': '416465', 'gender': 'male'}

###################    :500############################################ 
    

    ###### TXT ######
    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_txt_500(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        for data in reader.getlazy():
        #p(data)
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data
        #p(data)




    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_txt_for_given_colnames_501(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        for data in reader.getlazy(colnames=["text", 'star_constellation', 'gender']):
            assert isinstance(data, dict)
            assert len(data) == 3
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'gender' in data
        #p(data)




    ###### csv ######

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_csv_with_ascii_502(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.csv_blogger_small_fake_set), "csv", mode="test")
        for data in reader.getlazy():
            #p(data)
            assert isinstance(data, dict)
            assert len(data) == len(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"][0])
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_csv_with_utf8_503(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.csv_blogger_hightrepetativ_set ), "csv", mode="test")
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == len(self.configer.docs_row_values(token=True, unicode_str=True)["blogger"][0])
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_csv_for_given_colnames_504(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.csv_blogger_small_fake_set), "csv", mode="test")
        for data in reader.getlazy(colnames=["text", 'star_constellation', 'gender']):
            #p(data)
            assert isinstance(data, dict)
            assert len(data) == 3
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'gender' in data




    ###### XML ######


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_xml_with_ascii_505(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.xml_blogger_small_fake_set), "xml", mode="test")
        #p(reader.getlazy())
        #p(len(reader.getlazy()))
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_xml_with_utf8_506(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.xml_blogger_hightrepetativ_set), "xml", mode="test")
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_xml_for_given_colnames_507(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.xml_blogger_small_fake_set), "xml", mode="test")
        #reader = Reader(os.path.join(os.path.join(self.path_to_zas_rep_tools,self.path_to_test_sets_for_blogger_Corpus), self.xml_blogger_small_fake_set), "xml", mode="test")
        for data in reader.getlazy(colnames=["text", 'star_constellation', 'gender']):
            assert isinstance(data, dict)
            assert len(data) == 3
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'gender' in data



    ###### JSON ######

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_json_with_ascii_508(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.json_blogger_small_fake_set), "json", mode="test")
        for data in reader.getlazy():
            #p(data, "data")
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_json_with_utf8_509(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.json_blogger_hightrepetativ_set ), "json", mode="test")
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_json_for_given_colnames_510(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.json_blogger_small_fake_set), "json", mode="test")
        for data in reader.getlazy(colnames=["text", 'star_constellation', 'gender']):
            assert isinstance(data, dict)
            assert len(data) == 3
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'gender' in data



    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_twitter_json_with_utf8_511(self):
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter", mode="test")
        for data in reader.getlazy():
            if data:
                #p(data, c="r")
                assert isinstance(data, dict)
                #p(data["text"])
                assert 'text' in data
                assert 'u_lang' in data
                assert 'id' in data
                assert 'u_id' in data



    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_twitter_json_for_given_colnames_512(self):
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter", mode="test")
        for data in reader.getlazy(colnames=["text"]):
            if data:
                assert isinstance(data, dict)
                assert len(data)==1
                assert 'text' in data




    #self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVSmallFakeSubset')
    #self.csv_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVHighRepetativSubSet')
    #self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLSmallFakeSubset')
    #self.xml_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLHighRepetativSubSet')
       




    ###### parallel computing ######

    @attr(status='stable')
    #@wipd
    def test_getlazy_many_streams_from_txt_without_given_number_of_streams_adjusted_for_current_cpu_520(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        number_of_rows = len(reader.files_to_read)
        len(reader.getlazy(stream_number=4, adjust_to_cpu=True, min_files_pro_stream=5)).should.be.equal(get_number_of_streams_adjust_cpu(3, number_of_rows, 5))
        len(reader.getlazy(stream_number=4, adjust_to_cpu=True, min_files_pro_stream=3)).should.be.equal(get_number_of_streams_adjust_cpu(3, number_of_rows, 4))
        len(reader.getlazy(stream_number=4, adjust_to_cpu=True, min_files_pro_stream=2)).should.be.equal(get_number_of_streams_adjust_cpu(2, number_of_rows, 4))
        len(reader.getlazy(stream_number=4, adjust_to_cpu=True, min_files_pro_stream=1)).should.be.equal(get_number_of_streams_adjust_cpu(1, number_of_rows, 4))

        i = 0
        for gen in reader.getlazy(stream_number=1000,adjust_to_cpu=True, min_files_pro_stream=1):
            for row_dict in gen: 
                i+=1
                assert isinstance(row_dict, dict)
                assert len(row_dict) == 6
                assert 'text' in row_dict
                assert 'star_constellation' in row_dict
                assert 'working_area' in row_dict
                assert 'age' in row_dict
                assert 'id' in row_dict
                assert 'gender' in row_dict
        #p((number_of_rows, i))
        assert number_of_rows == i




    @attr(status='stable')
    #@wipd
    def test_getlazy_many_streams_from_txt_with_given_number_of_streams_without_adjust_for_current_cpu_521(self):
        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode="test")
        number_of_rows = len(reader.files_to_read)
        #p(number_of_rows)

        # Check for stream_number=3
        len(reader.getlazy(stream_number=3, adjust_to_cpu=False)).should.be.equal(3)
        len([rowdict for gen in reader.getlazy(stream_number=3, adjust_to_cpu=False) for rowdict in gen]).should.be.equal(number_of_rows)

        # Check for stream_number=2
        #p(reader.getlazy(stream_number=2, adjust_to_cpu=False))
        len(reader.getlazy(stream_number=2, adjust_to_cpu=False)).should.be.equal(2)
        len([rowdict for gen in reader.getlazy(stream_number=2, adjust_to_cpu=False) for rowdict in gen]).should.be.equal(number_of_rows)


        i = 0
        for gen, fname in zip(reader.getlazy(stream_number=3,adjust_to_cpu=False, min_files_pro_stream=1), reader.files_to_read):
            for row_dict in gen: 
                i +=1
                t = codecs.open(fname, "r", encoding="utf-8").read()
                assert row_dict["text"] == t
                assert isinstance(row_dict, dict)
                assert len(row_dict) == 6
                assert 'text' in row_dict
                assert 'star_constellation' in row_dict
                assert 'working_area' in row_dict
                assert 'age' in row_dict
                assert 'id' in row_dict
                assert 'gender' in row_dict
        assert number_of_rows == i






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







