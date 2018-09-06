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
import sure
import copy
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
import json
import csv
from collections import Counter, defaultdict


from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.classes.stats import Stats
from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.basetester import BaseTester
import  zas_rep_tools.src.utils.db_helper as db_helper



import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama



class TestZASstatsStats(BaseTester,unittest.TestCase):
    #_multiprocess_can_split_ = True
    _multiprocess_shared_  = True
    #@classmethod 
    def setUp(self):
        super(type(self), self).setUp()



        ########### EN ##############
        self.test_dict_row_en_1 = {u'star_constellation': u'lion', u'text': u'[[[["I", "PRP"], ["loved", "VBD"], ["it", "PRP"], [".", "symbol"]], ["positive", 0.7]], [[["But", "CC"], ["it", "PRP"], ["was", "VBD"], ["also", "RB"], ["verrrryyyyy", "JJ"], ["vvveRRRRRRrry", "NNP"], ["very", "RB"], ["piiiiiiiiity", "JJ"], ["pity", "NN"], ["pity", "NN"], ["piiitttyyy", "NN"], ["for", "IN"], ["me", "PRP"], ["......", "symbol"], [":-(((((", "EMOASC"], ["@real_trump", "mention"], ["#sheetlife", "hashtag"], ["#readytogo", "hashtag"], ["http://www.absurd.com", "URL"]], ["negative", -0.1875]]]', u'age': 37, u'working_area': u'IT', u'rowid': 1, u'gender': u'w', u'id': 1111}
        self.test_dict_row_en_2 = {u'star_constellation': u'lion', u'text': u'[[[["Tiny", "JJ"], ["model", "NN"], [",", "symbol"], ["but", "CC"], ["a", "DT"], ["big", "JJ"], ["big", "JJ"], ["big", "JJ"], ["explaaaaanation", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Riiiiiight", "UH"], ["?", "symbol"]], ["neutral", 0.0]], [[["What", "WP"], ["do", "VBP"], ["youuuuuu", "PRP"], ["think", "VB"], ["about", "IN"], ["it", "PRP"], ["????", "symbol"]], ["neutral", 0.0]]]', u'age': 35, u'working_area': u'Air Industry', u'rowid': 5, u'gender': u'w', u'id': 5555}


        ########## DE ###############
        self.test_dict_row_de_1 = {u'star_constellation': u'fish', u'text': u'[[[["Klitze", "NN"], ["kliiiitze", "VMFIN"], ["kleEEEEine", "NE"], ["kleinnne", "ADJA"], ["\\u00dcberaschung", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Trotzdem", "PAV"], ["hat", "VAFIN"], ["sie", "PPER"], ["mich", "PPER"], ["gl\\u00fccklich", "ADJD"], ["gemacht", "VVPP"], ["!", "symbol"], [":-))))", "EMOASC"], ["-)))", "EMOASC"]], ["positive", 0.5]]]', u'age': 23, u'working_area': u'Care', u'rowid': 8, u'gender': u'm', u'id': 8888}
        self.test_dict_row_de_2 = {u'star_constellation': u'aquarius', u'text': u'[[[["einen", "ART"], ["wundersch\\u00f6nen", "ADJA"], ["Taaaaaagggggg", "NN"], ["w\\u00fcnsche", "VVFIN"], ["ich", "PPER"], ["euch", "PRF"], [".", "symbol"]], ["neutral", 0.0]], [[["Genieeeeeeeeeeesst", "NN"], ["geniiiiiiiiiiiiist", "VVFIN"], ["das", "ART"], ["Leben", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Bleeeeeeeeibt", "NN"], ["bleeeeibt", "VVFIN"], ["Huuuuuuuuuuuungrig", "NN"], [".", "symbol"], ["\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00", "EMOIMG"], ["\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08", "EMOIMG"]], ["neutral", 0.0]]]', u'age': 22, u'working_area': u'Finance', u'rowid': 9, u'gender': u'w', u'id': 9999}
    

        self.docs_ids = {
            self.test_dict_row_en_1["id"]:self.test_dict_row_en_1,
            self.test_dict_row_en_2["id"]:self.test_dict_row_en_2,
            self.test_dict_row_de_1["id"]:self.test_dict_row_de_1,
            self.test_dict_row_de_2["id"]:self.test_dict_row_de_2,
            }

        self.gold_standard_data = {
                            "lower":{
                                    "repl":["rep_lower",""],
                                    "redu": [],
                                    },
                            }

        self.path_to_stats_test_data = "data/tests_data/stats/"



    #@classmethod 
    def tearDown(self):
        super(type(self), self).tearDown()


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
    def test_initialization_of_the_stats_instance_000(self):
        stats = Stats(mode=self.mode)
        stats.should.be.a(Stats)

        

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
        self.prj_folder()
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"


        stats = Stats(mode=self.mode)
        #stats = Corpus(logger_level=logging.DEBUG)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version)
   
        assert stats.exist()
   
    @attr(status='stable')
    #@wipd
    def test_new_encrypted_corpus_initialization_501(self):
        self.prj_folder()
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"


        stats = Stats(mode=self.mode)
        #stats = Corpus(logger_level=logging.DEBUG)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
   
        assert stats.exist()
        
        

    @attr(status='stable')
    #@wipd
    def test_open_plaintext_blogger_corpus_502(self):
        self.prj_folder()
        self.test_dbs()
        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"


        stats = Stats(mode=self.mode)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
  
        #p(stats.statsdb.get_all_attr("main"))
        stats.statsdb.get_all_attr("main")['name'].should.be.equal(name)
        #stats.statsdb.get_all_attr("main")['language'].should.be.equal(language)
        stats.statsdb.get_all_attr("main")['visibility'].should.be.equal(visibility)
        #stats.statsdb.get_all_attr("main")['platform_name'].should.be.equal(platform_name)
        stats.statsdb.get_all_attr("main")['typ'].should.be.equal(typ)
        stats.statsdb.get_all_attr("main")['id'].should.be.equal(stats_id)
        stats.statsdb.get_all_attr("main")['version'].should.be.equal(version)

        assert stats.exist()
   
    @attr(status='stable')
    #@wipdl
    def test_open_encrypted_twitter_corpus_503(self):
        self.prj_folder()
        self.test_dbs()
        name = self.configer.init_info_data["twitter"]["name"]
        language = self.configer.init_info_data["twitter"]["language"]
        visibility = self.configer.init_info_data["twitter"]["visibility"]
        platform_name = self.configer.init_info_data["twitter"]["platform_name"]
        license = self.configer.init_info_data["twitter"]["license"]
        template_name = self.configer.init_info_data["twitter"]["template_name"]
        version = self.configer.init_info_data["twitter"]["version"]
        source = self.configer.init_info_data["twitter"]["source"]
        encryption_key = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["twitter"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["twitter"]["id"]["stats"]
        typ= "stats"
        #p(encryption_key)

        stats = Stats(mode=self.mode)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_stats_de), encryption_key=encryption_key)
    

    
        stats.statsdb.get_all_attr("main")['name'].should.be.equal(name)
        #stats.statsdb.get_all_attr("main")['language'].should.be.equal(language)
        stats.statsdb.get_all_attr("main")['visibility'].should.be.equal(visibility)
        #stats.statsdb.get_all_attr("main")['platform_name'].should.be.equal(platform_name)
        stats.statsdb.get_all_attr("main")['typ'].should.be.equal(typ)
        stats.statsdb.get_all_attr("main")['id'].should.be.equal(stats_id)
        stats.statsdb.get_all_attr("main")['version'].should.be.equal(version)

        assert stats.exist()
   





