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

from zas_rep_tools.src.classes.Exporter import Exporter
from zas_rep_tools.src.classes.Reader import Reader

from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import Logger





class TestZAScorpusExporterExporter(unittest.TestCase):
    def setUp(self):



        ######## Folders Creation ##############
        ########### Begin ######################
        self.path_to_zas_rep_tools = os.path.dirname(os.path.dirname(os.path.dirname(inspect.getfile(Exporter))))
        txt_blogger_corpus_relativ_path_to_hight_repetativ_subset_with_unicode = "data/tests_data/Corpora/BloggerCorpus/txt/HighRepetativSubSet"
        
        #txt_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/txt/SmallFakeSubset"
        #txt_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/txt/SmallSubset"
        #txt_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/txt/MiddleSubset"
        #txt_blogger_corpus_relativ_path_to_small_fake_subset = "data/tests_data/Corpora/BloggerCorpus/txt/HighRepetativSubSet"
        
        self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode = os.path.join(self.path_to_zas_rep_tools,txt_blogger_corpus_relativ_path_to_hight_repetativ_subset_with_unicode)


        self.input_list_fake_blogger_corpus = [{'star': 'Capricorn', 'text': u'Well, the angel won. I went to work today....after alot of internal struggle with the facts. I calculated sick days left this year,', 'prof': 'Consulting', 'age': '46', 'id': '324114', 'sex': 'female'}, {'star': 'Pisces', 'text': u"urlLink Drawing Game  It's PICTIONARY. It's very cool.", 'prof': 'indUnk', 'age': '24', 'id': '416465', 'sex': 'male'}, {'star': 'Virgo', 'text': u'The mango said, "Hi there!!.... \n"Hi there!!.... \n"Hi there!!.... ', 'prof': 'Non-Profit', 'age': '17', 'id': '322624', 'sex': 'female'}]
        self.input_list_blogger_corpus_high_repetativ_subset = [{'star': 'Capricorn', 'text': u'Neeeeeeeeeeeeeeeeiiiiiiinnnnn!!!!! Bitte nicht \U0001f602\U0001f602\U0001f602 \nTest Version von einem Tweeeeeeeeet=)))))))\nnoch einen Tweeeeeeeeet=))))))) \U0001f605\U0001f605', 'prof': 'Consulting', 'age': '46', 'id': '324114', 'sex': 'female'}, {'star': 'Pisces', 'text': u'Einen weiteren Thread eingef\xfcgt!!! juHuuuuuuuu=) \U0001f49b\U0001f49b\U0001f49b\nden vierten Threadddddd!!! wooooowwwwww!!! \u263a\ufe0f \U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c\U0001f61c\U0001f61c\nDas ist einnnneeeen Teeeeest Quoted Tweet, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen beinhalten sollte. \U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c\U0001f61c Das ist einnnneeeen Teeeeest Tweeeets, das als "extended" klassifiziert werden sollte!!! Weil es bis 280 Zeichen \U0001f61c\U0001f61c h', 'prof': 'indUnk', 'age': '24', 'id': '416465', 'sex': 'male'}, {'star': 'Virgo', 'text': u'Eine Teeeeeest Diskussion wird er\xf6ffnet!!! @zas-rep-tools \nEinen Test Retweet wird gepostet!!!!! Juhuuuuuu=) \U0001f600\U0001f600\U0001f600\U0001f600\nnoooooooch einen Tweeeeeeeeet=)))))))', 'prof': 'Non-Profit', 'age': '17', 'id': '322624', 'sex': 'female'}]
        self.fieldnames = ["id", "text","star","prof","sex", "age" ]

        self.tempdir = TempDirectory()
        self.tempdir.makedir('BloggerCorpus')

        self.path_to_temp_BloggerCorpus  = self.tempdir.getpath('BloggerCorpus')
        #self.txt_blogger_corpus_temp_abs_path_to_small_fake_subset = os.path.join(self.path_to_temp_BloggerCorpus, 'SmallFakeSubset')


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
    def test_exporter_initialisation_with_list_000(self):
        exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)
        exporter.should.be.a(Exporter)

        

    @attr(status='stable')
    #@wipd
    def test_exporter_initialisation_with_reader_obj_001(self):
        reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
        exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
        exporter.should.be.a(Exporter)


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


