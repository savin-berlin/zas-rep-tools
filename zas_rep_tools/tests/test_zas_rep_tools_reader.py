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

from zas_rep_tools.src.classes.Reader import Reader
from zas_rep_tools.src.utils.recipes_test_db import *


from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZASreaderReader(unittest.TestCase):
    def setUp(self):


        ######## Folders Creation ##############
        ########### Begin ######################
        path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Reader))))
        #p(path_to_zas_rep_tools)

        self.txt_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/txt/SmallFakeSubset"
        self.csv_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/csv/SmallFakeSubset"
        self.csv_blogger_corpus_relativ_path_to_high_repetativ_subset = "data/tests_data/Corpora/BloggerCorpus/csv/HighRepetativSubSet"
        self.xml_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/xml/SmallFakeSubset"
        self.xml_blogger_corpus_relativ_path_to_high_repetativ_subset = "data/tests_data/Corpora/BloggerCorpus/xml/HighRepetativSubSet"
        self.json_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/json/SmallFakeSubset"
        self.json_blogger_corpus_relativ_path_to_high_repetativ_subset = "data/tests_data/Corpora/BloggerCorpus/json/HighRepetativSubSet"
        # txt_blogger_corpus_relativ_path_to_small_subset = "data/tests_data/Corpora/BloggerCorpus/txt/SmallSubset"
        # txt_blogger_corpus_relativ_path_to_the_middle_subset = "data/tests_data/Corpora/BloggerCorpus/txt/MiddleSubset"
        # txt_blogger_corpus_relativ_path_to_the_hightrepetativ_subset = "data/tests_data/Corpora/BloggerCorpus/txt/HighRepetativSubSet"

        self.txt_blogger_corpus_abs_path_to_small_fake_subset = os.path.join(path_to_zas_rep_tools,self.txt_blogger_corpus_relativ_path_to_small_fake_subset)
        self.csv_blogger_corpus_abs_path_to_small_fake_subset = os.path.join(path_to_zas_rep_tools,self.csv_blogger_corpus_relativ_path_to_small_fake_subset)
        self.csv_blogger_corpus_abs_path_to_high_repetativ_subset = os.path.join(path_to_zas_rep_tools,self.csv_blogger_corpus_relativ_path_to_high_repetativ_subset)
        self.xml_blogger_corpus_abs_path_to_small_fake_subset = os.path.join(path_to_zas_rep_tools,self.xml_blogger_corpus_relativ_path_to_small_fake_subset)
        self.xml_blogger_corpus_abs_path_to_high_repetativ_subset = os.path.join(path_to_zas_rep_tools,self.xml_blogger_corpus_relativ_path_to_high_repetativ_subset)
        self.json_blogger_corpus_abs_path_to_small_fake_subset = os.path.join(path_to_zas_rep_tools,self.json_blogger_corpus_relativ_path_to_small_fake_subset)
        self.json_blogger_corpus_abs_path_to_high_repetativ_subset = os.path.join(path_to_zas_rep_tools,self.json_blogger_corpus_relativ_path_to_high_repetativ_subset)
        

        # self.txt_blogger_corpus_abs_path_to_small_subset = os.path.join(path_to_zas_rep_tools,txt_blogger_corpus_relativ_path_to_small_subset)
        # self.txt_blogger_corpus_abs_path_to_middle_subset = os.path.join(path_to_zas_rep_tools,txt_blogger_corpus_relativ_path_to_the_middle_subset)
        # self.txt_blogger_corpus_abs_path_to_hightrepetativ_subset = os.path.join(path_to_zas_rep_tools,txt_blogger_corpus_relativ_path_to_the_hightrepetativ_subset)

        self.tempdir = TempDirectory()
        self.tempdir.makedir('BloggerCorpus')

        self.path_to_temp_BloggerCorpus  = self.tempdir.getpath('BloggerCorpus')
        #self.path_to_temp_testFolder  = self.tempdir.getpath('TestFolder')

        self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'TXTSmallFakeSubset')
        self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVSmallFakeSubset')
        self.csv_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVHighRepetativSubSet')
        self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLSmallFakeSubset')
        self.xml_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLHighRepetativSubSet')
        self.json_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLSmallFakeSubset')
        self.json_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLHighRepetativSubSet')
    
        # self.txt_blogger_corpus_temp_abs_path_to_small_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'SmallSubset')
        # self.txt_blogger_corpus_temp_abs_path_to_middle_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'MiddleSubset')
        # self.txt_blogger_corpus_temp_abs_path_to_hightrepetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'HighRepetativSubSet')

        copy_tree(self.txt_blogger_corpus_abs_path_to_small_fake_subset,self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset)
        copy_tree(self.csv_blogger_corpus_abs_path_to_small_fake_subset,self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset)
        copy_tree(self.csv_blogger_corpus_abs_path_to_high_repetativ_subset,self.csv_blogger_corpus_temp_abs_path_to_high_repetativ_subset)
        copy_tree(self.xml_blogger_corpus_abs_path_to_small_fake_subset,self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset)
        copy_tree(self.xml_blogger_corpus_abs_path_to_high_repetativ_subset,self.xml_blogger_corpus_temp_abs_path_to_high_repetativ_subset)
        copy_tree(self.json_blogger_corpus_abs_path_to_small_fake_subset,self.json_blogger_corpus_temp_abs_path_to_small_fake_subset)
        copy_tree(self.json_blogger_corpus_abs_path_to_high_repetativ_subset,self.json_blogger_corpus_temp_abs_path_to_high_repetativ_subset)
     
        # copy_tree(self.txt_blogger_corpus_abs_path_to_middle_subset,self.txt_blogger_corpus_temp_abs_path_to_middle_subset)
        # copy_tree(self.txt_blogger_corpus_abs_path_to_hightrepetativ_subset,self.txt_blogger_corpus_temp_abs_path_to_hightrepetativ_subset)
        

        ## create test-data
        #self.txt_small_fake_subset = {os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset,file):codecs.open(os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset,file), "r").read() for file in os.listdir(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset) if ".txt" in file}
        #self.csv_small_fake_subset = {os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset,file):codecs.open(os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset,file), "r").read() for file in os.listdir(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset) if ".txt" in file}
        # self.small_subset = {os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.txt_blogger_corpus_temp_abs_path_to_small_subset) if ".txt" in file}
        # self.middle_subset = {os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.txt_blogger_corpus_temp_abs_path_to_small_subset) if ".txt" in file }
        # self.hightrepetativ_subset = {os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file):codecs.open(os.path.join(self.txt_blogger_corpus_temp_abs_path_to_small_subset,file), "r").read() for file in os.listdir(self.txt_blogger_corpus_temp_abs_path_to_small_subset) if ".txt" in file }


        ######## Folders Creation ##############
        ########### End #####################
        
       



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
    def test_reader_initialisation_000(self):
        reader = Reader(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset, "txt", regex_template="blogger", logger_level=logging.ERROR)
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
        reader = Reader(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset, "txt", regex_template="blogger", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data
            #p(data)


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_txt_for_given_colnames_501(self):
        reader = Reader(self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset, "txt", regex_template="blogger", logger_level=logging.ERROR)
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
        reader = Reader(self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset, "csv", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_csv_with_utf8_503(self):
        reader = Reader(self.csv_blogger_corpus_abs_path_to_high_repetativ_subset, "csv", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_csv_for_given_colnames_504(self):
        reader = Reader(self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset, "csv", logger_level=logging.ERROR)
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
        reader = Reader(self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset, "xml", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_xml_with_utf8_506(self):
        reader = Reader(self.xml_blogger_corpus_abs_path_to_high_repetativ_subset, "xml", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_xml_for_given_colnames_507(self):
        reader = Reader(self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset, "xml", logger_level=logging.ERROR)
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
        reader = Reader(self.json_blogger_corpus_temp_abs_path_to_small_fake_subset, "json", logger_level=logging.ERROR)
        for data in reader.getlazy():
            #p(data)
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data

    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_json_with_utf8_509(self):
        reader = Reader(self.json_blogger_corpus_abs_path_to_high_repetativ_subset, "json", logger_level=logging.ERROR)
        for data in reader.getlazy():
            assert isinstance(data, dict)
            assert len(data) == 6
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'working_area' in data
            assert 'age' in data
            assert 'blogger_id' in data
            assert 'gender' in data


    @attr(status='stable')
    #@wipd
    def test_lazyreader_from_json_for_given_colnames_510(self):
        reader = Reader(self.json_blogger_corpus_temp_abs_path_to_small_fake_subset, "json", logger_level=logging.ERROR)
        for data in reader.getlazy(colnames=["text", 'star_constellation', 'gender']):
            assert isinstance(data, dict)
            assert len(data) == 3
            assert 'text' in data
            assert 'star_constellation' in data
            assert 'gender' in data





    #self.csv_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVSmallFakeSubset')
    #self.csv_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'CSVHighRepetativSubSet')
    #self.xml_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLSmallFakeSubset')
    #self.xml_blogger_corpus_temp_abs_path_to_high_repetativ_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'XMLHighRepetativSubSet')
       



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