###################    :550############################################ 
    #@attr(status='stable')
    #@wipd
    def test_single_stream_insert_550(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        p(list(corp.docs()))

        stats = Stats(mode=self.mode, force_cleaning=True)#, case_sensitiv=False)
        stats.corp = corp
        stats._corp_info = corp.info()
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        p(stats._add_context_columns("replications", 5,5))
        p(stats._add_context_columns("reduplications",5,5))
        #stats._add_context_columns("reduplications")
        p(stats.statsdb.col("replications"))
        # stats._compute(corp.docs(output="dict")) #, status_bar=True)
        # p(stats.statsdb.col("replications"))
        # #stats.insert(corp)
        # 
        #p(corp.additional_attr())
        #stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))



    ###################    :600############################################ 
    @attr(status='stable')
    #@wipd
    def test_extract_repl_lower_case_600(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()

        ## DE####

        ### ROW 1 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_de_1["text"]))
        #p(repl_free_text_container, "repl_free_text_container", c="m")
        #p([t[0] for i in json.loads(self.test_dict_row_de_1["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', [(u'i', 4, 2)], [(u'e', 5, 2)], [(u'n', 3, 4)], '', ''], ['', '', '', '', '', '', '', [(u')', 4, 2)], [(u')', 3, 1)]]])
        repl_free_text_container.should.be.equal([[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']])
        rle_for_repl_in_text_container.should.be.equal([['', u'kli^4tze', u'kle^5ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']])
        #repl_free_de_row_lowercased_1 = [[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]

        

        ### ROW 2 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_de_2["text"]) )
        
        # p([t[0] for i in json.loads(self.test_dict_row_de_2["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', [(u'a', 6, 1), (u'g', 6, 2)], '', '', '', ''], [[(u'e', 11, 4)], [(u'i', 13, 3)], '', '', ''], [[(u'e', 8, 2)], [(u'e', 4, 2)], [(u'u', 12, 1)], '', [(u'\U0001f600', 5, 0)], [(u'\U0001f308', 7, 0)]]])
        repl_free_text_container.should.be.equal([[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']])
        rle_for_repl_in_text_container.should.be.equal([['', '', u'ta^6g^6', '', '', '', ''], [u'genie^11s^2t', u'geni^13st', '', '', ''], [u'ble^8ibt', u'ble^4ibt', u'hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']])
        #repl_free_de_row_lowercased_2 = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]

        
        # ########### EN ##############

        ### ROW 1 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_en_1["text"]) )
        #p([t[0] for i in json.loads(self.test_dict_row_en_1["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', '', ''], ['', '', '', '', [(u'r', 4, 2), (u'y', 5, 3)], [(u'v', 3, 0), (u'r', 8, 2)], '', [(u'i', 9, 1)], '', '', [(u'i', 3, 1), (u't', 3, 2), (u'y', 3, 3)], '', '', [(u'.', 6, 0)], [(u'(', 5, 2)], '', '', '', '']])
        repl_free_text_container.should.be.equal([[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']])
        rle_for_repl_in_text_container.should.be.equal([['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3er^8y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']])
        #repl_free_en_row_lowercased_1 =    [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]

        
        ### ROW 2 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_en_2["text"]) )
        # p([t[0] for i in json.loads(self.test_dict_row_en_2["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', '', '', '', '', '', '', [(u'a', 5, 4)], ''], [[(u'i', 6, 1)], ''], ['', '', [(u'u', 6, 2)], '', '', '', [(u'?', 4, 0)]]])
        repl_free_text_container.should.be.equal([[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']])
        rle_for_repl_in_text_container.should.be.equal([['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']])
        #repl_free_en_row_lowercased_1 = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]

    



    @attr(status='stable')
    #@wipd
    def test_extract_repl_case_sensitiv_601(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()

        ### DE####

        ### ROW 1 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_de_1["text"]) )
        # p([t[0] for i in json.loads(self.test_dict_row_de_1["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', [(u'i', 4, 2)], [(u'E', 4, 3)], [(u'n', 3, 4)], '', ''], ['', '', '', '', '', '', '', [(u')', 4, 2)], [(u')', 3, 1)]]])
        repl_free_text_container.should.be.equal([[u'Klitze', u'klitze', u'kleEine', u'kleine', u'\xdcberaschung', u'.'], [u'Trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']])
        rle_for_repl_in_text_container.should.be.equal([['', u'kli^4tze', u'kleE^4ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']])
        
        ### ROW 2 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_de_2["text"]) )
        # p([t[0] for i in json.loads(self.test_dict_row_de_2["text"]) for t in i[0]])
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', [(u'a', 6, 1), (u'g', 6, 2)], '', '', '', ''], [[(u'e', 11, 4)], [(u'i', 13, 3)], '', '', ''], [[(u'e', 8, 2)], [(u'e', 4, 2)], [(u'u', 12, 1)], '', [(u'\U0001f600', 5, 0)], [(u'\U0001f308', 7, 0)]]])
        repl_free_text_container.should.be.equal([[u'einen', u'wundersch\xf6nen', u'Tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'Geniest', u'genist', u'das', u'Leben', u'.'], [u'Bleibt', u'bleibt', u'Hungrig', u'.', u'\U0001f600', u'\U0001f308']])
        rle_for_repl_in_text_container.should.be.equal([['', '', u'Ta^6g^6', '', '', '', ''], [u'Genie^11s^2t', u'geni^13st', '', '', ''], [u'Ble^8ibt', u'ble^4ibt', u'Hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']])
        

        # ########### EN ##############

        ### ROW 1 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_en_1["text"]) )
        # p([t[0] for i in json.loads(self.test_dict_row_en_1["text"]) for t in i[0]]) #[u'I', u'loved', u'it', u'.', u'But', u'it', u'was', u'also', u'verrrryyyyy', u'vvveRRRRRRrry', u'very', u'piiiiiiiiity', u'pity', u'pity', u'piiitttyyy', u'for', u'me', u'......', u':-(((((', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com']
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', '', ''], ['', '', '', '', [(u'r', 4, 2), (u'y', 5, 3)], [(u'v', 3, 0), (u'R', 6, 2)], '', [(u'i', 9, 1)], '', '', [(u'i', 3, 1), (u't', 3, 2), (u'y', 3, 3)], '', '', [(u'.', 6, 0)], [(u'(', 5, 2)], '', '', '', '']])
        repl_free_text_container.should.be.equal([[u'I', u'loved', u'it', u'.'], [u'But', u'it', u'was', u'also', u'very', u'veRry', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']])
        rle_for_repl_in_text_container.should.be.equal([['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3eR^6r^2y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']])
        
        ### ROW 2 ###
        extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container = stats.extract_replications(json.loads(self.test_dict_row_en_2["text"]) )
        # p([t[0] for i in json.loads(self.test_dict_row_en_2["text"]) for t in i[0]]) #[u'Tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explaaaaanation', u'.', u'Riiiiiight', u'?', u'What', u'do', u'youuuuuu', u'think', u'about', u'it', u'????']
        # p((len(extracted_repl_in_text_container),extracted_repl_in_text_container), "extracted_repl_in_text_container")
        # p((len(repl_free_text_container),repl_free_text_container), "repl_free_text_container")
        # p((len(rle_for_repl_in_text_container),rle_for_repl_in_text_container), "rle_for_repl_in_text_container")

        extracted_repl_in_text_container.should.be.equal([['', '', '', '', '', '', '', '', [(u'a', 5, 4)], ''], [[(u'i', 6, 1)], ''], ['', '', [(u'u', 6, 2)], '', '', '', [(u'?', 4, 0)]]])
        repl_free_text_container.should.be.equal([[u'Tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'Right', u'?'], [u'What', u'do', u'you', u'think', u'about', u'it', u'?']])
        rle_for_repl_in_text_container.should.be.equal([['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'Ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']])


  



    @attr(status='stable')
    #@wipd
    def test_insert_repl_into_db_lower_case_602(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)


        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))






        ## DE####


        ### ROW 1 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()


        rle_for_repl_in_text_container = [['', u'kli^4tze', u'kle^5ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']]
        extracted_repl_in_text_container = [['', [(u'i', 4, 2)], [(u'e', 5, 2)], [(u'n', 3, 4)], '', ''], ['', '', '', '', '', '', '', [(u')', 4, 2)], [(u')', 3, 1)]]]
        repl_free_text_container = [[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        redu_free_text_container = [[(u'klitze', {u'klitze': 1, u'kli^4tze': 1}), (u'kleine', {u'kle^5ine': 1, u'klein^3e': 1}), u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        mapping_redu = [[0, 2, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
        stats.insert_repl_into_db(self.test_dict_row_de_1,json.loads(self.test_dict_row_de_1["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu,)
        #p(list(stats.statsdb.getall("replications")))
        list(stats.statsdb.getall("replications")).should.be.equal([(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])



        # # ### ROW 2 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        rle_for_repl_in_text_container = [['', '', u'ta^6g^6', '', '', '', ''], [u'genie^11s^2t', u'geni^13st', '', '', ''], [u'ble^8ibt', u'ble^4ibt', u'hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']]
        extracted_repl_in_text_container = [['', '', [(u'a', 6, 1), (u'g', 6, 2)], '', '', '', ''], [[(u'e', 11, 4)], [(u'i', 13, 3)], '', '', ''], [[(u'e', 8, 2)], [(u'e', 4, 2)], [(u'u', 12, 1)], '', [(u'\U0001f600', 5, 0)], [(u'\U0001f308', 7, 0)]]]
        repl_free_text_container = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        redu_free_text_container = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [(u'bleibt', {u'ble^4ibt': 1, u'ble^8ibt': 1}), u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        mapping_redu = [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5]]
        stats.insert_repl_into_db(self.test_dict_row_de_2,json.loads(self.test_dict_row_de_2["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
        #p(list(stats.statsdb.getall("replications")))
        list(stats.statsdb.getall("replications")).should.be.equal([(1, 9999, u'[0, 2]', u'ta^6g^6', u'tag', u'NN', u'["neutral", 0.0]', u'a', u'[]', 6, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]'), (2, 9999, u'[0, 2]', u'ta^6g^6', u'tag', u'NN', u'["neutral", 0.0]', u'g', u'[]', 6, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]'), (3, 9999, u'[1, 0]', u'genie^11s^2t', u'geniest', u'NN', u'["neutral", 0.0]', u'e', u'[]', 11, 4, u'tag', u'["NN"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]'), (4, 9999, u'[1, 1]', u'geni^13st', u'genist', u'VVFIN', u'["neutral", 0.0]', u'i', u'[]', 13, 3, u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]'), (5, 9999, u'[2, 0]', u'ble^8ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 8, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]'), (6, 9999, u'[2, 1]', u'ble^4ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 4, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]'), (7, 9999, u'[2, 2]', u'hu^12ngrig', u'hungrig', u'NN', u'["neutral", 0.0]', u'u', u'[]', 12, 1, u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]'), (8, 9999, u'[2, 4]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f600', u'[]', 5, 0, u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (9, 9999, u'[2, 5]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f308', u'[]', 7, 0, u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])


        
        # # ########### EN ##############

        # # ### ROW 1 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        rle_for_repl_in_text_container = [['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3er^8y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']]
        extracted_repl_in_text_container = [['', '', '', ''], ['', '', '', '', [(u'r', 4, 2), (u'y', 5, 3)], [(u'v', 3, 0), (u'r', 8, 2)], '', [(u'i', 9, 1)], '', '', [(u'i', 3, 1), (u't', 3, 2), (u'y', 3, 3)], '', '', [(u'.', 6, 0)], [(u'(', 5, 2)], '', '', '', '']]
        repl_free_text_container = [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        redu_free_text_container =[[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', (u'very', {u'very': 1, u'ver^4y^5': 1, u'v^3er^8y': 1}), (u'pity', {u'pity': 2, u'pi^3t^3y^3': 1, u'pi^9ty': 1}), u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        mapping_redu = [[0, 1, 2, 3], [0, 1, 2, 3, 4, 7, 11, 12, 13, 14, 15, 16, 17, 18]]
        stats.insert_repl_into_db(self.test_dict_row_en_1,json.loads(self.test_dict_row_en_1["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
        #p(list(stats.statsdb.getall("replications")))
        list(stats.statsdb.getall("replications")).should.be.equal([(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]')])


        
        # # ### ROW 2 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        rle_for_repl_in_text_container = [['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']]
        extracted_repl_in_text_container = [['', '', '', '', '', '', '', '', [(u'a', 5, 4)], ''], [[(u'i', 6, 1)], ''], ['', '', [(u'u', 6, 2)], '', '', '', [(u'?', 4, 0)]]]
        repl_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        redu_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', (u'big', {u'big': 3}), u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        mapping_redu = [[0, 1, 2, 3, 4, 5, 8, 9], [0, 1], [0, 1, 2, 3, 4, 5, 6]]
        stats.insert_repl_into_db(self.test_dict_row_en_2,json.loads(self.test_dict_row_en_2["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
        #p(list(stats.statsdb.getall("replications")))
        list(stats.statsdb.getall("replications")).should.be.equal([(1, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (2, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (3, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]'), (4, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])



        ########################
        ####### many_rows ######
        ########################
        # # ### ROW 1 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        rle_for_repl_in_text_container = [['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3er^8y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']]
        extracted_repl_in_text_container = [['', '', '', ''], ['', '', '', '', [(u'r', 4, 2), (u'y', 5, 3)], [(u'v', 3, 0), (u'r', 8, 2)], '', [(u'i', 9, 1)], '', '', [(u'i', 3, 1), (u't', 3, 2), (u'y', 3, 3)], '', '', [(u'.', 6, 0)], [(u'(', 5, 2)], '', '', '', '']]
        repl_free_text_container = [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        redu_free_text_container = [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', (u'very', {u'very': 1, u'ver^4y^5': 1, u'v^3er^8y': 1}), (u'pity', {u'pity': 2, u'pi^3t^3y^3': 1, u'pi^9ty': 1}), u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        mapping_redu = [[0, 1, 2, 3], [0, 1, 2, 3, 4, 7, 11, 12, 13, 14, 15, 16, 17, 18]]
        stats.insert_repl_into_db(self.test_dict_row_en_1,json.loads(self.test_dict_row_en_1["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
        #p(list(stats.statsdb.getall("replications")))
        #list(stats.statsdb.getall("replications")).should.be.equal([(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', 4, 2, u'.', u'symbol', u'but', u'CC', u'it', u'PRP', u'was', u'VBD', u'also', u'RB', u'very', u'NNP', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', 5, 3, u'.', u'symbol', u'but', u'CC', u'it', u'PRP', u'was', u'VBD', u'also', u'RB', u'very', u'NNP', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'NNP', u'["negative", -0.1875]', u'v', 3, 0, u'but', u'CC', u'it', u'PRP', u'was', u'VBD', u'also', u'RB', u'very', u'JJ', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN', u'pity', u'NN'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'NNP', u'["negative", -0.1875]', u'r', 8, 2, u'but', u'CC', u'it', u'PRP', u'was', u'VBD', u'also', u'RB', u'very', u'JJ', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN', u'pity', u'NN'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', 9, 1, u'was', u'VBD', u'also', u'RB', u'very', u'JJ', u'very', u'NNP', u'very', u'RB', u'pity', u'NN', u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'NN', u'["negative", -0.1875]', u'i', 3, 1, u'very', u'NNP', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP', u'.', u'symbol', u':-(', u'EMOASC', u'@real_trump', u'mention'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'NN', u'["negative", -0.1875]', u't', 3, 2, u'very', u'NNP', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP', u'.', u'symbol', u':-(', u'EMOASC', u'@real_trump', u'mention'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'NN', u'["negative", -0.1875]', u'y', 3, 3, u'very', u'NNP', u'very', u'RB', u'pity', u'JJ', u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP', u'.', u'symbol', u':-(', u'EMOASC', u'@real_trump', u'mention'), (9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', 6, 0, u'pity', u'NN', u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP', u':-(', u'EMOASC', u'@real_trump', u'mention', u'#shetlife', u'hashtag', u'#readytogo', u'hashtag', u'http://www.absurd.com', u'URL'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', 5, 2, u'pity', u'NN', u'pity', u'NN', u'for', u'IN', u'me', u'PRP', u'.', u'symbol', u'@real_trump', u'mention', u'#shetlife', u'hashtag', u'#readytogo', u'hashtag', u'http://www.absurd.com', u'URL', u'[]', u'[]')])


        # # ### ROW 2 ###
        rle_for_repl_in_text_container = [['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']]
        extracted_repl_in_text_container = [['', '', '', '', '', '', '', '', [(u'a', 5, 4)], ''], [[(u'i', 6, 1)], ''], ['', '', [(u'u', 6, 2)], '', '', '', [(u'?', 4, 0)]]]
        repl_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        redu_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', (u'big', {u'big': 3}), u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        mapping_redu = [[0, 1, 2, 3, 4, 5, 8, 9], [0, 1], [0, 1, 2, 3, 4, 5, 6]]
        stats.insert_repl_into_db(self.test_dict_row_en_2,json.loads(self.test_dict_row_en_2["text"]),extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
        #p(list(stats.statsdb.getall("replications")))
        stats.statsdb.getall("replications").should.be.equal([(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]'), (11, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (12, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (13, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]'), (14, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])







    @attr(status='stable')
    #@wipd
    def test_extract_redu_lower_case_603(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()



        ## DE####

        ### ROW 1 ###
        #p(json.loads(self.test_dict_row_de_1["text"]), "text_elem")
        #text_elem = [[ [[t[0].lower(), t[1]] for t in s[0] ], s[1]] for s in json.loads(self.test_dict_row_de_1["text"]) ]
        #p(text_elem, "text_elem")
        repl_free_de_row_lowercased_1 = [[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        rle_for_repl_in_text_container = [['', u'kli^4tze', u'kle^5ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications(repl_free_de_row_lowercased_1,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_de_1["text"]) for t in i[0]])
        # p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu, "mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[{'start_index_in_orig': 0, 'length': 2, 'word': u'klitze', 'index_in_redu_free': 0}, {'start_index_in_orig': 2, 'length': 2, 'word': u'kleine', 'index_in_redu_free': 1}], []])
        redu_free_text_container.should.be.equal([[(u'klitze', {u'klitze': 1, u'kli^4tze': 1}), (u'kleine', {u'kle^5ine': 1, u'klein^3e': 1}), u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']])
        mapping_redu.should.be.equal([[0, 2, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]])
        

        # ### ROW 2 ###
        #text_elem = [[ [[t[0].lower(), t[1]] for t in s[0] ], s[1]] for s in json.loads(self.test_dict_row_de_1["text"]) ]
        repl_free_de_row_lowercased_2 = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        rle_for_repl_in_text_container = [['', '', u'ta^6g^6', '', '', '', ''], [u'genie^11s^2t', u'geni^13st', '', '', ''], [u'ble^8ibt', u'ble^4ibt', u'hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications(repl_free_de_row_lowercased_2,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_de_2["text"]) for t in i[0]])
        # #p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu,"mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[], [], [{'start_index_in_orig': 0, 'length': 2, 'word': u'bleibt', 'index_in_redu_free': 0}]])
        redu_free_text_container.should.be.equal([[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [(u'bleibt', {u'ble^4ibt': 1, u'ble^8ibt': 1}), u'hungrig', u'.', u'\U0001f600', u'\U0001f308']])
        mapping_redu.should.be.equal([[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5]])
        
        # # # ########### EN ##############


        # ### ROW 1 ###
        repl_free_en_row_lowercased_1 =    [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        rle_for_repl_in_text_container = [['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3er^8y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications(repl_free_en_row_lowercased_1,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_en_1["text"]) for t in i[0]])
        # #p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu,"mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[], [{'start_index_in_orig': 4, 'length': 3, 'word': u'very', 'index_in_redu_free': 4}, {'start_index_in_orig': 7, 'length': 4, 'word': u'pity', 'index_in_redu_free': 5}]])
        redu_free_text_container.should.be.equal([[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', (u'very', {u'very': 1, u'ver^4y^5': 1, u'v^3er^8y': 1}), (u'pity', {u'pity': 2, u'pi^3t^3y^3': 1, u'pi^9ty': 1}), u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']])
        mapping_redu.should.be.equal([[0, 1, 2, 3], [0, 1, 2, 3, 4, 7, 11, 12, 13, 14, 15, 16, 17, 18]])
        
        # ### ROW 2 ###
        repl_free_en_row_lowercased_2 = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        rle_for_repl_in_text_container =  [['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications(repl_free_en_row_lowercased_2,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_en_2["text"]) for t in i[0]])
        # #p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu,"mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[{'start_index_in_orig': 5, 'length': 3, 'word': u'big', 'index_in_redu_free': 5}], [], []])
        redu_free_text_container.should.be.equal([[u'tiny', u'model', u',', u'but', u'a', (u'big', {u'big': 3}), u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']])
        mapping_redu.should.be.equal([[0, 1, 2, 3, 4, 5, 8, 9], [0, 1], [0, 1, 2, 3, 4, 5, 6]])






    @attr(status='stable')
    #@wipd
    def test_extract_redu_case_sensitive_604(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()

        ### DE####

        ### ROW 1 ###
        repl_free_de_row_case_sensitive_1 = [[u'Klitze', u'klitze', u'kleEine', u'kleine', u'\xdcberaschung', u'.'], [u'Trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        rle_for_repl_in_text_container = [['', u'kli^4tze', u'kleE^4ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications( repl_free_de_row_case_sensitive_1,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_de_1["text"]) for t in i[0]])
        #p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu, "mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[], []])
        redu_free_text_container.should.be.equal([[u'Klitze', u'klitze', u'kleEine', u'kleine', u'\xdcberaschung', u'.'], [u'Trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']])
        mapping_redu.should.be.equal([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]])
        

        ### ROW 2 ###
        repl_free_de_row_case_sensitive_2 = [[u'einen', u'wundersch\xf6nen', u'Tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'Geniest', u'genist', u'das', u'Leben', u'.'], [u'Bleibt', u'bleibt', u'Hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        rle_for_repl_in_text_container = [['', '', u'Ta^6g^6', '', '', '', ''], [u'Genie^11s^2t', u'geni^13st', '', '', ''], [u'Ble^8ibt', u'ble^4ibt', u'Hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications( repl_free_de_row_case_sensitive_2,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_de_2["text"]) for t in i[0]])
        #p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu, "mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[], [], []])
        redu_free_text_container.should.be.equal([[u'einen', u'wundersch\xf6nen', u'Tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'Geniest', u'genist', u'das', u'Leben', u'.'], [u'Bleibt', u'bleibt', u'Hungrig', u'.', u'\U0001f600', u'\U0001f308']])
        mapping_redu.should.be.equal([[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5]])
        
        # # # ########### EN ##############


        ### ROW 1 ###
        repl_free_en_row_case_sensitive_1 = [[u'I', u'loved', u'it', u'.'], [u'But', u'it', u'was', u'also', u'very', u'veRry', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        rle_for_repl_in_text_container = [['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3eR^6r^2y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications( repl_free_en_row_case_sensitive_1,rle_for_repl_in_text_container)


        #p([t[0] for i in json.loads(self.test_dict_row_en_1["text"]) for t in i[0]])
        # p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu, "mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[], [{'start_index_in_orig': 7, 'length': 4, 'word': u'pity', 'index_in_redu_free': 7}]])
        redu_free_text_container.should.be.equal([[u'I', u'loved', u'it', u'.'], [u'But', u'it', u'was', u'also', u'very', u'veRry', u'very', (u'pity', {u'pity': 2, u'pi^3t^3y^3': 1, u'pi^9ty': 1}), u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']])
        mapping_redu.should.be.equal([[0, 1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 18]])
        
        ### ROW 2 ###
        repl_free_en_row_case_sensitive_2 = [[u'Tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'Right', u'?'], [u'What', u'do', u'you', u'think', u'about', u'it', u'?']]
        rle_for_repl_in_text_container = [['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'Ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']]
        extracted_redu_in_text_container, redu_free_text_container,mapping_redu = stats.extract_reduplications( repl_free_en_row_case_sensitive_2,rle_for_repl_in_text_container)

        #p([t[0] for i in json.loads(self.test_dict_row_en_2["text"]) for t in i[0]])
        # p((len(extracted_redu_in_text_container),extracted_redu_in_text_container), "extracted_redu_in_text_container")
        #p((len(redu_free_text_container),redu_free_text_container), "redu_free_text_container")
        #p(mapping_redu, "mapping_redu")

        extracted_redu_in_text_container.should.be.equal([[{'start_index_in_orig': 5, 'length': 3, 'word': u'big', 'index_in_redu_free': 5}], [], []])
        redu_free_text_container.should.be.equal([[u'Tiny', u'model', u',', u'but', u'a', (u'big', {u'big': 3}), u'explanation', u'.'], [u'Right', u'?'], [u'What', u'do', u'you', u'think', u'about', u'it', u'?']])
        mapping_redu.should.be.equal([[0, 1, 2, 3, 4, 5, 8, 9], [0, 1], [0, 1, 2, 3, 4, 5, 6]])

        
    # def compute_baseline_1(self, redu_free_text_container, context_right=5, context_left=5):
    #     inp_token_list = [token for sent in redu_free_text_container for token in sent]
    #     computed_baseline  = []
    #     ngramm_lenght = context_right+1+context_left
    #     for n in xrange(1,ngramm_lenght+1):
    #         computed_baseline += [tuple(inp_token_list[i:i+n]) for i in xrange(len(inp_token_list)-n+1)]
    #     return computed_baseline







    @attr(status='stable')
    #@wipd
    def test_insert_redu_into_db_lower_case_605(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"



        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))






        ### DE####

        ### ROW 1 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()


        repl_free_de_row_lowercased_1 = [[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        
        #p([t[0] for i in json.loads(self.test_dict_row_de_1["text"]) for t in i[0]])
        #p(self.test_dict_row_de_1["text"])
        extracted_redu_in_text_container = [[{'start_index_in_orig': 0, 'length': 2, 'word': u'klitze', 'index_in_redu_free': 0}, {'start_index_in_orig': 2, 'length': 2, 'word': u'kleine', 'index_in_redu_free': 1}], []]
        redu_free_text_container = [[(u'klitze', {u'klitze': 1, u'kli^4tze': 1}), (u'kleine', {u'kle^5ine': 1, u'klein^3e': 1}), u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        rle_for_repl_in_text_container = [['', u'kli^4tze', u'kle^5ine', u'klein^3e', '', ''], ['', '', '', '', '', '', '', u':-)^4', u'-)^3']]
        repl_free_text_container = [[u'klitze', u'klitze', u'kleine', u'kleine', u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        mapping_redu = [[0, 2, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
        stats.insert_redu_into_db(self.test_dict_row_de_1,json.loads(self.test_dict_row_de_1["text"]),extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container, repl_free_text_container,mapping_redu)
        
        #p(list(stats.statsdb.getall("reduplications")))
        inserted_columns =list(stats.statsdb.getall("reduplications"))
        right_output = [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]
        inserted_columns.should.be.equal(right_output)


        # ### ROW 2 ###

        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        repl_free_de_row_lowercased_2 = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
    
        #p([t[0] for i in json.loads(self.test_dict_row_de_2["text"]) for t in i[0]], c="r")
        #p(json.loads(self.test_dict_row_de_2["text"]))
        extracted_redu_in_text_container = [[], [], [{'start_index_in_orig': 0, 'length': 2, 'word': u'bleibt', 'index_in_redu_free': 0}]]
        redu_free_text_container = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [(u'bleibt', {u'ble^4ibt': 1, u'ble^8ibt': 1}), u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        rle_for_repl_in_text_container = [['', '', u'ta^6g^6', '', '', '', ''], [u'genie^11s^2t', u'geni^13st', '', '', ''], [u'ble^8ibt', u'ble^4ibt', u'hu^12ngrig', '', u'\U0001f600^5', u'\U0001f308^7']]
        repl_free_text_container = [[u'einen', u'wundersch\xf6nen', u'tag', u'w\xfcnsche', u'ich', u'euch', u'.'], [u'geniest', u'genist', u'das', u'leben', u'.'], [u'bleibt', u'bleibt', u'hungrig', u'.', u'\U0001f600', u'\U0001f308']]
        mapping_redu = [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5]]
        stats.insert_redu_into_db(self.test_dict_row_de_1,json.loads(self.test_dict_row_de_2["text"]),extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container, repl_free_text_container,mapping_redu)

        #p(list(stats.statsdb.getall("reduplications")))
        inserted_columns =list(stats.statsdb.getall("reduplications"))
        right_output = [(1, 8888, 2, u'bleibt', u'[2, 0]', u'NN', u'{"ble^4ibt": 1, "ble^8ibt": 1}', u'["neutral", 0.0]', u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]')]
        inserted_columns.should.be.equal(right_output)





        
        # ########### EN ##############
        # ### ROW 1 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        repl_free_en_row_lowercased_1 =    [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]

        #p([t[0] for i in json.loads(self.test_dict_row_en_1["text"]) for t in i[0]])
        #p(json.loads(self.test_dict_row_en_1["text"]))

        extracted_redu_in_text_container = [[], [{'start_index_in_orig': 4, 'length': 3, 'word': u'very', 'index_in_redu_free': 4}, {'start_index_in_orig': 7, 'length': 4, 'word': u'pity', 'index_in_redu_free': 5}]]
        redu_free_text_container = [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', (u'very', {u'very': 1, u'ver^4y^5': 1, u'v^3er^8y': 1}), (u'pity', {u'pity': 2, u'pi^3t^3y^3': 1, u'pi^9ty': 1}), u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        rle_for_repl_in_text_container = [['', '', '', ''], ['', '', '', '', u'ver^4y^5', u'v^3er^8y', '', u'pi^9ty', '', '', u'pi^3t^3y^3', '', '', u'.^6', u':-(^5', '', '', '', '']]
        repl_free_text_container =[[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'very', u'very', u'pity', u'pity', u'pity', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com']]
        mapping_redu = [[0, 1, 2, 3], [0, 1, 2, 3, 4, 7, 11, 12, 13, 14, 15, 16, 17, 18]]
        stats.insert_redu_into_db(self.test_dict_row_en_1,json.loads(self.test_dict_row_en_1["text"]),extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container,repl_free_text_container,mapping_redu)
        
        #p(list(stats.statsdb.getall("reduplications")))
        inserted_columns =list(stats.statsdb.getall("reduplications"))
        right_output = [(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')]
        inserted_columns.should.be.equal(right_output)




        # ### ROW 2 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()


        repl_free_en_row_lowercased_2 = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        

        #p([t[0] for i in json.loads(self.test_dict_row_en_2["text"]) for t in i[0]])
        #p(json.loads(self.test_dict_row_en_2["text"]))
        extracted_redu_in_text_container = [[{'start_index_in_orig': 5, 'length': 3, 'word': u'big', 'index_in_redu_free': 5}], [], []]
        redu_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', (u'big', {u'big': 3}), u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        rle_for_repl_in_text_container = [['', '', '', '', '', '', '', '', u'expla^5nation', ''], [u'ri^6ght', ''], ['', '', u'you^6', '', '', '', u'?^4']]
        repl_free_text_container = [[u'tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explanation', u'.'], [u'right', u'?'], [u'what', u'do', u'you', u'think', u'about', u'it', u'?']]
        mapping_redu = [[0, 1, 2, 3, 4, 5, 8, 9], [0, 1], [0, 1, 2, 3, 4, 5, 6]]
        stats.insert_redu_into_db(self.test_dict_row_en_2,json.loads(self.test_dict_row_en_2["text"]),extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container, repl_free_text_container,mapping_redu)
        
        #p(list(stats.statsdb.getall("reduplications")))
        inserted_columns =list(stats.statsdb.getall("reduplications"))
        right_output = [(1, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')]
        inserted_columns.should.be.equal(right_output)








    @attr(status='stable')
    #@wipd
    def test_compute_baseline_lowercased_606(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()



        # ##### FAKE SENT 1 #######
        inp = [[u'klitze', u'kleine', u'\xfcberaschung', u'.']]
        extracted_redu_in_text_container = [[{}]]
        #assert set(stats.compute_baseline(inp)) == set(self.compute_baseline_1(inp))
        #p( stats.compute_baseline(inp,extracted_redu_in_text_container))
        stats.compute_baseline(inp,extracted_redu_in_text_container).should.be.equal([(u'klitze',), (u'kleine',), (u'\xfcberaschung',), (u'.',), (u'klitze', u'kleine'), (u'kleine', u'\xfcberaschung'), (u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung'), (u'kleine', u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung', u'.')])


        # # ##### FAKE SENT 2#######
        inp = [[u'1', u'2', u'3', u'4', u'5', u'😂', u'🧑🏻']]
        extracted_redu_in_text_container = [[{}]]
        #assert set(stats.compute_baseline(inp)) == set(self.compute_baseline_1(inp))
        #p( stats.compute_baseline(inp))
        stats.compute_baseline(inp,extracted_redu_in_text_container).should.be.equal([(u'1',), (u'2',), (u'3',), (u'4',), (u'5',), (u'\U0001f602',), (u'\U0001f9d1\U0001f3fb',), (u'1', u'2'), (u'2', u'3'), (u'3', u'4'), (u'4', u'5'), (u'5', u'\U0001f602'), (u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3'), (u'2', u'3', u'4'), (u'3', u'4', u'5'), (u'4', u'5', u'\U0001f602'), (u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4'), (u'2', u'3', u'4', u'5'), (u'3', u'4', u'5', u'\U0001f602'), (u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4', u'5'), (u'2', u'3', u'4', u'5', u'\U0001f602'), (u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4', u'5', u'\U0001f602'), (u'2', u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb')])



        # ### DE####

        ## ROW 1 ###
        inp = [[(u'klitze', {u'klitze': 1, u'kli^4tze': 1}), (u'kleine', {u'kle^5ine': 1, u'klein^3e': 1}), u'\xfcberaschung', u'.'], [u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)']]
        extracted_redu_in_text_container = [[{'start_index_in_orig': 0, 'length': 2, 'word': u'klitze', 'index_in_redu_free': 0}, {'start_index_in_orig': 2, 'length': 2, 'word': u'kleine', 'index_in_redu_free': 1}], []]
        #p( stats.compute_baseline(inp,extracted_redu_in_text_container))
        stats.compute_baseline(inp,extracted_redu_in_text_container).should.be.equal([(u'klitze',), (u'kleine',), (u'\xfcberaschung',), (u'.',), (u'trotzdem',), (u'hat',), (u'sie',), (u'mich',), (u'gl\xfccklich',), (u'gemacht',), (u'!',), (u':-)',), (u'-)',), (u'klitze', u'kleine'), (u'kleine', u'\xfcberaschung'), (u'\xfcberaschung', u'.'), (u'.', u'trotzdem'), (u'trotzdem', u'hat'), (u'hat', u'sie'), (u'sie', u'mich'), (u'mich', u'gl\xfccklich'), (u'gl\xfccklich', u'gemacht'), (u'gemacht', u'!'), (u'!', u':-)'), (u':-)', u'-)'), (u'klitze', u'kleine', u'\xfcberaschung'), (u'kleine', u'\xfcberaschung', u'.'), (u'\xfcberaschung', u'.', u'trotzdem'), (u'.', u'trotzdem', u'hat'), (u'trotzdem', u'hat', u'sie'), (u'hat', u'sie', u'mich'), (u'sie', u'mich', u'gl\xfccklich'), (u'mich', u'gl\xfccklich', u'gemacht'), (u'gl\xfccklich', u'gemacht', u'!'), (u'gemacht', u'!', u':-)'), (u'!', u':-)', u'-)'), (u'klitze', u'kleine', u'\xfcberaschung', u'.'), (u'kleine', u'\xfcberaschung', u'.', u'trotzdem'), (u'\xfcberaschung', u'.', u'trotzdem', u'hat'), (u'.', u'trotzdem', u'hat', u'sie'), (u'trotzdem', u'hat', u'sie', u'mich'), (u'hat', u'sie', u'mich', u'gl\xfccklich'), (u'sie', u'mich', u'gl\xfccklich', u'gemacht'), (u'mich', u'gl\xfccklich', u'gemacht', u'!'), (u'gl\xfccklich', u'gemacht', u'!', u':-)'), (u'gemacht', u'!', u':-)', u'-)'), (u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem'), (u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'), (u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie'), (u'.', u'trotzdem', u'hat', u'sie', u'mich'), (u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich'), (u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht'), (u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!'), (u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)'), (u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)'), (u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'), (u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie'), (u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie', u'mich'), (u'.', u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich'), (u'trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht'), (u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!'), (u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)'), (u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-)', u'-)'), (u'klitze',), (u'kleine',)])


        # # # ########### EN ##############


        # ### ROW 1 ###
        inp = [[u'i', u'loved', u'it', u'.'], [u'but', u'it', u'was', u'also', u'very', u'pity', u'for', u'me', u'.', u':-(', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com']]
        extracted_redu_in_text_container = [[], [{'start_index_in_orig': 4, 'length': 3, 'word': u'very', 'index_in_redu_free': 4}, {'start_index_in_orig': 7, 'length': 4, 'word': u'pity', 'index_in_redu_free': 5}]]
        #p(stats.compute_baseline(inp,extracted_redu_in_text_container))
        stats.compute_baseline(inp,extracted_redu_in_text_container).should.be.equal([(u'i',), (u'loved',), (u'it',), (u'.',), (u'but',), (u'it',), (u'was',), (u'also',), (u'very',), (u'pity',), (u'for',), (u'me',), (u'.',), (u':-(',), (u'@real_trump',), (u'#sheetlife',), (u'#readytogo',), (u'http://www.absurd.com',), (u'i', u'loved'), (u'loved', u'it'), (u'it', u'.'), (u'.', u'but'), (u'but', u'it'), (u'it', u'was'), (u'was', u'also'), (u'also', u'very'), (u'very', u'pity'), (u'pity', u'for'), (u'for', u'me'), (u'me', u'.'), (u'.', u':-('), (u':-(', u'@real_trump'), (u'@real_trump', u'#sheetlife'), (u'#sheetlife', u'#readytogo'), (u'#readytogo', u'http://www.absurd.com'), (u'i', u'loved', u'it'), (u'loved', u'it', u'.'), (u'it', u'.', u'but'), (u'.', u'but', u'it'), (u'but', u'it', u'was'), (u'it', u'was', u'also'), (u'was', u'also', u'very'), (u'also', u'very', u'pity'), (u'very', u'pity', u'for'), (u'pity', u'for', u'me'), (u'for', u'me', u'.'), (u'me', u'.', u':-('), (u'.', u':-(', u'@real_trump'), (u':-(', u'@real_trump', u'#sheetlife'), (u'@real_trump', u'#sheetlife', u'#readytogo'), (u'#sheetlife', u'#readytogo', u'http://www.absurd.com'), (u'i', u'loved', u'it', u'.'), (u'loved', u'it', u'.', u'but'), (u'it', u'.', u'but', u'it'), (u'.', u'but', u'it', u'was'), (u'but', u'it', u'was', u'also'), (u'it', u'was', u'also', u'very'), (u'was', u'also', u'very', u'pity'), (u'also', u'very', u'pity', u'for'), (u'very', u'pity', u'for', u'me'), (u'pity', u'for', u'me', u'.'), (u'for', u'me', u'.', u':-('), (u'me', u'.', u':-(', u'@real_trump'), (u'.', u':-(', u'@real_trump', u'#sheetlife'), (u':-(', u'@real_trump', u'#sheetlife', u'#readytogo'), (u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com'), (u'i', u'loved', u'it', u'.', u'but'), (u'loved', u'it', u'.', u'but', u'it'), (u'it', u'.', u'but', u'it', u'was'), (u'.', u'but', u'it', u'was', u'also'), (u'but', u'it', u'was', u'also', u'very'), (u'it', u'was', u'also', u'very', u'pity'), (u'was', u'also', u'very', u'pity', u'for'), (u'also', u'very', u'pity', u'for', u'me'), (u'very', u'pity', u'for', u'me', u'.'), (u'pity', u'for', u'me', u'.', u':-('), (u'for', u'me', u'.', u':-(', u'@real_trump'), (u'me', u'.', u':-(', u'@real_trump', u'#sheetlife'), (u'.', u':-(', u'@real_trump', u'#sheetlife', u'#readytogo'), (u':-(', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com'), (u'i', u'loved', u'it', u'.', u'but', u'it'), (u'loved', u'it', u'.', u'but', u'it', u'was'), (u'it', u'.', u'but', u'it', u'was', u'also'), (u'.', u'but', u'it', u'was', u'also', u'very'), (u'but', u'it', u'was', u'also', u'very', u'pity'), (u'it', u'was', u'also', u'very', u'pity', u'for'), (u'was', u'also', u'very', u'pity', u'for', u'me'), (u'also', u'very', u'pity', u'for', u'me', u'.'), (u'very', u'pity', u'for', u'me', u'.', u':-('), (u'pity', u'for', u'me', u'.', u':-(', u'@real_trump'), (u'for', u'me', u'.', u':-(', u'@real_trump', u'#sheetlife'), (u'me', u'.', u':-(', u'@real_trump', u'#sheetlife', u'#readytogo'), (u'.', u':-(', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com'), (u'very',), (u'very',), (u'pity',), (u'pity',), (u'pity',)])

        







    @attr(status='stable')
    #@wipd
    def test_temporize_baseline_lowercased_607(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)



        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))


        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()



        # ##### FAKE SENT 1 #######

        stats._init_insertion_variables()

        #inp = [[u'klitze', u'kleine', u'\xfcberaschung', u'.']]
        computed_baseline = [(u'klitze',), (u'kleine',), (u'\xfcberaschung',), (u'.',), (u'klitze', u'kleine'), (u'kleine', u'\xfcberaschung'), (u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung'), (u'kleine', u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung', u'.')]
        #assert set(stats.compute_baseline(inp)) == set(self.compute_baseline_1(inp))
        #p( stats.compute_baseline(inp))
        stats.temporize_baseline(computed_baseline)
        #p(dict(stats.temporized_baseline), "temporized_list ")
        stats.temporized_baseline.should.be.equal( {(u'.',): 1,
                                                 (u'kleine',): 1,
                                                 (u'kleine', u'\xfcberaschung'): 1,
                                                 (u'kleine', u'\xfcberaschung', u'.'): 1,
                                                 (u'klitze',): 1,
                                                 (u'klitze', u'kleine'): 1,
                                                 (u'klitze', u'kleine', u'\xfcberaschung'): 1,
                                                 (u'klitze', u'kleine', u'\xfcberaschung', u'.'): 1,
                                                 (u'\xfcberaschung',): 1,
                                                 (u'\xfcberaschung', u'.'): 1}
                                                )     


        stats.temporize_baseline(computed_baseline)
        #p(dict(stats.temporized_baseline), "temporized_list ")
        stats.temporized_baseline.should.be.equal( {(u'.',): 2,
                                                 (u'kleine',): 2,
                                                 (u'kleine', u'\xfcberaschung'): 2,
                                                 (u'kleine', u'\xfcberaschung', u'.'): 2,
                                                 (u'klitze',): 2,
                                                 (u'klitze', u'kleine'): 2,
                                                 (u'klitze', u'kleine', u'\xfcberaschung'): 2,
                                                 (u'klitze', u'kleine', u'\xfcberaschung', u'.'): 2,
                                                 (u'\xfcberaschung',): 2,
                                                 (u'\xfcberaschung', u'.'): 2}
                                                 )





        # # ##### FAKE SENT 2#######
        stats._init_insertion_variables()
        computed_baseline = [(u'1',), (u'2',), (u'3',), (u'4',), (u'5',), (u'\U0001f602',), (u'\U0001f9d1\U0001f3fb',), (u'1', u'2'), (u'2', u'3'), (u'3', u'4'), (u'4', u'5'), (u'5', u'\U0001f602'), (u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3'), (u'2', u'3', u'4'), (u'3', u'4', u'5'), (u'4', u'5', u'\U0001f602'), (u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4'), (u'2', u'3', u'4', u'5'), (u'3', u'4', u'5', u'\U0001f602'), (u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4', u'5'), (u'2', u'3', u'4', u'5', u'\U0001f602'), (u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4', u'5', u'\U0001f602'), (u'2', u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'), (u'1', u'2', u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb')]
        stats.temporize_baseline(computed_baseline)
        #p(dict(stats.temporized_baseline), "temporized_list ")
        stats.temporized_baseline.should.be.equal( {(u'1',): 1,
                                                     (u'1', u'2'): 1,
                                                     (u'1', u'2', u'3'): 1,
                                                     (u'1', u'2', u'3', u'4'): 1,
                                                     (u'1', u'2', u'3', u'4', u'5'): 1,
                                                     (u'1', u'2', u'3', u'4', u'5', u'\U0001f602'): 1,
                                                     (u'1', u'2', u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'2',): 1,
                                                     (u'2', u'3'): 1,
                                                     (u'2', u'3', u'4'): 1,
                                                     (u'2', u'3', u'4', u'5'): 1,
                                                     (u'2', u'3', u'4', u'5', u'\U0001f602'): 1,
                                                     (u'2', u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'3',): 1,
                                                     (u'3', u'4'): 1,
                                                     (u'3', u'4', u'5'): 1,
                                                     (u'3', u'4', u'5', u'\U0001f602'): 1,
                                                     (u'3', u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'4',): 1,
                                                     (u'4', u'5'): 1,
                                                     (u'4', u'5', u'\U0001f602'): 1,
                                                     (u'4', u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'5',): 1,
                                                     (u'5', u'\U0001f602'): 1,
                                                     (u'5', u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'\U0001f602',): 1,
                                                     (u'\U0001f602', u'\U0001f9d1\U0001f3fb'): 1,
                                                     (u'\U0001f9d1\U0001f3fb',): 1}
                                                     )  








    @attr(status='stable')
    #@wipd
    def test_baseline_lazyinsertion_into_db_lowercased_607(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)



        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))


        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()



        # ##### FAKE SENT 1 #######

        stats._init_insertion_variables()

        #inp = [[u'klitze', u'kleine', u'\xfcberaschung', u'.']]
        computed_baseline = [(u'klitze',),(u'klitze',), (u'kleine',), (u'\xfcberaschung',), (u'.',), (u'klitze', u'kleine'), (u'kleine', u'\xfcberaschung'), (u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung'), (u'kleine', u'\xfcberaschung', u'.'), (u'klitze', u'kleine', u'\xfcberaschung', u'.')]
        #assert set(stats.compute_baseline(inp)) == set(self.compute_baseline_1(inp))
        #p( stats.compute_baseline(inp))
        # temporized_baseline = {(u'.',): 1,
        #                          (u'kleine',): 1,
        #                          (u'kleine', u'\xfcberaschung'): 1,
        #                          (u'kleine', u'\xfcberaschung', u'.'): 1,
        #                          (u'klitze',): 2,
        #                          (u'klitze', u'kleine'): 1,
        #                          (u'klitze', u'kleine', u'\xfcberaschung'): 1,
        #                          (u'klitze', u'kleine', u'\xfcberaschung', u'.'): 1,
        #                          (u'\xfcberaschung',): 1,
        #                          (u'\xfcberaschung', u'.'): 1}
        #stats.temporized_baseline = temporized_baseline
        stats.baseline_lazyinsertion_into_db(computed_baseline)

        ## 
        stats.statsdb.getall("baseline").should.be.equal([])

        ##
        stats.baseline_insert_left_over_data()
        inserted_baseline = stats.statsdb.getall("baseline")
        #p(inserted_baseline, "inserted_baseline1")
        
        baseline_should_be_in_the_db = [(u'.', 1), (u'\xfcberaschung++.', 1), (u'klitze++kleine', 1), (u'klitze++kleine++\xfcberaschung', 1), (u'klitze', 2), (u'\xfcberaschung', 1), (u'kleine', 1), (u'klitze++kleine++\xfcberaschung++.', 1), (u'kleine++\xfcberaschung++.', 1), (u'kleine++\xfcberaschung', 1)]
        set(inserted_baseline).should.be.equal(set(baseline_should_be_in_the_db))
        


        ### One More Time
        #stats.temporized_baseline = temporized_baseline
        stats.baseline_lazyinsertion_into_db(computed_baseline,baseline_insertion_border=1)
        stats.baseline_lazyinsertion_into_db(computed_baseline, baseline_insertion_border=1)
        
        stats.baseline_insert_left_over_data()
        
        inserted_baseline = stats.statsdb.getall("baseline")
        #p(inserted_baseline, "inserted_baseline2")

        baseline_should_be_in_the_db = [(u'.', 3), (u'\xfcberaschung++.', 3), (u'klitze++kleine', 3), (u'klitze++kleine++\xfcberaschung', 3), (u'klitze', 6), (u'\xfcberaschung', 3), (u'kleine', 3), (u'klitze++kleine++\xfcberaschung++.', 3), (u'kleine++\xfcberaschung++.', 3), (u'kleine++\xfcberaschung', 3)]
        set(inserted_baseline).should.be.equal(set(baseline_should_be_in_the_db))
        





    @attr(status='stable')
    #@wipd
    def test_intern_compute_function_lower_case_608(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,status_bar=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        #p(stats.statsdb, "stats.statsdb")

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.corp = corp
        stats._corp_info = corp.info()

        ## DE####
        import time
        ### ROW 1 ###
        ##### FIRST INSETION
        stats._compute([copy.deepcopy(self.test_dict_row_de_1)])

        redu = stats.statsdb.getall("reduplications")
        repl = stats.statsdb.getall("replications")
        baseline = stats.statsdb.getall("baseline")


        #p(redu,"redu")
        #p(repl,"repl")
        #p(baseline,"baseline")
        #time.sleep(7)

        redu.should.be.equal([(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')])
        repl.should.be.equal([(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])
        baseline.should.be.equal([(u'.++trotzdem', 1), (u'!', 1), (u'hat++sie++mich', 1), (u'sie++mich++gl\xfccklich++gemacht++!', 1), (u'gemacht++!', 1), (u'gl\xfccklich++gemacht', 1), (u'sie++mich++gl\xfccklich', 1), (u':-)', 1), (u'mich++gl\xfccklich++gemacht++!++:-)++-)', 1), (u'gl\xfccklich', 1), (u'gl\xfccklich++gemacht++!++:-)++-)', 1), (u'.++trotzdem++hat++sie++mich++gl\xfccklich', 1), (u'gemacht++!++:-)++-)', 1), (u'klitze++kleine++\xfcberaschung++.++trotzdem++hat', 1), (u'mich++gl\xfccklich++gemacht', 1), (u'gemacht', 1), (u'!++:-)', 1), (u'.++trotzdem++hat++sie++mich', 1), (u'trotzdem++hat++sie++mich++gl\xfccklich++gemacht', 1), (u'\xfcberaschung++.++trotzdem', 1), (u'klitze++kleine++\xfcberaschung++.++trotzdem', 1), (u':-)++-)', 1), (u'gl\xfccklich++gemacht++!', 1), (u'\xfcberaschung++.', 1), (u'hat++sie++mich++gl\xfccklich++gemacht', 1), (u'trotzdem++hat++sie++mich++gl\xfccklich', 1), (u'klitze++kleine', 1), (u'sie++mich++gl\xfccklich++gemacht++!++:-)', 1), (u'\xfcberaschung', 1), (u'trotzdem++hat++sie', 1), (u'kleine', 2), (u'-)', 1), (u'trotzdem++hat++sie++mich', 1), (u'trotzdem++hat', 1), (u'.', 1), (u'trotzdem', 1), (u'hat', 1), (u'mich', 1), (u'.++trotzdem++hat', 1), (u'klitze', 2), (u'hat++sie', 1), (u'hat++sie++mich++gl\xfccklich++gemacht++!', 1), (u'gemacht++!++:-)', 1), (u'hat++sie++mich++gl\xfccklich', 1), (u'kleine++\xfcberaschung++.++trotzdem', 1), (u'kleine++\xfcberaschung++.++trotzdem++hat', 1), (u'.++trotzdem++hat++sie', 1), (u'kleine++\xfcberaschung++.++trotzdem++hat++sie', 1), (u'\xfcberaschung++.++trotzdem++hat++sie++mich', 1), (u'mich++gl\xfccklich++gemacht++!++:-)', 1), (u'mich++gl\xfccklich', 1), (u'\xfcberaschung++.++trotzdem++hat++sie', 1), (u'sie++mich', 1), (u'sie', 1), (u'gl\xfccklich++gemacht++!++:-)', 1), (u'klitze++kleine++\xfcberaschung', 1), (u'\xfcberaschung++.++trotzdem++hat', 1), (u'klitze++kleine++\xfcberaschung++.', 1), (u'!++:-)++-)', 1), (u'mich++gl\xfccklich++gemacht++!', 1), (u'kleine++\xfcberaschung++.', 1), (u'sie++mich++gl\xfccklich++gemacht', 1), (u'kleine++\xfcberaschung', 1)])

        

        ##### SECOND INSETION
        stats._compute([copy.deepcopy(self.test_dict_row_de_1)])
        redu = stats.statsdb.getall("reduplications")
        repl = stats.statsdb.getall("replications")
        baseline = stats.statsdb.getall("baseline")

        # p(redu,"redu")
        # p(repl,"repl")
        #p(baseline,"baseline")
        #time.sleep(7)

        redu.should.be.equal([(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (4, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')])
        repl.should.be.equal([(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (6, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (7, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (8, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (9, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (10, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])
        baseline.should.be.equal([(u'.++trotzdem', 2), (u'!', 2), (u'hat++sie++mich', 2), (u'sie++mich++gl\xfccklich++gemacht++!', 2), (u'gemacht++!', 2), (u'gl\xfccklich++gemacht', 2), (u'sie++mich++gl\xfccklich', 2), (u':-)', 2), (u'mich++gl\xfccklich++gemacht++!++:-)++-)', 2), (u'gl\xfccklich', 2), (u'gl\xfccklich++gemacht++!++:-)++-)', 2), (u'.++trotzdem++hat++sie++mich++gl\xfccklich', 2), (u'gemacht++!++:-)++-)', 2), (u'klitze++kleine++\xfcberaschung++.++trotzdem++hat', 2), (u'mich++gl\xfccklich++gemacht', 2), (u'gemacht', 2), (u'!++:-)', 2), (u'.++trotzdem++hat++sie++mich', 2), (u'trotzdem++hat++sie++mich++gl\xfccklich++gemacht', 2), (u'\xfcberaschung++.++trotzdem', 2), (u'klitze++kleine++\xfcberaschung++.++trotzdem', 2), (u':-)++-)', 2), (u'gl\xfccklich++gemacht++!', 2), (u'\xfcberaschung++.', 2), (u'hat++sie++mich++gl\xfccklich++gemacht', 2), (u'trotzdem++hat++sie++mich++gl\xfccklich', 2), (u'klitze++kleine', 2), (u'sie++mich++gl\xfccklich++gemacht++!++:-)', 2), (u'\xfcberaschung', 2), (u'trotzdem++hat++sie', 2), (u'kleine', 4), (u'-)', 2), (u'trotzdem++hat++sie++mich', 2), (u'trotzdem++hat', 2), (u'.', 2), (u'trotzdem', 2), (u'hat', 2), (u'mich', 2), (u'.++trotzdem++hat', 2), (u'klitze', 4), (u'hat++sie', 2), (u'hat++sie++mich++gl\xfccklich++gemacht++!', 2), (u'gemacht++!++:-)', 2), (u'hat++sie++mich++gl\xfccklich', 2), (u'kleine++\xfcberaschung++.++trotzdem', 2), (u'kleine++\xfcberaschung++.++trotzdem++hat', 2), (u'.++trotzdem++hat++sie', 2), (u'kleine++\xfcberaschung++.++trotzdem++hat++sie', 2), (u'\xfcberaschung++.++trotzdem++hat++sie++mich', 2), (u'mich++gl\xfccklich++gemacht++!++:-)', 2), (u'mich++gl\xfccklich', 2), (u'\xfcberaschung++.++trotzdem++hat++sie', 2), (u'sie++mich', 2), (u'sie', 2), (u'gl\xfccklich++gemacht++!++:-)', 2), (u'klitze++kleine++\xfcberaschung', 2), (u'\xfcberaschung++.++trotzdem++hat', 2), (u'klitze++kleine++\xfcberaschung++.', 2), (u'!++:-)++-)', 2), (u'mich++gl\xfccklich++gemacht++!', 2), (u'kleine++\xfcberaschung++.', 2), (u'sie++mich++gl\xfccklich++gemacht', 2), (u'kleine++\xfcberaschung', 2)])

        # # ########### EN ##############

        
        ### ROW 2 ###
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,status_bar=False)#, case_sensitiv=False)
        
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)
        stats._init_insertion_variables()
        stats._init_preprocessors()
        stats.corp = corp
        stats._corp_info = corp.info()

        stats._compute([copy.deepcopy(self.test_dict_row_en_2)])

        redu = stats.statsdb.getall("reduplications")
        repl = stats.statsdb.getall("replications")
        baseline = stats.statsdb.getall("baseline")


        # #p(redu,"redu")
        # #p(repl,"repl")
        #p(baseline,"baseline")
        #time.sleep(7)

        redu.should.be.equal([(1, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')])
        repl.should.be.equal([(1, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (2, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (3, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]'), (4, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])
        baseline.should.be.equal([(u'model', 1), (u'but++a++big++explanation++.++right', 1), (u'what', 1), (u'do++you++think++about', 1), (u'a++big', 1), (u'it', 1), (u'but', 1), (u'you++think', 1), (u',++but++a++big++explanation++.', 1), (u'what++do++you++think++about++it', 1), (u'big++explanation++.++right++?++what', 1), (u'you++think++about++it++?', 1), (u'?++what++do', 1), (u'what++do++you', 1), (u'but++a++big++explanation++.', 1), (u',++but++a', 1), (u'model++,', 1), (u'?++what++do++you++think++about', 1), (u'what++do++you++think', 1), (u'right++?++what++do', 1), (u'what++do', 1), (u'.++right++?++what', 1), (u'but++a++big', 1), (u'tiny', 1), (u'tiny++model', 1), (u'think++about', 1), (u'explanation++.++right++?++what', 1), (u'model++,++but++a++big++explanation', 1), (u'a++big++explanation', 1), (u'explanation++.++right++?++what++do', 1), (u'?++what', 1), (u'right', 1), (u'big++explanation++.++right++?', 1), (u'it++?', 1), (u'what++do++you++think++about', 1), (u'explanation++.++right', 1), (u'.', 1), (u'you', 1), (u'?', 2), (u'explanation++.++right++?', 1), (u'tiny++model++,++but', 1), (u'do++you++think++about++it', 1), (u'big++explanation++.', 1), (u'.++right', 1), (u'explanation++.', 1), (u'model++,++but++a', 1), (u'you++think++about', 1), (u'?++what++do++you', 1), (u'explanation', 1), (u'do++you++think++about++it++?', 1), (u'do++you++think', 1), (u'model++,++but', 1), (u'tiny++model++,++but++a', 1), (u'right++?', 1), (u'model++,++but++a++big', 1), (u'think++about++it', 1), (u',', 1), (u',++but++a++big++explanation', 1), (u',++but', 1), (u'about', 1), (u'tiny++model++,++but++a++big', 1), (u'right++?++what', 1), (u'a++big++explanation++.++right', 1), (u'tiny++model++,', 1), (u'right++?++what++do++you++think', 1), (u'about++it++?', 1), (u'?++what++do++you++think', 1), (u'about++it', 1), (u'.++right++?', 1), (u'you++think++about++it', 1), (u'do++you', 1), (u'.++right++?++what++do', 1), (u'big++explanation++.++right', 1), (u'a', 1), (u'.++right++?++what++do++you', 1), (u'think', 1), (u'think++about++it++?', 1), (u'big', 3), (u'big++explanation', 1), (u'right++?++what++do++you', 1), (u'but++a++big++explanation', 1), (u'do', 1), (u'a++big++explanation++.', 1), (u'a++big++explanation++.++right++?', 1), (u'but++a', 1), (u',++but++a++big', 1)])

    





    @attr(status='stable')
    #@wipd
    def test_get_streams_from_corp_609(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        
        ### Try 1
        stream_num = 4
        streams = stats.get_streams_from_corpus(corp,stream_num )
        all_rows_from_corpus = []
        for stream in streams:
            rows = list(stream[1])
            all_rows_from_corpus += rows
            len(stream[1]).should.be.equal(len(rows))

        rows_as_text = [unicode(row) for row in all_rows_from_corpus]
        len(rows_as_text).should.be.equal(len(set(rows_as_text)))

        ### Try 2
        stream_num = 1
        streams = stats.get_streams_from_corpus(corp,stream_num )
        all_rows_from_corpus = []
        #p(( streams, len(streams[0][1]), len(list(streams[0][1]))  ))
        for stream in streams:
            rows = list(stream[1])
            all_rows_from_corpus += rows
            len(stream[1]).should.be.equal(len(rows))

        rows_as_text = [unicode(row) for row in all_rows_from_corpus]
        len(rows_as_text).should.be.equal(len(set(rows_as_text)))





    @attr(status='stable')
    #@wipd
    def test_main_compute_function_lower_case_for_1_stream_610_1(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=1,adjust_to_cpu=False)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")

        repls.should.be.equal([(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]'), (11, 2222, u'[0, 0]', u'gla^7d', u'glad', u'NN', u'["neutral", 0.0]', u'a', u'[]', 7, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]'), (12, 2222, u'[0, 2]', u'se^9', u'se', u'VB', u'["neutral", 0.0]', u'e', u'[]', 9, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]'), (13, 2222, u'[0, 4]', u'-)^4', u'-)', u'EMOASC', u'["neutral", 0.0]', u')', u'[]', 4, 1, u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (14, 3333, u'[0, 1]', u'bad^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (15, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 7, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (16, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 6, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (17, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 4, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (18, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 4, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (19, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (20, 3333, u'[0, 5]', u'ba^7d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (21, 3333, u'[0, 14]', u'-(^4', u'-(', u'EMOASC', u'["negative", -0.6999999999999998]', u'(', u'[]', 4, 1, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]'), (22, 3333, u'[0, 15]', u'\U0001f62b^12', u'\U0001f62b', u'EMOIMG', u'["negative", -0.6999999999999998]', u'\U0001f62b', u'[]', 12, 0, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]'), (23, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'o', u'[]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), (24, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'l', u'[]', 7, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), (25, 4444, u'[0, 15]', u'bi^3g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 3, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (26, 4444, u'[0, 16]', u'bi^15g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 15, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (27, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (28, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (29, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]'), (30, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (31, 6666, u'[0, 0]', u'tin^3y^2', u'tiny', u'JJ', u'["neutral", 0.0]', u'n', u'[0, 0]', 3, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (32, 7777, u'[0, 7]', u'\U0001f62b^4', u'\U0001f62b', u'EMOIMG', u'["positive", 0.27]', u'\U0001f62b', u'[]', 4, 0, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), (33, 7777, u'[0, 9]', u'bu^10t', u'but', u'MD', u'["positive", 0.27]', u'u', u'[]', 10, 1, u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]'), (34, 7777, u'[0, 12]', u'real^3y', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 3, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (35, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'e', u'[0, 11]', 5, 1, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (36, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 4, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (37, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'y', u'[0, 11]', 3, 4, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (38, 7777, u'[0, 16]', u'=)^10', u'=)', u'EMOASC', u'["positive", 0.27]', u')', u'[]', 10, 1, u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]'), (39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]'), (40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])
        redus.should.be.equal([(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (3, 3333, 5, u'bad', u'[0, 1]', u'JJ', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', u'["negative", -0.6999999999999998]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (4, 3333, 2, u'#shetlife', u'[0, 16]', u'hashtag', u'{"#shetlife": 2}', u'["negative", -0.6999999999999998]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'\U0001f62b', u'["EMOIMG"]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 4444, 6, u'tiny', u'[0, 0]', u'JJ', u'{"tiny": 6}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'model', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (6, 4444, 2, u'big', u'[0, 15]', u'NN', u'{"bi^3g": 1, "bi^15g": 1}', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (7, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'), (8, 6666, 3, u'tiny', u'[0, 0]', u'JJ', u'{"tin^3y^2": 1, "tiny": 2}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (9, 7777, 3, u'realy', u'[0, 11]', u'RB', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', u'["positive", 0.27]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')])

        #p()
        #p(repls, "repls")
        #p(redus, "redus")
        # for repl in repls:
        #     print repl


        # for redu in redus:
        #    print redu





    @attr(status='stable')
    #@wipd
    def test_main_compute_function_lower_case_for_4_streams_610_2(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"

        #stats = Corpus(logger_level=logging.DEBUG)

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=4,adjust_to_cpu=False)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")

        repls.should.be.equal([(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]'), (11, 2222, u'[0, 0]', u'gla^7d', u'glad', u'NN', u'["neutral", 0.0]', u'a', u'[]', 7, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]'), (12, 2222, u'[0, 2]', u'se^9', u'se', u'VB', u'["neutral", 0.0]', u'e', u'[]', 9, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]'), (13, 2222, u'[0, 4]', u'-)^4', u'-)', u'EMOASC', u'["neutral", 0.0]', u')', u'[]', 4, 1, u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (14, 3333, u'[0, 1]', u'bad^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (15, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 7, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (16, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 6, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (17, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 4, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (18, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 4, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (19, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (20, 3333, u'[0, 5]', u'ba^7d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (21, 3333, u'[0, 14]', u'-(^4', u'-(', u'EMOASC', u'["negative", -0.6999999999999998]', u'(', u'[]', 4, 1, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]'), (22, 3333, u'[0, 15]', u'\U0001f62b^12', u'\U0001f62b', u'EMOIMG', u'["negative", -0.6999999999999998]', u'\U0001f62b', u'[]', 12, 0, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]'), (23, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'o', u'[]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), (24, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'l', u'[]', 7, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), (25, 4444, u'[0, 15]', u'bi^3g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 3, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (26, 4444, u'[0, 16]', u'bi^15g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 15, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (27, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (28, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (29, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]'), (30, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (31, 6666, u'[0, 0]', u'tin^3y^2', u'tiny', u'JJ', u'["neutral", 0.0]', u'n', u'[0, 0]', 3, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (32, 7777, u'[0, 7]', u'\U0001f62b^4', u'\U0001f62b', u'EMOIMG', u'["positive", 0.27]', u'\U0001f62b', u'[]', 4, 0, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), (33, 7777, u'[0, 9]', u'bu^10t', u'but', u'MD', u'["positive", 0.27]', u'u', u'[]', 10, 1, u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]'), (34, 7777, u'[0, 12]', u'real^3y', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 3, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (35, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'e', u'[0, 11]', 5, 1, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (36, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 4, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (37, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'y', u'[0, 11]', 3, 4, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (38, 7777, u'[0, 16]', u'=)^10', u'=)', u'EMOASC', u'["positive", 0.27]', u')', u'[]', 10, 1, u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]'), (39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]'), (40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')])
        redus.should.be.equal([(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (3, 3333, 5, u'bad', u'[0, 1]', u'JJ', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', u'["negative", -0.6999999999999998]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (4, 3333, 2, u'#shetlife', u'[0, 16]', u'hashtag', u'{"#shetlife": 2}', u'["negative", -0.6999999999999998]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'\U0001f62b', u'["EMOIMG"]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 4444, 6, u'tiny', u'[0, 0]', u'JJ', u'{"tiny": 6}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'model', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (6, 4444, 2, u'big', u'[0, 15]', u'NN', u'{"bi^3g": 1, "bi^15g": 1}', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (7, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'), (8, 6666, 3, u'tiny', u'[0, 0]', u'JJ', u'{"tin^3y^2": 1, "tiny": 2}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (9, 7777, 3, u'realy', u'[0, 11]', u'RB', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', u'["positive", 0.27]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')])






    @attr(status='stable')
    #@wipd
    def test_get_data_611(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()



        #### DE ######
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))
        


        ### Case 0:
        syntagma = ["big"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")
        data.should.be.equal([])


        ### Case 1.1:
        syntagma = ["klitze"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (15, 10000, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), (17, 11111, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]')]
        right_redu = [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (4, 12222, 4, u'klitze', u'[0, 1]', u'NN', u'{"klitze": 4}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]')]
        right_baseline = [([u'klitze'], 8)]
        right_syntagma = [u'klitze']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])

        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     p(item,"item")
        #     print item["syntagma"]
        #     print "\n__REPL___\n"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___\n"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___\n"
        #     print item["baseline"] 



        ### Case 2:
        syntagma = ["klitze","kleine"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (15, 10000, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), (17, 11111, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]
        right_redu = [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (4, 12222, 4, u'klitze', u'[0, 1]', u'NN', u'{"klitze": 4}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]
        right_baseline = [([u'klitze', u'kleine'], 4)]
        right_syntagma = [u'klitze', u'kleine']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])


        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     #p(item,"item")
        #     print item["syntagma"]
        #     print "\n__REPL___\n"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___\n"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___\n"
        #     print item["baseline"] 



        ### Case 3:
        syntagma = "*"
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")
        right_data = [{'repl': [(23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]'), (24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'4', u'5'], 'baseline': ([u'4', u'5'], 1), 'redu': []}, {'repl': [(4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u':-)', u'-)'], 'baseline': ([u':-)', u'-)'], 1), 'redu': []}, {'repl': [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (15, 10000, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (16, 10000, u'[0, 3]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["VAPPER"]', u'kleine', u'["ADJA"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]', u'', u'[]'), (25, 12222, u'[0, 6]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["NN", {"klitze": 4}]', u'kleine', u'["ADJA"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]', u'mal', u'["PTKMA"]', u'gerne', u'["ADV"]')], 'syntagma': [u'klitze', u'kleine', u'\xfcberaschung'], 'baseline': ([u'klitze', u'kleine', u'\xfcberaschung'], 3), 'redu': []}, {'repl': [(2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')], 'syntagma': [u'kleine'], 'baseline': ([u'kleine'], 5), 'redu': [(2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]}, {'repl': [(22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]'), (24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'3', u'4', u'5'], 'baseline': ([u'3', u'4', u'5'], 1), 'redu': []}, {'repl': [(5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'-)'], 'baseline': ([u'-)'], 1), 'redu': []}, {'repl': [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]')], 'syntagma': [u'1'], 'baseline': ([u'1'], 1), 'redu': []}, {'repl': [(10, 9999, u'[2, 0]', u'ble^8ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 8, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]'), (11, 9999, u'[2, 1]', u'ble^4ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 4, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]')], 'syntagma': [u'bleibt'], 'baseline': ([u'bleibt'], 2), 'redu': [(3, 9999, 2, u'bleibt', u'[2, 0]', u'NN', u'{"ble^4ibt": 1, "ble^8ibt": 1}', u'["neutral", 0.0]', u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]')]}, {'repl': [(13, 9999, u'[2, 4]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f600', u'[]', 5, 0, u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f600'], 'baseline': ([u'\U0001f600'], 1), 'redu': []}, {'repl': [(10, 9999, u'[2, 0]', u'ble^8ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 8, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]'), (11, 9999, u'[2, 1]', u'ble^4ibt', u'bleibt', u'NN', u'["neutral", 0.0]', u'e', u'[2, 0]', 4, 2, u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]'), (12, 9999, u'[2, 2]', u'hu^12ngrig', u'hungrig', u'NN', u'["neutral", 0.0]', u'u', u'[]', 12, 1, u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'bleibt', u'hungrig'], 'baseline': ([u'bleibt', u'hungrig'], 1), 'redu': []}, {'repl': [(19, 11111, u'[1, 4]', u'is^6t', u'ist', u'NN', u'["neutral", 0.0]', u's', u'[]', 6, 1, u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]')], 'syntagma': [u'ist'], 'baseline': ([u'ist'], 1), 'redu': []}, {'repl': [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), (21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'1', u'2', u'3'], 'baseline': ([u'1', u'2', u'3'], 1), 'redu': []}, {'repl': [(8, 9999, u'[1, 0]', u'genie^11s^2t', u'geniest', u'NN', u'["neutral", 0.0]', u'e', u'[]', 11, 4, u'tag', u'["NN"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]')], 'syntagma': [u'geniest'], 'baseline': ([u'geniest'], 1), 'redu': []}, {'repl': [(9, 9999, u'[1, 1]', u'geni^13st', u'genist', u'VVFIN', u'["neutral", 0.0]', u'i', u'[]', 13, 3, u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]')], 'syntagma': [u'genist'], 'baseline': ([u'genist'], 1), 'redu': []}, {'repl': [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), (21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]')], 'syntagma': [u'1', u'2'], 'baseline': ([u'1', u'2'], 1), 'redu': []}, {'repl': [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (15, 10000, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), (17, 11111, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]')], 'syntagma': [u'klitze'], 'baseline': ([u'klitze'], 8), 'redu': [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (4, 12222, 4, u'klitze', u'[0, 1]', u'NN', u'{"klitze": 4}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]')]}, {'repl': [(14, 9999, u'[2, 5]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f308', u'[]', 7, 0, u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f308'], 'baseline': ([u'\U0001f308'], 1), 'redu': []}, {'repl': [(21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]'), (24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'2', u'3', u'4', u'5'], 'baseline': ([u'2', u'3', u'4', u'5'], 1), 'redu': []}, {'repl': [(13, 9999, u'[2, 4]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f600', u'[]', 5, 0, u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (14, 9999, u'[2, 5]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["neutral", 0.0]', u'\U0001f308', u'[]', 7, 0, u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f600', u'\U0001f308'], 'baseline': ([u'\U0001f600', u'\U0001f308'], 1), 'redu': []}, {'repl': [(22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'3', u'4'], 'baseline': ([u'3', u'4'], 1), 'redu': []}, {'repl': [(23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'4'], 'baseline': ([u'4'], 1), 'redu': []}, {'repl': [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), (21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'1', u'2', u'3', u'4'], 'baseline': ([u'1', u'2', u'3', u'4'], 1), 'redu': []}, {'repl': [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (15, 10000, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), (17, 11111, u'[0, 1]', u'klitze^4', u'klitze', u'VAPPER', u'["neutral", 0.0]', u'e', u'[]', 4, 5, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')], 'syntagma': [u'klitze', u'kleine'], 'baseline': ([u'klitze', u'kleine'], 4), 'redu': [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (4, 12222, 4, u'klitze', u'[0, 1]', u'NN', u'{"klitze": 4}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]}, {'repl': [(16, 10000, u'[0, 3]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["VAPPER"]', u'kleine', u'["ADJA"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]', u'', u'[]'), (25, 12222, u'[0, 6]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["NN", {"klitze": 4}]', u'kleine', u'["ADJA"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]', u'mal', u'["PTKMA"]', u'gerne', u'["ADV"]')], 'syntagma': [u'\xfcberaschung'], 'baseline': ([u'\xfcberaschung'], 3), 'redu': []}, {'repl': [(12, 9999, u'[2, 2]', u'hu^12ngrig', u'hungrig', u'NN', u'["neutral", 0.0]', u'u', u'[]', 12, 1, u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'hungrig'], 'baseline': ([u'hungrig'], 1), 'redu': []}, {'repl': [(8, 9999, u'[1, 0]', u'genie^11s^2t', u'geniest', u'NN', u'["neutral", 0.0]', u'e', u'[]', 11, 4, u'tag', u'["NN"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]'), (9, 9999, u'[1, 1]', u'geni^13st', u'genist', u'VVFIN', u'["neutral", 0.0]', u'i', u'[]', 13, 3, u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]')], 'syntagma': [u'geniest', u'genist'], 'baseline': ([u'geniest', u'genist'], 1), 'redu': []}, {'repl': [(18, 11111, u'[1, 3]', u'wichti^8g', u'wichtig', u'ADJA', u'["neutral", 0.0]', u'i', u'[]', 8, 5, u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]'), (19, 11111, u'[1, 4]', u'is^6t', u'ist', u'NN', u'["neutral", 0.0]', u's', u'[]', 6, 1, u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]')], 'syntagma': [u'wichtig', u'ist'], 'baseline': ([u'wichtig', u'ist'], 1), 'redu': []}, {'repl': [(24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'5'], 'baseline': ([u'5'], 1), 'redu': []}, {'repl': [(6, 9999, u'[0, 2]', u'ta^6g^6', u'tag', u'NN', u'["neutral", 0.0]', u'a', u'[]', 6, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]'), (7, 9999, u'[0, 2]', u'ta^6g^6', u'tag', u'NN', u'["neutral", 0.0]', u'g', u'[]', 6, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]')], 'syntagma': [u'tag'], 'baseline': ([u'tag'], 1), 'redu': []}, {'repl': [(21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'2', u'3'], 'baseline': ([u'2', u'3'], 1), 'redu': []}, {'repl': [(4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u':-)'], 'baseline': ([u':-)'], 1), 'redu': []}, {'repl': [(21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]')], 'syntagma': [u'2'], 'baseline': ([u'2'], 1), 'redu': []}, {'repl': [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), (21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]'), (24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'1', u'2', u'3', u'4', u'5'], 'baseline': ([u'1', u'2', u'3', u'4', u'5'], 1), 'redu': []}, {'repl': [(21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'2', u'3', u'4'], 'baseline': ([u'2', u'3', u'4'], 1), 'redu': []}, {'repl': [(22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'3'], 'baseline': ([u'3'], 1), 'redu': []}, {'repl': [(18, 11111, u'[1, 3]', u'wichti^8g', u'wichtig', u'ADJA', u'["neutral", 0.0]', u'i', u'[]', 8, 5, u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]')], 'syntagma': [u'wichtig'], 'baseline': ([u'wichtig'], 1), 'redu': []}, {'repl': [(2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (16, 10000, u'[0, 3]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["VAPPER"]', u'kleine', u'["ADJA"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]', u'', u'[]'), (25, 12222, u'[0, 6]', u'\xfcber^4aschung', u'\xfcberaschung', u'NN', u'["neutral", 0.0]', u'r', u'[]', 4, 3, u'', u'[]', u'', u'[]', u'eine', u'["ART"]', u'klitze', u'["NN", {"klitze": 4}]', u'kleine', u'["ADJA"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]', u'mal', u'["PTKMA"]', u'gerne', u'["ADV"]')], 'syntagma': [u'kleine', u'\xfcberaschung'], 'baseline': ([u'kleine', u'\xfcberaschung'], 3), 'redu': []}]

        for extracted_item, right_item in zip(data,right_data):
            #p(extracted_item,"extracted_item")
            #p(right_item,"right_item")
            extracted_item.should.be.equal(right_item)

        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     #p(item,"item")
        #     print "\n______item_________"
        #     #p( item["syntagma"], c="r")
        #     print "\n__REPL___"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___"
        #     print item["baseline"] 





        ### Case 4_1:
        syntagma = ["EMOASC"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = []
        right_baseline = [([u':-)'], 1), ([u':-)', u'-)'], 1), ([u'-)'], 1)]
        right_syntagma = ['EMOASC']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)




        ### Case 4_2:
        syntagma = ["EMOASC","EMOASC"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(4, 8888, u'[1, 7]', u':-)^4', u':-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 4, 2, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]'), (5, 8888, u'[1, 8]', u'-)^3', u'-)', u'EMOASC', u'["positive", 0.5]', u')', u'[]', 3, 1, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = []
        right_baseline = [([u':-)'], 1), ([u':-)', u'-)'], 1), ([u'-)'], 1)]
        right_syntagma = ['EMOASC', 'EMOASC']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)


        # ### Case 4_3:
        syntagma = ["NN", "NE"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",search_just_in_full_repetativ_syntagma=False))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(1, 8888, u'[0, 1]', u'kli^4tze', u'klitze', u'NN', u'["neutral", 0.0]', u'i', u'[0, 0]', 4, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, u'[0, 2]', u'kle^5ine', u'kleine', u'NE', u'["neutral", 0.0]', u'e', u'[0, 2]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[0, 3]', u'klein^3e', u'kleine', u'NE', u'["neutral", 0.0]', u'n', u'[0, 2]', 3, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]
        right_redu = [(1, 8888, 2, u'klitze', u'[0, 0]', u'NN', u'{"klitze": 1, "kli^4tze": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, 2, u'kleine', u'[0, 2]', u'NE', u'{"kle^5ine": 1, "klein^3e": 1}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')]
        right_baseline = [([u'klitze', u'kleine', u'\xfcberaschung'], 3), ([u'klitze', u'kleine'], 4), ([u'klitze'], 8), ([u'klitze', u'kleine', u'\xfcberaschung', u'.'], 1), ([u'kleine'], 5), ([u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1), ([u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1), ([u'kleine', u'\xfcberaschung', u'.'], 1), ([u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1), ([u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1), ([u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie'], 1), ([u'kleine', u'\xfcberaschung'], 3)]
        right_syntagma = ['NN', 'NE']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)



        # ### Case 5:
        syntagma = ["number"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",search_just_in_full_repetativ_syntagma=True))
        # p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(20, 11111, u'[1, 6]', u'1^5', u'1', u'number', u'["neutral", 0.0]', u'1', u'[]', 5, 0, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), (21, 11111, u'[1, 7]', u'2^4', u'2', u'number', u'["neutral", 0.0]', u'2', u'[]', 4, 0, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]'), (22, 11111, u'[1, 8]', u'3^5', u'3', u'number', u'["neutral", 0.0]', u'3', u'[]', 5, 0, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]'), (23, 11111, u'[1, 9]', u'4^4', u'4', u'number', u'["neutral", 0.0]', u'4', u'[]', 4, 0, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]'), (24, 11111, u'[1, 10]', u'5^5', u'5', u'number', u'["neutral", 0.0]', u'5', u'[]', 5, 0, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = []
        right_baseline = [([u'1', u'2', u'3', u'4'], 1), ([u'1', u'2', u'3', u'4', u'5'], 1), ([u'3', u'4', u'5'], 1), ([u'2', u'3', u'4', u'5', u'6'], 1), ([u'1', u'2'], 1), ([u'3', u'4', u'5', u'6'], 1), ([u'3', u'4'], 1), ([u'4', u'5'], 1), ([u'1', u'2', u'3'], 1), ([u'1'], 1), ([u'4'], 1), ([u'5', u'6'], 1), ([u'1', u'2', u'3', u'4', u'5', u'6'], 1), ([u'2', u'3', u'4', u'5'], 1), ([u'3'], 1), ([u'4', u'5', u'6'], 1), ([u'5'], 1), ([u'2'], 1), ([u'2', u'3'], 1), ([u'2', u'3', u'4'], 1)]
        right_syntagma = ['number']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        # print "\n"
        # for r in right_repl:
        #     print r



        # #### EN ######
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        
        


        ### Case 1.1:
        syntagma = ["big"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        #p(data[0]["repl"])
        #p(data[0]["redu"])
        #p(data[0]["baseline"])
        #p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(25, 4444, u'[0, 15]', u'bi^3g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 3, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (26, 4444, u'[0, 16]', u'bi^15g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 15, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = [(6, 4444, 2, u'big', u'[0, 15]', u'NN', u'{"bi^3g": 1, "bi^15g": 1}', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (7, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')]
        right_baseline = [([u'big'], 5)]
        right_syntagma = [u'big']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])

        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     p(item,"item")
        #     print item["syntagma"]
        #     print "\n__REPL___\n"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___\n"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___\n"
        #     print item["baseline"] 



        ### Case 1.2:
        syntagma = ["biiiiiiig"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(25, 4444, u'[0, 15]', u'bi^3g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 3, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (26, 4444, u'[0, 16]', u'bi^15g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 15, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = [(6, 4444, 2, u'big', u'[0, 15]', u'NN', u'{"bi^3g": 1, "bi^15g": 1}', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (7, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')]
        right_baseline = [([u'big'], 5)]
        right_syntagma = [u'big']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])





        ### Case 2:
        syntagma = ["very","pity"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')]
        right_redu = [(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')]
        right_baseline = [([u'very', u'pity'], 1)]
        right_syntagma = [u'very', u'pity']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])


        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     #p(item,"item")
        #     print item["syntagma"]
        #     print "\n__REPL___\n"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___\n"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___\n"
        #     print item["baseline"] 



        ### Case 3:
        syntagma = "*"
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")
        right_data = [{'repl': [(34, 7777, u'[0, 12]', u'real^3y', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 3, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (35, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'e', u'[0, 11]', 5, 1, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (36, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'l', u'[0, 11]', 4, 3, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), (37, 7777, u'[0, 13]', u're^5al^4y^3', u'realy', u'RB', u'["positive", 0.27]', u'y', u'[0, 11]', 3, 4, u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')], 'syntagma': [u'realy'], 'baseline': ([u'realy'], 4), 'redu': [(9, 7777, 3, u'realy', u'[0, 11]', u'RB', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', u'["positive", 0.27]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')]}, {'repl': [(31, 6666, u'[0, 0]', u'tin^3y^2', u'tiny', u'JJ', u'["neutral", 0.0]', u'n', u'[0, 0]', 3, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'tiny'], 'baseline': ([u'tiny'], 10), 'redu': [(5, 4444, 6, u'tiny', u'[0, 0]', u'JJ', u'{"tiny": 6}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'model', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (8, 6666, 3, u'tiny', u'[0, 0]', u'JJ', u'{"tin^3y^2": 1, "tiny": 2}', u'["neutral", 0.0]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'surprise', u'["NN"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]}, {'repl': [(40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f308'], 'baseline': ([u'\U0001f308'], 1), 'redu': []}, {'repl': [(12, 2222, u'[0, 2]', u'se^9', u'se', u'VB', u'["neutral", 0.0]', u'e', u'[]', 9, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'se'], 'baseline': ([u'se'], 1), 'redu': []}, {'repl': [(14, 3333, u'[0, 1]', u'bad^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (15, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 7, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (16, 3333, u'[0, 3]', u'b^7a^6d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 6, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (17, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'b', u'[0, 1]', 4, 0, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (18, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 4, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (19, 3333, u'[0, 4]', u'b^4a^4d^5', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'd', u'[0, 1]', 5, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), (20, 3333, u'[0, 5]', u'ba^7d', u'bad', u'JJ', u'["negative", -0.6999999999999998]', u'a', u'[0, 1]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]')], 'syntagma': [u'bad'], 'baseline': ([u'bad'], 6), 'redu': [(3, 3333, 5, u'bad', u'[0, 1]', u'JJ', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', u'["negative", -0.6999999999999998]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]')]}, {'repl': [(33, 7777, u'[0, 9]', u'bu^10t', u'but', u'MD', u'["positive", 0.27]', u'u', u'[]', 10, 1, u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]')], 'syntagma': [u'but'], 'baseline': ([u'but'], 3), 'redu': []}, {'repl': [(9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]')], 'syntagma': [u'.'], 'baseline': ([u'.'], 5), 'redu': []}, {'repl': [(5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')], 'syntagma': [u'pity'], 'baseline': ([u'pity'], 4), 'redu': [(2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')]}, {'repl': [(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]')], 'syntagma': [u'very'], 'baseline': ([u'very'], 3), 'redu': [(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]')]}, {'repl': [(25, 4444, u'[0, 15]', u'bi^3g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 3, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (26, 4444, u'[0, 16]', u'bi^15g', u'big', u'NN', u'["neutral", 0.0]', u'i', u'[0, 15]', 15, 1, u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'big'], 'baseline': ([u'big'], 5), 'redu': [(6, 4444, 2, u'big', u'[0, 15]', u'NN', u'{"bi^3g": 1, "bi^15g": 1}', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', u'', u'[]', u'', u'[]', u'', u'[]'), (7, 5555, 3, u'big', u'[0, 5]', u'JJ', u'{"big": 3}', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')]}, {'repl': [(23, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'o', u'[]', 7, 1, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), (24, 4444, u'[0, 6]', u'mo^7del^7', u'model', u'NN', u'["neutral", 0.0]', u'l', u'[]', 7, 4, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]')], 'syntagma': [u'model'], 'baseline': ([u'model'], 2), 'redu': []}, {'repl': [(13, 2222, u'[0, 4]', u'-)^4', u'-)', u'EMOASC', u'["neutral", 0.0]', u')', u'[]', 4, 1, u'', u'[]', u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'-)'], 'baseline': ([u'-)'], 1), 'redu': []}, {'repl': [(21, 3333, u'[0, 14]', u'-(^4', u'-(', u'EMOASC', u'["negative", -0.6999999999999998]', u'(', u'[]', 4, 1, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]'), (22, 3333, u'[0, 15]', u'\U0001f62b^12', u'\U0001f62b', u'EMOIMG', u'["negative", -0.6999999999999998]', u'\U0001f62b', u'[]', 12, 0, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'-(', u'\U0001f62b'], 'baseline': ([u'-(', u'\U0001f62b'], 1), 'redu': []}, {'repl': [(38, 7777, u'[0, 16]', u'=)^10', u'=)', u'EMOASC', u'["positive", 0.27]', u')', u'[]', 10, 1, u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]')], 'syntagma': [u'=)'], 'baseline': ([u'=)'], 1), 'redu': []}, {'repl': [(28, 5555, u'[1, 0]', u'ri^6ght', u'right', u'UH', u'["neutral", 0.0]', u'i', u'[]', 6, 1, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]')], 'syntagma': [u'right'], 'baseline': ([u'right'], 1), 'redu': []}, {'repl': [], 'syntagma': [u'#shetlife'], 'baseline': ([u'#shetlife'], 3), 'redu': [(4, 3333, 2, u'#shetlife', u'[0, 16]', u'hashtag', u'{"#shetlife": 2}', u'["negative", -0.6999999999999998]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'\U0001f62b', u'["EMOIMG"]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]}, {'repl': [(30, 5555, u'[2, 6]', u'?^4', u'?', u'symbol', u'["neutral", 0.0]', u'?', u'[]', 4, 0, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'?'], 'baseline': ([u'?'], 2), 'redu': []}, {'repl': [(39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]'), (40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f600', u'\U0001f308'], 'baseline': ([u'\U0001f600', u'\U0001f308'], 1), 'redu': []}, {'repl': [(27, 5555, u'[0, 8]', u'expla^5nation', u'explanation', u'NN', u'["neutral", 0.0]', u'a', u'[]', 5, 4, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]')], 'syntagma': [u'explanation'], 'baseline': ([u'explanation'], 1), 'redu': []}, {'repl': [(1, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 4, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, u'[1, 4]', u'ver^4y^5', u'very', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 4]', 5, 3, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (3, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'v', u'[1, 4]', 3, 0, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (4, 1111, u'[1, 5]', u'v^3er^8y', u'very', u'JJ', u'["negative", -0.1875]', u'r', u'[1, 4]', 8, 2, u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (5, 1111, u'[1, 7]', u'pi^9ty', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 9, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (6, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'i', u'[1, 7]', 3, 1, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (7, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u't', u'[1, 7]', 3, 2, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), (8, 1111, u'[1, 10]', u'pi^3t^3y^3', u'pity', u'JJ', u'["negative", -0.1875]', u'y', u'[1, 7]', 3, 3, u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')], 'syntagma': [u'very', u'pity'], 'baseline': ([u'very', u'pity'], 1), 'redu': [(1, 1111, 3, u'very', u'[1, 4]', u'JJ', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), (2, 1111, 4, u'pity', u'[1, 7]', u'JJ', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')]}, {'repl': [(39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]')], 'syntagma': [u'\U0001f600'], 'baseline': ([u'\U0001f600'], 2), 'redu': []}, {'repl': [(29, 5555, u'[2, 2]', u'you^6', u'you', u'PRP', u'["neutral", 0.0]', u'u', u'[]', 6, 2, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'', u'[]')], 'syntagma': [u'you'], 'baseline': ([u'you'], 2), 'redu': []}, {'repl': [(21, 3333, u'[0, 14]', u'-(^4', u'-(', u'EMOASC', u'["negative", -0.6999999999999998]', u'(', u'[]', 4, 1, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]')], 'syntagma': [u'-('], 'baseline': ([u'-('], 1), 'redu': []}, {'repl': [(22, 3333, u'[0, 15]', u'\U0001f62b^12', u'\U0001f62b', u'EMOIMG', u'["negative", -0.6999999999999998]', u'\U0001f62b', u'[]', 12, 0, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]'), (32, 7777, u'[0, 7]', u'\U0001f62b^4', u'\U0001f62b', u'EMOIMG', u'["positive", 0.27]', u'\U0001f62b', u'[]', 4, 0, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]')], 'syntagma': [u'\U0001f62b'], 'baseline': ([u'\U0001f62b'], 2), 'redu': []}, {'repl': [(10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]')], 'syntagma': [u':-('], 'baseline': ([u':-('], 1), 'redu': []}, {'repl': [(9, 1111, u'[1, 13]', u'.^6', u'.', u'symbol', u'["negative", -0.1875]', u'.', u'[]', 6, 0, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), (10, 1111, u'[1, 14]', u':-(^5', u':-(', u'EMOASC', u'["negative", -0.1875]', u'(', u'[]', 5, 2, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', u'', u'[]')], 'syntagma': [u'.', u':-('], 'baseline': ([u'.', u':-('], 1), 'redu': []}, {'repl': [(11, 2222, u'[0, 0]', u'gla^7d', u'glad', u'NN', u'["neutral", 0.0]', u'a', u'[]', 7, 2, u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', u'', u'[]')], 'syntagma': [u'glad'], 'baseline': ([u'glad'], 1), 'redu': []}]

        for extracted_item, right_item in zip(data,right_data):
            #p(extracted_item,"extracted_item")
            #p(right_item,"right_item")
            extracted_item.should.be.equal(right_item)

        # for item in data:
        #     #p(len(item["baseline"][0]), "len")
        #     #if len(item["baseline"][0])>1:
        #     #p(item,"item")
        #     print "\n\n\n______\nitem\n_________"
        #     #p( item["syntagma"], c="r")
        #     print "\n__REPL___\n"
        #     for repl in item["repl"]:
        #         print repl
        #     print "\n__REDU___\n"
        #     for redu in item["redu"]:
        #         print redu
        #     print "\n__BASELINE___\n"
        #     print item["baseline"] 

        ### Case 4:
        syntagma = ["EMOIMG"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(22, 3333, u'[0, 15]', u'\U0001f62b^12', u'\U0001f62b', u'EMOIMG', u'["negative", -0.6999999999999998]', u'\U0001f62b', u'[]', 12, 0, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', u'', u'[]', u'', u'[]', u'', u'[]'), (32, 7777, u'[0, 7]', u'\U0001f62b^4', u'\U0001f62b', u'EMOIMG', u'["positive", 0.27]', u'\U0001f62b', u'[]', 4, 0, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), (39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]'), (40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = []
        right_baseline = [([u'\U0001f600'], 2), ([u'\U0001f62b', u',', u'but', u'i', u'realy'], 1), ([u'\U0001f308', u'\U0001f600'], 1), ([u'\U0001f62b', u'#shetlife'], 1), ([u'\U0001f62b'], 2), ([u'\U0001f62b', u',', u'but', u'i'], 1), ([u'\U0001f308'], 1), ([u'\U0001f600', u'\U0001f308'], 1), ([u'\U0001f62b', u',', u'but'], 1), ([u'\U0001f62b', u',', u'but', u'i', u'realy', u'liked'], 1), ([u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1), ([u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1), ([u'\U0001f62b', u','], 1)]
        right_syntagma = ['EMOIMG']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        # print "\n\n"
        # for r in right_repl:
        #     print r

        # print "\n\n"
        # for b in right_baseline:
        #     print b




        ### Case 5:
        syntagma = ["EMOIMG"]
        data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment="positive", syntagma_type="pos",search_just_in_full_repetativ_syntagma=True))
        #p(data,"data")

        # p(data[0]["repl"])
        # p(data[0]["redu"])
        # p(data[0]["baseline"])
        # p(data[0]["syntagma"])

        extracted_repl = data[0]["repl"]
        extracted_redu = data[0]["redu"]
        extracted_baseline = data[0]["baseline"]
        extracted_syntagma = data[0]["syntagma"]

        right_repl = [(32, 7777, u'[0, 7]', u'\U0001f62b^4', u'\U0001f62b', u'EMOIMG', u'["positive", 0.27]', u'\U0001f62b', u'[]', 4, 0, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), (39, 7777, u'[0, 18]', u'\U0001f600^5', u'\U0001f600', u'EMOIMG', u'["positive", 0.27]', u'\U0001f600', u'[]', 5, 0, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]'), (40, 7777, u'[0, 19]', u'\U0001f308^7', u'\U0001f308', u'EMOIMG', u'["positive", 0.27]', u'\U0001f308', u'[]', 7, 0, u'liked', u'["VBD"]', u'it', u'["PRP"]', u'=)', u'["EMOASC"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'', u'[]', u'', u'[]', u'', u'[]', u'', u'[]')]
        right_redu = []
        right_baseline = [([u'\U0001f600'], 2), ([u'\U0001f62b', u',', u'but', u'i', u'realy'], 1), ([u'\U0001f308', u'\U0001f600'], 1), ([u'\U0001f308'], 1), ([u'\U0001f62b', u',', u'but', u'i'], 1), ([u'\U0001f62b'], 2), ([u'\U0001f600', u'\U0001f308'], 1), ([u'\U0001f62b', u',', u'but'], 1), ([u'\U0001f62b', u',', u'but', u'i', u'realy', u'liked'], 1), ([u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1), ([u'\U0001f62b', u','], 1)]
        right_syntagma = ['EMOIMG']


        extracted_repl.should.be.equal(right_repl)
        extracted_redu.should.be.equal(right_redu)
        extracted_baseline.should.be.equal(right_baseline)
        extracted_syntagma.should.be.equal(right_syntagma)

        # print "\n\n"
        # for r in right_repl:
        #     print r

        # print "\n\n"
        # for b in right_baseline:
        #     print b








    #@attr(status='stable')
    #@wipd
    def test_test_export_generator_612(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"




        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))

        ## get for syntagma
        #syntagma = ["klitze","kleine"]
        syntagma = ["kleine"]
        #syntagma = "*"
        data = list(stats._export_generator(syntagma, repl=True, redu=True, baseline=True))
        p(data,"exportr_data")
        #p(data[0]["repl"],"repl")
        #p(data[0]["redu"],"redu")
        #p(data[0]["baseline"],"baseline")
        #data[0]["baseline"][0][1].should.be.equal(4)
        #for d in data:
        #   print d, "\n\n"
        #    #break

        #p(list(data[0]["repl"],))
        #p(list(data[0]["redu"],))
        #p(list(data[0]["baseline"],))
        #
        #syntagma = ["klitze","kleine"]
        #repls = list(stats._repl(syntagma))
        #redus = list(stats._redu(syntagma))
        #baseline = list(stats._baseline(syntagma))        

        # p(repls, "repls")
        # p(redus, "redus")
        # p(baseline, "baseline")
















    @attr(status='stable')
    #@wipd
    def test_clean_baseline_table_615(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"




        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        #stats.hhh()

        baseline_rownum_bevore = stats.statsdb.rownum("baseline")

        assert stats._clean_baseline_table()

        baseline_rownum_after = stats.statsdb.rownum("baseline")


        assert baseline_rownum_bevore > baseline_rownum_after







    @attr(status='stable')
    #@wipd
    def test_clean_baseline_table_616(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode, force_cleaning=True)
        stats = Stats(mode=self.mode, force_cleaning=True, case_sensitiv=False,use_cash=True)#, case_sensitiv=False)


        name = self.configer.init_info_data["blogger"]["name"]
        language = self.configer.init_info_data["blogger"]["language"]
        visibility = self.configer.init_info_data["blogger"]["visibility"]
        platform_name = self.configer.init_info_data["blogger"]["platform_name"]
        license = self.configer.init_info_data["blogger"]["license"]
        template_name = self.configer.init_info_data["blogger"]["template_name"]
        version = self.configer.init_info_data["blogger"]["version"]
        source = self.configer.init_info_data["blogger"]["source"]
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["stats"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "stats"




        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        #stats.hhh()

        

        assert stats.optimize_db()







    def get_dict_rows_from_csv(self,fname):
         with open(fname+".csv") as csvfile:
             readCSV = csv.reader(csvfile, delimiter=';')
             #print readCSV
             columns =  readCSV.next()
             for row in readCSV:
                 if row[0]:
                     #print(row)
                     yield {k:v for k,v in zip(columns, row)  if k}


    def get_list_rows_from_csv(self,fname):
         with open(fname+".csv") as csvfile:
             readCSV = csv.reader(csvfile, delimiter=';')
             #print readCSV
             columns =  readCSV.next()
             for row in readCSV:
                 if row[0]:
                     #print(row)
                     yield row

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