###################    :500############################################ 
    ###### ***** ######
   

    @attr(status='stable')
    #@wipd
    def test_export_to_csv_from_list_000(self):
        #real_fold = os.path.join(self.path_to_zas_rep_tools, "data/tests_data/Corpora/BloggerCorpus/txt")
        exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)
        #exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)
        #exporter.should.be.a(Exporter)
        exporter.tocsv(self.path_to_temp_BloggerCorpus, "blogger_corpus",self.fieldnames, rows_limit_in_file=1)
        #exporter.tocsv(real_fold, "blogger_corpus",self.fieldnames, rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".csv" in item:
                i+=1

        if len(self.input_list_fake_blogger_corpus) != i:
            assert False


    @attr(status='stable')
    #@wipd
    def test_export_to_csv_from_reader_001(self):
        reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
        exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)

        exporter.tocsv(self.path_to_temp_BloggerCorpus, "blogger_corpus",self.fieldnames, rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".csv" in item:
                i+=1

        if len(list(reader.getlazy())) != i:
            assert False




    @attr(status='stable')
    #@wipd
    def test_export_to_xml_from_list_002(self):
        #real_fold = os.path.join(self.path_to_zas_rep_tools, "data/tests_data/Corpora/BloggerCorpus/xml")
        exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)
        #exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)

        exporter.toxml(self.path_to_temp_BloggerCorpus, "blogger_corpus", rows_limit_in_file=1)
        #exporter.toxml(real_fold, "blogger_corpus", rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".xml" in item:
                i+=1

        if len(self.input_list_fake_blogger_corpus) != i:
            assert False


    @attr(status='stable')
    #@wipd
    def test_export_to_xml_from_reader_003(self):
        reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
        exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)

        exporter.toxml(self.path_to_temp_BloggerCorpus, "blogger_corpus", rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".xml" in item:
                i+=1


        if len(list(reader.getlazy())) != i:
            assert False






    @attr(status='stable')
    #@wipd
    def test_export_to_json_from_list_003(self):
        #real_fold = os.path.join(self.path_to_zas_rep_tools, "data/tests_data/Corpora/BloggerCorpus/json")
        exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)

        exporter.tojson(self.path_to_temp_BloggerCorpus, "blogger_corpus", rows_limit_in_file=1)
        #exporter.tojson(real_fold, "blogger_corpus", rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".json" in item:
                i+=1

        #p((len(self.input_list_fake_blogger_corpus), i))
        if len(self.input_list_fake_blogger_corpus) != i:
            assert False




    @attr(status='stable')
    #@wipd
    def test_export_to_json_from_reader_004(self):
        reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
        exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)

        exporter.tojson(self.path_to_temp_BloggerCorpus, "blogger_corpus", rows_limit_in_file=1)

        i=0
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".json" in item:
                i+=1

        #p((len(self.input_list_fake_blogger_corpus), i))
        if len(list(reader.getlazy())) != i:
            assert False





    @attr(status='stable')
    #@wipd
    def test_export_to_sqlite_from_list_005(self):
        #real_fold = os.path.join(self.path_to_zas_rep_tools, "data/tests_data/Corpora/BloggerCorpus/")
        exporter = Exporter(self.input_list_fake_blogger_corpus, logger_level=logging.ERROR)

        dbname = "blogger_corpus"
        exporter.tosqlite(self.path_to_temp_BloggerCorpus, dbname, self.fieldnames)
        #exporter.tosqlite(real_fold, dbname, self.fieldnames)

 
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".db" in item:
                if dbname not in item:
                    assert False




    @attr(status='stable')
    #@wipd
    def test_export_to_sqlite_from_reader_006(self):
        reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
        exporter = Exporter(reader.getlazy(), logger_level=logging.ERROR)
        dbname = "blogger_corpus"

        exporter.tosqlite(self.path_to_temp_BloggerCorpus, dbname, self.fieldnames)

 
        for item in os.listdir(self.path_to_temp_BloggerCorpus):
            if ".db" in item:
                if dbname not in item:
                    assert False



    # #@attr(status='stable')
    # @wipd
    # def test_export_to_json_from_reader_(self):
    #     real_fold = os.path.join(self.path_to_zas_rep_tools, "data/tests_data/Corpora/BloggerCorpus/xml")
    #     reader = Reader(self.txt_blogger_corpus_abs_path_to_hight_repetativ_subset_with_unicode, "txt", regex_template="blogger", logger_level=logging.ERROR)
    #     exporter = Exporter(reader.getlazy())

    #     exporter.tojson(real_fold, "blogger_corpus", rows_limit_in_file=100)





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







