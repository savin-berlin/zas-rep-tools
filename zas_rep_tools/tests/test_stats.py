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


#from zas_rep_tools.src.classes.configer import Configer
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
        #p(stats.statsdb.get_all_attr())
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
   

    @attr(status='stable')
    #@wipd
    def test_attach_corpdb_504(self):
        self.prj_folder()
        self.test_dbs()
        

        #p(encryption_key)
    

        ### plaintext
        stats = Stats(mode=self.mode)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))

        stats.attach_corpdb(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        assert stats.exist()
        #p(stats.attached_corpdb_number())
        assert stats.attached_corpdb_number() == 1


        ### excrypted
        encryption_key_corp = self.configer.init_info_data["twitter"]["encryption_key"]["corpus"]
        encryption_key_stats = self.configer.init_info_data["twitter"]["encryption_key"]["stats"]
        stats = Stats(mode=self.mode)
        stats.open(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_stats_de), encryption_key=encryption_key_stats)

        stats.attach_corpdb(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_corp_de), encryption_key=encryption_key_corp)

        assert stats.exist()
        #assert stats.attached_corpdb_number() == 1









###################    :550############################################ 
    #@attr(status='stable')
    #@wipd
    def test_single_stream_insert_550(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        #p(list(corp.docs()))

        stats = Stats(mode=self.mode)#, )
        stats.corp = corp
        stats._corp_info = corp.info()
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        #p(stats._add_context_columns("replications", 5,5))
        #p(stats._add_context_columns("reduplications",5,5))
        #stats._add_context_columns("reduplications")
        #p(stats.statsdb.col("replications"))
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
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode)#, )


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

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, case_sensitiv=True)
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
        #stats = Stats(mode=self.mode)
        


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
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                            (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                            (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                            (4, 8888, u'[4, 9]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u')', 4, 2, u'EMOASC', u'["positive", 0.5]', None, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None, None, None), 
                            (5, 8888, u'[4, 9]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u')', 3, 1, u'EMOASC', u'["positive", 0.5]', None, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', None, None, None, None, None, None, None, None, None, None)
                        ]
        list(stats.statsdb.getall("replications")).should.be.equal(right_output)



        # # ### ROW 2 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 9999, u'[7, 5, 5]', u'[0, 2]', u'[0, 2]', u'tag', u'ta^6g^6', u'a', 6, 1, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]'), 
                            (2, 9999, u'[7, 5, 5]', u'[0, 2]', u'[0, 2]', u'tag', u'ta^6g^6', u'g', 6, 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'einen', u'["ART"]', u'wundersch\xf6nen', u'["ADJA"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]'), 
                            (3, 9999, u'[7, 5, 5]', u'[1, 0]', u'[1, 0]', u'geniest', u'genie^11s^2t', u'e', 11, 4, u'NN', u'["neutral", 0.0]', None, u'tag', u'["NN"]', u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]'), 
                            (4, 9999, u'[7, 5, 5]', u'[1, 1]', u'[1, 1]', u'genist', u'geni^13st', u'i', 13, 3, u'VVFIN', u'["neutral", 0.0]', None, u'w\xfcnsche', u'["VVFIN"]', u'ich', u'["PPER"]', u'euch', u'["PRF"]', u'.', u'["symbol"]', u'geniest', u'["NN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]'), 
                            (5, 9999, u'[7, 5, 5]', u'[2, 0]', u'[2, 0]', u'bleibt', u'ble^8ibt', u'e', 8, 2, u'NN', u'["neutral", 0.0]', u'[2, 0]', u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None), 
                            (6, 9999, u'[7, 5, 5]', u'[2, 1]', u'[2, 0]', u'bleibt', u'ble^4ibt', u'e', 4, 2, u'NN', u'["neutral", 0.0]', u'[2, 0]', u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None), 
                            (7, 9999, u'[7, 5, 5]', u'[2, 2]', u'[2, 1]', u'hungrig', u'hu^12ngrig', u'u', 12, 1, u'NN', u'["neutral", 0.0]', None, u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None, None, None), 
                            (8, 9999, u'[7, 5, 5]', u'[2, 4]', u'[2, 3]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'leben', u'["NN"]', u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f308', u'["EMOIMG"]', None, None, None, None, None, None, None, None), 
                            (9, 9999, u'[7, 5, 5]', u'[2, 5]', u'[2, 4]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None, None, None)
                        ]
        list(stats.statsdb.getall("replications")).should.be.equal(right_output)


        
        # # ########### EN ##############

        # # ### ROW 1 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'r', 4, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'y', 5, 3, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (3, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'v', 3, 0, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (4, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'r', 8, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (5, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'pi^9ty', u'i', 9, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (6, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'i', 3, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (7, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u't', 3, 2, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (8, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'y', 3, 3, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (9, 1111, u'[4, 14]', u'[1, 13]', u'[1, 8]', u'.', u'.^6', u'.', 6, 0, u'symbol', u'["negative", -0.1875]', None, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), 
                            (10, 1111, u'[4, 14]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', None, None)
                        ]
        list(stats.statsdb.getall("replications")).should.be.equal(right_output)


        
        # # ### ROW 2 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 5555, u'[8, 2, 7]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), 
                            (2, 5555, u'[8, 2, 7]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), 
                            (3, 5555, u'[8, 2, 7]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', None, None), 
                            (4, 5555, u'[8, 2, 7]', u'[2, 6]', u'[2, 6]', u'?', u'?^4', u'?', 4, 0, u'symbol', u'["neutral", 0.0]', None, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', None, None, None, None, None, None, None, None, None, None)
                        ]

        list(stats.statsdb.getall("replications")).should.be.equal(right_output)



        ########################
        ####### many_rows ######
        ########################
        # # ### ROW 1 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'r', 4, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'y', 5, 3, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (3, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'v', 3, 0, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (4, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'r', 8, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (5, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'pi^9ty', u'i', 9, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (6, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'i', 3, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (7, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u't', 3, 2, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (8, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'y', 3, 3, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (9, 1111, u'[4, 14]', u'[1, 13]', u'[1, 8]', u'.', u'.^6', u'.', 6, 0, u'symbol', u'["negative", -0.1875]', None, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), 
                            (10, 1111, u'[4, 14]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', None, None), 
                            (11, 5555, u'[8, 2, 7]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), 
                            (12, 5555, u'[8, 2, 7]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), 
                            (13, 5555, u'[8, 2, 7]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', None, None), 
                            (14, 5555, u'[8, 2, 7]', u'[2, 6]', u'[2, 6]', u'?', u'?^4', u'?', 4, 0, u'symbol', u'["neutral", 0.0]', None, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', None, None, None, None, None, None, None, None, None, None)
                        ]
        stats.statsdb.getall("replications").should.be.equal(right_output)







    @attr(status='stable')
    #@wipd
    def test_extract_redu_lower_case_603(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode)#, )


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

        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, case_sensitiv=True)
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
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                            (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                        ]
        
        inserted_columns.should.be.equal(right_output)


        # ### ROW 2 ###

        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 8888, u'[7, 5, 5]', u'[2, 0]', u'[2, 0]', u'bleibt', u'{"ble^4ibt": 1, "ble^8ibt": 1}', 2, u'NN', u'["neutral", 0.0]', u'geniest', u'["NN"]', u'genist', u'["VVFIN"]', u'das', u'["ART"]', u'leben', u'["NN"]', u'.', u'["symbol"]', u'hungrig', u'["NN"]', u'.', u'["symbol"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None)
                        ]
        inserted_columns.should.be.equal(right_output)





        
        # ########### EN ##############
        # ### ROW 1 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                                (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', 3, u'JJ', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                                (2, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', 4, u'JJ', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]')
                        ]
        inserted_columns.should.be.equal(right_output)




        # ### ROW 2 ###
        stats = Stats(mode=self.mode, )#, )
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
        right_output = [
                            (1, 5555, u'[8, 2, 7]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')
                        ]

        inserted_columns.should.be.equal(right_output)








    @attr(status='stable')
    #@wipd
    def test_compute_baseline_lowercased_606(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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
    def test_temporize_baseline_lowercased_607_1(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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


        stats = Stats(mode=self.mode, )#, )
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
    def test_baseline_lazyinsertion_into_db_lowercased_607_2(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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


        stats = Stats(mode=self.mode, )#, )
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
        
        baseline_should_be_in_the_db = [(u'.', 1, 1, None, None, None, None, None, None), (u'\xfcberaschung++.', 1, 2, None, None, None, None, None, None), (u'klitze++kleine', 1, 2, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung', 1, 3, None, None, None, None, None, None), (u'klitze', 2, 1, None, None, None, None, None, None), (u'\xfcberaschung', 1, 1, None, None, None, None, None, None), (u'kleine', 1, 1, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.', 1, 3, None, None, None, None, None, None), (u'kleine++\xfcberaschung', 1, 2, None, None, None, None, None, None)]
        set(inserted_baseline).should.be.equal(set(baseline_should_be_in_the_db))
        


        ### One More Time
        #stats.temporized_baseline = temporized_baseline
        stats.baseline_lazyinsertion_into_db(computed_baseline,baseline_insertion_border=1)
        stats.baseline_lazyinsertion_into_db(computed_baseline, baseline_insertion_border=1)
        
        stats.baseline_insert_left_over_data()
        
        inserted_baseline = stats.statsdb.getall("baseline")
        #p(inserted_baseline, "inserted_baseline2")

        baseline_should_be_in_the_db = [(u'.', 3, 1, None, None, None, None, None, None), (u'\xfcberaschung++.', 3, 2, None, None, None, None, None, None), (u'klitze++kleine', 3, 2, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung', 3, 3, None, None, None, None, None, None), (u'klitze', 6, 1, None, None, None, None, None, None), (u'\xfcberaschung', 3, 1, None, None, None, None, None, None), (u'kleine', 3, 1, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.', 3, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.', 3, 3, None, None, None, None, None, None), (u'kleine++\xfcberaschung', 3, 2, None, None, None, None, None, None)]
        set(inserted_baseline).should.be.equal(set(baseline_should_be_in_the_db))
        





    @attr(status='stable')
    #@wipd
    def test_intern_compute_function_lower_case_608(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,status_bar=False)#, )


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

        redu.should.be.equal(
                                [
                                    (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                                ]
                            )
        
        repl.should.be.equal(
                                [
                                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                    (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                    (4, 8888, u'[4, 9]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u')', 4, 2, u'EMOASC', u'["positive", 0.5]', None, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None, None, None), 
                                    (5, 8888, u'[4, 9]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u')', 3, 1, u'EMOASC', u'["positive", 0.5]', None, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', None, None, None, None, None, None, None, None, None, None)
                                ]
                            )
        
        baseline.should.be.equal([(u'.++trotzdem', 1, 2, None, None, None, None, None, None), (u'!', 1, 1, None, None, None, None, None, None), (u'hat++sie++mich', 1, 3, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht++!', 1, 5, None, None, None, None, None, None), (u'gemacht++!', 1, 2, None, None, None, None, None, None), (u'gl\xfccklich++gemacht', 1, 2, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich', 1, 3, None, None, None, None, None, None), (u':-)', 1, 1, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!++:-)++-)', 1, 6, None, None, None, None, None, None), (u'gl\xfccklich', 1, 1, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!++:-)++-)', 1, 5, None, None, None, None, None, None), (u'.++trotzdem++hat++sie++mich++gl\xfccklich', 1, 6, None, None, None, None, None, None), (u'gemacht++!++:-)++-)', 1, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.++trotzdem++hat', 1, 6, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht', 1, 3, None, None, None, None, None, None), (u'gemacht', 1, 1, None, None, None, None, None, None), (u'!++:-)', 1, 2, None, None, None, None, None, None), (u'.++trotzdem++hat++sie++mich', 1, 5, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich++gl\xfccklich++gemacht', 1, 6, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem', 1, 3, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.++trotzdem', 1, 5, None, None, None, None, None, None), (u':-)++-)', 1, 2, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!', 1, 3, None, None, None, None, None, None), (u'\xfcberaschung++.', 1, 2, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich++gemacht', 1, 5, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich++gl\xfccklich', 1, 5, None, None, None, None, None, None), (u'klitze++kleine', 1, 2, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht++!++:-)', 1, 6, None, None, None, None, None, None), (u'\xfcberaschung', 1, 1, None, None, None, None, None, None), (u'trotzdem++hat++sie', 1, 3, None, None, None, None, None, None), (u'kleine', 2, 1, None, None, None, None, None, None), (u'-)', 1, 1, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich', 1, 4, None, None, None, None, None, None), (u'trotzdem++hat', 1, 2, None, None, None, None, None, None), (u'.', 1, 1, None, None, None, None, None, None), (u'trotzdem', 1, 1, None, None, None, None, None, None), (u'hat', 1, 1, None, None, None, None, None, None), (u'mich', 1, 1, None, None, None, None, None, None), (u'.++trotzdem++hat', 1, 3, None, None, None, None, None, None), (u'klitze', 2, 1, None, None, None, None, None, None), (u'hat++sie', 1, 2, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich++gemacht++!', 1, 6, None, None, None, None, None, None), (u'gemacht++!++:-)', 1, 3, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem++hat', 1, 5, None, None, None, None, None, None), (u'.++trotzdem++hat++sie', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem++hat++sie', 1, 6, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat++sie++mich', 1, 6, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!++:-)', 1, 5, None, None, None, None, None, None), (u'mich++gl\xfccklich', 1, 2, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat++sie', 1, 5, None, None, None, None, None, None), (u'sie++mich', 1, 2, None, None, None, None, None, None), (u'sie', 1, 1, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!++:-)', 1, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung', 1, 3, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat', 1, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.', 1, 4, None, None, None, None, None, None), (u'!++:-)++-)', 1, 3, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.', 1, 3, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht', 1, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung', 1, 2, None, None, None, None, None, None)])

        

        ##### SECOND INSETION
        stats._compute([copy.deepcopy(self.test_dict_row_de_1)])
        redu = stats.statsdb.getall("reduplications")
        repl = stats.statsdb.getall("replications")
        baseline = stats.statsdb.getall("baseline")

        # p(redu,"redu")
        # p(repl,"repl")
        #p(baseline,"baseline")
        #time.sleep(7)

        redu.should.be.equal(
                                [
                                   (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                                   (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                   (3, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                                   (4, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                                ]
                            )
        
        repl.should.be.equal(
                                [(1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (4, 8888, u'[4, 9]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u')', 4, 2, u'EMOASC', u'["positive", 0.5]', None, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None, None, None), (5, 8888, u'[4, 9]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u')', 3, 1, u'EMOASC', u'["positive", 0.5]', None, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', None, None, None, None, None, None, None, None, None, None), (6, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), (7, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (8, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), (9, 8888, u'[4, 9]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u')', 4, 2, u'EMOASC', u'["positive", 0.5]', None, u'sie', u'["PPER"]', u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None, None, None), (10, 8888, u'[4, 9]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u')', 3, 1, u'EMOASC', u'["positive", 0.5]', None, u'mich', u'["PPER"]', u'gl\xfccklich', u'["ADJD"]', u'gemacht', u'["VVPP"]', u'!', u'["symbol"]', u':-)', u'["EMOASC"]', None, None, None, None, None, None, None, None, None, None)]
                            )
        
        baseline.should.be.equal([(u'.++trotzdem', 2, 2, None, None, None, None, None, None), (u'!', 2, 1, None, None, None, None, None, None), (u'hat++sie++mich', 2, 3, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht++!', 2, 5, None, None, None, None, None, None), (u'gemacht++!', 2, 2, None, None, None, None, None, None), (u'gl\xfccklich++gemacht', 2, 2, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich', 2, 3, None, None, None, None, None, None), (u':-)', 2, 1, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!++:-)++-)', 2, 6, None, None, None, None, None, None), (u'gl\xfccklich', 2, 1, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!++:-)++-)', 2, 5, None, None, None, None, None, None), (u'.++trotzdem++hat++sie++mich++gl\xfccklich', 2, 6, None, None, None, None, None, None), (u'gemacht++!++:-)++-)', 2, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.++trotzdem++hat', 2, 6, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht', 2, 3, None, None, None, None, None, None), (u'gemacht', 2, 1, None, None, None, None, None, None), (u'!++:-)', 2, 2, None, None, None, None, None, None), (u'.++trotzdem++hat++sie++mich', 2, 5, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich++gl\xfccklich++gemacht', 2, 6, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem', 2, 3, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.++trotzdem', 2, 5, None, None, None, None, None, None), (u':-)++-)', 2, 2, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!', 2, 3, None, None, None, None, None, None), (u'\xfcberaschung++.', 2, 2, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich++gemacht', 2, 5, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich++gl\xfccklich', 2, 5, None, None, None, None, None, None), (u'klitze++kleine', 2, 2, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht++!++:-)', 2, 6, None, None, None, None, None, None), (u'\xfcberaschung', 2, 1, None, None, None, None, None, None), (u'trotzdem++hat++sie', 2, 3, None, None, None, None, None, None), (u'kleine', 4, 1, None, None, None, None, None, None), (u'-)', 2, 1, None, None, None, None, None, None), (u'trotzdem++hat++sie++mich', 2, 4, None, None, None, None, None, None), (u'trotzdem++hat', 2, 2, None, None, None, None, None, None), (u'.', 2, 1, None, None, None, None, None, None), (u'trotzdem', 2, 1, None, None, None, None, None, None), (u'hat', 2, 1, None, None, None, None, None, None), (u'mich', 2, 1, None, None, None, None, None, None), (u'.++trotzdem++hat', 2, 3, None, None, None, None, None, None), (u'klitze', 4, 1, None, None, None, None, None, None), (u'hat++sie', 2, 2, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich++gemacht++!', 2, 6, None, None, None, None, None, None), (u'gemacht++!++:-)', 2, 3, None, None, None, None, None, None), (u'hat++sie++mich++gl\xfccklich', 2, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem', 2, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem++hat', 2, 5, None, None, None, None, None, None), (u'.++trotzdem++hat++sie', 2, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.++trotzdem++hat++sie', 2, 6, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat++sie++mich', 2, 6, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!++:-)', 2, 5, None, None, None, None, None, None), (u'mich++gl\xfccklich', 2, 2, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat++sie', 2, 5, None, None, None, None, None, None), (u'sie++mich', 2, 2, None, None, None, None, None, None), (u'sie', 2, 1, None, None, None, None, None, None), (u'gl\xfccklich++gemacht++!++:-)', 2, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung', 2, 3, None, None, None, None, None, None), (u'\xfcberaschung++.++trotzdem++hat', 2, 4, None, None, None, None, None, None), (u'klitze++kleine++\xfcberaschung++.', 2, 4, None, None, None, None, None, None), (u'!++:-)++-)', 2, 3, None, None, None, None, None, None), (u'mich++gl\xfccklich++gemacht++!', 2, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung++.', 2, 3, None, None, None, None, None, None), (u'sie++mich++gl\xfccklich++gemacht', 2, 4, None, None, None, None, None, None), (u'kleine++\xfcberaschung', 2, 2, None, None, None, None, None, None)])

        # # ########### EN ##############

        
        ### ROW 2 ###
        stats = Stats(mode=self.mode,status_bar=False)#, )
        
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

        redu.should.be.equal(
                                [(1, 5555, u'[8, 2, 7]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]')]
                            )

        repl.should.be.equal(
                                [(1, 5555, u'[8, 2, 7]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), (2, 5555, u'[8, 2, 7]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), (3, 5555, u'[8, 2, 7]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', None, None), (4, 5555, u'[8, 2, 7]', u'[2, 6]', u'[2, 6]', u'?', u'?^4', u'?', 4, 0, u'symbol', u'["neutral", 0.0]', None, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', None, None, None, None, None, None, None, None, None, None)]
                            )
        
        baseline.should.be.equal([(u'model', 1, 1, None, None, None, None, None, None), (u'but++a++big++explanation++.++right', 1, 6, None, None, None, None, None, None), (u'what', 1, 1, None, None, None, None, None, None), (u'do++you++think++about', 1, 4, None, None, None, None, None, None), (u'a++big', 1, 2, None, None, None, None, None, None), (u'it', 1, 1, None, None, None, None, None, None), (u'but', 1, 1, None, None, None, None, None, None), (u'you++think', 1, 2, None, None, None, None, None, None), (u',++but++a++big++explanation++.', 1, 6, None, None, None, None, None, None), (u'what++do++you++think++about++it', 1, 6, None, None, None, None, None, None), (u'big++explanation++.++right++?++what', 1, 6, None, None, None, None, None, None), (u'you++think++about++it++?', 1, 5, None, None, None, None, None, None), (u'?++what++do', 1, 3, None, None, None, None, None, None), (u'what++do++you', 1, 3, None, None, None, None, None, None), (u'but++a++big++explanation++.', 1, 5, None, None, None, None, None, None), (u',++but++a', 1, 3, None, None, None, None, None, None), (u'model++,', 1, 2, None, None, None, None, None, None), (u'?++what++do++you++think++about', 1, 6, None, None, None, None, None, None), (u'what++do++you++think', 1, 4, None, None, None, None, None, None), (u'right++?++what++do', 1, 4, None, None, None, None, None, None), (u'what++do', 1, 2, None, None, None, None, None, None), (u'.++right++?++what', 1, 4, None, None, None, None, None, None), (u'but++a++big', 1, 3, None, None, None, None, None, None), (u'tiny', 1, 1, None, None, None, None, None, None), (u'tiny++model', 1, 2, None, None, None, None, None, None), (u'think++about', 1, 2, None, None, None, None, None, None), (u'explanation++.++right++?++what', 1, 5, None, None, None, None, None, None), (u'model++,++but++a++big++explanation', 1, 6, None, None, None, None, None, None), (u'a++big++explanation', 1, 3, None, None, None, None, None, None), (u'explanation++.++right++?++what++do', 1, 6, None, None, None, None, None, None), (u'?++what', 1, 2, None, None, None, None, None, None), (u'right', 1, 1, None, None, None, None, None, None), (u'big++explanation++.++right++?', 1, 5, None, None, None, None, None, None), (u'it++?', 1, 2, None, None, None, None, None, None), (u'what++do++you++think++about', 1, 5, None, None, None, None, None, None), (u'explanation++.++right', 1, 3, None, None, None, None, None, None), (u'.', 1, 1, None, None, None, None, None, None), (u'you', 1, 1, None, None, None, None, None, None), (u'?', 2, 1, None, None, None, None, None, None), (u'explanation++.++right++?', 1, 4, None, None, None, None, None, None), (u'tiny++model++,++but', 1, 4, None, None, None, None, None, None), (u'do++you++think++about++it', 1, 5, None, None, None, None, None, None), (u'big++explanation++.', 1, 3, None, None, None, None, None, None), (u'.++right', 1, 2, None, None, None, None, None, None), (u'explanation++.', 1, 2, None, None, None, None, None, None), (u'model++,++but++a', 1, 4, None, None, None, None, None, None), (u'you++think++about', 1, 3, None, None, None, None, None, None), (u'?++what++do++you', 1, 4, None, None, None, None, None, None), (u'explanation', 1, 1, None, None, None, None, None, None), (u'do++you++think++about++it++?', 1, 6, None, None, None, None, None, None), (u'do++you++think', 1, 3, None, None, None, None, None, None), (u'model++,++but', 1, 3, None, None, None, None, None, None), (u'tiny++model++,++but++a', 1, 5, None, None, None, None, None, None), (u'right++?', 1, 2, None, None, None, None, None, None), (u'model++,++but++a++big', 1, 5, None, None, None, None, None, None), (u'think++about++it', 1, 3, None, None, None, None, None, None), (u',', 1, 1, None, None, None, None, None, None), (u',++but++a++big++explanation', 1, 5, None, None, None, None, None, None), (u',++but', 1, 2, None, None, None, None, None, None), (u'about', 1, 1, None, None, None, None, None, None), (u'tiny++model++,++but++a++big', 1, 6, None, None, None, None, None, None), (u'right++?++what', 1, 3, None, None, None, None, None, None), (u'a++big++explanation++.++right', 1, 5, None, None, None, None, None, None), (u'tiny++model++,', 1, 3, None, None, None, None, None, None), (u'right++?++what++do++you++think', 1, 6, None, None, None, None, None, None), (u'about++it++?', 1, 3, None, None, None, None, None, None), (u'?++what++do++you++think', 1, 5, None, None, None, None, None, None), (u'about++it', 1, 2, None, None, None, None, None, None), (u'.++right++?', 1, 3, None, None, None, None, None, None), (u'you++think++about++it', 1, 4, None, None, None, None, None, None), (u'do++you', 1, 2, None, None, None, None, None, None), (u'.++right++?++what++do', 1, 5, None, None, None, None, None, None), (u'big++explanation++.++right', 1, 4, None, None, None, None, None, None), (u'a', 1, 1, None, None, None, None, None, None), (u'.++right++?++what++do++you', 1, 6, None, None, None, None, None, None), (u'think', 1, 1, None, None, None, None, None, None), (u'think++about++it++?', 1, 4, None, None, None, None, None, None), (u'big', 3, 1, None, None, None, None, None, None), (u'big++explanation', 1, 2, None, None, None, None, None, None), (u'right++?++what++do++you', 1, 5, None, None, None, None, None, None), (u'but++a++big++explanation', 1, 4, None, None, None, None, None, None), (u'do', 1, 1, None, None, None, None, None, None), (u'a++big++explanation++.', 1, 4, None, None, None, None, None, None), (u'a++big++explanation++.++right++?', 1, 6, None, None, None, None, None, None), (u'but++a', 1, 2, None, None, None, None, None, None), (u',++but++a++big', 1, 4, None, None, None, None, None, None)])

    





    @attr(status='stable')
    #@wipd
    def test_get_streams_from_corp_609(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode, )#, )


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
    def test_preprocess_610(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        

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


        #######without_closing_db_at_the_end #########
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version,
                    encryption_key=encryption_key,
                    ignore_hashtag=True, force_cleaning=True,
                    ignore_url=True,  ignore_mention=True, ignore_punkt=True, ignore_num=True)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        #stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        stats.corp = corp
        stats._corp_info  = stats.corp.info()
        stats._init_insertion_variables()
        stats._compute_cleaning_flags()
        text_elem = [[[[u'I', u'PRP'], [u'loved', u'VBD'], [u'it', u'PRP'], [u'.', u'symbol']], [u'positive', 0.7]], [[[u'But', u'CC'], [u'it', u'PRP'], [u'was', u'VBD'], [u'also', u'RB'], [u'verrrryyyyy', u'JJ'], [u'vvveRRRRRRrry', u'NNP'], [u'very', u'RB'], [u'piiiiiiiiity', u'JJ'], [u'pity', u'NN'], [u'pity', u'NN'], [u'piiitttyyy', u'NN'], [u'for', u'IN'], [u'me', u'PRP'], [u'......', u'symbol'], [u':-(((((', u'EMOASC'], [u'@real_trump', u'mention'], [u'#sheetlife', u'hashtag'], [u'#readytogo', u'hashtag'], [u'http://www.absurd.com', u'URL']], [u'negative', -0.1875]]]

        results = stats._preprocess(text_elem)
        #p(results, "results")
        right_results = [([[u'I', u'PRP'], [u'loved', u'VBD'], [u'it', u'PRP'], (None, ':symbol:')], [u'positive', 0.7]), ([[u'But', u'CC'], [u'it', u'PRP'], [u'was', u'VBD'], [u'also', u'RB'], [u'verrrryyyyy', u'JJ'], [u'vvveRRRRRRrry', u'NNP'], [u'very', u'RB'], [u'piiiiiiiiity', u'JJ'], [u'pity', u'NN'], [u'pity', u'NN'], [u'piiitttyyy', u'NN'], [u'for', u'IN'], [u'me', u'PRP'], (None, ':symbol:'), [u':-(((((', u'EMOASC'], (None, ':mention:'), (None, ':hashtag:'), (None, ':hashtag:'), (None, ':URL:')], [u'negative', -0.1875])]
        results.should.be.equal(right_results)






    @attr(status='stable')
    #@wipd
    def test_main_compute_function_lower_case_for_1_stream__610_1(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        right_repls = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'r', 4, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'y', 5, 3, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (3, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'v', 3, 0, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (4, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'r', 8, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (5, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'pi^9ty', u'i', 9, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (6, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'i', 3, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (7, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u't', 3, 2, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (8, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'y', 3, 3, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (9, 1111, u'[4, 14]', u'[1, 13]', u'[1, 8]', u'.', u'.^6', u'.', 6, 0, u'symbol', u'["negative", -0.1875]', None, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), 
                            (10, 1111, u'[4, 14]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', None, None), 
                            (11, 2222, u'[5]', u'[0, 0]', u'[0, 0]', u'glad', u'gla^7d', u'a', 7, 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, None, u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', None, None), 
                            (12, 2222, u'[5]', u'[0, 2]', u'[0, 2]', u'se', u'se^9', u'e', 9, 1, u'VB', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'glad', u'["NN"]', u'to', u'["TO"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None), 
                            (13, 2222, u'[5]', u'[0, 4]', u'[0, 4]', u'-)', u'-)^4', u')', 4, 1, u'EMOASC', u'["neutral", 0.0]', None, None, None, u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', None, None, None, None, None, None, None, None, None, None), 
                            (14, 3333, u'[14]', u'[0, 1]', u'[0, 1]', u'bad', u'bad^5', u'd', 5, 2, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (15, 3333, u'[14]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'b', 7, 0, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (16, 3333, u'[14]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'a', 6, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (17, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'b', 4, 0, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (18, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'a', 4, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (19, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'd', 5, 2, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (20, 3333, u'[14]', u'[0, 5]', u'[0, 1]', u'bad', u'ba^7d', u'a', 7, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (21, 3333, u'[14]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'(', 4, 1, u'EMOASC', u'["negative", -0.6999999999999998]', None, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None), 
                            (22, 3333, u'[14]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.6999999999999998]', None, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None), 
                            (23, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'o', 7, 1, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), 
                            (24, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'l', 7, 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), 
                            (25, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'bi^3g', u'i', 3, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (26, 4444, u'[13]', u'[0, 16]', u'[0, 10]', u'big', u'bi^15g', u'i', 15, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (27, 5555, u'[8, 2, 11, 4]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), 
                            (28, 5555, u'[8, 2, 11, 4]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), 
                            (29, 5555, u'[8, 2, 11, 4]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]'), 
                            (30, 5555, u'[8, 2, 11, 4]', u'[2, 6]', u'[2, 6]', u'?', u'?^4', u'?', 4, 0, u'symbol', u'["neutral", 0.0]', None, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]'), 
                            (31, 5555, u'[8, 2, 11, 4]', u'[2, 7]', u'[2, 7]', u'1', u'1^6', u'1', 6, 0, u'number', u'["neutral", 0.0]', None, u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]'), 
                            (32, 5555, u'[8, 2, 11, 4]', u'[2, 8]', u'[2, 8]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]'), 
                            (33, 5555, u'[8, 2, 11, 4]', u'[2, 9]', u'[2, 9]', u'1', u'1^8', u'1', 8, 0, u'number', u'["neutral", 0.0]', None, u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]'), 
                            (34, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (35, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'u', 4, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (36, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (37, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (38, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (39, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'y^6ou', u'y', 6, 0, u'NN', u'["neutral", 0.0]', u'[3, 2]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (40, 5555, u'[8, 2, 11, 4]', u'[3, 3]', u'[3, 1]', u'you', u'yo^6u', u'o', 6, 1, u'NN', u'["neutral", 0.0]', u'[3, 2]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (41, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'b^6ut', u'b', 6, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (42, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (43, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u't', 4, 2, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (44, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (45, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'u', 5, 1, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (46, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'y', 3, 0, u'FW', u'["neutral", 0.0]', None, 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', None, None, None, None, None, None, None, None, None, None), 
                            (47, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'u', 4, 2, u'FW', u'["neutral", 0.0]', None, 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', None, None, None, None, None, None, None, None, None, None), 
                            (48, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'tin^3y^2', u'n', 3, 2, u'JJ', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]'), 
                            (49, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'b^5ut', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (50, 6666, u'[3, 9]', u'[1, 1]', u'[1, 0]', u'but', u'bu^5t', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (51, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'y^6ou', u'y', 6, 0, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (52, 6666, u'[3, 9]', u'[1, 3]', u'[1, 1]', u'you', u'yo^6u', u'o', 6, 1, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (53, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'b^6ut', u'b', 6, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (54, 6666, u'[3, 9]', u'[1, 5]', u'[1, 2]', u'but', u'b^5ut', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (55, 6666, u'[3, 9]', u'[1, 6]', u'[1, 2]', u'but', u'b^5ut', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (56, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'y', 3, 0, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (57, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'u', 4, 2, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (58, 6666, u'[3, 9]', u'[1, 8]', u'[1, 4]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None), 
                            (59, 6666, u'[3, 9]', u'[1, 9]', u'[1, 5]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None), 
                            (60, 6666, u'[3, 9]', u'[1, 10]', u'[1, 6]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None), 
                            (61, 6666, u'[3, 9]', u'[1, 11]', u'[1, 7]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None), 
                            (62, 6666, u'[3, 9]', u'[1, 12]', u'[1, 8]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None, None, None, None, None, None, None, None, None), 
                            (63, 7777, u'[19]', u'[0, 7]', u'[0, 7]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), 
                            (64, 7777, u'[19]', u'[0, 9]', u'[0, 9]', u'but', u'bu^10t', u'u', 10, 1, u'MD', u'["positive", 0.27]', None, u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]'), 
                            (65, 7777, u'[19]', u'[0, 12]', u'[0, 11]', u'realy', u'real^3y', u'l', 3, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (66, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'e', 5, 1, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (67, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'l', 4, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (68, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'y', 3, 4, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None), 
                            (70, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None), 
                            (71, 7777, u'[19]', u'[0, 19]', u'[0, 17]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["positive", 0.27]', None, u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None)
                        ]




        right_redus = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', 3, u'JJ', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', 4, u'JJ', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (3, 3333, u'[14]', u'[0, 1]', u'[0, 1]', u'bad', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', 5, u'JJ', u'["negative", -0.6999999999999998]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (4, 3333, u'[14]', u'[0, 16]', u'[0, 12]', u'#shetlife', u'{"#shetlife": 2}', 2, u'hashtag', u'["negative", -0.6999999999999998]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'\U0001f62b', u'["EMOIMG"]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None, None, None), 
                            (5, 4444, u'[13]', u'[0, 0]', u'[0, 0]', u'tiny', u'{"tiny": 6}', 6, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'model', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (6, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'{"bi^3g": 1, "bi^15g": 1}', 2, u'NN', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (7, 5555, u'[8, 2, 11, 4]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'), 
                            (8, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'{"bu^5t^4": 1, "b^5u^4t^4": 1}', 2, u'NNP', u'["neutral", 0.0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (9, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'NN', u'["neutral", 0.0]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (10, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'{"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}', 3, u'FW', u'["neutral", 0.0]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (11, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'{"tin^3y^2": 1, "tiny": 2}', 3, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]'), 
                            (12, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'{"bu^5t": 1, "b^5ut": 1}', 2, u'NNP', u'["neutral", 0.0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (13, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'JJ', u'["neutral", 0.0]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (14, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'{"b^6ut": 1, "b^5ut": 2}', 3, u'CC', u'["neutral", 0.0]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (15, 7777, u'[19]', u'[0, 11]', u'[0, 11]', u'realy', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', 3, u'RB', u'["positive", 0.27]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')
                        ]




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


        #######without_closing_db_at_the_end #########
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")


        repls.should.be.equal(right_repls)
        redus.should.be.equal(right_redus)

 
        #######with_closing_db_at_the_end #########

        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=True)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")

        repls.should.be.equal(right_repls)
        redus.should.be.equal(right_redus)




    @attr(status='stable')
    #@wipd
    def test_main_compute_function_lower_case_for_1_stream_with_preprocessing_610_2(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        right_repls = [
                  (1, 1111, u'[4, 13]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'veri', u'r', 4, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]'), 
                  (2, 1111, u'[4, 13]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'veri', u'y', 5, 3, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]'), 
                  (3, 1111, u'[4, 13]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'veri', u'v', 3, 0, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]'), 
                  (4, 1111, u'[4, 13]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'veri', u'r', 8, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]'), 
                  (5, 1111, u'[4, 13]', u'[1, 7]', u'[1, 5]', u'pity', u'pi^9ty', u'piti', u'i', 9, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]'), 
                  (6, 1111, u'[4, 13]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'piti', u'i', 3, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]'), 
                  (7, 1111, u'[4, 13]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'piti', u't', 3, 2, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]'), 
                  (8, 1111, u'[4, 13]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'piti', u'y', 3, 3, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]'), 
                  (9, 1111, u'[4, 13]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u':-(', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':mention:', u'[":mention:", null, ":mention:"]', u':hashtag:', u'[":hashtag:", {":hashtag:": 2}, ":hashtag:"]', u':URL:', u'[":URL:", null, ":URL:"]', None, None, None, None), 
                  (10, 2222, u'[5]', u'[0, 0]', u'[0, 0]', u'glad', u'gla^7d', u'glad', u'a', 7, 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, None, u'to', u'["TO", null, "to"]', u'se', u'["VB", null, "se"]', u'you', u'["PRP", null, "you"]', u'-)', u'["EMOASC", null, "-)"]', None, None), 
                  (11, 2222, u'[5]', u'[0, 2]', u'[0, 2]', u'se', u'se^9', u'se', u'e', 9, 1, u'VB', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'glad', u'["NN", null, "glad"]', u'to', u'["TO", null, "to"]', u'you', u'["PRP", null, "you"]', u'-)', u'["EMOASC", null, "-)"]', None, None, None, None, None, None), 
                  (12, 2222, u'[5]', u'[0, 4]', u'[0, 4]', u'-)', u'-)^4', u'-)', u')', 4, 1, u'EMOASC', u'["neutral", 0.0]', None, None, None, u'glad', u'["NN", null, "glad"]', u'to', u'["TO", null, "to"]', u'se', u'["VB", null, "se"]', u'you', u'["PRP", null, "you"]', None, None, None, None, None, None, None, None, None, None), 
                  (13, 3333, u'[15]', u'[0, 1]', u'[0, 1]', u'bad', u'bad^5', u'bad', u'd', 5, 2, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (14, 3333, u'[15]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'bad', u'b', 7, 0, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (15, 3333, u'[15]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'bad', u'a', 6, 1, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (16, 3333, u'[15]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'bad', u'b', 4, 0, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (17, 3333, u'[15]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'bad', u'a', 4, 1, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (18, 3333, u'[15]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'bad', u'd', 5, 2, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (19, 3333, u'[15]', u'[0, 5]', u'[0, 1]', u'bad', u'ba^7d', u'bad', u'a', 7, 1, u'JJ', u'["negative", -0.7249999999999999]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                  (20, 3333, u'[15]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'-(', u'(', 4, 1, u'EMOASC', u'["negative", -0.7249999999999999]', None, u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]', u'not', u'["RB", null, "not"]', u'acept', u'["VB", null, "acept"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':-(', u'["EMOASC", null, ":-("]', u':hashtag:', u'[":hashtag:", {":hashtag:": 2}, ":hashtag:"]', u':URL:', u'[":URL:", null, ":URL:"]', None, None), 
                  (21, 3333, u'[15]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.7249999999999999]', None, u'can', u'["MD", null, "can"]', u'not', u'["RB", null, "not"]', u'acept', u'["VB", null, "acept"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'-(', u'["EMOASC", null, "-("]', u':-(', u'["EMOASC", null, ":-("]', u':hashtag:', u'[":hashtag:", {":hashtag:": 2}, ":hashtag:"]', u':URL:', u'[":URL:", null, ":URL:"]', None, None, None, None), 
                  (22, 3333, u'[15]', u'[0, 16]', u'[0, 12]', u':-(', u':-(^5', u':-(', u'(', 5, 2, u'EMOASC', u'["negative", -0.7249999999999999]', None, u'not', u'["RB", null, "not"]', u'acept', u'["VB", null, "acept"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'-(', u'["EMOASC", null, "-("]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':hashtag:', u'[":hashtag:", {":hashtag:": 2}, ":hashtag:"]', u':URL:', u'[":URL:", null, ":URL:"]', None, None, None, None, None, None), 
                  (23, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'model', u'o', 7, 1, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}, "tini"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]', u'use', u'["VB", null, "use"]'), 
                  (24, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'model', u'l', 7, 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}, "tini"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]', u'use', u'["VB", null, "use"]'), 
                  (25, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'bi^3g', u'big', u'i', 3, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD", null, "can"]', u'use', u'["VB", null, "use"]', u'for', u'["IN", null, "for"]', u'explain', u'["VB", null, "explain"]', u'a', u'["DT", null, "a"]', u'things', u'["NNS", null, "thing"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', None, None, None, None, None, None), 
                  (26, 4444, u'[13]', u'[0, 16]', u'[0, 10]', u'big', u'bi^15g', u'big', u'i', 15, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD", null, "can"]', u'use', u'["VB", null, "use"]', u'for', u'["IN", null, "for"]', u'explain', u'["VB", null, "explain"]', u'a', u'["DT", null, "a"]', u'things', u'["NNS", null, "thing"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', None, None, None, None, None, None), 
                  (27, 5555, u'[8, 2, 11, 4]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'explan', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN", null, "model"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'a', u'["DT", null, "a"]', u'big', u'["JJ", {"big": 3}, "big"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'right', u'["UH", null, "right"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'what', u'["WP", null, "what"]', u'do', u'["VBP", null, "do"]'), 
                  (28, 5555, u'[8, 2, 11, 4]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'right', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC", null, "but"]', u'a', u'["DT", null, "a"]', u'big', u'["JJ", {"big": 3}, "big"]', u'explanation', u'["NN", null, "explan"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'what', u'["WP", null, "what"]', u'do', u'["VBP", null, "do"]', u'you', u'["PRP", null, "you"]', u'think', u'["VB", null, "think"]'), 
                  (29, 5555, u'[8, 2, 11, 4]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'you', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u':symbol:', u'[":symbol:", null, ":symbol:"]', u'right', u'["UH", null, "right"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'what', u'["WP", null, "what"]', u'do', u'["VBP", null, "do"]', u'think', u'["VB", null, "think"]', u'about', u'["IN", null, "about"]', u'it', u'["PRP", null, "it"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]'), 
                  (30, 5555, u'[8, 2, 11, 4]', u'[2, 8]', u'[2, 8]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'think', u'["VB", null, "think"]', u'about', u'["IN", null, "about"]', u'it', u'["PRP", null, "it"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]'), 
                  (31, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'but', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                  (32, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'but', u'u', 4, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                  (33, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'but', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                  (34, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u'but', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                  (35, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u'but', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                  (36, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'y^6ou', u'you', u'y', 6, 0, u'NN', u'["neutral", 0.0]', u'[3, 2]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None), 
                  (37, 5555, u'[8, 2, 11, 4]', u'[3, 3]', u'[3, 1]', u'you', u'yo^6u', u'you', u'o', 6, 1, u'NN', u'["neutral", 0.0]', u'[3, 2]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None), 
                  (38, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'b^6ut', u'but', u'b', 6, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                  (39, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u'but', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                  (40, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u'but', u't', 4, 2, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                  (41, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'but', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                  (42, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'but', u'u', 5, 1, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                  (43, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'you', u'y', 3, 0, u'FW', u'["neutral", 0.0]', None, u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', None, None, None, None, None, None, None, None, None, None), 
                  (44, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'you', u'u', 4, 2, u'FW', u'["neutral", 0.0]', None, u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', None, None, None, None, None, None, None, None, None, None), 
                  (45, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'tin^3y^2', u'tini', u'n', 3, 2, u'JJ', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]'), 
                  (46, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'b^5ut', u'but', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                  (47, 6666, u'[3, 9]', u'[1, 1]', u'[1, 0]', u'but', u'bu^5t', u'but', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                  (48, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'y^6ou', u'you', u'y', 6, 0, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (49, 6666, u'[3, 9]', u'[1, 3]', u'[1, 1]', u'you', u'yo^6u', u'you', u'o', 6, 1, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (50, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'b^6ut', u'but', u'b', 6, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                  (51, 6666, u'[3, 9]', u'[1, 5]', u'[1, 2]', u'but', u'b^5ut', u'but', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                  (52, 6666, u'[3, 9]', u'[1, 6]', u'[1, 2]', u'but', u'b^5ut', u'but', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                  (53, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'you', u'y', 3, 0, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (54, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'you', u'u', 4, 2, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (55, 6666, u'[3, 9]', u'[1, 8]', u'[1, 4]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None), 
                  (56, 6666, u'[3, 9]', u'[1, 9]', u'[1, 5]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None), 
                  (57, 6666, u'[3, 9]', u'[1, 10]', u'[1, 6]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None), 
                  (58, 6666, u'[3, 9]', u'[1, 11]', u'[1, 7]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None), 
                  (59, 6666, u'[3, 9]', u'[1, 12]', u'[1, 8]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', None, None, None, None, None, None, None, None, None, None), 
                  (60, 7777, u'[19]', u'[0, 7]', u'[0, 7]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", null, "reali"]', u'bad', u'["JJ", null, "bad"]', u'surprise', u'["NN", null, "surpris"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}, "reali"]', u'liked', u'["VBD", null, "like"]'), 
                  (61, 7777, u'[19]', u'[0, 9]', u'[0, 9]', u'but', u'bu^10t', u'but', u'u', 10, 1, u'MD', u'["positive", 0.27]', None, u'surprise', u'["NN", null, "surpris"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'i', u'["PRP", null, "i"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}, "reali"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]'), 
                  (62, 7777, u'[19]', u'[0, 12]', u'[0, 11]', u'realy', u'real^3y', u'reali', u'l', 3, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (63, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'reali', u'e', 5, 1, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (64, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'reali', u'l', 4, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (65, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'reali', u'y', 3, 4, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                  (66, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u'=)', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP", null, "i"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}, "reali"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None), 
                  (67, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}, "reali"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None), 
                  (68, 7777, u'[19]', u'[0, 19]', u'[0, 17]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', u'\U0001f308', 7, 0, u'EMOIMG', u'["positive", 0.27]', None, u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None)

            ]






        right_redus = [
                        (1, 1111, u'[4, 13]', u'[1, 4]', u'[1, 4]', u'very', u'veri', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', 3, u'JJ', u'["negative", -0.1875]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}, "piti"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]'), 
                        (2, 1111, u'[4, 13]', u'[1, 7]', u'[1, 5]', u'pity', u'piti', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', 4, u'JJ', u'["negative", -0.1875]', u'but', u'["CC", null, "but"]', u'it', u'["PRP", null, "it"]', u'was', u'["VBD", null, "was"]', u'also', u'["RB", null, "also"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}, "veri"]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]'), 
                        (3, 1111, u'[4, 13]', u'[1, 16]', u'[1, 11]', u':hashtag:', u':hashtag:', u'{":hashtag:": 2}', 2, u':hashtag:', u'["negative", -0.1875]', u'for', u'["IN", null, "for"]', u'me', u'["PRP", null, "me"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':-(', u'["EMOASC", null, ":-("]', u':mention:', u'[":mention:", null, ":mention:"]', u':URL:', u'[":URL:", null, ":URL:"]', None, None, None, None, None, None, None, None), 
                        (4, 3333, u'[15]', u'[0, 1]', u'[0, 1]', u'bad', u'bad', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', 5, u'JJ', u'["negative", -0.7249999999999999]', None, None, None, None, None, None, None, None, u'a', u'["DT", null, "a"]', u'news', u'["NN", null, "news"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                        (5, 3333, u'[15]', u'[0, 17]', u'[0, 13]', u':hashtag:', u':hashtag:', u'{":hashtag:": 2}', 2, u':hashtag:', u'["negative", -0.7249999999999999]', u'acept', u'["VB", null, "acept"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'-(', u'["EMOASC", null, "-("]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':-(', u'["EMOASC", null, ":-("]', u':URL:', u'[":URL:", null, ":URL:"]', None, None, None, None, None, None, None, None), 
                        (6, 4444, u'[13]', u'[0, 0]', u'[0, 0]', u'tiny', u'tini', u'{"tiny": 6}', 6, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'model', u'["NN", null, "model"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'which', u'["WDT", null, "which"]', u'we', u'["PRP", null, "we"]', u'can', u'["MD", null, "can"]'), 
                        (7, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'big', u'{"bi^3g": 1, "bi^15g": 1}', 2, u'NN', u'["neutral", 0.0]', u'can', u'["MD", null, "can"]', u'use', u'["VB", null, "use"]', u'for', u'["IN", null, "for"]', u'explain', u'["VB", null, "explain"]', u'a', u'["DT", null, "a"]', u'things', u'["NNS", null, "thing"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', None, None, None, None, None, None), 
                        (8, 5555, u'[8, 2, 11, 4]', u'[0, 5]', u'[0, 5]', u'big', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ", null, "tini"]', u'model', u'["NN", null, "model"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["CC", null, "but"]', u'a', u'["DT", null, "a"]', u'explanation', u'["NN", null, "explan"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'right', u'["UH", null, "right"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'what', u'["WP", null, "what"]'), 
                        (9, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'but', u'{"bu^5t^4": 1, "b^5u^4t^4": 1}', 2, u'NNP', u'["neutral", 0.0]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None), 
                        (10, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'NN', u'["neutral", 0.0]', u':number:', u'[":number:", null, ":number:"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}, "but"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None), 
                        (11, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'but', u'{"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}', 3, u'FW', u'["neutral", 0.0]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':number:', u'[":number:", null, ":number:"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}, "but"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["FW", null, "you"]', None, None, None, None, None, None, None, None), 
                        (12, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'tini', u'{"tin^3y^2": 1, "tiny": 2}', 3, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]'), 
                        (13, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'but', u'{"bu^5t": 1, "b^5ut": 1}', 2, u'NNP', u'["neutral", 0.0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                        (14, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'JJ', u'["neutral", 0.0]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}, "but"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]'), 
                        (15, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'but', u'{"b^6ut": 1, "b^5ut": 2}', 3, u'CC', u'["neutral", 0.0]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}, "tini"]', u'surprise', u'["NN", null, "surpris"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}, "but"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}, "you"]', u'you', u'["VBD", null, "you"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'\U0001f308', u'["EMOIMG", null, "\\ud83c\\udf08"]'), 
                        (16, 7777, u'[19]', u'[0, 11]', u'[0, 11]', u'realy', u'reali', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', 3, u'RB', u'["positive", 0.27]', u'me', u'["PRP", null, "me"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u':symbol:', u'[":symbol:", null, ":symbol:"]', u'but', u'["MD", null, "but"]', u'i', u'["PRP", null, "i"]', u'liked', u'["VBD", null, "like"]', u'it', u'["PRP", null, "it"]', u':p', u'["EMOASC", null, ":p"]', u'=)', u'["EMOASC", null, "=)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]')


            ]


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


        #######without_closing_db_at_the_end #########
        stats = Stats(mode=self.mode,use_cash=True,status_bar=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version,
                    encryption_key=encryption_key,
                    ignore_hashtag=True, force_cleaning=True,
                    ignore_url=True,  ignore_mention=True, ignore_punkt=True, ignore_num=True)


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")


        repls.should.be.equal(right_repls)
        redus.should.be.equal(right_redus)





    @attr(status='stable')
    #@wipd
    def test_main_compute_function_lower_case_for_4_streams_610_3(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        right_repls = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'r', 4, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'ver^4y^5', u'y', 5, 3, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (3, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'v', 3, 0, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (4, 1111, u'[4, 14]', u'[1, 5]', u'[1, 4]', u'very', u'v^3er^8y', u'r', 8, 2, u'JJ', u'["negative", -0.1875]', u'[1, 4]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (5, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'pi^9ty', u'i', 9, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (6, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'i', 3, 1, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (7, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u't', 3, 2, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (8, 1111, u'[4, 14]', u'[1, 10]', u'[1, 5]', u'pity', u'pi^3t^3y^3', u'y', 3, 3, u'JJ', u'["negative", -0.1875]', u'[1, 7]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (9, 1111, u'[4, 14]', u'[1, 13]', u'[1, 8]', u'.', u'.^6', u'.', 6, 0, u'symbol', u'["negative", -0.1875]', None, u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]'), 
                            (10, 1111, u'[4, 14]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', None, None), 
                            (11, 2222, u'[5]', u'[0, 0]', u'[0, 0]', u'glad', u'gla^7d', u'a', 7, 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, None, u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', None, None), 
                            (12, 2222, u'[5]', u'[0, 2]', u'[0, 2]', u'se', u'se^9', u'e', 9, 1, u'VB', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'glad', u'["NN"]', u'to', u'["TO"]', u'you', u'["PRP"]', u'-)', u'["EMOASC"]', None, None, None, None, None, None), 
                            (13, 2222, u'[5]', u'[0, 4]', u'[0, 4]', u'-)', u'-)^4', u')', 4, 1, u'EMOASC', u'["neutral", 0.0]', None, None, None, u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', None, None, None, None, None, None, None, None, None, None), 
                            (14, 3333, u'[14]', u'[0, 1]', u'[0, 1]', u'bad', u'bad^5', u'd', 5, 2, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (15, 3333, u'[14]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'b', 7, 0, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (16, 3333, u'[14]', u'[0, 3]', u'[0, 1]', u'bad', u'b^7a^6d', u'a', 6, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (17, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'b', 4, 0, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (18, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'a', 4, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (19, 3333, u'[14]', u'[0, 4]', u'[0, 1]', u'bad', u'b^4a^4d^5', u'd', 5, 2, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (20, 3333, u'[14]', u'[0, 5]', u'[0, 1]', u'bad', u'ba^7d', u'a', 7, 1, u'JJ', u'["negative", -0.6999999999999998]', u'[0, 1]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (21, 3333, u'[14]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'(', 4, 1, u'EMOASC', u'["negative", -0.6999999999999998]', None, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None), 
                            (22, 3333, u'[14]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.6999999999999998]', None, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None), 
                            (23, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'o', 7, 1, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), 
                            (24, 4444, u'[13]', u'[0, 6]', u'[0, 1]', u'model', u'mo^7del^7', u'l', 7, 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'tiny', u'["JJ", {"tiny": 6}]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]', u'use', u'["VB"]'), 
                            (25, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'bi^3g', u'i', 3, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (26, 4444, u'[13]', u'[0, 16]', u'[0, 10]', u'big', u'bi^15g', u'i', 15, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (27, 5555, u'[8, 2, 11, 4]', u'[0, 8]', u'[0, 6]', u'explanation', u'expla^5nation', u'a', 5, 4, u'NN', u'["neutral", 0.0]', None, u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]'), 
                            (28, 5555, u'[8, 2, 11, 4]', u'[1, 0]', u'[1, 0]', u'right', u'ri^6ght', u'i', 6, 1, u'UH', u'["neutral", 0.0]', None, u'but', u'["CC"]', u'a', u'["DT"]', u'big', u'["JJ", {"big": 3}]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]'), 
                            (29, 5555, u'[8, 2, 11, 4]', u'[2, 2]', u'[2, 2]', u'you', u'you^6', u'u', 6, 2, u'PRP', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]', u'do', u'["VBP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]'), 
                            (30, 5555, u'[8, 2, 11, 4]', u'[2, 6]', u'[2, 6]', u'?', u'?^4', u'?', 4, 0, u'symbol', u'["neutral", 0.0]', None, u'do', u'["VBP"]', u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]'), 
                            (31, 5555, u'[8, 2, 11, 4]', u'[2, 7]', u'[2, 7]', u'1', u'1^6', u'1', 6, 0, u'number', u'["neutral", 0.0]', None, u'you', u'["PRP"]', u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]'), 
                            (32, 5555, u'[8, 2, 11, 4]', u'[2, 8]', u'[2, 8]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]'), 
                            (33, 5555, u'[8, 2, 11, 4]', u'[2, 9]', u'[2, 9]', u'1', u'1^8', u'1', 8, 0, u'number', u'["neutral", 0.0]', None, u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]'), 
                            (34, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (35, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u'u', 4, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (36, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'b^5u^4t^4', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (37, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (38, 5555, u'[8, 2, 11, 4]', u'[3, 1]', u'[3, 0]', u'but', u'bu^5t^4', u't', 4, 2, u'NNP', u'["neutral", 0.0]', u'[3, 0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (39, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'y^6ou', u'y', 6, 0, u'NN', u'["neutral", 0.0]', u'[3, 2]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (40, 5555, u'[8, 2, 11, 4]', u'[3, 3]', u'[3, 1]', u'you', u'yo^6u', u'o', 6, 1, u'NN', u'["neutral", 0.0]', u'[3, 2]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (41, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'b^6ut', u'b', 6, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (42, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (43, 5555, u'[8, 2, 11, 4]', u'[3, 5]', u'[3, 2]', u'but', u'b^5ut^4', u't', 4, 2, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (44, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'b', 5, 0, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (45, 5555, u'[8, 2, 11, 4]', u'[3, 6]', u'[3, 2]', u'but', u'b^5u^5t', u'u', 5, 1, u'FW', u'["neutral", 0.0]', u'[3, 4]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (46, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'y', 3, 0, u'FW', u'["neutral", 0.0]', None, 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', None, None, None, None, None, None, None, None, None, None), 
                            (47, 5555, u'[8, 2, 11, 4]', u'[3, 7]', u'[3, 3]', u'you', u'y^3o^2u^4', u'u', 4, 2, u'FW', u'["neutral", 0.0]', None, 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', None, None, None, None, None, None, None, None, None, None), 
                            (48, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'tin^3y^2', u'n', 3, 2, u'JJ', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]'), 
                            (49, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'b^5ut', u'b', 5, 0, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (50, 6666, u'[3, 9]', u'[1, 1]', u'[1, 0]', u'but', u'bu^5t', u'u', 5, 1, u'NNP', u'["neutral", 0.0]', u'[1, 0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (51, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'y^6ou', u'y', 6, 0, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (52, 6666, u'[3, 9]', u'[1, 3]', u'[1, 1]', u'you', u'yo^6u', u'o', 6, 1, u'JJ', u'["neutral", 0.0]', u'[1, 2]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (53, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'b^6ut', u'b', 6, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (54, 6666, u'[3, 9]', u'[1, 5]', u'[1, 2]', u'but', u'b^5ut', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (55, 6666, u'[3, 9]', u'[1, 6]', u'[1, 2]', u'but', u'b^5ut', u'b', 5, 0, u'CC', u'["neutral", 0.0]', u'[1, 4]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (56, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'y', 3, 0, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (57, 6666, u'[3, 9]', u'[1, 7]', u'[1, 3]', u'you', u'y^3o^2u^4', u'u', 4, 2, u'VBD', u'["neutral", 0.0]', None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (58, 6666, u'[3, 9]', u'[1, 8]', u'[1, 4]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None), 
                            (59, 6666, u'[3, 9]', u'[1, 9]', u'[1, 5]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None), 
                            (60, 6666, u'[3, 9]', u'[1, 10]', u'[1, 6]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None), 
                            (61, 6666, u'[3, 9]', u'[1, 11]', u'[1, 7]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None), 
                            (62, 6666, u'[3, 9]', u'[1, 12]', u'[1, 8]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None, None, None, None, None, None, None, None, None), 
                            (63, 7777, u'[19]', u'[0, 7]', u'[0, 7]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'), 
                            (64, 7777, u'[19]', u'[0, 9]', u'[0, 9]', u'but', u'bu^10t', u'u', 10, 1, u'MD', u'["positive", 0.27]', None, u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]'), 
                            (65, 7777, u'[19]', u'[0, 12]', u'[0, 11]', u'realy', u'real^3y', u'l', 3, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (66, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'e', 5, 1, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (67, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'l', 4, 3, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (68, 7777, u'[19]', u'[0, 13]', u'[0, 11]', u'realy', u're^5al^4y^3', u'y', 3, 4, u'RB', u'["positive", 0.27]', u'[0, 11]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None), 
                            (70, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None), 
                            (71, 7777, u'[19]', u'[0, 19]', u'[0, 17]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["positive", 0.27]', None, u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None)
                        ]


        right_redus = [
                            (1, 1111, u'[4, 14]', u'[1, 4]', u'[1, 4]', u'very', u'{"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}', 3, u'JJ', u'["negative", -0.1875]', u'.', u'["symbol"]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]'), 
                            (2, 1111, u'[4, 14]', u'[1, 7]', u'[1, 5]', u'pity', u'{"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}', 4, u'JJ', u'["negative", -0.1875]', u'but', u'["CC"]', u'it', u'["PRP"]', u'was', u'["VBD"]', u'also', u'["RB"]', u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u':-(', u'["EMOASC"]', u'@real_trump', u'["mention"]'), 
                            (3, 3333, u'[14]', u'[0, 1]', u'[0, 1]', u'bad', u'{"b^7a^6d": 1, "bad": 1, "ba^7d": 1, "b^4a^4d^5": 1, "bad^5": 1}', 5, u'JJ', u'["negative", -0.6999999999999998]', None, None, None, None, None, None, None, None, u'a', u'["DT"]', u'news', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (4, 3333, u'[14]', u'[0, 16]', u'[0, 12]', u'#shetlife', u'{"#shetlife": 2}', 2, u'hashtag', u'["negative", -0.6999999999999998]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'\U0001f62b', u'["EMOIMG"]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None, None, None), 
                            (5, 4444, u'[13]', u'[0, 0]', u'[0, 0]', u'tiny', u'{"tiny": 6}', 6, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'model', u'["NN"]', u',', u'["symbol"]', u'which', u'["WDT"]', u'we', u'["PRP"]', u'can', u'["MD"]'), 
                            (6, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'{"bi^3g": 1, "bi^15g": 1}', 2, u'NN', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None), 
                            (7, 5555, u'[8, 2, 11, 4]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'), 
                            (8, 5555, u'[8, 2, 11, 4]', u'[3, 0]', u'[3, 0]', u'but', u'{"bu^5t^4": 1, "b^5u^4t^4": 1}', 2, u'NNP', u'["neutral", 0.0]', u'?', u'["symbol"]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None), 
                            (9, 5555, u'[8, 2, 11, 4]', u'[3, 2]', u'[3, 1]', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'NN', u'["neutral", 0.0]', 1, u'["number"]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]', u'you', u'["FW"]', None, None, None, None, None, None), 
                            (10, 5555, u'[8, 2, 11, 4]', u'[3, 4]', u'[3, 2]', u'but', u'{"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}', 3, u'FW', u'["neutral", 0.0]', u'\U0001f62b', u'["EMOIMG"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["FW"]', None, None, None, None, None, None, None, None), 
                            (11, 6666, u'[3, 9]', u'[0, 0]', u'[0, 0]', u'tiny', u'{"tin^3y^2": 1, "tiny": 2}', 3, u'JJ', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]'), 
                            (12, 6666, u'[3, 9]', u'[1, 0]', u'[1, 0]', u'but', u'{"bu^5t": 1, "b^5ut": 1}', 2, u'NNP', u'["neutral", 0.0]', None, None, None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (13, 6666, u'[3, 9]', u'[1, 2]', u'[1, 1]', u'you', u'{"yo^6u": 1, "y^6ou": 1}', 2, u'JJ', u'["neutral", 0.0]', None, None, u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]'), 
                            (14, 6666, u'[3, 9]', u'[1, 4]', u'[1, 2]', u'but', u'{"b^6ut": 1, "b^5ut": 2}', 3, u'CC', u'["neutral", 0.0]', u'tiny', u'["JJ", {"tin^3y^2": 1, "tiny": 2}]', u'surprise', u'["NN"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]'), 
                            (15, 7777, u'[19]', u'[0, 11]', u'[0, 11]', u'realy', u'{"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}', 3, u'RB', u'["positive", 0.27]', u'me', u'["PRP"]', u'\U0001f62b', u'["EMOIMG"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]')
                        ]




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


        #######without_closing_db_at_the_end #########
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=4,adjust_to_cpu=False, freeze_db=False)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")


        repls.should.be.equal(right_repls)
        redus.should.be.equal(right_redus)

 
        #######with_closing_db_at_the_end #########

        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key)

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))

        stats.compute(corp,stream_number=4,adjust_to_cpu=False, freeze_db=True)
        baseline = stats.statsdb.getall("baseline")
        repls = stats.statsdb.getall("replications")
        redus = stats.statsdb.getall("reduplications")

        repls.should.be.equal(right_repls)
        redus.should.be.equal(right_redus)




    def pretty_print_uniq(self,item, syn_order=False, baseline_small=True ):
        if syn_order:
            #print "fghjk"
            print "\n\n\n"
            for k,v in item.iteritems():
                #print "fghjk111"
                #print v
                print "\n"
                #print "--------------- {} -------------------".format(k)
                #p((k,v))
                if v and k not in ["syntagma", "baseline", "stem_syn"]:
                    main_open_tag = "(" if isinstance(v, tuple) else "["
                    print "\t\tright_{} = {}".format(k,main_open_tag)

                    if len(v) == 3 and v[1] in [True, False]:
                        main_open_tag1 ="(" if isinstance( v[0], tuple) else "["
                        print "\t\t\t\t\t\t {}".format(main_open_tag1)

                        for data_for_syntagmas_part in v[0]:
                            word = data_for_syntagmas_part[0]
                            reps = data_for_syntagmas_part[1]
                            #p((word, reps))
                            #p(data_for_syntagmas_part, "data_for_syntagmas_part")
                            #print "%%"
                            main_open_tag_2 = "(" if isinstance(data_for_syntagmas_part, tuple) else "["
                            open_tag = "(" if isinstance(reps, tuple) else "["
                            #print "\t\t\t\t\t {}, {}".format(repr(word),open_tag)
                            print "\t\t\t\t\t\t\t{}{}, {}".format( main_open_tag_2,repr(word),open_tag)
                            # #print open_tag
                            # open_tag = "(" if isinstance(reps[0], tuple) else "["
                            # print "\t\t\t\t\t\t\t\t\t {}".format(open_tag)
                            for row in reps:

                                print "\t\t\t\t\t\t\t\t\t\t\t {},".format(row)
                                #for row in rows:
                                #    print "\t\t\t\t\t\t\t\t {},".format(row)
                            # close_tag = ")" if isinstance(reps[0], tuple) else "]"
                            # print "\t\t\t\t\t\t\t\t\t {},".format(close_tag)
                            # print "\t\t\t\t\t\t\t\t\t {},".format(reps[1])
                            # print "\t\t\t\t\t\t\t\t\t {},".format(reps[2])
                            main_close_tag_2 = ")" if isinstance(data_for_syntagmas_part, tuple) else "]"
                            close_tag = ")" if isinstance(reps, tuple) else "]"
                            # #print "\t\t\t\t\t\t {}".format(close_tag)
                            print "\t\t\t\t\t\t\t\t\t\t {}\n\t\t\t\t\t\t\t\t  {},".format(close_tag,main_close_tag_2)
                        # main_close_tag = ")" if isinstance(v, tuple) else "]"
                        # print "\t\t\t {}".format(main_close_tag)
                        main_close_tag1 =")" if isinstance( v[0], tuple) else "]"
                        print "\t\t\t\t\t\t {},".format(main_close_tag1)
                        print "\t\t\t\t\t\t {},".format(v[1])
                        print "\t\t\t\t\t\t {},".format(v[2])
                    else:
                        #p("fghjkl")
                        for data in v: 
                            word = data[0]
                            reps = data[1]
                            #print "ff§"
                            main_open_tag_2 = "(" if isinstance(data, tuple) else "["
                            open_tag = "(" if isinstance(reps, tuple) else "["
                            #print "\t\t\t\t\tright_{} = {}".format(k,open_tag)
                            print "\t\t\t\t\t{}{}, {}".format( main_open_tag_2,repr(word),open_tag)
                            #print open_tag
                            #p(reps,"reps")
                            for row in reps:
                                print "\t\t\t\t\t\t\t\t {},".format(row)
                            close_tag = ")" if isinstance(reps, tuple) else "]"
                            main_close_tag_2 = ")" if isinstance(data, tuple) else "]"
                            print "\t\t\t\t\t\t\t {}\n\t\t\t\t\t  {},".format(close_tag,main_close_tag_2)

                            
                            #print "\t\t\t\t {}".format(main_close_tag_2)

                    main_close_tag = ")" if isinstance(v, tuple) else "]"
                    print "\t\t\t\t {}".format(main_close_tag)

                else:
                    #print "fghjk333"
                    #open_tag = "(" if isinstance(reps, tuple) else "["
                    #close_tag = ")" if isinstance(reps, tuple) else "]"
                    #print "\t\tright_{} = {} {} {}".format(k,open_tag, reps, close_tag)
                    print "\t\tright_{} = {}".format(k, v)
        else:
            print "\n\n\n"
            for k,v in item.iteritems():
                #print v
                print "\n"
                #print "--------------- {} -------------------".format(k)
                l = len(v)
                #p((l,v))
                if len(v) >= 2 and k not in ["syntagma", "stem_syn"]:
                    if k == "baseline" and baseline_small:
                        print "\t\tright_{} = {}".format(k, v,)
                        continue

                    if len(v) == 3 and v[1] in [True, False]:
                        open_tag = "(" if isinstance(v, tuple) else "["
                        print "\t\tright_{} = {}".format(k,open_tag)
                        #print open_tag
                        open_tag = "(" if isinstance(v[0], tuple) else "["
                        print "\t\t\t\t\t\t {}".format(open_tag)
                        for row in v[0]:

                            print "\t\t\t\t\t\t\t {},".format(row)
                            #for row in rows:
                            #    print "\t\t\t\t\t {},".format(row)
                        close_tag = ")" if isinstance(v[0], tuple) else "]"
                        print "\t\t\t\t\t\t {},".format(close_tag)
                        print "\t\t\t\t\t\t {},".format(v[1])
                        print "\t\t\t\t\t\t {},".format(v[2])
                        close_tag = ")" if isinstance(v, tuple) else "]"
                        print "\t\t\t {}".format(close_tag)
                    else:
                        open_tag = "(" if isinstance(v, tuple) else "["
                        print "\t\tright_{} = {}".format(k,open_tag)
                        #print open_tag
                        for row in v:
                            print "\t\t\t\t\t {},".format(row)
                        close_tag = ")" if isinstance(v, tuple) else "]"
                        print "\t\t\t\t {}".format(close_tag)

                else:
                    #open_tag = "(" if isinstance(v, tuple) else "["
                    #close_tag = ")" if isinstance(v, tuple) else "]"
                    #print "\t\tright_{} = {} {} {}".format(k,open_tag, v, close_tag)
                    print "\t\tright_{} = {}".format(k, v,)







    # def pretty_print_uniq(self,item, syn_order=False):
    #     if syn_order:
    #         #print "fghjk"
    #         print "\n\n\n"
    #         for k,v in item.iteritems():
    #             #print "fghjk111"
    #             #print v
    #             print "\n"
    #             #print "--------------- {} -------------------".format(k)
    #             p((k,v))
    #             if v and k not in ["syntagma", "baseline"]:
    #                 main_open_tag = "(" if isinstance(v, tuple) else "["
    #                 print "\t\tright_{} = {}".format(k,main_open_tag)

    #                 for data in v:

    #                     word = data[0]
    #                     reps = data[1]
    #                     #main_open_tag_2 = "(" if isinstance(data, tuple) else "["
    #                     #print "\t\t\t {}".format(main_open_tag_2)
    #                     p(word,"word")

    #                     print 
    #                     if  k not in ["syntagma", "baseline"]:
    #                         #print "!!"
    #                         if len(reps) == 3 and reps[1] in [True, False]:
    #                             print "%%"
    #                             main_open_tag_2 = "(" if isinstance(data, tuple) else "["
    #                             open_tag = "(" if isinstance(reps, tuple) else "["
    #                             #print "\t\t\t\t\t {}, {}".format(repr(word),open_tag)
    #                             print "\t\t\t\t\t{}{}, {}".format( main_open_tag_2,repr(word),open_tag)
    #                             #print open_tag
    #                             open_tag = "(" if isinstance(reps[0], tuple) else "["
    #                             print "\t\t\t\t\t\t\t\t\t {}".format(open_tag)
    #                             for row in reps[0]:

    #                                 print "\t\t\t\t\t\t\t\t\t\t {},".format(row)
    #                                 #for row in rows:
    #                                 #    print "\t\t\t\t\t\t\t\t {},".format(row)
    #                             close_tag = ")" if isinstance(reps[0], tuple) else "]"
    #                             print "\t\t\t\t\t\t\t\t\t {},".format(close_tag)
    #                             print "\t\t\t\t\t\t\t\t\t {},".format(reps[1])
    #                             print "\t\t\t\t\t\t\t\t\t {},".format(reps[2])
    #                             main_close_tag_2 = ")" if isinstance(data, tuple) else "]"
    #                             close_tag = ")" if isinstance(reps, tuple) else "]"
    #                             #print "\t\t\t\t\t\t {}".format(close_tag)
    #                             print "\t\t\t\t\t\t\t {}\n\t\t\t\t\t  {}".format(close_tag,main_close_tag_2)
    #                         else:
    #                             #print "ff§"
    #                             main_open_tag_2 = "(" if isinstance(data, tuple) else "["
    #                             open_tag = "(" if isinstance(reps, tuple) else "["
    #                             #print "\t\t\t\t\tright_{} = {}".format(k,open_tag)
    #                             print "\t\t\t\t\t{}{}, {}".format( main_open_tag_2,repr(word),open_tag)
    #                             #print open_tag
    #                             #p(reps,"reps")
    #                             for row in reps:
    #                                 print "\t\t\t\t\t\t\t\t {},".format(row)
    #                             close_tag = ")" if isinstance(reps, tuple) else "]"
    #                             main_close_tag_2 = ")" if isinstance(data, tuple) else "]"
    #                             print "\t\t\t\t\t\t\t {}\n\t\t\t\t\t  {},".format(close_tag,main_close_tag_2)

                                
    #                             #print "\t\t\t\t {}".format(main_close_tag_2)

    #                 main_close_tag = ")" if isinstance(v, tuple) else "]"
    #                 print "\t\t\t {}".format(main_close_tag)

    #             else:
    #                 #print "fghjk333"
    #                 #open_tag = "(" if isinstance(reps, tuple) else "["
    #                 #close_tag = ")" if isinstance(reps, tuple) else "]"
    #                 #print "\t\tright_{} = {} {} {}".format(k,open_tag, reps, close_tag)
    #                 print "\t\tright_{} = {}".format(k, v)
    #     else:
    #         print "\n\n\n"
    #         for k,v in item.iteritems():
    #             #print v
    #             print "\n"
    #             #print "--------------- {} -------------------".format(k)
    #             if len(v) >= 2 and k not in ["syntagma", "baseline"]:
    #                 if len(v) == 3 and v[1] in [True, False]:
    #                     open_tag = "(" if isinstance(v, tuple) else "["
    #                     print "\t\tright_{} = {}".format(k,open_tag)
    #                     #print open_tag
    #                     open_tag = "(" if isinstance(v[0], tuple) else "["
    #                     print "\t\t\t\t\t\t {}".format(open_tag)
    #                     for row in v[0]:

    #                         print "\t\t\t\t\t\t\t {},".format(row)
    #                         #for row in rows:
    #                         #    print "\t\t\t\t\t {},".format(row)
    #                     close_tag = ")" if isinstance(v[0], tuple) else "]"
    #                     print "\t\t\t\t\t\t {},".format(close_tag)
    #                     print "\t\t\t\t\t\t {},".format(v[1])
    #                     print "\t\t\t\t\t\t {},".format(v[2])
    #                     close_tag = ")" if isinstance(v, tuple) else "]"
    #                     print "\t\t\t {}".format(close_tag)
    #                 else:
    #                     open_tag = "(" if isinstance(v, tuple) else "["
    #                     print "\t\tright_{} = {}".format(k,open_tag)
    #                     #print open_tag
    #                     for row in v:
    #                         print "\t\t\t\t\t {},".format(row)
    #                     close_tag = ")" if isinstance(v, tuple) else "]"
    #                     print "\t\t\t\t {}".format(close_tag)
    #             else:
    #                 #open_tag = "(" if isinstance(v, tuple) else "["
    #                 #close_tag = ")" if isinstance(v, tuple) else "]"
    #                 #print "\t\tright_{} = {} {} {}".format(k,open_tag, v, close_tag)
    #                 print "\t\tright_{} = {}".format(k, v,)




    @attr(status='stable')
    #@wipd
    def test__get_data_for_one_syntagma_611_1(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()

        #### DE ######
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))


    ################################################################################################################################################
    ################################################ I. FullRepetativnes= True   #################################################################################
    ########################################################################################################################################
        stats.recompute_syntagma_repetativity_scope(True)


    ################################################################################################################################################
    ################################################################################################################################################
    ##### return_full_tuple = False #######################################################################################################+
    ###########################################################################################################################################
    ################################################################################################################################################

    ############################
    ####### SCOPE 1 ##############
    ############################


        ####################### syntagma_type="lexem" #############################

        # # ########stemmed_search=False #

        # ### Case 1.1:
        # syntagma = ["klitze"]
        # item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem")
        # #self.pretty_print_uniq(item)
        # #p(item,"item")


        # extracted_repl = item["repl"]
        # extracted_redu = item["redu"]
        # extracted_baseline = item["baseline"]
        # extracted_syntagma = item["syntagma"]


        # right_repl = [
        #              (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #              (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #              (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
        #              (54, 11111, u'[5, 6, 15, 3]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]'),
        #          ]


        # right_syntagma = ['klitze']


        # right_baseline = [[[u'klitze'], u'klitz', 1, 8, u'3', u'4', u'2', u'6', u'3', u'2']]


        # right_redu = [
        #              (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #              (14, 12222, u'[24]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitz', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]'),
        #          ]



        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})


        # ########stemmed_search=False #

        # ### Case 1.2:
        # syntagma = ["kleine"]
        # item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem")
        # #self.pretty_print_uniq(item)
        # #p(item,"item")


        # extracted_repl = item["repl"]
        # extracted_redu = item["redu"]
        # extracted_baseline = item["baseline"]
        # extracted_syntagma = item["syntagma"]

        # right_repl = [
        #              (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #              (57, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (58, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (59, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = ['kleine']


        # right_baseline = [[[u'kleine'], u'klein', 1, 7, u'5', u'11', u'1', u'2', u'5', u'1']]


        # right_redu = [(2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})




    #     ########stemmed_search=True #

    #     ### Case 1.3:
    #     syntagma = ["klein"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True)
    #     self.pretty_print_uniq(item)
    #     #p(item,"item")



    #     right_repl = [
    #                  (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
    #                  (26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
    #                  (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
    #                  (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
    #                  (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'[2, 12]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #                  (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'[2, 12]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #                  (57, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
    #                  (58, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
    #                  (59, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
    #                  (71, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
    #                  (72, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
    #                  (73, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
    #                  (74, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
    #              ]


    #     right_syntagma = [u'klein']


    #     right_baseline = [[[u'kleines'], u'klein', 1, 5, u'5', u'11', u'2', u'5', None, None], [[u'kleinere'], u'klein', 1, 2, u'2', u'3', u'1', u'2', None, None], [[u'kleine'], u'klein', 1, 7, u'5', u'11', u'1', u'2', None, None], [[u'klein'], u'klein', 1, 2, u'2', u'4', u'1', u'2', None, None]]


    #     right_redu = [
    #                  (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (6, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'klein', u'{"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}', 3, u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
    #                  (7, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'klein', u'{"kleinere^5": 1, "kleine^3r^2e^5": 1}', 2, u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
    #                  (9, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (11, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #              ]

    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]


    #     extracted_repl.should.be.equal(right_repl)
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})






    # # ############################
    # # ####### SCOPE 2 ##############
    # # ############################


    #     ####################### syntagma_type="lexem" #############################

    #     ########stemmed_search=False #
    #     ### Case 1.1:
    #     syntagma = ["klitze", "kleine"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem")
    #     #p(item,"item")
    #     #self.pretty_print_uniq(item)


    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]



    #     right_repl = [
    #                  (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
    #                  (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
    #              ]


    #     right_syntagma = ['klitze', 'kleine']


    #     right_baseline = [[[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1']]


    #     right_redu = [
    #                  (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #              ]
    #     extracted_repl.should.be.equal(right_repl)  
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})



    #     ########stemmed_search=Truee #
    #     ### Case 1.2:
    #     syntagma = ["klitz", "klein"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True)
    #     #p(item,"item")
    #     #self.pretty_print_uniq(item)


    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]



    #     right_repl = [
    #                  (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
    #                  (42, 10000, u'[12, 3, 8]', u'[2, 5]', u'[2, 3]', u'klitz', u'kli^4tz', u'klitz', u'i', 4, 2, u'[2, 4]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
    #                  (43, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'i', 4, 2, u'[2, 4]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
    #                  (44, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'z', 3, 4, u'[2, 4]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
    #                  (49, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitzes^4', u'klitz', u's', 4, 6, u'[2, 10]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
    #                  (50, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u'i', 3, 2, u'[2, 10]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
    #                  (51, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u's', 3, 6, u'[2, 10]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
    #                  (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
    #                  (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'[2, 12]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #                  (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'[2, 12]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #              ]


    #     right_syntagma = [u'klitz', u'klein']


    #     right_baseline = [
    #                     [[u'klitzes', u'kleines'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 2]', u'[1, 1]', u'[2, 2]', u'1', u'1'], 
    #                     [[u'klitz', u'klein'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 4]', u'[1, 1]', u'[3, 2]', u'1', u'1'], 
    #                     [[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1']]


    #     right_redu = [
    #                  (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (8, 10000, u'[12, 3, 8]', u'[2, 4]', u'[2, 3]', u'klitz', u'klitz', u'{"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}', 3, u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
    #                  (10, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitz', u'{"klitzes^4": 1, "kli^3tzes^3": 1}', 2, u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
    #                  (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (9, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
    #                  (11, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
    #              ]

    #     extracted_repl.should.be.equal(right_repl)  
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})




        ########get_also_non_full_repetativ_result=True #
        ### Case 1.3:
        syntagma = [u'.', u'kleinere', u'auswahl']
        item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=False,get_also_non_full_repetativ_result=True)
        #p(item,"item")
        #self.pretty_print_uniq(item)


        right_repl = [
                     (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'),
                     (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
                     (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
                     (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
                     (40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'),
                     (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'),
                 ]


        right_syntagma = [u'.', u'kleinere', u'auswahl']


        right_baseline = [[[u'.', u'kleinere', u'auswahl'], u'.++klein++auswahl', 3, 1, u'[1, 2, 1]', u'[1, 3, 2]', None, None, u'1', None]]


        right_redu = [(12, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'klein', u'{"kleinere^5": 1, "kleine^3r^2e^5": 1}', 2, u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')]




        extracted_repl = item["repl"]
        extracted_redu = item["redu"]
        extracted_baseline = item["baseline"]
        extracted_syntagma = item["syntagma"]


        # extracted_repl.should.be.equal(right_repl)  
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})










    # # ################################################################################################################################################
    # # ################################################################################################################################################
    # # ##### return_full_tuple = True #######################################################################################################+
    # # ###########################################################################################################################################
    # # ################################################################################################################################################



    # # ############################
    # # ####### SCOPE 1 ##############
    # # ############################


    #     ####################### syntagma_type="lexem" #############################

    #     ### Case 1.1:
    #     syntagma = ["klitze"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem", return_full_tuple=True)
    #     #self.pretty_print_uniq(item)
    #     #p(item,"item")

    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]

    #     right_repl = (
    #                      [
    #                          (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
    #                          (54, 11111, u'[5, 6, 14]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]'),
    #                      ],
    #                      True,
    #                      None,
    #          )


    #     right_syntagma = ['klitze']


    #     right_baseline = [[[u'klitze'], u'klitz', 1, 8, u'3', u'4', u'2', u'6', None, None]]


    #     right_redu = (
    #                      [
    #                          (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (12, 12222, u'[24]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitz', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]'),
    #                      ],
    #                      True,
    #                      None,
    #          )

    #     extracted_repl.should.be.equal(right_repl)
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})



    # # # ############################
    # # # ####### SCOPE 2 ##############
    # # # ############################


    #     ####################### syntagma_type="lexem" #############################

    #     ### Case 1.1:
    #     syntagma = ["klitze", "kleine"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem", return_full_tuple=True)
    #     #p(item,"item")
    #     #self.pretty_print_uniq(item)


    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]

    #     right_repl = (
    #                      [
    #                          (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
    #                          (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                          (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                          (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                          (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
    #                      ],
    #                      True,
    #                      2,
    #          )


    #     right_syntagma = ['klitze', 'kleine']


    #     right_baseline = [[[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1']]


    #     right_redu = (
    #                      [
    #                          (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                          (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                      ],
    #                      True,
    #                      1,
    #          )

    #     extracted_repl.should.be.equal(right_repl)
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})







    # # ################################################################################################################################################
    # # ################################################ II. FullRepetativnes= False   #################################################################################
    # # ########################################################################################################################################
    #     stats.recompute_syntagma_repetativity_scope(False)



    # # # ############################
    # # # ####### SCOPE 2 ##############
    # # # ############################


    #     ####################### syntagma_type="lexem" #############################

    #     ### Case 1.1:
    #     syntagma = ["klitze", "kleine"]
    #     item = stats._get_data_for_one_syntagma(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem")
    #     #p(item,"item")
    #     #self.pretty_print_uniq(item)


    #     extracted_repl = item["repl"]
    #     extracted_redu = item["redu"]
    #     extracted_baseline = item["baseline"]
    #     extracted_syntagma = item["syntagma"]

    #     right_repl = [
    #                  (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
    #                  (54, 11111, u'[5, 6, 14]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]'),
    #                  (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 2]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #                  (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
    #              ]


    #     right_syntagma = ['klitze', 'kleine']


    #     right_baseline = [[[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[3, 3]', u'[4, 4]', u'[2, 1]', u'[6, 2]', None, None]]


    #     right_redu = [
    #                  (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
    #                  (12, 12222, u'[24]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitz', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]'),
    #                  (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
    #              ]

    #     extracted_repl.should.be.equal(right_repl)
    #     extracted_redu.should.be.equal(right_redu)
    #     extracted_baseline.should.be.equal(right_baseline)
    #     extracted_syntagma.should.be.equal(right_syntagma)

    #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma})



        ####################### syntagma_type="pos" #############################








    @attr(status='stable')
    #@wipd
    def test_get_data_611_2(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()

        #### DE ######
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )
        

        ######### EN ########

        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))

        ###### 3
        syntagma = ["EMOIMG","EMOIMG"]
        data1 = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=False))
        repl1 = sorted(data1[0]["repl"])
        redu1 = sorted(data1[0]["redu"])

        data2 =  list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=True))
        ext_id = []
        repl2 = []
        for item in data2:
            for r in item["repl"]:
                if r[0] not in ext_id:
                    ext_id.append(r[0])
                    repl2.append(r)

        ext_id = []
        redu2 = []
        for item in data2:
            for r in item["redu"]:
                if r[0] not in ext_id:
                    ext_id.append(r[0])
                    redu2.append(r)


        #repl2 = sorted([r for item in data2  )
        #redu2 = sorted([r for item in data2  for r in item["redu"]])

        assert len(repl1)<= len(repl2)
        assert len(redu1)<= len(redu2)
        #p((repl1, repl2))
        #p((redu1, redu2))





        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------

        ######### DE #######
        stats.close()
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))
        
    ################################################################################################
    ################################################################################################
    ###################################################################################################
    ############################stemmed_search = False #########################################
    #################################################################################################
    ################################################################################################
    ################################################################################################
#
 

    ################################################################################################################################################
    ################################################ II. FullRepetativnes= True   #################################################################################
    ########################################################################################################################################
        stats.recompute_syntagma_repetativity_scope(True)

        # ### Case 0:
        # syntagma = ["big"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # data.should.be.equal([])


        # # # # ####################################################################################
        # # # # ####################################################################################
        # # # # #################################################################################


        # ### Case 1.1:
        # syntagma = ["kleine"]
        # data = stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem")
        # #p()
        # len1 = len(data)
        # data = list(data)
        # len2 = len(data)
        # len1.should.be.equal(len2)
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0])


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #              (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #              (57, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (58, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (59, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #              (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #              (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'kleine']


        # right_baseline = [[[u'kleine'], u'klein', 1, 7, u'5', u'11', u'1', u'2', u'5', u'1']]


        # right_redu = [(2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])




        # # # ####################################################################################
        # # # ######################GET JUST FEW COLUMNS ##################################
        # # # ################################################################################

        # ### Case 1.2:
        # columns_repl=['doc_id', 'redufree_len','index_in_redufree','index_in_corpus']
        # columns_redu = ['doc_id', 'redufree_len','index_in_redufree', 'index_in_corpus',"redu_length"]
        # columns_baseline = ['syntagma', 'occur_syntagma_all', "scope"]
        # #columns_baseline = 
        # syntagma = ["kleine"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem", get_columns_repl=columns_repl , get_columns_redu=columns_redu, get_columns_baseline=columns_baseline ))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0])


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]

        # right_repl = [
        #              [8888, u'[4, 11]', u'[0, 1]', u'[0, 2]'],
        #              [8888, u'[4, 11]', u'[0, 1]', u'[0, 2]'],
        #              [8888, u'[4, 11]', u'[0, 1]', u'[0, 3]'],
        #              [10000, u'[11]', u'[0, 2]', u'[0, 2]'],
        #              [11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]'],
        #              [11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]'],
        #              [11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]'],
        #              [12222, u'[24]', u'[0, 21]', u'[0, 24]'],
        #              [12222, u'[24]', u'[0, 21]', u'[0, 24]'],
        #              [12222, u'[24]', u'[0, 21]', u'[0, 24]'],
        #              [12222, u'[24]', u'[0, 21]', u'[0, 24]'],
        #          ]


        # right_syntagma = [u'kleine']


        # right_baseline = [[[u'kleine'], 7, 1]]


        # right_redu = [[8888, u'[4, 11]', u'[0, 1]', u'[0, 2]', 2]]


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])




        # # # ####################################################################################
        # # # ##################### #GET ORDERED SYNTAGMA (SCOPE 1) ##################################
        # # # ##############################################################################

        # ### Case 1.3: #order_output_by_syntagma_order
        # syntagma = ["kleine"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",order_output_by_syntagma_order=True))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=True)

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]




        # right_repl = [

        #             (u'kleine', (
        #                          (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #                          (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #                          (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #                          (21, 10000, u'[11]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]'),
        #                          (29, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                          (30, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                          (31, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 5, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                          (43, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 4, 2, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                          (44, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'i', 5, 3, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                          (45, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                          (46, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 8, 5, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                      )
        #               )
        #      ]


        # right_syntagma = [u'kleine']


        # right_baseline = [[[u'kleine'], 7, 1, u'5', u'11', u'1', u'2', None, None]]


        # right_redu = [

        #             (u'kleine', (
        #                          (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #                      )
        #               )
        #      ]


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])






        # # # ####################################################################################
        # # # ######################GET JUST FEW PHENOMENA AND NOT ALL#########################
        # # # ####################################################################################

        # ### Case 2.1:
        # ### repl=True,redu=False, baseline=False
        # syntagma = ["kleine"]
        # data = list(stats.get_data(syntagma, repl=True, redu=False, baseline=False, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0])

        # right_repl = [
        #              (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (21, 10000, u'[11]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]'),
        #              (29, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #              (30, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #              (31, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 5, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #              (43, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 4, 2, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #              (44, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'i', 5, 3, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #              (45, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #              (46, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 8, 5, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'kleine']


        # right_baseline = []


        # right_redu = []

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]



        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])




        # ### Case 2.2:
        # ### repl=False,redu=True, baseline=False
        # syntagma = ["kleine"]
        # data = list(stats.get_data(syntagma, repl=False, redu=True, baseline=False, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0])


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]

        # right_repl = []


        # right_syntagma = [u'kleine']


        # right_baseline = []


        # right_redu = [
        #                 (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
        #             ]

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])





        # ### Case 2.3:
        # ### repl=False,redu=False, baseline=True
        # syntagma = ["kleine"]
        # data = list(stats.get_data(syntagma, repl=False, redu=False, baseline=True, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0])


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]

        # right_repl = []


        # right_syntagma = [u'kleine']


        # right_baseline = [[[u'kleine'], 7, 1, u'5', u'11', u'1', u'2', None, None]]


        # right_redu = []


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])





        # # # ####################################################################################
        # # # #################. GET ORDERED/UNORDERED OUTPUT #################################
        # # # # #################################################################################

        # ### Case 3.1: 
        # #order_output_by_syntagma_order = True
        # # full_tuple = False
        # syntagma = ["kleine","Überaschung"] 
        # data = stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",order_output_by_syntagma_order=True,return_full_tuple=False)
        # len1 = len(data)
        # data = list(data)
        # len2 = len(data)
        # len1.should.be.equal(len2)
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=True)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]



        # right_repl = [
        #             (u'kleine', (
        #                          (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #                          (57, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                          (58, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                          (59, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                          (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                          (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                          (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                          (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      )
        #               ),
        #             (u'\xfcberaschung', (
        #                          (22, 10000, u'[12, 3, 8]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'uberasch', u'r', 4, 3, None, u'NN', u'["neutral", 0.0]', None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'kleine', u'["ADJA", null, "klein"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]'),
        #                          (60, 11111, u'[5, 6, 15, 3]', u'[2, 5]', u'[2, 5]', u'\xfcberaschung', u'\xfcber^5aschung', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]'),
        #                          (86, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'e', 4, 2, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None),
        #                          (87, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None),
        #                          (88, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'a', 3, 4, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None),
        #                          (89, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'n', 6, 9, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None),
        #                          (90, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'g', 3, 10, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None),
        #                      )
        #               ),
        #          ]


        # right_syntagma = [u'kleine', u'\xfcberaschung']


        # right_baseline = [[[u'kleine', u'\xfcberaschung'], u'klein++uberasch', 2, 5, u'[3, 3]', u'[8, 7]', None, None, u'3', None]]


        # right_redu = ()

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])


        # ### Case 3.2: 
        # #order_output_by_syntagma_order = True
        # # full_tuple = True
        # syntagma = ["kleine","Überaschung"] 
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",order_output_by_syntagma_order=True,return_full_tuple=True))
        # #p(data,"data")
        # #p(data[0],"data[0]")
        # #self.pretty_print_uniq(data[0],syn_order=True)



        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]




        # right_repl = (
        #                  [
        #                     (u'kleine', (
        #                                      (21, 10000, u'[11]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]'),
        #                                      (29, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                                      (30, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                                      (31, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'e', 5, 5, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol"]', u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]'),
        #                                      (43, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 4, 2, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                                      (44, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'i', 5, 3, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                                      (45, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                                      (46, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'e', 8, 5, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol"]', u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #                                  )
        #                           ),
        #                     (u'\xfcberaschung', (
        #                                      (22, 10000, u'[11]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'r', 4, 3, u'NN', u'["neutral", 0.0]', None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'kleine', u'["ADJA"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]', u'beser', u'["ADJD"]'),
        #                                      (32, 11111, u'[5, 6, 14]', u'[2, 5]', u'[2, 5]', u'\xfcberaschung', u'\xfcber^5aschung', u'r', 5, 3, u'NN', u'["neutral", 0.0]', None, u'weil', u'["KOUS"]', u'es', u'["PPER"]', u'ja', u'["PTKMA"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]'),
        #                                      (47, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'e', 4, 2, u'NN', u'["neutral", 0.0]', None, u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'.', u'["symbol"]', None, None, None, None, None, None, None, None),
        #                                      (48, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'r', 5, 3, u'NN', u'["neutral", 0.0]', None, u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'.', u'["symbol"]', None, None, None, None, None, None, None, None),
        #                                      (49, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'a', 3, 4, u'NN', u'["neutral", 0.0]', None, u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'.', u'["symbol"]', None, None, None, None, None, None, None, None),
        #                                      (50, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'n', 6, 9, u'NN', u'["neutral", 0.0]', None, u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'.', u'["symbol"]', None, None, None, None, None, None, None, None),
        #                                      (51, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'g', 3, 10, u'NN', u'["neutral", 0.0]', None, u'es', u'["PPER"]', u'war', u'["VAFIN"]', u'so', u'["ADV"]', u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'.', u'["symbol"]', None, None, None, None, None, None, None, None),
        #                                  )
        #                           ),
        #                  ],
        #                  True,
        #                  3,
        #          )


        # right_syntagma = [u'kleine', u'\xfcberaschung']


        # right_baseline = [[[u'kleine', u'\xfcberaschung'], 5, 2, u'[3, 3]', u'[8, 7]', None, None, u'3', u'0']]


        # right_redu = (
        #                  (
        #                  ),
        #                  False,
        #                  0,
        #          )


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])





        # ### Case 3.3:
        # #order_output_by_syntagma_order
        # syntagma = ["klitze","kleine", "überaschung"] 
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",order_output_by_syntagma_order=True))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=True)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #             (u'klitze', (
        #                          (20, 10000, u'[11]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'),
        #                      )
        #               ),
        #             (u'kleine', (
        #                          (21, 10000, u'[11]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]'),
        #                      )
        #               ),
        #             (u'\xfcberaschung', (
        #                          (22, 10000, u'[11]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'r', 4, 3, u'NN', u'["neutral", 0.0]', None, None, None, None, None, u'eine', u'["ART"]', u'klitze', u'["ADJA"]', u'kleine', u'["ADJA"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]', u'https://www.freiesinternet.de', u'["URL"]', u'beser', u'["ADJD"]'),
        #                      )
        #               ),
        #          ]


        # right_syntagma = [u'klitze', u'kleine', u'\xfcberaschung']


        # right_baseline = [[[u'klitze', u'kleine', u'\xfcberaschung'], 3, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0']]


        # right_redu = ()




        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])











        # # # ####################################################################################
        # # # #################. GET INFOS ZU ALLEN SYNTAGMAS (*)  #################################
        # # # #################################################################################



        # ### Case 4.1:
        # syntagma = "*"
        # data = stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",max_scope=False)
        # len1 = len(data)
        # data = list(data)
        # len2 = len(data)
        # len1.should.be.equal(len2)
        # #p((len1, len2))
        # #p(data,"data")
        # right_data = [
        #                   {'repl': [(64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]'), (65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'4', u'5'], 'baseline': [[u'4', u'5'], u'4++5', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(17, 9999, u'[7, 4, 3]', u'[2, 0]', u'[2, 0]', u'bleibt', u'ble^8ibt', u'bleibt', u'e', 8, 2, u'[2, 0]', u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'hungrig', u'["NN", null, "hungrig"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (18, 9999, u'[7, 4, 3]', u'[2, 1]', u'[2, 0]', u'bleibt', u'ble^4ibt', u'bleibt', u'e', 4, 2, u'[2, 0]', u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'hungrig', u'["NN", null, "hungrig"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)], 'syntagma': [u'bleibt'], 'baseline': [[u'bleibt'], u'bleibt', 1, 2, u'2', u'2', u'1', u'2', None, None], 'redu': [(5, 9999, u'[7, 4, 3]', u'[2, 0]', u'[2, 0]', u'bleibt', u'bleibt', u'{"ble^4ibt": 1, "ble^8ibt": 1}', 2, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'hungrig', u'["NN", null, "hungrig"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)]}, 
        #                   {'repl': [(42, 10000, u'[12, 3, 8]', u'[2, 5]', u'[2, 3]', u'klitz', u'kli^4tz', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (43, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (44, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'z', 3, 4, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None)], 'syntagma': [u'klitz'], 'baseline': [[u'klitz'], u'klitz', 1, 3, u'2', u'3', u'1', u'3', None, None], 'redu': [(9, 10000, u'[12, 3, 8]', u'[2, 4]', u'[2, 3]', u'klitz', u'klitz', u'{"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}', 3, u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None)]}, 
        #                   {'repl': [(61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'), (62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]')], 'syntagma': [u'1', u'2', u'3'], 'baseline': [[u'1', u'2', u'3'], u'1++2++3', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(49, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitzes^4', u'klitz', u's', 4, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (50, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u'i', 3, 2, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (51, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u's', 3, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None)], 'syntagma': [u'klitzes'], 'baseline': [[u'klitzes'], u'klitz', 1, 2, u'2', u'3', u'1', u'2', None, None], 'redu': [(11, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitz', u'{"klitzes^4": 1, "kli^3tzes^3": 1}', 2, u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None)]}, 
        #                   {'repl': [(1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'), (54, 11111, u'[5, 6, 15, 3]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]')], 'syntagma': [u'klitze'], 'baseline': [[u'klitze'], u'klitz', 1, 8, u'3', u'4', u'2', u'6', None, None], 'redu': [(1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (14, 12222, u'[24]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitz', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]')]}, 
        #                   {'repl': [(62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]'), (65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'2', u'3', u'4', u'5'], 'baseline': [[u'2', u'3', u'4', u'5'], u'2++3++4++5', 4, 1, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]')], 'syntagma': [u'3', u'4'], 'baseline': [[u'3', u'4'], u'3++4', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(77, 12222, u'[24]', u'[0, 6]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'uberasch', u'r', 4, 3, None, u'NN', u'["neutral", 0.0]', None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["NN", {"klitze": 4}, "klitz"]', u'kleine', u'["ADJA", null, "klein"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]'), (86, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'e', 4, 2, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (87, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (88, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'a', 3, 4, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (89, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'n', 6, 9, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (90, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'g', 3, 10, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (22, 10000, u'[12, 3, 8]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'uberasch', u'r', 4, 3, None, u'NN', u'["neutral", 0.0]', None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'kleine', u'["ADJA", null, "klein"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]'), (60, 11111, u'[5, 6, 15, 3]', u'[2, 5]', u'[2, 5]', u'\xfcberaschung', u'\xfcber^5aschung', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]')], 'syntagma': [u'\xfcberaschung'], 'baseline': [[u'\xfcberaschung'], u'uberasch', 1, 5, u'4', u'8', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(55, 11111, u'[5, 6, 15, 3]', u'[1, 3]', u'[1, 3]', u'wichtig', u'wichti^8g', u'wichtig', u'i', 8, 5, None, u'NN', u'["neutral", 0.0]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]', u'trotzdem', u'["PAV", null, "trotzd"]', u'ist', u'["VVPP", null, "ist"]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]'), (56, 11111, u'[5, 6, 15, 3]', u'[1, 4]', u'[1, 4]', u'ist', u'is^6t', u'ist', u's', 6, 1, None, u'VVPP', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]', u'trotzdem', u'["PAV", null, "trotzd"]', u'wichtig', u'["NN", null, "wichtig"]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]')], 'syntagma': [u'wichtig', u'ist'], 'baseline': [[u'wichtig', u'ist'], u'wichtig++ist', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(49, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitzes^4', u'klitz', u's', 4, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (50, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u'i', 3, 2, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (51, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u's', 3, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None), (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u'klitzes', u'kleines'], 'baseline': [[u'klitzes', u'kleines'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 2]', u'[1, 1]', u'[2, 2]', u'1', u'1'], 'redu': [(11, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitz', u'{"klitzes^4": 1, "kli^3tzes^3": 1}', 2, u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None), (12, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None)]}, 
        #                   {'repl': [(52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None), (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None), (26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (66, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (67, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (68, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (69, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (70, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (71, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (72, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (73, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (74, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)], 'syntagma': [u'kleines'], 'baseline': [[u'kleines'], u'klein', 1, 8, u'8', u'20', u'3', u'8', None, None], 'redu': [(12, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None), (7, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'klein', u'{"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}', 3, u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (13, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'klein', u'{"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}', 3, u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)]}, 
        #                   {'repl': [(35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (75, 11111, u'[5, 6, 15, 3]', u'[3, 3]', u'[3, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (76, 11111, u'[5, 6, 15, 3]', u'[3, 4]', u'[3, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u'm\xe4dchen', u'.'], 'baseline': [[u'm\xe4dchen', u'.'], u'madch++.', 2, 2, u'[2, 2]', u'[2, 2]', None, None, u'2', u'0'], 'redu': ()}, 
        #                   {'repl': [(42, 10000, u'[12, 3, 8]', u'[2, 5]', u'[2, 3]', u'klitz', u'kli^4tz', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (43, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (44, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'z', 3, 4, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)], 'syntagma': [u'klitz', u'klein'], 'baseline': [[u'klitz', u'klein'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 4]', u'[1, 1]', u'[3, 2]', u'1', u'1'], 'redu': [(9, 10000, u'[12, 3, 8]', u'[2, 4]', u'[2, 3]', u'klitz', u'klitz', u'{"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}', 3, u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None), (10, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)]}, 
        #                   {'repl': [(6, 8888, u'[4, 11]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u':-)', u')', 4, 2, None, u'EMOASC', u'["positive", 0.5]', u'sie', u'["PPER", null, "sie"]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None), (7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None)], 'syntagma': [u':-)', u'-)'], 'baseline': [[u':-)', u'-)'], u':-)++-)', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'), (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]')], 'syntagma': [u'.', u'kleinere', u'auswahl'], 'baseline': [[u'.', u'kleinere', u'auswahl'], u'.++klein++auswahl', 3, 1, u'[1, 2, 1]', u'[1, 3, 2]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(76, 11111, u'[5, 6, 15, 3]', u'[3, 4]', u'[3, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', None, None, None, None, None, None, None, None, None, None), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]')], 'syntagma': [u'.'], 'baseline': [[u'.'], u'.', 1, 14, u'2', u'2', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(81, 12222, u'[24]', u'[0, 23]', u'[0, 20]', u'eine', u'eine^4', u'ein', u'e', 4, 3, None, u'ART', u'["neutral", 0.0]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None), (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (86, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'e', 4, 2, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (87, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (88, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'a', 3, 4, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (89, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'n', 6, 9, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (90, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'g', 3, 10, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'eine', u'kleine', u'\xfcberaschung'], 'baseline': [[u'eine', u'kleine', u'\xfcberaschung'], u'ein++klein++uberasch', 3, 2, u'[1, 1, 1]', u'[1, 4, 5]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'), (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]')], 'syntagma': [u'kleines', u'm\xe4dchen', u'.', u'kleinere', u'auswahl'], 'baseline': [[u'kleines', u'm\xe4dchen', u'.', u'kleinere', u'auswahl'], u'klein++madch++.++klein++auswahl', 5, 1, u'[3, 1, 1, 2, 1]', u'[9, 1, 1, 3, 2]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (75, 11111, u'[5, 6, 15, 3]', u'[3, 3]', u'[3, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'm\xe4dchen'], 'baseline': [[u'm\xe4dchen'], u'madch', 1, 2, u'2', u'2', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'.', u'kleinere'], 'baseline': [[u'.', u'kleinere'], u'.++klein', 2, 1, u'[1, 2]', u'[1, 3]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]')], 'syntagma': [u'4'], 'baseline': [[u'4'], u'4', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]')], 'syntagma': [u'2', u'3', u'4'], 'baseline': [[u'2', u'3', u'4'], u'2++3++4', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(6, 8888, u'[4, 11]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u':-)', u')', 4, 2, None, u'EMOASC', u'["positive", 0.5]', u'sie', u'["PPER", null, "sie"]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None)], 'syntagma': [u':-)'], 'baseline': [[u':-)'], u':-)', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(78, 12222, u'[24]', u'[0, 14]', u'[0, 11]', u'1', u'1^6', u'1', u'1', 6, 0, None, u'number', u'["neutral", 0.0]', u'ich', u'["PPER", null, "ich"]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]'), (79, 12222, u'[24]', u'[0, 15]', u'[0, 12]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, None, u'EMOIMG', u'["neutral", 0.0]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]'), (80, 12222, u'[24]', u'[0, 16]', u'[0, 13]', u'1', u'1^8', u'1', u'1', 8, 0, None, u'number', u'["neutral", 0.0]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]')], 'syntagma': [u'1', u'\U0001f62b', u'1'], 'baseline': [[u'1', u'\U0001f62b', u'1'], u'1++\U0001f62b++1', 3, 1, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(6, 8888, u'[4, 11]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u':-)', u')', 4, 2, None, u'EMOASC', u'["positive", 0.5]', u'sie', u'["PPER", null, "sie"]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None), (7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None), (8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None), (9, 8888, u'[4, 11]', u'[1, 10]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None), (10, 8888, u'[4, 11]', u'[1, 11]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u':-)', u'-)', u'\U0001f600', u'-)'], 'baseline': [[u':-)', u'-)', u'\U0001f600', u'-)'], u':-)++-)++\U0001f600++-)', 4, 1, u'[1, 3, 1, "IGNOR"]', u'[1, 3, 1, "IGNOR"]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]')], 'syntagma': [u'2', u'3'], 'baseline': [[u'2', u'3'], u'2++3', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]')], 'syntagma': [u'3'], 'baseline': [[u'3'], u'3', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'kleinere'], 'baseline': [[u'kleinere'], u'klein', 1, 2, u'2', u'3', u'1', u'2', None, None], 'redu': [(8, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'klein', u'{"kleinere^5": 1, "kleine^3r^2e^5": 1}', 2, u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')]}, 
        #                   {'repl': [(55, 11111, u'[5, 6, 15, 3]', u'[1, 3]', u'[1, 3]', u'wichtig', u'wichti^8g', u'wichtig', u'i', 8, 5, None, u'NN', u'["neutral", 0.0]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]', u'trotzdem', u'["PAV", null, "trotzd"]', u'ist', u'["VVPP", null, "ist"]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]')], 'syntagma': [u'wichtig'], 'baseline': [[u'wichtig'], u'wichtig', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'), (57, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (58, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (59, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (22, 10000, u'[12, 3, 8]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'uberasch', u'r', 4, 3, None, u'NN', u'["neutral", 0.0]', None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'kleine', u'["ADJA", null, "klein"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]'), (60, 11111, u'[5, 6, 15, 3]', u'[2, 5]', u'[2, 5]', u'\xfcberaschung', u'\xfcber^5aschung', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]'), (86, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'e', 4, 2, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (87, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'r', 5, 3, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (88, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'a', 3, 4, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (89, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'n', 6, 9, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (90, 12222, u'[24]', u'[0, 25]', u'[0, 22]', u'\xfcberaschung', u'\xfcbe^4r^5a^3schun^6g^3', u'uberasch', u'g', 3, 10, None, u'NN', u'["neutral", 0.0]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'kleine', u'\xfcberaschung'], 'baseline': [[u'kleine', u'\xfcberaschung'], u'klein++uberasch', 2, 5, u'[3, 3]', u'[8, 7]', None, None, u'3', u'0'], 'redu': ()}, 
        #                   {'repl': [(35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'm\xe4dchen', u'.', u'kleinere'], 'baseline': [[u'm\xe4dchen', u'.', u'kleinere'], u'madch++.++klein', 3, 1, u'[1, 1, 2]', u'[1, 1, 3]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]'), (65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'3', u'4', u'5'], 'baseline': [[u'3', u'4', u'5'], u'3++4++5', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(9, 8888, u'[4, 11]', u'[1, 10]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None), (10, 8888, u'[4, 11]', u'[1, 11]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None), (7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None)], 'syntagma': [u'-)'], 'baseline': [[u'-)'], u'-)', 1, 3, u'3', u'3', u'1', u'2', None, None], 'redu': [(3, 8888, u'[4, 11]', u'[1, 10]', u'[1, 10]', u'-)', u'-)', u'{"-)^3": 2}', 2, u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None)]}, 
        #                   {'repl': [(7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None), (8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None), (9, 8888, u'[4, 11]', u'[1, 10]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None), (10, 8888, u'[4, 11]', u'[1, 11]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u'-)', u'\U0001f600', u'-)'], 'baseline': [[u'-)', u'\U0001f600', u'-)'], u'-)++\U0001f600++-)', 3, 1, u'[3, 1, "IGNOR"]', u'[3, 1, "IGNOR"]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (66, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (67, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (68, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (69, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (70, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (71, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (72, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (73, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (74, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (75, 11111, u'[5, 6, 15, 3]', u'[3, 3]', u'[3, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (76, 11111, u'[5, 6, 15, 3]', u'[3, 4]', u'[3, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u'kleines', u'm\xe4dchen', u'.'], 'baseline': [[u'kleines', u'm\xe4dchen', u'.'], u'klein++madch++.', 3, 2, u'[6, 2, 2]', u'[18, 2, 2]', None, None, u'2', u'0'], 'redu': ()}, 
        #                   {'repl': [(78, 12222, u'[24]', u'[0, 14]', u'[0, 11]', u'1', u'1^6', u'1', u'1', 6, 0, None, u'number', u'["neutral", 0.0]', u'ich', u'["PPER", null, "ich"]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]'), (79, 12222, u'[24]', u'[0, 15]', u'[0, 12]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, None, u'EMOIMG', u'["neutral", 0.0]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]')], 'syntagma': [u'1', u'\U0001f62b'], 'baseline': [[u'1', u'\U0001f62b'], u'1++\U0001f62b', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'), (62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'1', u'2'], 'baseline': [[u'1', u'2'], u'1++2', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None), (9, 8888, u'[4, 11]', u'[1, 10]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None), (10, 8888, u'[4, 11]', u'[1, 11]', u'[1, 10]', u'-)', u'-)^3', u'-)', u')', 3, 1, u'[1, 10]', u'EMOASC', u'["positive", 0.5]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', None, None, None, None, None, None, None, None, None, None)], 'syntagma': [u'\U0001f600', u'-)'], 'baseline': [[u'\U0001f600', u'-)'], u'\U0001f600++-)', 2, 1, u'[1, 2]', u'[1, 2]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'), (62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]')], 'syntagma': [u'1', u'2', u'3', u'4'], 'baseline': [[u'1', u'2', u'3', u'4'], u'1++2++3++4', 4, 1, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'), (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]')], 'syntagma': [u'm\xe4dchen', u'.', u'kleinere', u'auswahl'], 'baseline': [[u'm\xe4dchen', u'.', u'kleinere', u'auswahl'], u'madch++.++klein++auswahl', 4, 1, u'[1, 1, 2, 1]', u'[1, 1, 3, 2]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'), (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]')], 'syntagma': [u'klitze', u'kleine'], 'baseline': [[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1'], 'redu': [(1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'), (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]}, 
        #                   {'repl': [(19, 9999, u'[7, 4, 3]', u'[2, 2]', u'[2, 1]', u'hungrig', u'hu^12ngrig', u'hungrig', u'u', 12, 1, None, u'NN', u'["neutral", 0.0]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'hungrig'], 'baseline': [[u'hungrig'], u'hungrig', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(23, 10000, u'[12, 3, 8]', u'[0, 9]', u'[0, 9]', u'kan', u'kan^6', u'kan', u'n', 6, 2, u'[0, 9]', u'FM', u'["neutral", 0.0]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]'), (24, 10000, u'[12, 3, 8]', u'[0, 10]', u'[0, 9]', u'kan', u'ka^4n^5', u'kan', u'a', 4, 1, u'[0, 9]', u'FM', u'["neutral", 0.0]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]'), (25, 10000, u'[12, 3, 8]', u'[0, 10]', u'[0, 9]', u'kan', u'ka^4n^5', u'kan', u'n', 5, 2, u'[0, 9]', u'FM', u'["neutral", 0.0]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'kan'], 'baseline': [[u'kan'], u'kan', 1, 2, u'2', u'3', u'1', u'2', None, None], 'redu': [(6, 10000, u'[12, 3, 8]', u'[0, 9]', u'[0, 9]', u'kan', u'kan', u'{"ka^4n^5": 1, "kan^6": 1}', 2, u'FM', u'["neutral", 0.0]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')]}, 
        #                   {'repl': [(65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'5'], 'baseline': [[u'5'], u'5', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(79, 12222, u'[24]', u'[0, 15]', u'[0, 12]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, None, u'EMOIMG', u'["neutral", 0.0]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]'), (80, 12222, u'[24]', u'[0, 16]', u'[0, 13]', u'1', u'1^8', u'1', u'1', 8, 0, None, u'number', u'["neutral", 0.0]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]')], 'syntagma': [u'\U0001f62b', u'1'], 'baseline': [[u'\U0001f62b', u'1'], u'\U0001f62b++1', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(11, 9999, u'[7, 4, 3]', u'[0, 2]', u'[0, 2]', u'tag', u'ta^6g^6', u'tag', u'a', 6, 1, None, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, u'einen', u'["ART", null, "ein"]', u'wundersch\xf6nen', u'["ADJA", null, "wunderschon"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]'), (12, 9999, u'[7, 4, 3]', u'[0, 2]', u'[0, 2]', u'tag', u'ta^6g^6', u'tag', u'g', 6, 2, None, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, u'einen', u'["ART", null, "ein"]', u'wundersch\xf6nen', u'["ADJA", null, "wunderschon"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]')], 'syntagma': [u'tag'], 'baseline': [[u'tag'], u'tag', 1, 1, u'1', u'2', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'2'], 'baseline': [[u'2'], u'2', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(6, 8888, u'[4, 11]', u'[1, 7]', u'[1, 7]', u':-)', u':-)^4', u':-)', u')', 4, 2, None, u'EMOASC', u'["positive", 0.5]', u'sie', u'["PPER", null, "sie"]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u'-)', u'["EMOASC", null, "-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None), (7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None), (8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None)], 'syntagma': [u':-)', u'-)', u'\U0001f600'], 'baseline': [[u':-)', u'-)', u'\U0001f600'], u':-)++-)++\U0001f600', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (66, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (67, 11111, u'[5, 6, 15, 3]', u'[3, 0]', u'[3, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (68, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (69, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (70, 11111, u'[5, 6, 15, 3]', u'[3, 1]', u'[3, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (71, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (72, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (73, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (74, 11111, u'[5, 6, 15, 3]', u'[3, 2]', u'[3, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[3, 0]', u'NN', u'["neutral", 0.0]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (75, 11111, u'[5, 6, 15, 3]', u'[3, 3]', u'[3, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'kleines', u'm\xe4dchen'], 'baseline': [[u'kleines', u'm\xe4dchen'], u'klein++madch', 2, 2, u'[6, 2]', u'[18, 2]', None, None, u'2', u'0'], 'redu': ()}, 
        #                   {'repl': [(26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'[1, 0]', u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'), (35, 10000, u'[12, 3, 8]', u'[1, 3]', u'[1, 1]', u'm\xe4dchen', u'm\xe4dchen^5', u'madch', u'n', 5, 6, None, u'NN', u'["neutral", 0.0]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]'), (36, 10000, u'[12, 3, 8]', u'[1, 4]', u'[1, 2]', u'.', u'.^5', u'.', u'.', 5, 0, None, u'symbol', u'["neutral", 0.0]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]'), (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'kleines', u'm\xe4dchen', u'.', u'kleinere'], 'baseline': [[u'kleines', u'm\xe4dchen', u'.', u'kleinere'], u'klein++madch++.++klein', 4, 1, u'[3, 1, 1, 2]', u'[9, 1, 1, 3]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(81, 12222, u'[24]', u'[0, 23]', u'[0, 20]', u'eine', u'eine^4', u'ein', u'e', 4, 3, None, u'ART', u'["neutral", 0.0]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None), (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)], 'syntagma': [u'eine', u'kleine'], 'baseline': [[u'eine', u'kleine'], u'ein++klein', 2, 2, u'[1, 1]', u'[1, 4]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'), (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'), (22, 10000, u'[12, 3, 8]', u'[0, 3]', u'[0, 3]', u'\xfcberaschung', u'\xfcber^4aschung', u'uberasch', u'r', 4, 3, None, u'NN', u'["neutral", 0.0]', None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'kleine', u'["ADJA", null, "klein"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]')], 'syntagma': [u'klitze', u'kleine', u'\xfcberaschung'], 'baseline': [[u'klitze', u'kleine', u'\xfcberaschung'], u'klitz++klein++uberasch', 3, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'), (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'), (57, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (58, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (59, 11111, u'[5, 6, 15, 3]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, None, u'ADJA', u'["neutral", 0.0]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'), (82, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (83, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (84, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (85, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, None, u'ADJA', u'["neutral", 0.0]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None)], 'syntagma': [u'kleine'], 'baseline': [[u'kleine'], u'klein', 1, 7, u'5', u'11', u'1', u'2', None, None], 'redu': [(2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]}, 
        #                   {'repl': [(61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'), (80, 12222, u'[24]', u'[0, 16]', u'[0, 13]', u'1', u'1^8', u'1', u'1', 8, 0, None, u'number', u'["neutral", 0.0]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]'), (78, 12222, u'[24]', u'[0, 14]', u'[0, 11]', u'1', u'1^6', u'1', u'1', 6, 0, None, u'number', u'["neutral", 0.0]', u'ich', u'["PPER", null, "ich"]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]')], 'syntagma': [u'1'], 'baseline': [[u'1'], u'1', 1, 3, u'3', u'3', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None)], 'syntagma': [u'\U0001f600'], 'baseline': [[u'\U0001f600'], u'\U0001f600', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(17, 9999, u'[7, 4, 3]', u'[2, 0]', u'[2, 0]', u'bleibt', u'ble^8ibt', u'bleibt', u'e', 8, 2, u'[2, 0]', u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'hungrig', u'["NN", null, "hungrig"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (18, 9999, u'[7, 4, 3]', u'[2, 1]', u'[2, 0]', u'bleibt', u'ble^4ibt', u'bleibt', u'e', 4, 2, u'[2, 0]', u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'hungrig', u'["NN", null, "hungrig"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None), (19, 9999, u'[7, 4, 3]', u'[2, 2]', u'[2, 1]', u'hungrig', u'hu^12ngrig', u'hungrig', u'u', 12, 1, None, u'NN', u'["neutral", 0.0]', u'geniest', u'["NE", {"geni^5es^8t^5": 1, "genies^4t^2": 1}, "geni"]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None, None, None)], 'syntagma': [u'bleibt', u'hungrig'], 'baseline': [[u'bleibt', u'hungrig'], u'bleibt++hungrig', 2, 1, u'[2, 1]', u'[2, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(56, 11111, u'[5, 6, 15, 3]', u'[1, 4]', u'[1, 4]', u'ist', u'is^6t', u'ist', u's', 6, 1, None, u'VVPP', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]', u'trotzdem', u'["PAV", null, "trotzd"]', u'wichtig', u'["NN", null, "wichtig"]', u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]')], 'syntagma': [u'ist'], 'baseline': [[u'ist'], u'ist', 1, 2, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(81, 12222, u'[24]', u'[0, 23]', u'[0, 20]', u'eine', u'eine^4', u'ein', u'e', 4, 3, None, u'ART', u'["neutral", 0.0]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None)], 'syntagma': [u'eine'], 'baseline': [[u'eine'], u'ein', 1, 5, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(13, 9999, u'[7, 4, 3]', u'[1, 0]', u'[1, 0]', u'geniest', u'genies^4t^2', u'geni', u's', 4, 5, u'[1, 0]', u'NE', u'["neutral", 0.0]', u'tag', u'["NN", null, "tag"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'hungrig', u'["NN", null, "hungrig"]'), (14, 9999, u'[7, 4, 3]', u'[1, 1]', u'[1, 0]', u'geniest', u'geni^5es^8t^5', u'geni', u'i', 5, 3, u'[1, 0]', u'NE', u'["neutral", 0.0]', u'tag', u'["NN", null, "tag"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'hungrig', u'["NN", null, "hungrig"]'), (15, 9999, u'[7, 4, 3]', u'[1, 1]', u'[1, 0]', u'geniest', u'geni^5es^8t^5', u'geni', u's', 8, 5, u'[1, 0]', u'NE', u'["neutral", 0.0]', u'tag', u'["NN", null, "tag"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'hungrig', u'["NN", null, "hungrig"]'), (16, 9999, u'[7, 4, 3]', u'[1, 1]', u'[1, 0]', u'geniest', u'geni^5es^8t^5', u'geni', u't', 5, 6, u'[1, 0]', u'NE', u'["neutral", 0.0]', u'tag', u'["NN", null, "tag"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'hungrig', u'["NN", null, "hungrig"]')], 'syntagma': [u'geniest'], 'baseline': [[u'geniest'], u'geni', 1, 2, u'2', u'4', u'1', u'2', None, None], 'redu': [(4, 9999, u'[7, 4, 3]', u'[1, 0]', u'[1, 0]', u'geniest', u'geni', u'{"geni^5es^8t^5": 1, "genies^4t^2": 1}', 2, u'NE', u'["neutral", 0.0]', u'tag', u'["NN", null, "tag"]', u'w\xfcnsche', u'["VVFIN", null, "wunsch"]', u'ich', u'["PPER", null, "ich"]', u'euch', u'["PRF", null, "euch"]', u'.', u'["symbol", null, "."]', u'das', u'["ART", null, "das"]', u'leben', u'["NN", null, "leb"]', u'.', u'["symbol", null, "."]', u'bleibt', u'["NN", {"ble^4ibt": 1, "ble^8ibt": 1}, "bleibt"]', u'hungrig', u'["NN", null, "hungrig"]')]}, 
        #                   {'repl': [(61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'), (62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'), (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'), (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]'), (65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]')], 'syntagma': [u'1', u'2', u'3', u'4', u'5'], 'baseline': [[u'1', u'2', u'3', u'4', u'5'], u'1++2++3++4++5', 5, 1, u'[1, 1, 1, 1, 1]', u'[1, 1, 1, 1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(7, 8888, u'[4, 11]', u'[1, 8]', u'[1, 8]', u'-)', u'-)^3', u'-)', u')', 3, 1, None, u'EMOASC', u'["positive", 0.5]', u'mich', u'["PPER", null, "mich"]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'\U0001f600', u'["EMOIMG", null, "\\ud83d\\ude00"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None), (8, 8888, u'[4, 11]', u'[1, 9]', u'[1, 9]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', u'\U0001f600', 5, 0, None, u'EMOIMG', u'["positive", 0.5]', u'gl\xfccklich', u'["ADJD", null, "glucklich"]', u'gemacht', u'["VVPP", null, "gemacht"]', u'!', u'["symbol", null, "!"]', u':-)', u'["EMOASC", null, ":-)"]', u'-)', u'["EMOASC", null, "-)"]', u'-)', u'["EMOASC", {"-)^3": 2}, "-)"]', None, None, None, None, None, None, None, None)], 'syntagma': [u'-)', u'\U0001f600'], 'baseline': [[u'-)', u'\U0001f600'], u'-)++\U0001f600', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(79, 12222, u'[24]', u'[0, 15]', u'[0, 12]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', u'\U0001f62b', 4, 0, None, u'EMOIMG', u'["neutral", 0.0]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]')], 'syntagma': [u'\U0001f62b'], 'baseline': [[u'\U0001f62b'], u'\U0001f62b', 1, 1, u'1', u'1', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'), (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]')], 'syntagma': [u'auswahl'], 'baseline': [[u'auswahl'], u'auswahl', 1, 1, u'1', u'2', u'0', u'0', None, None], 'redu': ()}, 
        #                   {'repl': [(37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'[2, 0]', u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'), (40, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'h', 3, 5, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]'), (41, 10000, u'[12, 3, 8]', u'[2, 2]', u'[2, 1]', u'auswahl', u'auswah^3l^4', u'auswahl', u'l', 4, 6, None, u'NN', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]')], 'syntagma': [u'kleinere', u'auswahl'], 'baseline': [[u'kleinere', u'auswahl'], u'klein++auswahl', 2, 1, u'[2, 1]', u'[3, 2]', None, None, u'1', u'0'], 'redu': ()}, 
        #                   {'repl': [(45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None), (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)], 'syntagma': [u'klein'], 'baseline': [[u'klein'], u'klein', 1, 2, u'2', u'4', u'1', u'2', None, None], 'redu': [(10, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)]}
        #                     ]  


        # for extracted_item, right_item in zip(data,right_data):
        #     #p(extracted_item,"extracted_item")
        #     #p(right_item,"right_item")
        #     set(extracted_item).should.be.equal(set(right_item))








        # # # ####################################################################################
        # # # #################. WORK WITH POS   #########################################
        # # # ##############################################################################


        # # ### Case 5.1:
        # #full_repetativ_syntagma=False
        # syntagma = ["NN", "NE"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]




        # right_repl = [
        #              (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'e', 7, 5, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #          ]


        # right_syntagma = [u'NN', u'NE']


        # right_baseline = [[[u'klitze', u'kleine', u'\xfcberaschung'], 3, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], [[u'klitze', u'kleine'], 4, 2, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1'], [[u'klitze'], 8, 1, u'3', u'4', u'2', u'6', None, None], [[u'klitze', u'kleine', u'\xfcberaschung', u'.'], 1, 4, None, None, None, None, None, None], [[u'kleine'], 7, 1, u'5', u'11', u'1', u'2', None, None], [[u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1, 6, None, None, None, None, None, None], [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1, 4, None, None, None, None, None, None], [[u'kleine', u'\xfcberaschung', u'.'], 2, 3, None, None, None, None, None, None], [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1, 5, None, None, None, None, None, None], [[u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1, 5, None, None, None, None, None, None], [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie'], 1, 6, None, None, None, None, None, None], [[u'kleine', u'\xfcberaschung'], 5, 2, u'[3, 3]', u'[8, 7]', None, None, u'3', u'0']]


        # right_redu = [
        #              (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #          ]




        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)









        # # # ####################################################################################
        # # # ################ #WORK WITH NUMBERS##########################################
        # # # #################################################################################


        # # ### Case 6.1:
        # syntagma = ["number"]
        # data = stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos")
        # len1 = len(data)
        # data = list(data)
        # len2 = len(data)
        # len1.should.be.equal(len2)
        # #p((len1, len2))
        # # p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (78, 12222, u'[24]', u'[0, 14]', u'[0, 11]', u'1', u'1^6', u'1', u'1', 6, 0, None, u'number', u'["neutral", 0.0]', u'ich', u'["PPER", null, "ich"]', u'mal', u'["PTKMA", null, "mal"]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', 1, u'["number", null, "1"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]'),
        #              (80, 12222, u'[24]', u'[0, 16]', u'[0, 13]', u'1', u'1^8', u'1', u'1', 8, 0, None, u'number', u'["neutral", 0.0]', u'gerne', u'["ADV", null, "gern"]', u'hate', u'["VAFIN", null, "hat"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', u'\U0001f62b', u'["EMOIMG", null, "\\ud83d\\ude2b"]', u'du', u'["PPER", null, "du"]', u'meintest', u'["VVFIN", null, "meint"]', u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]'),
        #              (61, 11111, u'[5, 6, 15, 3]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', u'1', 5, 0, None, u'number', u'["neutral", 0.0]', u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]'),
        #              (62, 11111, u'[5, 6, 15, 3]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', u'2', 4, 0, None, u'number', u'["neutral", 0.0]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]'),
        #              (63, 11111, u'[5, 6, 15, 3]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', u'3', 5, 0, None, u'number', u'["neutral", 0.0]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 4, u'["number", null, "4"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]'),
        #              (64, 11111, u'[5, 6, 15, 3]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', u'4', 4, 0, None, u'number', u'["neutral", 0.0]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 5, u'["number", null, "5"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]'),
        #              (65, 11111, u'[5, 6, 15, 3]', u'[2, 12]', u'[2, 12]', u'5', u'5^5', u'5', u'5', 5, 0, None, u'number', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]', 3, u'["number", null, "3"]', 4, u'["number", null, "4"]', 6, u'["number", null, "6"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]'),
        #          ]


        # right_syntagma = [u'number']


        # right_baseline = [[[u'1', u'\U0001f62b', u'1', u'du', u'meintest'], u'1++\U0001f62b++1++du++meint', 5, 1, None, None, None, None, None, None], [[u'3', u'4', u'5', u'6', u'.', u'kleines'], u'3++4++5++6++.++klein', 6, 1, None, None, None, None, None, None], [[u'3', u'4', u'5', u'6'], u'3++4++5++6', 4, 1, None, None, None, None, None, None], [[u'1', u'2'], u'1++2', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', None], [[u'5', u'6'], u'5++6', 2, 1, None, None, None, None, None, None], [[u'1', u'\U0001f62b', u'1', u'du', u'meintest', u','], u'1++\U0001f62b++1++du++meint++,', 6, 1, None, None, None, None, None, None], [[u'2'], u'2', 1, 1, u'1', u'1', None, None, u'1', None], [[u'1', u'2', u'3', u'4'], u'1++2++3++4', 4, 1, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', None], [[u'2', u'3', u'4', u'5', u'6'], u'2++3++4++5++6', 5, 1, None, None, None, None, None, None], [[u'1', u'\U0001f62b'], u'1++\U0001f62b', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', None], [[u'5', u'6', u'.', u'kleines'], u'5++6++.++klein', 4, 1, None, None, None, None, None, None], [[u'3', u'4'], u'3++4', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', None], [[u'1', u'du', u'meintest', u','], u'1++du++meint++,', 4, 1, None, None, None, None, None, None], [[u'1', u'2', u'3', u'4', u'5', u'6'], u'1++2++3++4++5++6', 6, 1, None, None, None, None, None, None], [[u'4', u'5', u'6', u'.', u'kleines', u'm\xe4dchen'], u'4++5++6++.++klein++madch', 6, 1, None, None, None, None, None, None], [[u'1', u'\U0001f62b', u'1', u'du'], u'1++\U0001f62b++1++du', 4, 1, None, None, None, None, None, None], [[u'2', u'3', u'4'], u'2++3++4', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', None], [[u'3', u'4', u'5'], u'3++4++5', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', None], [[u'4', u'5', u'6', u'.'], u'4++5++6++.', 4, 1, None, None, None, None, None, None], [[u'4'], u'4', 1, 1, u'1', u'1', None, None, u'1', None], [[u'1', u'2', u'3'], u'1++2++3', 3, 1, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', None], [[u'1', u'du'], u'1++du', 2, 1, None, None, None, None, None, None], [[u'1'], u'1', 1, 3, u'3', u'3', None, None, u'3', None], [[u'2', u'3'], u'2++3', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', None], [[u'3'], u'3', 1, 1, u'1', u'1', None, None, u'1', None], [[u'4', u'5', u'6'], u'4++5++6', 3, 1, None, None, None, None, None, None], [[u'1', u'\U0001f62b', u'1'], u'1++\U0001f62b++1', 3, 1, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', None], [[u'5'], u'5', 1, 1, u'1', u'1', None, None, u'1', None], [[u'4', u'5', u'6', u'.', u'kleines'], u'4++5++6++.++klein', 5, 1, None, None, None, None, None, None], [[u'5', u'6', u'.'], u'5++6++.', 3, 1, None, None, None, None, None, None], [[u'2', u'3', u'4', u'5', u'6', u'.'], u'2++3++4++5++6++.', 6, 1, None, None, None, None, None, None], [[u'1', u'du', u'meintest', u',', u'es'], u'1++du++meint++,++es', 5, 1, None, None, None, None, None, None], [[u'5', u'6', u'.', u'kleines', u'm\xe4dchen', u'.'], u'5++6++.++klein++madch++.', 6, 1, None, None, None, None, None, None], [[u'3', u'4', u'5', u'6', u'.'], u'3++4++5++6++.', 5, 1, None, None, None, None, None, None], [[u'1', u'du', u'meintest', u',', u'es', u'war'], u'1++du++meint++,++es++war', 6, 1, None, None, None, None, None, None], [[u'2', u'3', u'4', u'5'], u'2++3++4++5', 4, 1, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', None], [[u'1', u'du', u'meintest'], u'1++du++meint', 3, 1, None, None, None, None, None, None], [[u'1', u'2', u'3', u'4', u'5'], u'1++2++3++4++5', 5, 1, u'[1, 1, 1, 1, 1]', u'[1, 1, 1, 1, 1]', None, None, u'1', None], [[u'5', u'6', u'.', u'kleines', u'm\xe4dchen'], u'5++6++.++klein++madch', 5, 1, None, None, None, None, None, None], [[u'4', u'5'], u'4++5', 2, 1, u'[1, 1]', u'[1, 1]', None, None, u'1', None]]


        # right_redu = ()

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)






        # # ### Case 6.2:
        # #### Problem, by repetativ syntagmas -> repetativ rep_ids
        # syntagma = ["number","number"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # # p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (33, 11111, u'[5, 6, 14]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'),
        #              (34, 11111, u'[5, 6, 14]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None),
        #              (35, 11111, u'[5, 6, 14]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None),
        #              (36, 11111, u'[5, 6, 14]', u'[2, 11]', u'[2, 11]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'number', u'number']


        # right_baseline = [
        #              [[u'1', u'2', u'3', u'4'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3', u'4', u'5'], 1, 5, u'[1, 1, 1, 1, 1]', u'[1, 1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4', u'5', u'6'], 1, 5, None, None, None, None, None, None],
        #              [[u'2'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'1', u'2'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'3', u'4', u'5', u'6'], 1, 4, None, None, None, None, None, None],
        #              [[u'3', u'4'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'1'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'2', u'3'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3', u'4', u'5', u'6'], 1, 6, None, None, None, None, None, None],
        #              [[u'2', u'3', u'4', u'5'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'3'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'4', u'5', u'6'], 1, 3, None, None, None, None, None, None],
        #              [[u'4'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'3', u'4', u'5'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'4', u'5'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #          ]


        # right_redu = ()




        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)





        # # ### Case 6.3:
        # syntagma = ["number","number","number"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # # p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (33, 11111, u'[5, 6, 14]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'),
        #              (34, 11111, u'[5, 6, 14]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None),
        #              (35, 11111, u'[5, 6, 14]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None),
        #          ]


        # right_syntagma = [u'number', u'number', u'number']


        # right_baseline = [
        #              [[u'1', u'2', u'3', u'4'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4', u'5', u'6'], 1, 5, None, None, None, None, None, None],
        #              [[u'2'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'1', u'2'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'3', u'4', u'5', u'6'], 1, 4, None, None, None, None, None, None],
        #              [[u'3', u'4'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'1'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'2', u'3'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3', u'4', u'5', u'6'], 1, 6, None, None, None, None, None, None],
        #              [[u'2', u'3', u'4', u'5'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'3'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'1', u'2', u'3', u'4', u'5'], 1, 5, u'[1, 1, 1, 1, 1]', u'[1, 1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'3', u'4', u'5'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #          ]


        # right_redu = ()




        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)





        # # ### Case 6.4:#
        # syntagma = ["number","number","number"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=True))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (u'number', ((33, 11111, u'[5, 6, 14]', u'[2, 8]', u'[2, 8]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'),)),
        #              (u'number', ((34, 11111, u'[5, 6, 14]', u'[2, 9]', u'[2, 9]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None),)),
        #              (u'number', ((35, 11111, u'[5, 6, 14]', u'[2, 10]', u'[2, 10]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'\xfcberaschung', u'["NN"]', u'ist', u'["VAFIN"]', u'.', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None),)),
        #          ]


        # right_syntagma = [u'number', u'number', u'number']


        # right_baseline = [
        #              [[u'1', u'2', u'3', u'4'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'2', u'3', u'4', u'5', u'6'], 1, 5, None, None, None, None, None, None],
        #              [[u'2'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'1', u'2'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'3', u'4', u'5', u'6'], 1, 4, None, None, None, None, None, None],
        #              [[u'3', u'4'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'1'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'2', u'3'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'1', u'2', u'3', u'4', u'5', u'6'], 1, 6, None, None, None, None, None, None],
        #              [[u'2', u'3', u'4', u'5'], 1, 4, u'[1, 1, 1, 1]', u'[1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'3'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'1', u'2', u'3', u'4', u'5'], 1, 5, u'[1, 1, 1, 1, 1]', u'[1, 1, 1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'3', u'4', u'5'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #          ]


        # right_redu = ()



        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)






        ### Case 6.5:#
        ###### 1
        syntagma = ["EMOIMG"]
        data1 = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=False))
        repl1 = sorted(data1[0]["repl"])
        redu1 = sorted(data1[0]["redu"])

        data2 =  list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=True))
        repl2 = sorted([r for item in data2  for r in item["repl"]])
        redu2 = sorted([r for item in data2  for r in item["redu"]])

        repl1.should.be.equal(repl2)
        redu1.should.be.equal(redu2)
        #p((repl1, repl2))
        #p((redu1, redu2))

        ###### 2
        syntagma = ["EMOIMG","EMOASC"]
        data1 = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=False))
        repl1 = sorted(data1[0]["repl"])
        redu1 = sorted(data1[0]["redu"])

        data2 =  list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=True))
        repl2 = sorted([r for item in data2  for r in item["repl"]])
        redu2 = sorted([r for item in data2  for r in item["redu"]])

        repl1.should.be.equal(repl2)
        redu1.should.be.equal(redu2)
        #p((repl1, repl2))
        #p((redu1, redu2))

        ###### 3
        syntagma = ["EMOASC"]
        data1 = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=False))
        repl1 = sorted(data1[0]["repl"])
        redu1 = sorted(data1[0]["redu"])

        data2 =  list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False,if_type_pos_return_lexem_syn=True))
        ext_id = []
        repl2 = []
        for item in data2:
            for r in item["repl"]:
                if r[0] not in ext_id:
                    ext_id.append(r[0])
                    repl2.append(r)
        repl2 = sorted(repl2)

        ext_id = []
        redu2 = []
        for item in data2:
            for r in item["redu"]:
                if r[0] not in ext_id:
                    ext_id.append(r[0])
                    redu2.append(r)
        redu2 = sorted(redu2)


        if len(repl1) == len(repl2):
            assert repl1 == repl2
        else:
            assert len(repl1)<= len(repl2)

        if len(redu1) == len(redu2):
            assert redu1 == redu2
        else:
            assert len(redu1)<= len(redu2)


        #p((repl1, repl2))
        #p((redu1, redu2))


    ################################################################################################
    ################################################################################################
    ###################################################################################################
    ############################stemmed_search = True #########################################
    #################################################################################################
    ################################################################################################
    ################################################################################################


        ########stemmed_search=True #

        # ### Case 10.1:
        # syntagma = ["klitze","kleines"]
        # items = stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True, )
        # len1 = len(items)
        # items = list(items)
        # len2 = len(items)
        # len1.should.be.equal(len2)
        # #p((len1, len2))
        # #self.pretty_print_uniq(item)
        # #p(items,"item")

        # for item in items:
        #     #p(item["syntagma"])

        #     if item["syntagma"] == [u'klitzes', u'kleines']:
        #         #self.pretty_print_uniq(item)

        #         right_stem_syn = [u'klitz', u'klein']


        #         right_repl = [
        #                      (49, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitzes^4', u'klitz', u's', 4, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (50, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u'i', 3, 2, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (51, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u's', 3, 6, u'[2, 6]', u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'[2, 7]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klitzes', u'kleines']


        #         right_baseline = ([[u'klitzes', u'kleines'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 2]', u'[1, 1]', u'[2, 2]', u'1', u'1'],)


        #         right_redu = [
        #                      (11, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitz', u'{"klitzes^4": 1, "kli^3tzes^3": 1}', 2, u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (12, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                  ]



        #     elif item["syntagma"] == [u'klitz', u'klein']:
        #         #self.pretty_print_uniq(item)

        #         right_stem_syn = [u'klitz', u'klein']


        #         right_repl = [
        #                      (42, 10000, u'[12, 3, 8]', u'[2, 5]', u'[2, 3]', u'klitz', u'kli^4tz', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (43, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'i', 4, 2, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (44, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'z', 3, 4, u'[2, 3]', u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'[2, 4]', u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klitz', u'klein']


        #         right_baseline = ([[u'klitz', u'klein'], u'klitz++klein', 2, 1, u'[2, 2]', u'[3, 4]', u'[1, 1]', u'[3, 2]', u'1', u'1'],)


        #         right_redu = [
        #                      (9, 10000, u'[12, 3, 8]', u'[2, 4]', u'[2, 3]', u'klitz', u'klitz', u'{"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}', 3, u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (10, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]









        #     elif  item["syntagma"] == [u'klitze', u'kleine']:
        #         #self.pretty_print_uniq(item)
                
        #         right_stem_syn = [u'klitz', u'klein']


        #         right_repl = [
        #                      (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'[0, 0]', u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
        #                      (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'[0, 1]', u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, None, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #                  ]


        #         right_syntagma = [u'klitze', u'kleine']


        #         right_baseline = ([[u'klitze', u'kleine'], u'klitz++klein', 2, 4, u'[2, 3]', u'[3, 4]', u'[1, 1]', u'[2, 2]', u'2', u'1'],)


        #         right_redu = [
        #                      (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                  ]



        #     else:
        #         assert False



        #     extracted_repl = item["repl"]
        #     extracted_redu = item["redu"]
        #     extracted_baseline = item["baseline"]
        #     extracted_syntagma = item["syntagma"]

        #     assert item["stem_syn"] == ["klitz", "klein"]
        #     extracted_repl.should.be.equal(right_repl)
        #     extracted_redu.should.be.equal(right_redu)
        #     extracted_baseline.should.be.equal(right_baseline)
        #     extracted_syntagma.should.be.equal(right_syntagma)

        #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma, "stem_syn":item["stem_syn"]})









    ###############################################################################################################################################
    ############################################### II. FullRepetativnes= False   #################################################################################
    #######################################################################################################################################
        #p(stats._language)
        #stats.recompute_syntagma_repetativity_scope(False)



        # # ### Case 5.2:
        # #full_repetativ_syntagma=True
        # syntagma = ["NN", "NE", "NN"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos", order_output_by_syntagma_order=False))
        # #p(data,"data")

        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'e', 7, 5, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #              (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #          ]


        # right_syntagma = [u'NN', u'NE', u'NN']


        # right_baseline = [
        #              [[u'klitze', u'kleine', u'\xfcberaschung'], 3, 3, u'[2, 3, 2]', u'[3, 4, 2]', u'[2, 1, 0]', u'[6, 2, 0]', None, None],
        #              [[u'klitze', u'kleine'], 4, 2, u'[3, 3]', u'[4, 4]', u'[2, 1]', u'[6, 2]', None, None],
        #              [[u'klitze'], 8, 1, u'3', u'4', u'2', u'6', None, None],
        #              [[u'klitze', u'kleine', u'\xfcberaschung', u'.'], 1, 4, u'[1, 2, 0, 0]', u'[2, 3, 0, 0]', u'[1, 1, 0, 0]', u'[2, 2, 0, 0]', None, None],
        #              [[u'kleine'], 7, 1, u'5', u'11', u'1', u'2', None, None],
        #              [[u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1, 6, u'[1, 2, 0, 0, 0, 0]', u'[2, 3, 0, 0, 0, 0]', u'[1, 1, 0, 0, 0, 0]', u'[2, 2, 0, 0, 0, 0]', None, None],
        #              [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1, 4, u'[2, 0, 0, 0]', u'[3, 0, 0, 0]', u'[1, 0, 0, 0]', u'[2, 0, 0, 0]', None, None],
        #              [[u'kleine', u'\xfcberaschung', u'.'], 2, 3, u'[3, 1, 0]', u'[7, 5, 0]', u'[1, 0, 0]', u'[2, 0, 0]', None, None],
        #              [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat'], 1, 5, u'[2, 0, 0, 0, 0]', u'[3, 0, 0, 0, 0]', u'[1, 0, 0, 0, 0]', u'[2, 0, 0, 0, 0]', None, None],
        #              [[u'klitze', u'kleine', u'\xfcberaschung', u'.', u'trotzdem'], 1, 5, u'[1, 2, 0, 0, 0]', u'[2, 3, 0, 0, 0]', u'[1, 1, 0, 0, 0]', u'[2, 2, 0, 0, 0]', None, None],
        #              [[u'kleine', u'\xfcberaschung', u'.', u'trotzdem', u'hat', u'sie'], 1, 6, u'[2, 0, 0, 0, 0, 0]', u'[3, 0, 0, 0, 0, 0]', u'[1, 0, 0, 0, 0, 0]', u'[2, 0, 0, 0, 0, 0]', None, None],
        #              [[u'kleine', u'\xfcberaschung'], 5, 2, u'[5, 4]', u'[11, 8]', u'[1, 0]', u'[2, 0]', None, None],
        #          ]


        # right_redu = [
        #              (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
        #              (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
        #          ]



        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)








        # # # ####################################################################################
        # # # ####################################################################################
        # # # #################################################################################


        # # #### EN ######
        # #stats = Stats(mode=self.mode)

        # stats = Stats(mode=self.mode,use_cash=True)#, )
        # stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        
        


        # ### Case 1.1:
        # syntagma = ["big"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (25, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'bi^3g', u'i', 3, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #              (26, 4444, u'[13]', u'[0, 16]', u'[0, 10]', u'big', u'bi^15g', u'i', 15, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'big']


        # right_baseline = [[[u'big'], 5, 1, u'2', u'2', u'2', u'5', None, None]]


        # right_redu = [
        #              (7, 5555, u'[8, 2, 11, 4]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'),
        #              (6, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'{"bi^3g": 1, "bi^15g": 1}', 2, u'NN', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #          ]



        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])



        # # # ####################################################################################
        # # # ####################################################################################
        # # # #################################################################################


        # ### Case 1.2:
        # syntagma = ["biiiiiiig"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]

        # right_repl = [
        #              (25, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'bi^3g', u'i', 3, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #              (26, 4444, u'[13]', u'[0, 16]', u'[0, 10]', u'big', u'bi^15g', u'i', 15, 1, u'NN', u'["neutral", 0.0]', u'[0, 15]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'big']


        # right_baseline = [[[u'big'], 5, 1, u'2', u'2', u'2', u'5', None, None]]


        # right_redu = [
        #              (7, 5555, u'[8, 2, 11, 4]', u'[0, 5]', u'[0, 5]', u'big', u'{"big": 3}', 3, u'JJ', u'["neutral", 0.0]', u'tiny', u'["JJ"]', u'model', u'["NN"]', u',', u'["symbol"]', u'but', u'["CC"]', u'a', u'["DT"]', u'explanation', u'["NN"]', u'.', u'["symbol"]', u'right', u'["UH"]', u'?', u'["symbol"]', u'what', u'["WP"]'),
        #              (6, 4444, u'[13]', u'[0, 15]', u'[0, 10]', u'big', u'{"bi^3g": 1, "bi^15g": 1}', 2, u'NN', u'["neutral", 0.0]', u'can', u'["MD"]', u'use', u'["VB"]', u'for', u'["IN"]', u'explain', u'["VB"]', u'a', u'["DT"]', u'things', u'["NNS"]', u'.', u'["symbol"]', None, None, None, None, None, None),
        #          ]


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)

        # data.should.be.equal([{"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma}])







        # # # ####################################################################################
        # # # #################. WORK WITH EMOJIS   #########################################
        # # # ####################################################################################

        # ### Case 2.1:
        # syntagma = ["EMOIMG"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]

        # right_repl = [
        #              (62, 6666, u'[3, 9]', u'[1, 12]', u'[1, 8]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', None, None, None, None, None, None, None, None, None, None),
        #              (58, 6666, u'[3, 9]', u'[1, 8]', u'[1, 4]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None),
        #              (59, 6666, u'[3, 9]', u'[1, 9]', u'[1, 5]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["NNP", {"bu^5t": 1, "b^5ut": 1}]', u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None),
        #              (60, 6666, u'[3, 9]', u'[1, 10]', u'[1, 6]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'you', u'["JJ", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None),
        #              (61, 6666, u'[3, 9]', u'[1, 11]', u'[1, 7]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'but', u'["CC", {"b^6ut": 1, "b^5ut": 2}]', u'you', u'["VBD"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None),
        #              (70, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None),
        #              (71, 7777, u'[19]', u'[0, 19]', u'[0, 17]', u'\U0001f308', u'\U0001f308^7', u'\U0001f308', 7, 0, u'EMOIMG', u'["positive", 0.27]', None, u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None, None, None),
        #              (22, 3333, u'[14]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.6999999999999998]', None, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None),
        #              (32, 5555, u'[8, 2, 11, 4]', u'[2, 8]', u'[2, 8]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["neutral", 0.0]', None, u'think', u'["VB"]', u'about', u'["IN"]', u'it', u'["PRP"]', u'?', u'["symbol"]', 1, u'["number"]', 1, u'["number"]', u'.', u'["symbol"]', u'but', u'["NNP", {"bu^5t^4": 1, "b^5u^4t^4": 1}]', u'you', u'["NN", {"yo^6u": 1, "y^6ou": 1}]', u'but', u'["FW", {"b^5u^5t": 1, "b^5ut^4": 1, "b^6ut": 1}]'),
        #              (63, 7777, u'[19]', u'[0, 7]', u'[0, 7]', u'\U0001f62b', u'\U0001f62b^4', u'\U0001f62b', 4, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB"]', u'bad', u'["JJ"]', u'surprise', u'["NN"]', u'for', u'["IN"]', u'me', u'["PRP"]', u',', u'["symbol"]', u'but', u'["MD"]', u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]'),
        #          ]


        # right_syntagma = [u'EMOIMG']


        # right_baseline = [
        #              [[u'\U0001f62b', u'1'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'\U0001f62b', u',', u'but', u'i', u'realy'], 1, 5, None, None, None, None, None, None],
        #              [[u'\U0001f600', u'\U0001f308'], 3, 2, u'[3, 3]', u'[3, 3]', None, None, u'3', u'0'],
        #              [[u'\U0001f600', u'\U0001f308', u'\U0001f600'], 3, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'],
        #              [[u'\U0001f62b', u'1', u'.', u'but', u'you'], 1, 5, None, None, None, None, None, None],
        #              [[u'\U0001f62b', u'1', u'.'], 1, 3, None, None, None, None, None, None],
        #              [[u'\U0001f62b', u',', u'but', u'i', u'realy', u'liked'], 1, 6, None, None, None, None, None, None],
        #              [[u'\U0001f62b', u','], 1, 2, None, None, None, None, None, None],
        #              [[u'\U0001f600', u'\U0001f308', u'\U0001f600', u'\U0001f308'], 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'],
        #              [[u'\U0001f308', u'\U0001f600', u'\U0001f308'], 1, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'],
        #              [[u'\U0001f62b', u'#shetlife'], 1, 2, None, None, None, None, None, None],
        #              [[u'\U0001f308'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'\U0001f62b', u',', u'but'], 1, 3, None, None, None, None, None, None],
        #              [[u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 3, None, None, None, None, None, None],
        #              [[u'\U0001f62b', u'1', u'.', u'but', u'you', u'but'], 1, 6, None, None, None, None, None, None],
        #              [[u'\U0001f308', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'],
        #              [[u'\U0001f600'], 5, 1, u'4', u'4', u'0', u'0', None, None],
        #              [[u'\U0001f308', u'\U0001f600'], 3, 2, u'[2, 2]', u'[2, 2]', None, None, u'2', u'0'],
        #              [[u'\U0001f62b', u'1', u'.', u'but'], 1, 4, None, None, None, None, None, None],
        #              [[u'\U0001f62b'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'\U0001f62b', u',', u'but', u'i'], 1, 4, None, None, None, None, None, None],
        #              [[u'\U0001f600', u'\U0001f308', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 5, u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', None, None, u'1', u'0'],
        #          ]


        # right_redu = ()




        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)



        # # # ####################################################################################
        # # # ####################################################################################
        # # # #################################################################################
  



        # ### Case 2.2:
        # #- sentiment=False
        # syntagma = ["EMOASC"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)

        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [
        #              (13, 2222, u'[5]', u'[0, 4]', u'[0, 4]', u'-)', u'-)^4', u')', 4, 1, u'EMOASC', u'["neutral", 0.0]', None, None, None, u'glad', u'["NN"]', u'to', u'["TO"]', u'se', u'["VB"]', u'you', u'["PRP"]', None, None, None, None, None, None, None, None, None, None),
        #              (21, 3333, u'[14]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'(', 4, 1, u'EMOASC', u'["negative", -0.6999999999999998]', None, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None),
        #              (69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None),
        #              (10, 1111, u'[4, 14]', u'[1, 14]', u'[1, 9]', u':-(', u':-(^5', u'(', 5, 2, u'EMOASC', u'["negative", -0.1875]', None, u'very', u'["JJ", {"very": 1, "ver^4y^5": 1, "v^3er^8y": 1}]', u'pity', u'["JJ", {"pity": 2, "pi^3t^3y^3": 1, "pi^9ty": 1}]', u'for', u'["IN"]', u'me', u'["PRP"]', u'.', u'["symbol"]', u'@real_trump', u'["mention"]', u'#shetlife', u'["hashtag"]', u'#readytogo', u'["hashtag"]', u'http://www.absurd.com', u'["URL"]', None, None),
        #          ]


        # right_syntagma = [u'EMOASC']


        # right_baseline = [
        #              [[u':-(', u'@real_trump', u'#shetlife'], 1, 3, None, None, None, None, None, None],
        #              [[u'-(', u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 4, None, None, None, None, None, None],
        #              [[u'=)'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u':-('], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u':-(', u'@real_trump', u'#shetlife', u'#readytogo'], 1, 4, None, None, None, None, None, None],
        #              [[u'-)'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'=)', u'\U0001f600', u'\U0001f308'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'=)', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 4, None, None, None, None, None, None],
        #              [[u'=)', u'\U0001f600'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u':-(', u'@real_trump'], 1, 2, None, None, None, None, None, None],
        #              [[u'-(', u'\U0001f62b'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'-('], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u':-(', u'@real_trump', u'#shetlife', u'#readytogo', u'http://www.absurd.com'], 1, 5, None, None, None, None, None, None],
        #              [[u'-(', u'\U0001f62b', u'#shetlife'], 1, 3, None, None, None, None, None, None],
        #          ]


        # right_redu = ()

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)









        # ### Case 2.3:
        # syntagma = ["EMOASC","EMOIMG"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]



        # right_repl = [
        #              (21, 3333, u'[14]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'(', 4, 1, u'EMOASC', u'["negative", -0.6999999999999998]', None, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None),
        #              (69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None),
        #              (70, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None),
        #              (22, 3333, u'[14]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.6999999999999998]', None, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None),
        #          ]


        # right_syntagma = [u'EMOASC', u'EMOIMG']


        # right_baseline = [
        #              [[u'\U0001f600', u'\U0001f308'], 3, 2, u'[3, 3]', u'[3, 3]', None, None, u'3', u'0'],
        #              [[u'\U0001f600'], 5, 1, u'4', u'4', u'0', u'0', None, None],
        #              [[u'-(', u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 4, None, None, None, None, None, None],
        #              [[u'=)'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'\U0001f62b', u'#shetlife'], 1, 2, None, None, None, None, None, None],
        #              [[u'=)', u'\U0001f600', u'\U0001f308'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'=)', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 4, None, None, None, None, None, None],
        #              [[u'\U0001f62b'], 3, 1, u'3', u'3', u'0', u'0', None, None],
        #              [[u'=)', u'\U0001f600'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 3, None, None, None, None, None, None],
        #              [[u'-(', u'\U0001f62b'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'-('], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #              [[u'\U0001f600', u'\U0001f308', u'\U0001f600'], 3, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'],
        #              [[u'-(', u'\U0001f62b', u'#shetlife'], 1, 3, None, None, None, None, None, None],
        #          ]


        # right_redu = ()

        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)





        # ### Case 2.4:
        # #order_output_by_syntagma_order
        # syntagma = ["EMOASC","EMOIMG"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="pos",order_output_by_syntagma_order=True))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=True)



        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]





        # right_repl = [
        #             (u'EMOASC', (
        #                          (21, 3333, u'[14]', u'[0, 14]', u'[0, 10]', u'-(', u'-(^4', u'(', 4, 1, u'EMOASC', u'["negative", -0.6999999999999998]', None, u'we', u'["PRP"]', u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'\U0001f62b', u'["EMOIMG"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None),
        #                          (69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None),
        #                      )
        #               ),
        #             (u'EMOIMG', (
        #                          (70, 7777, u'[19]', u'[0, 18]', u'[0, 16]', u'\U0001f600', u'\U0001f600^5', u'\U0001f600', 5, 0, u'EMOIMG', u'["positive", 0.27]', None, u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'=)', u'["EMOASC"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None, None, None),
        #                          (22, 3333, u'[14]', u'[0, 15]', u'[0, 11]', u'\U0001f62b', u'\U0001f62b^12', u'\U0001f62b', 12, 0, u'EMOIMG', u'["negative", -0.6999999999999998]', None, u'can', u'["MD"]', u'not', u'["RB"]', u'acept', u'["VB"]', u'.', u'["symbol"]', u'-(', u'["EMOASC"]', u'#shetlife', u'["hashtag", {"#shetlife": 2}]', u'http://www.noooo.com', u'["URL"]', None, None, None, None, None, None),
        #                      )
        #               ),
        #          ]


        # right_syntagma = [u'EMOASC', u'EMOIMG']


        # right_baseline = [[[u'\U0001f600', u'\U0001f308'], 3, 2, u'[3, 3]', u'[3, 3]', None, None, u'3', u'0'], [[u'\U0001f600'], 5, 1, u'4', u'4', u'0', u'0', None, None], [[u'-(', u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 4, None, None, None, None, None, None], [[u'=)'], 1, 1, u'1', u'1', u'0', u'0', None, None], [[u'\U0001f62b', u'#shetlife'], 1, 2, None, None, None, None, None, None], [[u'=)', u'\U0001f600', u'\U0001f308'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'], [[u'=)', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 4, None, None, None, None, None, None], [[u'\U0001f62b'], 3, 1, u'3', u'3', u'0', u'0', None, None], [[u'=)', u'\U0001f600'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], [[u'\U0001f62b', u'#shetlife', u'http://www.noooo.com'], 1, 3, None, None, None, None, None, None], [[u'-(', u'\U0001f62b'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'], [[u'-('], 1, 1, u'1', u'1', u'0', u'0', None, None], [[u'\U0001f600', u'\U0001f308', u'\U0001f600'], 3, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'], [[u'-(', u'\U0001f62b', u'#shetlife'], 1, 3, None, None, None, None, None, None]]


        # right_redu = ()


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)






        # # # ####################################################################################
        # # # #################. WORK WITH SENTIMENT   #########################################
        # # # #################################################################################



        # ### Case 3.1:
        # #- sentiment="positive"
        # syntagma = ["EMOASC"]
        # data = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment="positive", syntagma_type="pos"))
        # #p(data,"data")
        # #self.pretty_print_uniq(data[0],syn_order=False)


        # extracted_repl = data[0]["repl"]
        # extracted_redu = data[0]["redu"]
        # extracted_baseline = data[0]["baseline"]
        # extracted_syntagma = data[0]["syntagma"]


        # right_repl = [(69, 7777, u'[19]', u'[0, 17]', u'[0, 15]', u'=)', u'=)^10', u')', 10, 1, u'EMOASC', u'["positive", 0.27]', None, u'i', u'["PRP"]', u'realy', u'["RB", {"realy": 1, "real^3y": 1, "re^5al^4y^3": 1}]', u'liked', u'["VBD"]', u'it', u'["PRP"]', u':p', u'["EMOASC"]', u'\U0001f600', u'["EMOIMG"]', u'\U0001f308', u'["EMOIMG"]', u'\U0001f600', u'["EMOIMG"]', None, None, None, None)]


        # right_syntagma = [u'EMOASC']


        # right_baseline = [
        #              [[u'=)', u'\U0001f600'], 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'],
        #              [[u'=)', u'\U0001f600', u'\U0001f308'], 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'],
        #              [[u'=)', u'\U0001f600', u'\U0001f308', u'\U0001f600'], 1, 4, None, None, None, None, None, None],
        #              [[u'=)'], 1, 1, u'1', u'1', u'0', u'0', None, None],
        #          ]


        # right_redu = ()


        # extracted_repl.should.be.equal(right_repl)
        # extracted_redu.should.be.equal(right_redu)
        # extracted_baseline.should.be.equal(right_baseline)
        # extracted_syntagma.should.be.equal(right_syntagma)



    ################################################################################################
    ################################################################################################
    ###################################################################################################
    ############################stemmed_search = True #########################################
    #################################################################################################
    ################################################################################################
    ################################################################################################



        # ########stemmed_search=True #

        # ### Case 10.1:
        # syntagma = ["klein"]
        # items = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True))
        # #item = item
        # #self.pretty_print_uniq(item)
        # #p(items,"item")
        # for item in items:
        #     #p(item["syntagma"])

        #     if item["syntagma"] == [u'kleines']:
        #         #self.pretty_print_uniq(item)


        #         right_repl = [
        #                      (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                  ]


        #         right_syntagma = [u'kleines']


        #         right_baseline = [[u'kleines'], 5, 1, u'klein', u'5', u'11', u'2', u'5', None, None]


        #         right_redu = [
        #                      (11, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (6, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'klein', u'{"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}', 3, u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                  ]






        #     elif item["syntagma"] == [u'kleinere']:
        #         #self.pretty_print_uniq(item)
        #         right_repl = [
        #                      (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                      (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                      (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                  ]


        #         right_syntagma = [u'kleinere']


        #         right_baseline = [[u'kleinere'], 2, 1, u'klein', u'2', u'3', u'1', u'2', None, None]


        #         right_redu = [(7, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'klein', u'{"kleinere^5": 1, "kleine^3r^2e^5": 1}', 2, u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')]






        #     elif  item["syntagma"] == [u'kleine']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #                      (57, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (58, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (59, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (71, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (72, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (73, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (74, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                  ]


        #         right_syntagma = [u'kleine']


        #         right_baseline = [[u'kleine'], 7, 1, u'klein', u'5', u'11', u'1', u'2', None, None]


        #         right_redu = [(2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]






        #     elif  item["syntagma"] == [u'klein']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klein']


        #         right_baseline = [[u'klein'], 2, 1, u'klein', u'2', u'4', u'1', u'2', None, None]


        #         right_redu = [(9, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)]



        #     else:
        #         assert False



        #     extracted_repl = item["repl"]
        #     extracted_redu = item["redu"]
        #     extracted_baseline = item["baseline"]
        #     extracted_syntagma = item["syntagma"]

        #     item["stem_syn"] = ["klein"]
        #     extracted_repl.should.be.equal(right_repl)
        #     extracted_redu.should.be.equal(right_redu)
        #     extracted_baseline.should.be.equal(right_baseline)
        #     extracted_syntagma.should.be.equal(right_syntagma)

        #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma, "stem_syn":item["stem_syn"]})




        # ########stemmed_search=True #

        # ### Case 10.2:
        # syntagma = ["kleines"]
        # items = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True))
        # #item = item
        # #self.pretty_print_uniq(item)
        # #p(items,"item")
        # for item in items:
        #     #p(item["syntagma"])

        #     if item["syntagma"] == [u'kleines']:
        #         #self.pretty_print_uniq(item)


        #         right_repl = [
        #                      (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (26, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u'e', 4, 5, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (27, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'kleine^4s^7', u'klein', u's', 7, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (28, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'n', 4, 4, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (29, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u'e', 3, 5, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (30, 10000, u'[12, 3, 8]', u'[1, 1]', u'[1, 0]', u'kleines', u'klein^4e^3s^4', u'klein', u's', 4, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (31, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'e', 4, 2, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (32, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'i', 5, 3, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (33, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u'n', 3, 4, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                      (34, 10000, u'[12, 3, 8]', u'[1, 2]', u'[1, 0]', u'kleines', u'kle^4i^5n^3e^2s^3', u'klein', u's', 3, 6, u'NN', u'["neutral", 0.0]', u'[1, 0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                  ]


        #         right_syntagma = [u'kleines']


        #         right_baseline = [[u'kleines'], 5, 1, u'klein', u'5', u'11', u'2', u'5', None, None]


        #         right_redu = [
        #                      (11, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (6, 10000, u'[12, 3, 8]', u'[1, 0]', u'[1, 0]', u'kleines', u'klein', u'{"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}', 3, u'NN', u'["neutral", 0.0]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]', u'beser', u'["ADJD", null, "bes"]', u'kan', u'["FM", {"ka^4n^5": 1, "kan^6": 1}, "kan"]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]'),
        #                  ]






        #     elif item["syntagma"] == [u'kleinere']:
        #         #self.pretty_print_uniq(item)
        #         right_repl = [
        #                      (37, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'kleinere^5', u'klein', u'e', 5, 7, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                      (38, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 3, 5, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                      (39, 10000, u'[12, 3, 8]', u'[2, 1]', u'[2, 0]', u'kleinere', u'kleine^3r^2e^5', u'klein', u'e', 5, 7, u'NE', u'["neutral", 0.0]', u'[2, 0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]'),
        #                  ]


        #         right_syntagma = [u'kleinere']


        #         right_baseline = [[u'kleinere'], 2, 1, u'klein', u'2', u'3', u'1', u'2', None, None]


        #         right_redu = [(7, 10000, u'[12, 3, 8]', u'[2, 0]', u'[2, 0]', u'kleinere', u'klein', u'{"kleinere^5": 1, "kleine^3r^2e^5": 1}', 2, u'NE', u'["neutral", 0.0]', u'es', u'["VVFIN", null, "es"]', u'.', u'["symbol", null, "."]', u'kleines', u'["NN", {"kle^4i^5n^3e^2s^3": 1, "klein^4e^3s^4": 1, "kleine^4s^7": 1}, "klein"]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]')]






        #     elif  item["syntagma"] == [u'kleine']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #                      (57, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (58, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (59, 11111, u'[5, 6, 14]', u'[2, 4]', u'[2, 4]', u'kleine', u'kle^5i^2n^4e^5', u'klein', u'e', 5, 5, u'ADJA', u'["neutral", 0.0]', None, u'!', u'["symbol", null, "!"]', u'weil', u'["KOUS", null, "weil"]', u'es', u'["PPER", null, "es"]', u'ja', u'["PTKMA", null, "ja"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'ist', u'["VAFIN", null, "ist"]', u'.', u'["symbol", null, "."]', 1, u'["number", null, "1"]', 2, u'["number", null, "2"]'),
        #                      (71, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 4, 2, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (72, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'i', 5, 3, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (73, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'n', 4, 4, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                      (74, 12222, u'[24]', u'[0, 24]', u'[0, 21]', u'kleine', u'kle^4i^5n^4e^8', u'klein', u'e', 8, 5, u'ADJA', u'["neutral", 0.0]', None, u',', u'["symbol", null, ","]', u'es', u'["PPER", null, "es"]', u'war', u'["VAFIN", null, "war"]', u'so', u'["ADV", null, "so"]', u'eine', u'["ART", null, "ein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', None, None, None, None, None, None),
        #                  ]


        #         right_syntagma = [u'kleine']


        #         right_baseline = [[u'kleine'], 7, 1, u'klein', u'5', u'11', u'1', u'2', None, None]


        #         right_redu = [(2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]')]






        #     elif  item["syntagma"] == [u'klein']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klein']


        #         right_baseline = [[u'klein'], 2, 1, u'klein', u'2', u'4', u'1', u'2', None, None]


        #         right_redu = [(9, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None)]



        #     else:
        #         assert False



        #     extracted_repl = item["repl"]
        #     extracted_redu = item["redu"]
        #     extracted_baseline = item["baseline"]
        #     extracted_syntagma = item["syntagma"]

        #     assert item["stem_syn"] == ["klein"]
        #     extracted_repl.should.be.equal(right_repl)
        #     extracted_redu.should.be.equal(right_redu)
        #     extracted_baseline.should.be.equal(right_baseline)
        #     extracted_syntagma.should.be.equal(right_syntagma)

        #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma, "stem_syn":item["stem_syn"]})






        # ########stemmed_search=True #

        # ### Case 10.3:
        # syntagma = ["klitze","kleines"]
        # items = list(stats.get_data(syntagma, repl=True, redu=True, baseline=True, sentiment=False, syntagma_type="lexem",stemmed_search=True))
        # #item = item
        # #self.pretty_print_uniq(item)
        # #p(items,"item")
        # for item in items:
        #     #p(item["syntagma"])

        #     if item["syntagma"] == [u'klitzes', u'kleines']:
        #         #self.pretty_print_uniq(item)



        #         right_repl = [
        #                      (49, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitzes^4', u'klitz', u's', 4, 6, u'FM', u'["neutral", 0.0]', u'[2, 10]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (50, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u'i', 3, 2, u'FM', u'["neutral", 0.0]', u'[2, 10]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (51, 10000, u'[12, 3, 8]', u'[2, 11]', u'[2, 6]', u'klitzes', u'kli^3tzes^3', u'klitz', u's', 3, 6, u'FM', u'["neutral", 0.0]', u'[2, 10]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (52, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein^3e^2s', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                      (53, 10000, u'[12, 3, 8]', u'[2, 13]', u'[2, 7]', u'kleines', u'kleines^4', u'klein', u's', 4, 6, u'FM', u'["neutral", 0.0]', u'[2, 12]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klitzes', u'kleines']


        #         right_baseline = [[u'klitzes', u'kleines'], 1, 2, u'klitz++klein', u'[2, 2]', u'[3, 2]', u'[1, 1]', u'[2, 2]', None, None]


        #         right_redu = [
        #                      (10, 10000, u'[12, 3, 8]', u'[2, 10]', u'[2, 6]', u'klitzes', u'klitz', u'{"klitzes^4": 1, "kli^3tzes^3": 1}', 2, u'FM', u'["neutral", 0.0]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None, None, None, None, None),
        #                      (11, 10000, u'[12, 3, 8]', u'[2, 12]', u'[2, 7]', u'kleines', u'klein', u'{"klein^3e^2s": 1, "kleines^4": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', None, None, None, None, None, None, None, None, None, None),
        #                  ]






        #     elif item["syntagma"] == [u'klitz', u'klein']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (42, 10000, u'[12, 3, 8]', u'[2, 5]', u'[2, 3]', u'klitz', u'kli^4tz', u'klitz', u'i', 4, 2, u'NE', u'["neutral", 0.0]', u'[2, 4]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (43, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'i', 4, 2, u'NE', u'["neutral", 0.0]', u'[2, 4]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (44, 10000, u'[12, 3, 8]', u'[2, 6]', u'[2, 3]', u'klitz', u'kli^4tz^3', u'klitz', u'z', 3, 4, u'NE', u'["neutral", 0.0]', u'[2, 4]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (45, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'e', 3, 2, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (46, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'i', 3, 3, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (47, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'kle^3i^3n^3', u'klein', u'n', 3, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                      (48, 10000, u'[12, 3, 8]', u'[2, 8]', u'[2, 4]', u'klein', u'klein^5', u'klein', u'n', 5, 4, u'FM', u'["neutral", 0.0]', u'[2, 7]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]


        #         right_syntagma = [u'klitz', u'klein']


        #         right_baseline = [[u'klitz', u'klein'], 1, 2, u'klitz++klein', u'[2, 2]', u'[3, 4]', u'[1, 1]', u'[3, 2]', None, None]


        #         right_redu = [
        #                      (8, 10000, u'[12, 3, 8]', u'[2, 4]', u'[2, 3]', u'klitz', u'klitz', u'{"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}', 3, u'NE', u'["neutral", 0.0]', u'm\xe4dchen', u'["NN", null, "madch"]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klein', u'["FM", {"kle^3i^3n^3": 1, "klein^5": 1}, "klein"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None),
        #                      (9, 10000, u'[12, 3, 8]', u'[2, 7]', u'[2, 4]', u'klein', u'klein', u'{"kle^3i^3n^3": 1, "klein^5": 1}', 2, u'FM', u'["neutral", 0.0]', u'.', u'["symbol", null, "."]', u'kleinere', u'["NE", {"kleinere^5": 1, "kleine^3r^2e^5": 1}, "klein"]', u'auswahl', u'["NN", null, "auswahl"]', u'.', u'["symbol", null, "."]', u'klitz', u'["NE", {"kli^4tz": 1, "klitz": 1, "kli^4tz^3": 1}, "klitz"]', u'.', u'["symbol", null, "."]', u'klitzes', u'["FM", {"klitzes^4": 1, "kli^3tzes^3": 1}, "klitz"]', u'kleines', u'["FM", {"klein^3e^2s": 1, "kleines^4": 1}, "klein"]', None, None, None, None),
        #                  ]




        #     elif  item["syntagma"] == [u'klitze', u'kleine']:
        #         #self.pretty_print_uniq(item)

        #         right_repl = [
        #                      (1, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (2, 8888, u'[4, 11]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze^7', u'klitz', u'e', 7, 5, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (20, 10000, u'[12, 3, 8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]'),
        #                      (54, 11111, u'[5, 6, 14]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'klitz', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'sache', u'["NN", null, "sach"]', u'.', u'["symbol", null, "."]', u'die', u'["PDS", null, "die"]', u'aber', u'["ADV", null, "aber"]'),
        #                      (3, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (4, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5in^5e', u'klein', u'n', 5, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (5, 8888, u'[4, 11]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'klein', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                      (21, 10000, u'[12, 3, 8]', u'[0, 2]', u'[0, 2]', u'kleine', u'kle^5ine', u'klein', u'e', 5, 2, u'ADJA', u'["neutral", 0.0]', None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'klitze', u'["ADJA", null, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'@sch\xf6nesleben', u'["mention", null, "@schonesleb"]', u'#machwasdaraus', u'["hashtag", null, "#machwasdaraus"]', u'#bewegedeinarsch', u'["hashtag", null, "#bewegedeinarsch"]', u'https://www.freiesinternet.de', u'["URL", null, "https://www.freiesinternet.d"]'),
        #                  ]


        #         right_syntagma = [u'klitze', u'kleine']


        #         right_baseline = [[u'klitze', u'kleine'], 4, 2, u'klitz++klein', u'[3, 3]', u'[4, 4]', u'[2, 1]', u'[6, 2]', None, None]


        #         right_redu = [
        #                      (1, 8888, u'[4, 11]', u'[0, 0]', u'[0, 0]', u'klitze', u'klitz', u'{"klitze": 1, "kli^4tze^7": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5in^5e": 1, "klein^3e": 1}, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]'),
        #                      (12, 12222, u'[24]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitz', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART", null, "ein"]', u'kleine', u'["ADJA", null, "klein"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u',', u'["symbol", null, ","]', u'die', u'["PRELS", null, "die"]', u'ich', u'["PPER", null, "ich"]'),
        #                      (2, 8888, u'[4, 11]', u'[0, 2]', u'[0, 1]', u'kleine', u'klein', u'{"kle^5in^5e": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze^7": 1}, "klitz"]', u'\xfcberaschung', u'["NN", null, "uberasch"]', u'.', u'["symbol", null, "."]', u'trotzdem', u'["PAV", null, "trotzd"]', u'hat', u'["VAFIN", null, "hat"]', u'sie', u'["PPER", null, "sie"]'),
        #                  ]




        #     else:
        #         assert False



        #     extracted_repl = item["repl"]
        #     extracted_redu = item["redu"]
        #     extracted_baseline = item["baseline"]
        #     extracted_syntagma = item["syntagma"]

        #     assert item["stem_syn"] == ["klitz", "klein"]
        #     extracted_repl.should.be.equal(right_repl)
        #     extracted_redu.should.be.equal(right_redu)
        #     extracted_baseline.should.be.equal(right_baseline)
        #     extracted_syntagma.should.be.equal(right_syntagma)

        #     item.should.be.equal({"repl":right_repl, "redu":right_redu,"baseline":right_baseline, "syntagma":right_syntagma, "stem_syn":item["stem_syn"]})









    @attr(status='stable')
    #@wipd
    def test_test_get_header_for_exhausted_output_table_type_612_1(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))


        ## Case 1:
        cols = stats._get_header_exhausted(repl=False, redu=False, baseline=False, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        assert not cols
        #for k,v in cols.iteritems():
        #    assert not v


        ###### repl = True

        ## Case 2.1:
        cols = stats._get_header_exhausted(repl=True, redu=False, baseline=False, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]

        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu'))
        assert not cols["redu"] 
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        assert not cols["baseline"] 



        ## Case 2.2:
        cols = stats._get_header_exhausted(repl=True, redu=False, baseline=False, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]

        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu'))
        assert not cols["redu"] 
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        assert not cols["baseline"] 


        ## Case 2.3:
        cols = stats._get_header_exhausted(repl=True, redu=False, baseline=True, additional_doc_cols=False, context_len_left=1, context_len_right=1)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        #print cols["context"]
        #print cols["baseline"]

        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu'))
        assert not cols["redu"] 
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL1', 'context_infoL1', 'contextR1', 'context_infoR1'))
        cols["baseline"].should.be.equal(('syntagma', 'stemmed', 'scope', 'occur_syntagma_all', 'occur_repl_uniq', 'occur_repl_exhausted', 'occur_full_syn_repl'))


        ## Case 2.4:
        cols = stats._get_header_exhausted(repl=True, redu=False, baseline=False, additional_doc_cols=False, context_len_left=False, context_len_right=False)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        #print cols["context"]

        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu'))
        assert not cols["redu"] 
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        assert not cols["context"]
        assert not cols["baseline"] 



        ## Case 2.5:
        #additional_doc_cols = True
        cols = stats._get_header_exhausted(repl=True, redu=False, baseline=False, additional_doc_cols=["gender", "sex"], context_len_left=False, context_len_right=False)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        #print cols["document"]
        #print cols["context"]

        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu'))
        assert not cols["redu"] 
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'), ('gender', 'sex')))
        assert not cols["context"]
        assert not cols["baseline"] 




        ###### redu ; baseline

        ## Case 2.1:
        cols = stats._get_header_exhausted(repl=False, redu=True, baseline=False, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]
        # print cols["baseline"]


        assert not cols["repl"] 
        cols["redu"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'orig_words', 'redu_length'))
        cols["word"].should.be.equal(('normalized_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        assert not cols["baseline"]


        ###### redu  baseline
        ## Case 2.2:
        cols = stats._get_header_exhausted(repl=False, redu=True, baseline=True, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]
        #print cols["baseline"]

        assert not cols["repl"] 
        cols["redu"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'orig_words', 'redu_length'))
        cols["word"].should.be.equal(('normalized_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        cols["baseline"].should.be.equal(('syntagma', 'stemmed', 'scope', 'occur_syntagma_all', 'occur_redu_uniq', 'occur_redu_exhausted', 'occur_full_syn_redu'))





        ###### repl=True; redu = True; 

        ## Case 3.1:
        cols = stats._get_header_exhausted(repl=True, redu=True, baseline=False, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]
        # print cols["baseline"]


        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu')) 
        cols["redu"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'orig_words', 'redu_length'))
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        assert not cols["baseline"]


        ###### repl=True; redu = True; baseline=True;

        ## Case 4.1:
        cols = stats._get_header_exhausted(repl=True, redu=True, baseline=True, additional_doc_cols=False, context_len_left=True, context_len_right=True)
        #p(cols, "cols")
        # print cols["repl"]
        # print cols["redu"]
        # print cols["word"]
        # print cols["document"]
        # print cols["context"]
        #print cols["baseline"]


        cols["repl"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'repl_letter', 'repl_length', 'index_of_repl', 'in_redu')) 
        cols["redu"].should.be.equal(('id', 'index_in_corpus', 'index_in_redufree', 'orig_words', 'redu_length'))
        cols["word"].should.be.equal(('normalized_word', 'rle_word', 'stemmed', 'pos', 'polarity'))
        cols["document"].should.be.equal((('doc_id', 'redufree_len'),))
        cols["context"].should.be.equal(('contextL5', 'context_infoL5', 'contextL4', 'context_infoL4', 'contextL3', 'context_infoL3', 'contextL2', 'context_infoL2', 'contextL1', 'context_infoL1', 'contextR1', 'context_infoR1', 'contextR2', 'context_infoR2', 'contextR3', 'context_infoR3', 'contextR4', 'context_infoR4', 'contextR5', 'context_infoR5'))
        cols["baseline"].should.be.equal(('syntagma', 'stemmed', 'scope', 'occur_syntagma_all', 'occur_repl_uniq', 'occur_repl_exhausted', 'occur_redu_uniq', 'occur_redu_exhausted', 'occur_full_syn_repl', 'occur_full_syn_redu'))







    @attr(status='stable')
    #@wipd
    def test_test_get_header_for_sum_output_table_type_612_2(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))


        ## Case 1:
        cols = stats._get_header_sum(repl=False, redu=False, word_examples_sum_table=True)
        #p(cols, "cols")
        cols.should.be.equal(False)


        #### repl #####
        ## Case 2.1:
        cols = stats._get_header_sum(repl=True, redu=False, word_examples_sum_table=True)
        #p(cols, "cols")
        cols.should.be.equal(('letter', 'NrOfRepl', 'Occur', 'Examples'))

        ## Case 2.2:
        cols = stats._get_header_sum(repl=True, redu=False, word_examples_sum_table=False)
        #p(cols, "cols")
        cols.should.be.equal(('letter', 'NrOfRepl', 'Occur'))



        #### redu #####
        ## Case 2.1:
        cols = stats._get_header_sum(repl=False, redu=True, word_examples_sum_table=True)
        #p(cols, "cols")
        cols.should.be.equal(('word', 'ReduLength', 'Occur'))

        ## Case 2.2:
        cols = stats._get_header_sum(repl=False, redu=True, word_examples_sum_table=False)
        #p(cols, "cols")
        cols.should.be.equal(('word', 'ReduLength', 'Occur'))





    @attr(status='stable')
    @wipd
    def test_export_613_1(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )


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
        #p( stats.statsdb.getall("replications"))
        ########################################
        ######## EXHAUSTED TYPE ###########
        ########################################
        rewrite= True
        #self.tempdir_project_folder = "./export"
        # ######### I FOR ALL SYNTAGMA ##############
        # ##### Export in dirr formats
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,)
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="xml",output_table_type="exhausted",rewrite=rewrite,)
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="json",output_table_type="exhausted",rewrite=rewrite,)
        
        

        # #### Export with additional columns from CorpusDB
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            additional_doc_cols=["gender", "working_area", "age"],  fname="WITH_ADDIT_COLS_FROM_CORP",
            path_to_corpdb=os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))


        #### Export with NULL Kontext
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
                    context_len_left=False, context_len_right=False, fname="NULL_KONTEXT")
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
                    context_len_left=1, context_len_right=2, fname="1_2_KONTEXT_")


        #### Export with NULL Kontext
        stats.export(self.tempdir_project_folder, repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
                    max_scope=1, fname="MAX_SCOPE_VON_ONE")
# 







#         # # ######### II FOR FEW SYNTAGMA #############

        ##### stemmed search 
        stats.export(self.tempdir_project_folder, syntagma=["klitze"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
                   stemmed_search=True, fname="STEMMED_FOR_KLITZE")

        stats.export(self.tempdir_project_folder, syntagma=["klitze", "kleine"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=True, fname="STEMMED_FOR_KLITZE_KLEINE")

        stats.export(self.tempdir_project_folder, syntagma=["klitze", "kleine"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=False, fname="UN_STEMMED_FOR_KLITZE_KLEINE")

        stats.export(self.tempdir_project_folder, syntagma=[["klitze", "kleine"],["klitzes", "kleines"],["klitz", "klein"]], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=False, fname="UN_STEMMED_FOR_ALL_KLITZ_KLEIN")

        # ##### pos search 
        stats.export(self.tempdir_project_folder, syntagma=["EMOIMG", "EMOASC"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=False, fname="EMOIMG_EMOASC", syntagma_type="pos")


        stats.export(self.tempdir_project_folder, syntagma=["EMOIMG"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=False, fname="EMOIMG", syntagma_type="pos")


        stats.export(self.tempdir_project_folder, syntagma=["EMOASC"], repl=True, redu=True,export_file_type="csv",output_table_type="exhausted",rewrite=rewrite,
            stemmed_search=False, fname="EMOASC", syntagma_type="pos")

        # # ########################################
        # # ######## SUM TYPE ###########
        # # ########################################
        stats.export(self.tempdir_project_folder, repl=True, redu=False,export_file_type="csv", output_table_type="sum", fname="SUM_REPL",rewrite=rewrite,)
        stats.export(self.tempdir_project_folder, repl=False, redu=True,export_file_type="csv", output_table_type="sum", fname="SUM_REDU",rewrite=rewrite,)

        stats.export(self.tempdir_project_folder,syntagma=["EMOIMG"], repl=True, redu=False,export_file_type="csv", rewrite=rewrite,
            output_table_type="sum", fname="SUM_REPL_EMOIMG",syntagma_type="pos")
        stats.export(self.tempdir_project_folder,syntagma=["EMOASC"], repl=False, redu=True,export_file_type="csv", rewrite=rewrite,
            output_table_type="sum", fname="SUM_REDU_EMOASC",syntagma_type="pos")




        files = os.listdir(self.tempdir_project_folder)
        #p(files)
        len(files).should.be.equal(18)



    @attr(status='stable')
    #@wipd
    def test_test_export_generator_613_2(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )


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
        stats.attach_corpdb(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))
        
        # # ############################################################
        # # ####### output_table_type = "exhausted" ########
        # # ##################################################################

        ##################
        #### Case 1.1 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True



        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")




        ##################
        #### Case 1.2 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True



        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = ["klitze","kleine"]
        stemmed_search = True

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")




        ##################
        #### Case 1.3 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = True

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")


        ##################
        #### Case 1.3 ######
        ##################
        repl = False
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 38
        #p(header, "header")
        #syntagma = ["kleine"]
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = True

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")


        ##################
        #### Case 1.4 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = True

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,sentiment="positive")

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")



        ##################
        #### Case 1.4 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"


        rows_equal = []
        rows_not_equal = []

        counter2 = 0
        syntagma = [["klitzes","kleines"], ["klitz","klein"], ["klitze","kleine"]]
        stemmed_search = False
        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)
        #list(data)
        # if not data:
        #    assert False

        for row in data:
            if row:
                rows_equal.append(row)
                counter2 += 1
                len(row).should.be.equal(col_num)
            #p(row, "row")

        
        counter1 = 0
        syntagma = ["klitze","kleine"]
        stemmed_search = True
        
        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)
        #list(data)
        # if not data:
        #    assert False
        rows = []
        for row in data:
            if row:
                #rows.add(row)
                counter1 += 1
                len(row).should.be.equal(col_num)
                if row not in rows_equal:
                    rows_not_equal.append(row)
            #p(row, "row")

        counter1.should.be.equal(counter2)
        assert not rows_not_equal
        #p((counter1, counter2))





        ##################
        #### Case 1.4 ######
        ##################
        repl = True
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 49
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = [["klitze","kleine"]]
        stemmed_search = True

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,sentiment="positive")
        if not data:
           assert False

        i = 0 
        for row in data:
            i+= 1
            len(row).should.be.equal(col_num)
            #p(row, "row")
        assert i == 0




        ##################
        #### Case 2 ######
        ##################
        repl = True
        redu = False
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True



        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 41
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")



        ##################
        #### Case 3 ######
        ##################
        repl = False
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        additional_doc_cols = ()
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 38
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")



        ##################
        #### Case 4 ######
        ##################
        repl = False
        redu = True
        baseline = True
        output_table_type = "exhausted"
        max_scope = False
        #additional_doc_cols = ()
        additional_doc_cols = ("gender", "age", "working_area")
        context_len_left = True
        context_len_right = True
        word_examples_sum_table = True

        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = sum([sum([len(doc_cols) for doc_cols in cols if doc_cols]) if tables_part_name == "document" else  len(cols) for tables_part_name, cols in header.iteritems() if cols ])
        #p(col_num, "col_num")
        assert col_num == 41
        stats.cols_exists_in_corpb(additional_doc_cols)
        #p(header, "header")
        #syntagma = ["kleine"]
        #syntagma = "*"
        syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search)

        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")




        ##########################################################
        ##########################################################
        ##########################################################
        ############################################################
        ####### output_table_type = "sum" ########
        ##################################################################
        ##########################################################


        ##################
        #### Case 1.1 ######
        ##################
        repl = False
        redu = True
        baseline = True
        output_table_type = "sum"
        max_scope = False
        word_examples_sum_table = True
        additional_doc_cols = False
        context_len_right =True
        context_len_left = True
        reptype_sum_table = "redu"
        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = len(header)
        #p(header, "header")
        #assert col_num == 41
        #stats.cols_exists_in_corpb(additional_doc_cols)
        #p(header, "header")
        #syntagma = ["kleine"]
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,output_table_type=output_table_type, reptype_sum_table=reptype_sum_table)


        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")




        ##################
        #### Case 1.2 ######
        ##################
        repl = False
        redu = True
        baseline = True
        output_table_type = "sum"
        max_scope = False
        word_examples_sum_table = True
        additional_doc_cols = False
        context_len_right =True
        context_len_left = True
        reptype_sum_table = "redu"
        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = len(header)
        sentiment = "positive"
        #p(header, "header")
        #assert col_num == 41
        #stats.cols_exists_in_corpb(additional_doc_cols)
        #p(header, "header")
        #syntagma = ["kleine"]
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,output_table_type=output_table_type, reptype_sum_table=reptype_sum_table,sentiment=sentiment)


        for row in data:
            len(row).should.be.equal(col_num)
            #p(row, "row")



        ##################
        #### Case 2.1 ######
        ##################
        repl = True
        redu = False
        baseline = True
        output_table_type = "sum"
        max_scope = False
        word_examples_sum_table = True
        additional_doc_cols = False
        context_len_right =True
        context_len_left = True
        reptype_sum_table = "repl"
        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = len(header)

        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,output_table_type=output_table_type, reptype_sum_table=reptype_sum_table)


        for row in data:
            #print "ghjk"
            #p(row, "row")
            len(row).should.be.equal(col_num)
            



        ##################
        #### Case 2.2 ######
        ##################
        repl = True
        redu = False
        baseline = True
        output_table_type = "sum"
        max_scope = False
        word_examples_sum_table = True
        additional_doc_cols = False
        context_len_right =True
        context_len_left = True
        reptype_sum_table = "repl"
        header = stats._get_header( repl=repl, redu=redu, baseline=baseline, output_table_type=output_table_type,  max_scope=max_scope, additional_doc_cols=additional_doc_cols, context_len_left=context_len_left, context_len_right=context_len_right,word_examples_sum_table=word_examples_sum_table)
        col_num = len(header)
        sentiment = "positive"
        syntagma = "*"
        #syntagma = ["klitze","kleine"]
        stemmed_search = False

        data = stats._export_generator(header,inp_syntagma=syntagma,  stemmed_search=stemmed_search,output_table_type=output_table_type, reptype_sum_table=reptype_sum_table,sentiment=sentiment)

        for row in data:
            #print "ghjk"
            #p(row, "row")
            len(row).should.be.equal(col_num)
            




    @attr(status='stable')
    #@wipd
    def test_get_where_statement_type_614(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )


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

        ################################################################################
        ##############################LEXEM############################################
        ################################################################################

        #########################
        ####1. with_context#####
        ########################
        ### Case 1.0.1
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = u'😀'
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#

        ### Case 1.0.2
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = '😀'
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#

        ### Case 1.0.3
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = '😀'
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#

        ### Case 1.0.4
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = u'😀'
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#



        ### Case 1.0.5
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#


        ### Case 1.0.6
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='\U0001f600' "]]
        #p(where, "where")#


        ### Case 1.1
        inp_syntagma_splitted = [u'.']
        inp_syntagma_unsplitted = u'.'
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='.' "]]
        #p(where, "where")



        ### Case 1.2
        inp_syntagma_splitted = ['klitze', 'kleine']
        inp_syntagma_unsplitted = 'klitze++kleine'
        scope = 2
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='klitze' ", u"contextR1='kleine'"], [u"contextL1='klitze'", u"normalized_word='kleine' "]]
        #p(where, "where")


        ### Case 1.3
        inp_syntagma_splitted = ['klitze', 'kleine', "überaschung"]
        inp_syntagma_unsplitted = 'klitze++kleine++überaschung'
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='klitze' ", u"contextR1='kleine'", u"contextR2='\xfcberaschung'"], [u"contextL1='klitze'", u"normalized_word='kleine' ", u"contextR1='\xfcberaschung'"], [u"contextL2='klitze'", u"contextL1='kleine'", u"normalized_word='\xfcberaschung' "]]
        #p(where, "where")



        ### Case 1.3.1
        inp_syntagma_splitted = ['1', 2, 3]
        inp_syntagma_unsplitted = '1++2++3'
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")

        ### Case 1.3.2
        inp_syntagma_splitted = [u'1', 2, 3]
        inp_syntagma_unsplitted = '1++2++3'
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")


        ### Case 1.3.3
        inp_syntagma_splitted = [u'1', 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")



        ### Case 1.3.4
        inp_syntagma_splitted = ['1', 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = "1++2++3"
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = u"1++2++3"
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [[u"normalized_word='1' ", u"contextR1='2'", u"contextR2='3'"], [u"contextL1='1'", u"normalized_word='2' ", u"contextR1='3'"], [u"contextL2='1'", u"contextL1='2'", u"normalized_word='3' "]]
        #p(where, "where")


        #########################
        ##2. without_context####
        #########################

        ### Case 2.0.1
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = u'😀'
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '\U0001f600'"]
        #p(where)

        ### Case 2.0.2
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = '😀'
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        #p(where)
        assert where == [u"syntagma= '\U0001f600'"]

        ### Case 2.0.3
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = u'😀'
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        #p(where)
        assert where == [u"syntagma= '\U0001f600'"]

        ### Case 2.0.4
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = '😀'
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        #p(where)
        assert where == [u"syntagma= '\U0001f600'"]

        ### Case 2.0.5
        inp_syntagma_splitted = [u"😀"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        #p(where)
        assert where == [u"syntagma= '\U0001f600'"]

        ### Case 2.0.6
        inp_syntagma_splitted = ["😀"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        #p(where)
        assert where == [u"syntagma= '\U0001f600'"]



        ### Case 2.1
        inp_syntagma_splitted = ['klitze', 'kleine']
        inp_syntagma_unsplitted = 'klitze++kleine'
        scope = 2
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= 'klitze++kleine'"]
        #p(where, "where")


        ### Case 2.2
        inp_syntagma_splitted = ['klitze', 'kleine', "überaschung"]
        inp_syntagma_unsplitted = 'klitze++kleine++überaschung'
        scope = 3
        with_context =False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= 'klitze++kleine++\xfcberaschung'"]
        #p(where, "where")



        ### Case 1.3.1
        inp_syntagma_splitted = ['1', 2, 3]
        inp_syntagma_unsplitted = '1++2++3'
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")

        ### Case 1.3.2
        inp_syntagma_splitted = [u'1', 2, 3]
        inp_syntagma_unsplitted = '1++2++3'
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")


        ### Case 1.3.3
        inp_syntagma_splitted = [u'1', 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")



        ### Case 1.3.4
        inp_syntagma_splitted = ['1', 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = "1++2++3"
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")


        ### Case 1.3.5
        inp_syntagma_splitted = [1, 2, 3]
        inp_syntagma_unsplitted = u"1++2++3"
        scope = 3
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context)
        assert where == [u"syntagma= '1++2++3'"]
        # p(where, "where")







        ################################################################################
        ###########################OTHERS###############################################
        ###############################################################################
        #########################
        ####1. with_context#####
        ########################
        ### Case 1.0.1
        inp_syntagma_splitted = ["JJ"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type="pos")
        assert where == [[u"pos='JJ' "]]
        #p(where, "where")#

        ### Case 1.0.2
        inp_syntagma_splitted = ["JJ", "JJ"]
        inp_syntagma_unsplitted = False
        scope = 2
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type="pos")
        assert where == [[u"pos='JJ' ", u'json_extract("context_infoR1", "$[0]")  = "JJ"'], [u'json_extract("context_infoL1", "$[0]")  = "JJ"', u"pos='JJ' "]]
        #p(where, "where")#

        ### Case 1.0.3
        inp_syntagma_splitted = ["JJ", "JJ", "JJ"]
        inp_syntagma_unsplitted = False
        scope = 3
        with_context = True
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type="pos")
        assert where == [[u"pos='JJ' ", u'json_extract("context_infoR1", "$[0]")  = "JJ"', u'json_extract("context_infoR2", "$[0]")  = "JJ"'], [u'json_extract("context_infoL1", "$[0]")  = "JJ"', u"pos='JJ' ", u'json_extract("context_infoR1", "$[0]")  = "JJ"'], [u'json_extract("context_infoL2", "$[0]")  = "JJ"', u'json_extract("context_infoL1", "$[0]")  = "JJ"', u"pos='JJ' "]]
        #p(where, "where")#



        ### Case 1.0.4
        inp_syntagma_splitted = ["JJ"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = True
        sentiment = "positive"
        syntagma_type = "pos"
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type=syntagma_type, sentiment=sentiment)
        assert where == [[u"pos='JJ' ", u"polarity LIKE '%positive%'"]]
        #p(where, "where")#


        ### Case 1.0.5
        inp_syntagma_splitted = ["JJ", "JJ"]
        inp_syntagma_unsplitted = False
        scope = 2
        with_context = True
        sentiment = "positive"
        syntagma_type = "pos"
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type=syntagma_type, sentiment=sentiment)
        assert where == [[u"pos='JJ' ", u'json_extract("context_infoR1", "$[0]")  = "JJ"', u"polarity LIKE '%positive%'"], [u'json_extract("context_infoL1", "$[0]")  = "JJ"', u"pos='JJ' ", u"polarity LIKE '%positive%'"]]
        #p(where, "where")#



        ### Case 1.0.6
        inp_syntagma_splitted = ["like",]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = True
        sentiment = "positive"
        syntagma_type = "lexem"
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type=syntagma_type, sentiment=sentiment)
        assert where == [[u"normalized_word='like' ", u"polarity LIKE '%positive%'"]]
        #p(where, "where")#


        ### Case 1.0.7
        inp_syntagma_splitted = ["like","you"]
        inp_syntagma_unsplitted = False
        scope = 2
        with_context = True
        sentiment = "positive"
        syntagma_type = "lexem"
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type=syntagma_type, sentiment=sentiment)
        assert where == [[u"normalized_word='like' ", u"contextR1='you'", u"polarity LIKE '%positive%'"], [u"contextL1='like'", u"normalized_word='you' ", u"polarity LIKE '%positive%'"]]
        #p(where, "where")#

        #########################
        ##2. without_context###
        #######################

        ### Case 2.0.1
        stats = Stats(mode="free",use_cash=True,  logger_usage=False)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))
        inp_syntagma_splitted = ["JJ"]
        inp_syntagma_unsplitted = False
        scope = 1
        with_context = False
        where = stats._get_where_statement(inp_syntagma_splitted, inp_syntagma_unsplitted,scope, with_context= with_context, syntagma_type="pos")
        assert where == False
        #p(where, "where", c="r")#
        #stats









    @attr(status='stable')
    #@wipd
    def test_clean_baseline_table_615(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )


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
        #stats.hhh()

        baseline_rownum_bevore = stats.statsdb.rownum("baseline")
        #p((baseline_rownum_bevore))
        assert stats._clean_baseline_table()
        assert stats._clean_baseline_table()
        #assert stats._clean_baseline_table()


        baseline_rownum_after = stats.statsdb.rownum("baseline")


        assert baseline_rownum_bevore > baseline_rownum_after



    @attr(status='stable')
    #@wipd
    def test_drop_indexes_616(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )


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

        assert stats._get_created_indexes()
        
        stats._drop_created_indexes()

        assert not stats._get_created_indexes()
        #assert 




    @attr(status='stable')
    #@wipd
    def test_create_indexes_617(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )

        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))


        ##### Case 1
        ##### optimized_for_long_syntagmas=True #####
        ################################################
        stats._drop_created_indexes()        
        #indexes_bevore = stats._get_created_indexes()
        number_indexes_bevore = stats._get_number_created_indexes()
        number_should_be_created = stats.create_additional_indexes(optimized_for_long_syntagmas=True)
        #indexes_after = stats._get_created_indexes()
        number_indexes_after = stats._get_number_created_indexes()

        assert (number_indexes_after - number_indexes_bevore) == number_should_be_created


        ### Case 2
        ##### optimized_for_long_syntagmas=False #####
        ################################################
        stats._drop_created_indexes()        
        #indexes_bevore = stats._get_created_indexes()
        number_indexes_bevore = stats._get_number_created_indexes()
        number_should_be_created = stats.create_additional_indexes(optimized_for_long_syntagmas=False)
        #indexes_after = stats._get_created_indexes()
        number_indexes_after = stats._get_number_created_indexes()

        assert (number_indexes_after - number_indexes_bevore) == number_should_be_created



        ### Case 3
        ##### scope=3 #####
        ################################################
        stats._drop_created_indexes()        
        #indexes_bevore = stats._get_created_indexes()
        number_indexes_bevore = stats._get_number_created_indexes()
        number_should_be_created = stats.create_additional_indexes(scope=3, optimized_for_long_syntagmas=False)
        #indexes_after = stats._get_created_indexes()
        number_indexes_after = stats._get_number_created_indexes()

        assert (number_indexes_after - number_indexes_bevore) == number_should_be_created



        ### Case 4
        ##### indexes upgrade #####
        ################################################
        stats._drop_created_indexes()        
        #indexes_bevore = stats._get_created_indexes()
        number_indexes_bevore = stats._get_number_created_indexes()
        number_should_be_created = stats.create_additional_indexes(scope=2, optimized_for_long_syntagmas=False)
        stats._drop_created_indexes() 
        number_should_be_created = stats.create_additional_indexes(scope=3, optimized_for_long_syntagmas=False)
        #indexes_after = stats._get_created_indexes()
        # number_indexes_after = stats._get_number_created_indexes()

        # assert (number_indexes_after - number_indexes_bevore) == number_should_be_created




        ## Case 5
        ################################################
        ##### creation of the same indexes #####
        stats._drop_created_indexes()        
        #indexes_bevore = stats._get_created_indexes()
        number_indexes_bevore = stats._get_number_created_indexes()
        number_should_be_created1 = stats.create_additional_indexes()
        number_indexes_after1 = stats._get_number_created_indexes()
        
        ### repetativ creation of the same indexes
        number_should_be_created2 = stats.create_additional_indexes()
        #indexes_after = stats._get_created_indexes()
        number_indexes_after2 = stats._get_number_created_indexes()

        assert (number_indexes_after2 - number_indexes_bevore) == number_should_be_created1






    @attr(status='stable')
    #@wipd
    def test_clean_baseline_table_618(self):
        self.prj_folder()

        #self.blogger_corpus()
        self.test_dbs()
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True)#, )

        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_en))
        #stats.hhh()

        assert stats.optimize_db()

        

    @attr(status='stable')
    #@wipd
    def test_compute_baseline_sum_619(self):
        
        self.prj_folder()
        #self.blogger_corpus()
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


    ################################################
    ############ full_repetativ_syntagma=True
    #################################################

        ##### EN ######
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, full_repetativ_syntagma=True)
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        stats.optimize_db()

        ### RepCompution 
        stats._compute_baseline_sum()

        baseline = stats.statsdb.getall("baseline")

        #right_baseline  = [(u'realy', 4, 1, 2, 4, 1, 3, None, None), (u'tiny', 10, 1, 1, 1, 2, 9, None, None), (u'\U0001f308', 1, 1, 1, 1, 0, 0, None, None), (u'se', 1, 1, 1, 1, 0, 0, None, None), (u'bad', 6, 1, 4, 7, 1, 5, None, None), (u'but', 3, 1, 1, 1, 0, 0, None, None), (u'.', 5, 1, 1, 1, 0, 0, None, None), (u'pity', 4, 1, 2, 4, 1, 4, None, None), (u'very', 3, 1, 2, 4, 1, 3, None, None), (u'big', 5, 1, 2, 2, 2, 5, None, None), (u'model', 2, 1, 1, 2, 0, 0, None, None), (u'-)', 1, 1, 1, 1, 0, 0, None, None), (u'-(++\U0001f62b', 1, 2, 2, 2, 0, 0, 1, 0), (u'=)', 1, 1, 1, 1, 0, 0, None, None), (u'right', 1, 1, 1, 1, 0, 0, None, None), (u'#shetlife', 3, 1, 0, 0, 1, 2, None, None), (u'?', 2, 1, 1, 1, 0, 0, None, None), (u'\U0001f600++\U0001f308', 1, 2, 2, 2, 0, 0, 1, 0), (u'explanation', 1, 1, 1, 1, 0, 0, None, None), (u'very++pity', 1, 2, 4, 8, 2, 7, 1, 1), (u'\U0001f600', 2, 1, 1, 1, 0, 0, None, None), (u'you', 2, 1, 1, 1, 0, 0, None, None), (u'-(', 1, 1, 1, 1, 0, 0, None, None), (u'\U0001f62b', 2, 1, 2, 2, 0, 0, None, None), (u':-(', 1, 1, 1, 1, 0, 0, None, None), (u'.++:-(', 1, 2, 2, 2, 0, 0, 1, 0), (u'glad', 1, 1, 1, 1, 0, 0, None, None)]

        right_baseline  = [
                                (u'tiny++model++,++which++we', 1, 5, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++model++,++which', 1, 4, None, None, None, None, None, None), 
                                (u'a++bad++news++,', 1, 4, None, None, None, None, None, None), 
                                (u'.++but', 3, 2, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump', 1, 3, None, None, None, None, None, None), 
                                (u'about++it++?++1++\U0001f62b++1', 1, 6, None, None, None, None, None, None), 
                                (u'explain++a++big', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,', 1, 3, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)++\U0001f600', 1, 5, None, None, None, None, None, None), 
                                (u'to++se++you++-)', 1, 4, None, None, None, None, None, None), 
                                (u'about++it++?++1', 1, 4, None, None, None, None, None, None), 
                                (u'but++it++was++also++very', 1, 5, None, None, None, None, None, None), 
                                (u'surprise++.++but++you', 1, 4, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 6, None, None, None, None, None, None), 
                                (u'explanation++.++right++?++what++do', 1, 6, None, None, None, None, None, None), 
                                (u'=)++\U0001f600++\U0001f308++\U0001f600', 1, 4, None, None, None, None, None, None), 
                                (u'what++do++you++think++about', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++,', 1, 2, None, None, None, None, None, None), 
                                (u'surprise++.++but', 1, 3, None, None, None, None, None, None), 
                                (u'can++not++acept++.++-(++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'but++it++was++also++very++pity', 1, 6, None, None, None, None, None, None), 
                                (u'i++realy++liked', 1, 3, None, None, None, None, None, None), 
                                (u'a++big++things', 1, 3, None, None, None, None, None, None), 
                                (u'?++what++do++you', 1, 4, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b++#shetlife', 1, 4, None, None, None, None, None, None), 
                                (u'.++but++you++but++you', 2, 5, None, None, None, None, None, None), 
                                (u'very++pity++for++me', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++surprise++.', 1, 3, None, None, None, None, None, None), 
                                (u':-(++@real_trump', 1, 2, None, None, None, None, None, None), 
                                (u'.++but++you++but', 2, 4, None, None, None, None, None, None), 
                                (u',++but++a++big++explanation', 1, 5, None, None, None, None, None, None), 
                                (u'for++me++.++:-(++@real_trump', 1, 5, None, None, None, None, None, None), 
                                (u'tiny++model++,', 2, 3, None, None, None, None, None, None), 
                                (u'you++think++about++it++?++1', 1, 6, None, None, None, None, None, None), 
                                (u'use++for++explain++a++big++things', 1, 6, None, None, None, None, None, None), 
                                (u'use++for++explain++a++big', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++which++we++can', 1, 5, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600++\U0001f308++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'?++what++do++you++think', 1, 5, None, None, None, None, None, None), 
                                (u'bad++news++,', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for++me', 1, 3, None, None, None, None, None, None), 
                                (u'.++right++?', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but++you', 1, 5, None, None, None, None, None, None), 
                                (u'but++i++realy++liked', 1, 4, None, None, None, None, None, None), 
                                (u',++but++i++realy++liked', 1, 5, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'a++bad++news++,++which++we', 1, 6, None, None, None, None, None, None), 
                                (u'.++but++it++was++also++very', 1, 6, None, None, None, None, None, None), 
                                (u',++but++a++big', 1, 4, None, None, None, None, None, None), 
                                (u'also++very++pity++for++me', 1, 5, None, None, None, None, None, None), 
                                (u'but++a++big++explanation++.++right', 1, 6, None, None, None, None, None, None), 
                                (u'it++was++also++very', 1, 4, None, None, None, None, None, None), 
                                (u'but++a++big++explanation++.', 1, 5, None, None, None, None, None, None), 
                                (u',++but++i++realy', 1, 4, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u'a++big', 2, 2, None, None, None, None, None, None), 
                                (u'acept++.++-(', 1, 3, None, None, None, None, None, None), 
                                (u'-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++surprise', 1, 2, None, None, None, None, None, None), 
                                (u'realy++liked', 1, 2, None, None, None, None, None, None), 
                                (u'what++do++you++think++about++it', 1, 6, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600++\U0001f308++\U0001f600', 1, 5, None, None, None, None, None, None), 
                                (u'you++-)', 1, 2, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife++#readytogo', 1, 5, None, None, None, None, None, None), 
                                (u'what++do++you', 1, 3, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u'?++what++do++you++think++about', 1, 6, None, None, None, None, None, None), 
                                (u'a++bad++news', 1, 3, None, None, None, None, None, None), 
                                (u'very++pity++for', 1, 3, None, None, None, None, None, None), 
                                (u',++but++i', 1, 3, None, None, None, None, None, None), 
                                (u'glad++to', 1, 2, None, None, None, None, None, None), 
                                (u'big++things++.', 1, 3, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,', 1, 4, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife++#readytogo', 1, 4, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife++#readytogo++http://www.absurd.com', 1, 6, None, None, None, None, None, None), 
                                (u'but++i++realy++liked++it', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.++right++?', 1, 4, None, None, None, None, None, None), 
                                (u'do++you++think++about++it', 1, 5, None, None, None, None, None, None), 
                                (u'think++about++it++?++1', 1, 5, None, None, None, None, None, None), 
                                (u'also++very++pity++for++me++.', 1, 6, None, None, None, None, None, None), 
                                (u'se++you', 1, 2, None, None, None, None, None, None), 
                                (u'realy++liked++it', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++.++:-(++@real_trump++#shetlife', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.++right++?', 1, 5, None, None, None, None, None, None), 
                                (u'glad++to++se++you', 1, 4, None, None, None, None, None, None), 
                                (u'bad++news', 1, 2, None, None, None, None, None, None), 
                                (u'-(++\U0001f62b++#shetlife', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++but++a++big', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.', 1, 3, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600++\U0001f308', 1, 5, None, None, None, None, None, None), 
                                (u'explain++a++big++things', 1, 4, None, None, None, None, None, None), 
                                (u'also++very', 1, 2, None, None, None, None, None, None), 
                                (u'to++se', 1, 2, None, None, None, None, None, None), 
                                (u'to++se++you', 1, 3, None, None, None, None, None, None), 
                                (u'realy++bad++surprise++for++me++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p', 1, 4, None, None, None, None, None, None), 
                                (u'1++.++but++you', 1, 4, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b++,', 1, 5, None, None, None, None, None, None), 
                                (u'.++right++?++what++do', 1, 5, None, None, None, None, None, None), 
                                (u'was++also++very++pity', 1, 4, None, None, None, None, None, None), 
                                (u'big++explanation++.++right', 1, 4, None, None, None, None, None, None), 
                                (u'for++explain++a++big', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,++but++i', 1, 6, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 5, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife', 1, 3, None, None, None, None, None, None), 
                                (u'?++1++\U0001f62b++1++.++but', 1, 6, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.++but', 1, 5, None, None, None, None, None, None), 
                                (u'think++about++it++?', 1, 4, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p++=)', 1, 5, None, None, None, None, None, None), 
                                (u'we++can++not++acept++.++-(', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation++.', 1, 4, None, None, None, None, None, None), 
                                (u'for++explain++a++big++things', 1, 5, None, None, None, None, None, None), 
                                (u'bad++news++,++which', 1, 4, None, None, None, None, None, None), 
                                (u'i++realy++liked++it++:p', 1, 5, None, None, None, None, None, None), 
                                (u'but++i++realy++liked++it++:p', 1, 6, None, None, None, None, None, None), 
                                (u'glad++to++se++you++-)', 1, 5, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.', 1, 4, None, None, None, None, None, None), 
                                (u'you++think', 1, 2, None, None, None, None, None, None), 
                                (u'not++acept++.++-(++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u',++but++a++big++explanation++.', 1, 6, None, None, None, None, None, None), 
                                (u'think++about++it++?++1++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.++right++?++what', 1, 6, None, None, None, None, None, None), 
                                (u'me++.++:-(', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but', 1, 4, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but++you', 1, 5, None, None, None, None, None, None), 
                                (u'it++?', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but', 1, 3, None, None, None, None, None, None), 
                                (u'model++,', 2, 2, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump++#shetlife++#readytogo', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what++do', 1, 4, None, None, None, None, None, None), 
                                (u'it++was++also++very++pity', 1, 5, None, None, None, None, None, None), 
                                (u'i++realy++liked++it', 1, 4, None, None, None, None, None, None), 
                                (u'se++you++-)', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++model', 2, 2, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600', 1, 4, None, None, None, None, None, None), 
                                (u'a++bad++news++,++which', 1, 5, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b++1++.', 1, 6, None, None, None, None, None, None), 
                                (u'1++.++but++you++but', 1, 5, None, None, None, None, None, None), 
                                (u'it++:p++=)', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++which++we', 1, 4, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump', 1, 4, None, None, None, None, None, None), 
                                (u'very++pity++for++me++.', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.', 1, 2, None, None, None, None, None, None), 
                                (u'.++but++you++but++you++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'.++-(', 1, 2, None, None, None, None, None, None), 
                                (u'i++realy++liked++it++:p++=)', 1, 6, None, None, None, None, None, None), 
                                (u'do++you++think', 1, 3, None, None, None, None, None, None), 
                                (u'but++i', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i++realy++liked', 1, 6, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but++i++realy', 1, 6, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u',++but', 2, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++#shetlife', 1, 2, None, None, None, None, None, None), 
                                (u'was++also++very++pity++for', 1, 5, None, None, None, None, None, None), 
                                (u'surprise++.++but++you++but', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++#shetlife++http://www.noooo.com', 1, 3, None, None, None, None, None, None), 
                                (u'surprise++.++but++you++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation++.++right', 1, 5, None, None, None, None, None, None), 
                                (u':p++=)', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++model++,++which++we++can', 1, 6, None, None, None, None, None, None), 
                                (u'was++also++very', 1, 3, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600++\U0001f308', 1, 4, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b++,++but', 1, 6, None, None, None, None, None, None), 
                                (u'about++it++?++1++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump++#shetlife', 1, 5, None, None, None, None, None, None), 
                                (u'you++think++about++it', 1, 4, None, None, None, None, None, None), 
                                (u'also++very++pity++for', 1, 4, None, None, None, None, None, None), 
                                (u'glad++to++se', 1, 3, None, None, None, None, None, None), 
                                (u'#shetlife++http://www.noooo.com', 1, 2, None, None, None, None, None, None), 
                                (u'1++.++but++you++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'was++also++very++pity++for++me', 1, 6, None, None, None, None, None, None), 
                                (u'1++.', 1, 2, None, None, None, None, None, None), 
                                (u'i++realy', 1, 2, None, None, None, None, None, None), 
                                (u'can++use++for++explain++a++big', 1, 6, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)++\U0001f600++\U0001f308', 1, 6, None, None, None, None, None, None), 
                                (u'do++you++think++about', 1, 4, None, None, None, None, None, None), 
                                (u'bad++surprise++for++me++\U0001f62b++,', 1, 6, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife++#readytogo++http://www.absurd.com', 1, 5, None, None, None, None, None, None), 
                                (u'me++.', 1, 2, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but++i', 1, 5, None, None, None, None, None, None), 
                                (u'you++think++about++it++?', 1, 5, None, None, None, None, None, None), 
                                (u'right++?++what++do++you', 1, 5, None, None, None, None, None, None), 
                                (u'pity++for++me++.', 1, 4, None, None, None, None, None, None), 
                                (u'explain++a++big++things++.', 1, 5, None, None, None, None, None, None), 
                                (u'what++do++you++think', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++.++:-(', 1, 4, None, None, None, None, None, None), 
                                (u'bad++news++,++which++we', 1, 5, None, None, None, None, None, None), 
                                (u'very++pity++for++me++.++:-(', 1, 6, None, None, None, None, None, None), 
                                (u'.++right++?++what', 1, 4, None, None, None, None, None, None), 
                                (u'.++but++you', 2, 3, None, None, None, None, None, None), 
                                (u'but++a++big', 1, 3, None, None, None, None, None, None), 
                                (u'it++was++also++very++pity++for', 1, 6, None, None, None, None, None, None), 
                                (u'bad++news++,++which++we++can', 1, 6, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i++realy', 1, 5, None, None, None, None, None, None), 
                                (u'for++me++.', 1, 3, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p++=)++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'explanation++.++right++?++what', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++but++a++big++explanation', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for++me++.++:-(', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.++right', 1, 3, None, None, None, None, None, None), 
                                (u'big++things', 1, 2, None, None, None, None, None, None), 
                                (u'it++?++1', 1, 3, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but++you++but', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what++do++you++think', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.', 1, 3, None, None, None, None, None, None), 
                                (u'for++explain++a++big++things++.', 1, 6, None, None, None, None, None, None), 
                                (u'.++right', 1, 2, None, None, None, None, None, None), 
                                (u'not++acept++.++-(', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,++but', 1, 5, None, None, None, None, None, None), 
                                (u'not++acept++.++-(++\U0001f62b++#shetlife', 1, 6, None, None, None, None, None, None), 
                                (u'you++think++about', 1, 3, None, None, None, None, None, None), 
                                (u'a++bad', 1, 2, None, None, None, None, None, None), 
                                (u'do++you++think++about++it++?', 1, 6, None, None, None, None, None, None), 
                                (u'can++not++acept++.++-(', 1, 5, None, None, None, None, None, None), 
                                (u'a++big++things++.', 1, 4, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but', 1, 4, None, None, None, None, None, None), 
                                (u'right++?', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but++you++but', 1, 6, None, None, None, None, None, None), 
                                (u'pity++for++me++.++:-(++@real_trump', 1, 6, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b++1', 1, 5, None, None, None, None, None, None), 
                                (u'tiny++model++,++but++a++big', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what', 1, 3, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b++#shetlife', 1, 5, None, None, None, None, None, None), 
                                (u'bad++surprise++for++me++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++which', 1, 3, None, None, None, None, None, None), 
                                (u'1++.++but', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for', 1, 2, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b', 1, 2, None, None, None, None, None, None), 
                                (u'also++very++pity', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++which++we++can++use', 1, 6, None, None, None, None, None, None), 
                                (u'about++it++?', 1, 3, None, None, None, None, None, None), 
                                (u'but++i++realy', 1, 3, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)', 1, 4, None, None, None, None, None, None), 
                                (u'do++you', 1, 2, None, None, None, None, None, None), 
                                (u'?++1++\U0001f62b++1++.', 1, 5, None, None, None, None, None, None), 
                                (u'.++right++?++what++do++you', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation', 1, 2, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b', 1, 3, None, None, None, None, None, None), 
                                (u'but++a++big++explanation', 1, 4, None, None, None, None, None, None), 
                                (u'a++big++explanation++.++right++?', 1, 6, None, None, None, None, None, None), 
                                (u',++but++i++realy++liked++it', 1, 6, None, None, None, None, None, None), 
                                (u'\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'realy', 4, 1, u'2', u'4', u'1', u'3', None, None), 
                                (u'tiny', 10, 1, u'1', u'1', u'2', u'9', None, None), 
                                (u'\U0001f308++\U0001f600++\U0001f308', 1, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f308', 3, 1, u'3', u'3', u'0', u'0', None, None), 
                                (u'but++you++but', 2, 3, u'[10, 4, "IGNOR"]', u'[15, 4, "IGNOR"]', u'[4, 2, "IGNOR"]', u'[10, 4, "IGNOR"]', u'2', u'2'), 
                                (u'se', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'=)++\U0001f600', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++but++you', 2, 4, u'[10, 6, "IGNOR", "IGNOR"]', u'[15, 8, "IGNOR", "IGNOR"]', None, None, u'2', u'0'), 
                                (u'bad', 6, 1, u'4', u'7', u'1', u'5', None, None), 
                                (u'?++1++\U0001f62b++1', 1, 4, u'[1, 2, 1, "IGNOR"]', u'[1, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but', 13, 1, u'11', u'16', u'4', u'10', None, None), 
                                (u'\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'.', 7, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'pity', 4, 1, u'2', u'4', u'1', u'4', None, None), 
                                (u'\U0001f600++\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 5, u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f600++\U0001f308++\U0001f600', 3, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'you++but++you++\U0001f600++\U0001f308', 1, 5, u'[3, 3, "IGNOR", 1, 1]', u'[4, 3, "IGNOR", 1, 1]', None, None, u'1', u'0'), 
                                (u'you++but++you++\U0001f600', 1, 4, u'[3, 3, "IGNOR", 1]', u'[4, 3, "IGNOR", 1]', None, None, u'1', u'0'), 
                                (u'very', 3, 1, u'2', u'4', u'1', u'3', None, None), 
                                (u'1++\U0001f62b++1', 1, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'big', 5, 1, u'2', u'2', u'2', u'5', None, None), 
                                (u'model', 2, 1, u'1', u'2', u'0', u'0', None, None), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600', 1, 4, u'[1, 2, 1, "IGNOR"]', u'[2, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you', 4, 2, u'[10, 6]', u'[15, 8]', u'[2, 2]', u'[4, 4]', u'4', u'2'), 
                                (u'-)', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'-(++\U0001f62b', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'\U0001f308++\U0001f600', 3, 2, u'[2, 2]', u'[2, 2]', None, None, u'2', u'0'), 
                                (u'=)', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'right', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'but++you++but++you++\U0001f600++\U0001f308', 1, 6, u'[5, 3, "IGNOR", "IGNOR", 1, 1]', u'[5, 4, "IGNOR", "IGNOR", 1, 1]', None, None, u'1', u'0'), 
                                (u'#shetlife', 3, 1, u'0', u'0', u'1', u'2', None, None), 
                                (u'?', 2, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'but++you++\U0001f600++\U0001f308', 1, 4, u'[3, 1, 1, 1]', u'[3, 2, 1, 1]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 6, u'[1, 3, 2, "IGNOR", "IGNOR", "IGNOR"]', u'[2, 3, 2, "IGNOR", "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f600++\U0001f308', 3, 2, u'[3, 3]', u'[3, 3]', None, None, u'3', u'0'), 
                                (u'explanation', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'you++but++you++\U0001f600++\U0001f308++\U0001f600', 1, 6, u'[3, 3, "IGNOR", 2, 1, "IGNOR"]', u'[4, 3, "IGNOR", 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you++but++you++\U0001f600', 1, 5, u'[5, 3, "IGNOR", "IGNOR", 1]', u'[5, 4, "IGNOR", "IGNOR", 1]', None, None, u'1', u'0'), 
                                (u'\U0001f62b++1', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'?++1++\U0001f62b', 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600++\U0001f308++\U0001f600', 1, 5, u'[3, 1, 2, 1, "IGNOR"]', u'[3, 2, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 6, u'[3, 1, 2, 2, "IGNOR", "IGNOR"]', u'[3, 2, 2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600', 1, 2, u'[1, 1]', u'[2, 1]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 5, u'[1, 2, 2, "IGNOR", "IGNOR"]', u'[2, 2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'very++pity', 1, 2, u'[2, 2]', u'[4, 4]', u'[1, 1]', u'[3, 4]', u'1', u'1'), 
                                (u'1', 2, 1, u'2', u'2', u'0', u'0', None, None), 
                                (u'\U0001f600', 5, 1, u'4', u'4', u'0', u'0', None, None), 
                                (u'you++but', 2, 2, u'[4, 6]', u'[4, 8]', u'[2, 2]', u'[4, 6]', u'2', u'2'), 
                                (u'=)++\U0001f600++\U0001f308', 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'), 
                                (u'you++but++you', 2, 3, u'[6, 6, "IGNOR"]', u'[8, 8, "IGNOR"]', None, None, u'2', u'0'), 
                                (u'you', 8, 1, u'7', u'9', u'2', u'4', None, None), 
                                (u'-(', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'\U0001f62b', 3, 1, u'3', u'3', u'0', u'0', None, None), 
                                (u'?++1', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600', 1, 3, u'[3, 1, 1]', u'[3, 2, 1]', None, None, u'1', u'0'), 
                                (u'1++\U0001f62b', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u':-(', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'.++:-(', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'glad', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'you++\U0001f600++\U0001f308', 1, 3, u'[1, 1, 1]', u'[2, 1, 1]', None, None, u'1', u'0')
                            ]
        #p(baseline ,"baseline")
    

        baseline.should.be.equal(right_baseline)
        #assert stats._compute_baseline_sum() > 0



    ################################################
    ############ full_repetativ_syntagma=False
    ################################################

        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, full_repetativ_syntagma=False)
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        stats.optimize_db()

        ### RepCompution 
        stats._compute_baseline_sum()


        right_baseline  = [
                                (u'tiny++model++,++which++we', 1, 5, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++model++,++which', 1, 4, None, None, None, None, None, None), 
                                (u'a++bad++news++,', 1, 4, None, None, None, None, None, None), 
                                (u'.++but', 3, 2, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump', 1, 3, None, None, None, None, None, None), 
                                (u'about++it++?++1++\U0001f62b++1', 1, 6, None, None, None, None, None, None), 
                                (u'explain++a++big', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,', 1, 3, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)++\U0001f600', 1, 5, None, None, None, None, None, None), 
                                (u'to++se++you++-)', 1, 4, None, None, None, None, None, None), 
                                (u'about++it++?++1', 1, 4, None, None, None, None, None, None), 
                                (u'but++it++was++also++very', 1, 5, None, None, None, None, None, None), 
                                (u'surprise++.++but++you', 1, 4, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 6, None, None, None, None, None, None), 
                                (u'explanation++.++right++?++what++do', 1, 6, None, None, None, None, None, None), 
                                (u'=)++\U0001f600++\U0001f308++\U0001f600', 1, 4, None, None, None, None, None, None), 
                                (u'what++do++you++think++about', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++,', 1, 2, None, None, None, None, None, None), 
                                (u'surprise++.++but', 1, 3, None, None, None, None, None, None), 
                                (u'can++not++acept++.++-(++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'but++it++was++also++very++pity', 1, 6, None, None, None, None, None, None), 
                                (u'i++realy++liked', 1, 3, None, None, None, None, None, None), 
                                (u'a++big++things', 1, 3, None, None, None, None, None, None), 
                                (u'?++what++do++you', 1, 4, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b++#shetlife', 1, 4, None, None, None, None, None, None), 
                                (u'.++but++you++but++you', 2, 5, None, None, None, None, None, None), 
                                (u'very++pity++for++me', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++surprise++.', 1, 3, None, None, None, None, None, None), 
                                (u':-(++@real_trump', 1, 2, None, None, None, None, None, None), 
                                (u'.++but++you++but', 2, 4, None, None, None, None, None, None), 
                                (u',++but++a++big++explanation', 1, 5, None, None, None, None, None, None), 
                                (u'for++me++.++:-(++@real_trump', 1, 5, None, None, None, None, None, None), 
                                (u'tiny++model++,', 2, 3, None, None, None, None, None, None), 
                                (u'you++think++about++it++?++1', 1, 6, None, None, None, None, None, None), 
                                (u'use++for++explain++a++big++things', 1, 6, None, None, None, None, None, None), 
                                (u'use++for++explain++a++big', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++which++we++can', 1, 5, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600++\U0001f308++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'?++what++do++you++think', 1, 5, None, None, None, None, None, None), 
                                (u'bad++news++,', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for++me', 1, 3, None, None, None, None, None, None), 
                                (u'.++right++?', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but++you', 1, 5, None, None, None, None, None, None), 
                                (u'but++i++realy++liked', 1, 4, None, None, None, None, None, None), 
                                (u',++but++i++realy++liked', 1, 5, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'a++bad++news++,++which++we', 1, 6, None, None, None, None, None, None), 
                                (u'.++but++it++was++also++very', 1, 6, None, None, None, None, None, None), 
                                (u',++but++a++big', 1, 4, None, None, None, None, None, None), 
                                (u'also++very++pity++for++me', 1, 5, None, None, None, None, None, None), 
                                (u'but++a++big++explanation++.++right', 1, 6, None, None, None, None, None, None), 
                                (u'it++was++also++very', 1, 4, None, None, None, None, None, None), 
                                (u'but++a++big++explanation++.', 1, 5, None, None, None, None, None, None), 
                                (u',++but++i++realy', 1, 4, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u'a++big', 2, 2, None, None, None, None, None, None), 
                                (u'acept++.++-(', 1, 3, None, None, None, None, None, None), 
                                (u'-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++surprise', 1, 2, None, None, None, None, None, None), 
                                (u'realy++liked', 1, 2, None, None, None, None, None, None), 
                                (u'what++do++you++think++about++it', 1, 6, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600++\U0001f308++\U0001f600', 1, 5, None, None, None, None, None, None), 
                                (u'you++-)', 1, 2, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife++#readytogo', 1, 5, None, None, None, None, None, None), 
                                (u'what++do++you', 1, 3, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u'?++what++do++you++think++about', 1, 6, None, None, None, None, None, None), 
                                (u'a++bad++news', 1, 3, None, None, None, None, None, None), 
                                (u'very++pity++for', 1, 3, None, None, None, None, None, None), 
                                (u',++but++i', 1, 3, None, None, None, None, None, None), 
                                (u'glad++to', 1, 2, None, None, None, None, None, None), 
                                (u'big++things++.', 1, 3, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,', 1, 4, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife++#readytogo', 1, 4, None, None, None, None, None, None), 
                                (u'.++:-(++@real_trump++#shetlife++#readytogo++http://www.absurd.com', 1, 6, None, None, None, None, None, None), 
                                (u'but++i++realy++liked++it', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.++right++?', 1, 4, None, None, None, None, None, None), 
                                (u'do++you++think++about++it', 1, 5, None, None, None, None, None, None), 
                                (u'think++about++it++?++1', 1, 5, None, None, None, None, None, None), 
                                (u'also++very++pity++for++me++.', 1, 6, None, None, None, None, None, None), 
                                (u'se++you', 1, 2, None, None, None, None, None, None), 
                                (u'realy++liked++it', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++.++:-(++@real_trump++#shetlife', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.++right++?', 1, 5, None, None, None, None, None, None), 
                                (u'glad++to++se++you', 1, 4, None, None, None, None, None, None), 
                                (u'bad++news', 1, 2, None, None, None, None, None, None), 
                                (u'-(++\U0001f62b++#shetlife', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++but++a++big', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.', 1, 3, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600++\U0001f308', 1, 5, None, None, None, None, None, None), 
                                (u'explain++a++big++things', 1, 4, None, None, None, None, None, None), 
                                (u'also++very', 1, 2, None, None, None, None, None, None), 
                                (u'to++se', 1, 2, None, None, None, None, None, None), 
                                (u'to++se++you', 1, 3, None, None, None, None, None, None), 
                                (u'realy++bad++surprise++for++me++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p', 1, 4, None, None, None, None, None, None), 
                                (u'1++.++but++you', 1, 4, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b++,', 1, 5, None, None, None, None, None, None), 
                                (u'.++right++?++what++do', 1, 5, None, None, None, None, None, None), 
                                (u'was++also++very++pity', 1, 4, None, None, None, None, None, None), 
                                (u'big++explanation++.++right', 1, 4, None, None, None, None, None, None), 
                                (u'for++explain++a++big', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,++but++i', 1, 6, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b++#shetlife++http://www.noooo.com', 1, 5, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife', 1, 3, None, None, None, None, None, None), 
                                (u'?++1++\U0001f62b++1++.++but', 1, 6, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.++but', 1, 5, None, None, None, None, None, None), 
                                (u'think++about++it++?', 1, 4, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p++=)', 1, 5, None, None, None, None, None, None), 
                                (u'we++can++not++acept++.++-(', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation++.', 1, 4, None, None, None, None, None, None), 
                                (u'for++explain++a++big++things', 1, 5, None, None, None, None, None, None), 
                                (u'bad++news++,++which', 1, 4, None, None, None, None, None, None), 
                                (u'i++realy++liked++it++:p', 1, 5, None, None, None, None, None, None), 
                                (u'but++i++realy++liked++it++:p', 1, 6, None, None, None, None, None, None), 
                                (u'glad++to++se++you++-)', 1, 5, None, None, None, None, None, None), 
                                (u'1++\U0001f62b++1++.', 1, 4, None, None, None, None, None, None), 
                                (u'you++think', 1, 2, None, None, None, None, None, None), 
                                (u'not++acept++.++-(++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u',++but++a++big++explanation++.', 1, 6, None, None, None, None, None, None), 
                                (u'think++about++it++?++1++\U0001f62b', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.++right++?++what', 1, 6, None, None, None, None, None, None), 
                                (u'me++.++:-(', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but', 1, 4, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but++you', 1, 5, None, None, None, None, None, None), 
                                (u'it++?', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but', 1, 3, None, None, None, None, None, None), 
                                (u'model++,', 2, 2, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump++#shetlife++#readytogo', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what++do', 1, 4, None, None, None, None, None, None), 
                                (u'it++was++also++very++pity', 1, 5, None, None, None, None, None, None), 
                                (u'i++realy++liked++it', 1, 4, None, None, None, None, None, None), 
                                (u'se++you++-)', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++model', 2, 2, None, None, None, None, None, None), 
                                (u'it++:p++=)++\U0001f600', 1, 4, None, None, None, None, None, None), 
                                (u'a++bad++news++,++which', 1, 5, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b++1++.', 1, 6, None, None, None, None, None, None), 
                                (u'1++.++but++you++but', 1, 5, None, None, None, None, None, None), 
                                (u'it++:p++=)', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++which++we', 1, 4, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump', 1, 4, None, None, None, None, None, None), 
                                (u'very++pity++for++me++.', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.', 1, 2, None, None, None, None, None, None), 
                                (u'.++but++you++but++you++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'.++-(', 1, 2, None, None, None, None, None, None), 
                                (u'i++realy++liked++it++:p++=)', 1, 6, None, None, None, None, None, None), 
                                (u'do++you++think', 1, 3, None, None, None, None, None, None), 
                                (u'but++i', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i++realy++liked', 1, 6, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but++i++realy', 1, 6, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b', 1, 4, None, None, None, None, None, None), 
                                (u',++but', 2, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++#shetlife', 1, 2, None, None, None, None, None, None), 
                                (u'was++also++very++pity++for', 1, 5, None, None, None, None, None, None), 
                                (u'surprise++.++but++you++but', 1, 5, None, None, None, None, None, None), 
                                (u'\U0001f62b++#shetlife++http://www.noooo.com', 1, 3, None, None, None, None, None, None), 
                                (u'surprise++.++but++you++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation++.++right', 1, 5, None, None, None, None, None, None), 
                                (u':p++=)', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i', 1, 4, None, None, None, None, None, None), 
                                (u'tiny++model++,++which++we++can', 1, 6, None, None, None, None, None, None), 
                                (u'was++also++very', 1, 3, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600++\U0001f308', 1, 4, None, None, None, None, None, None), 
                                (u'surprise++for++me++\U0001f62b++,++but', 1, 6, None, None, None, None, None, None), 
                                (u'about++it++?++1++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u'me++.++:-(++@real_trump++#shetlife', 1, 5, None, None, None, None, None, None), 
                                (u'you++think++about++it', 1, 4, None, None, None, None, None, None), 
                                (u'also++very++pity++for', 1, 4, None, None, None, None, None, None), 
                                (u'glad++to++se', 1, 3, None, None, None, None, None, None), 
                                (u'#shetlife++http://www.noooo.com', 1, 2, None, None, None, None, None, None), 
                                (u'1++.++but++you++but++you', 1, 6, None, None, None, None, None, None), 
                                (u'was++also++very++pity++for++me', 1, 6, None, None, None, None, None, None), 
                                (u'1++.', 1, 2, None, None, None, None, None, None), 
                                (u'i++realy', 1, 2, None, None, None, None, None, None), 
                                (u'can++use++for++explain++a++big', 1, 6, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)++\U0001f600++\U0001f308', 1, 6, None, None, None, None, None, None), 
                                (u'do++you++think++about', 1, 4, None, None, None, None, None, None), 
                                (u'bad++surprise++for++me++\U0001f62b++,', 1, 6, None, None, None, None, None, None), 
                                (u':-(++@real_trump++#shetlife++#readytogo++http://www.absurd.com', 1, 5, None, None, None, None, None, None), 
                                (u'me++.', 1, 2, None, None, None, None, None, None), 
                                (u'me++\U0001f62b++,++but++i', 1, 5, None, None, None, None, None, None), 
                                (u'you++think++about++it++?', 1, 5, None, None, None, None, None, None), 
                                (u'right++?++what++do++you', 1, 5, None, None, None, None, None, None), 
                                (u'pity++for++me++.', 1, 4, None, None, None, None, None, None), 
                                (u'explain++a++big++things++.', 1, 5, None, None, None, None, None, None), 
                                (u'what++do++you++think', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++.++:-(', 1, 4, None, None, None, None, None, None), 
                                (u'bad++news++,++which++we', 1, 5, None, None, None, None, None, None), 
                                (u'very++pity++for++me++.++:-(', 1, 6, None, None, None, None, None, None), 
                                (u'.++right++?++what', 1, 4, None, None, None, None, None, None), 
                                (u'.++but++you', 2, 3, None, None, None, None, None, None), 
                                (u'but++a++big', 1, 3, None, None, None, None, None, None), 
                                (u'it++was++also++very++pity++for', 1, 6, None, None, None, None, None, None), 
                                (u'bad++news++,++which++we++can', 1, 6, None, None, None, None, None, None), 
                                (u'\U0001f62b++,++but++i++realy', 1, 5, None, None, None, None, None, None), 
                                (u'for++me++.', 1, 3, None, None, None, None, None, None), 
                                (u'realy++liked++it++:p++=)++\U0001f600', 1, 6, None, None, None, None, None, None), 
                                (u'explanation++.++right++?++what', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++but++a++big++explanation', 1, 6, None, None, None, None, None, None), 
                                (u'a++big++explanation', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for++me++.++:-(', 1, 5, None, None, None, None, None, None), 
                                (u'explanation++.++right', 1, 3, None, None, None, None, None, None), 
                                (u'big++things', 1, 2, None, None, None, None, None, None), 
                                (u'it++?++1', 1, 3, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b', 1, 3, None, None, None, None, None, None), 
                                (u'tiny++surprise++.++but++you++but', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what++do++you++think', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation++.', 1, 3, None, None, None, None, None, None), 
                                (u'for++explain++a++big++things++.', 1, 6, None, None, None, None, None, None), 
                                (u'.++right', 1, 2, None, None, None, None, None, None), 
                                (u'not++acept++.++-(', 1, 4, None, None, None, None, None, None), 
                                (u'for++me++\U0001f62b++,++but', 1, 5, None, None, None, None, None, None), 
                                (u'not++acept++.++-(++\U0001f62b++#shetlife', 1, 6, None, None, None, None, None, None), 
                                (u'you++think++about', 1, 3, None, None, None, None, None, None), 
                                (u'a++bad', 1, 2, None, None, None, None, None, None), 
                                (u'do++you++think++about++it++?', 1, 6, None, None, None, None, None, None), 
                                (u'can++not++acept++.++-(', 1, 5, None, None, None, None, None, None), 
                                (u'a++big++things++.', 1, 4, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but', 1, 4, None, None, None, None, None, None), 
                                (u'right++?', 1, 2, None, None, None, None, None, None), 
                                (u'\U0001f62b++1++.++but++you++but', 1, 6, None, None, None, None, None, None), 
                                (u'pity++for++me++.++:-(++@real_trump', 1, 6, None, None, None, None, None, None), 
                                (u'it++?++1++\U0001f62b++1', 1, 5, None, None, None, None, None, None), 
                                (u'tiny++model++,++but++a++big', 1, 6, None, None, None, None, None, None), 
                                (u'right++?++what', 1, 3, None, None, None, None, None, None), 
                                (u'acept++.++-(++\U0001f62b++#shetlife', 1, 5, None, None, None, None, None, None), 
                                (u'bad++surprise++for++me++\U0001f62b', 1, 5, None, None, None, None, None, None), 
                                (u'model++,++which', 1, 3, None, None, None, None, None, None), 
                                (u'1++.++but', 1, 3, None, None, None, None, None, None), 
                                (u'pity++for', 1, 2, None, None, None, None, None, None), 
                                (u':p++=)++\U0001f600', 1, 3, None, None, None, None, None, None), 
                                (u'me++\U0001f62b', 1, 2, None, None, None, None, None, None), 
                                (u'also++very++pity', 1, 3, None, None, None, None, None, None), 
                                (u'model++,++which++we++can++use', 1, 6, None, None, None, None, None, None), 
                                (u'about++it++?', 1, 3, None, None, None, None, None, None), 
                                (u'but++i++realy', 1, 3, None, None, None, None, None, None), 
                                (u'liked++it++:p++=)', 1, 4, None, None, None, None, None, None), 
                                (u'do++you', 1, 2, None, None, None, None, None, None), 
                                (u'?++1++\U0001f62b++1++.', 1, 5, None, None, None, None, None, None), 
                                (u'.++right++?++what++do++you', 1, 6, None, None, None, None, None, None), 
                                (u'big++explanation', 1, 2, None, None, None, None, None, None), 
                                (u'.++-(++\U0001f62b', 1, 3, None, None, None, None, None, None), 
                                (u'but++a++big++explanation', 1, 4, None, None, None, None, None, None), 
                                (u'a++big++explanation++.++right++?', 1, 6, None, None, None, None, None, None), 
                                (u',++but++i++realy++liked++it', 1, 6, None, None, None, None, None, None), 
                                (u'\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'realy', 4, 1, u'2', u'4', u'1', u'3', None, None), 
                                (u'tiny', 10, 1, u'1', u'1', u'2', u'9', None, None), 
                                (u'\U0001f308++\U0001f600++\U0001f308', 1, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f308', 3, 1, u'3', u'3', u'0', u'0', None, None), 
                                (u'but++you++but', 2, 3, u'[10, 4, "IGNOR"]', u'[15, 4, "IGNOR"]', u'[4, 2, "IGNOR"]', u'[10, 4, "IGNOR"]', u'2', u'2'), 
                                (u'se', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'=)++\U0001f600', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++but++you', 2, 4, u'[10, 6, "IGNOR", "IGNOR"]', u'[15, 8, "IGNOR", "IGNOR"]', None, None, u'2', u'0'), 
                                (u'bad', 6, 1, u'4', u'7', u'1', u'5', None, None), 
                                (u'?++1++\U0001f62b++1', 1, 4, u'[1, 2, 1, "IGNOR"]', u'[1, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but', 13, 1, u'11', u'16', u'4', u'10', None, None), 
                                (u'\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 4, u'[2, 2, "IGNOR", "IGNOR"]', u'[2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'.', 7, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'pity', 4, 1, u'2', u'4', u'1', u'4', None, None), 
                                (u'\U0001f600++\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 5, u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', u'[3, 2, "IGNOR", "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f600++\U0001f308++\U0001f600', 3, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'you++but++you++\U0001f600++\U0001f308', 1, 5, u'[3, 3, "IGNOR", 1, 1]', u'[4, 3, "IGNOR", 1, 1]', None, None, u'1', u'0'), 
                                (u'you++but++you++\U0001f600', 1, 4, u'[3, 3, "IGNOR", 1]', u'[4, 3, "IGNOR", 1]', None, None, u'1', u'0'), 
                                (u'very', 3, 1, u'2', u'4', u'1', u'3', None, None), 
                                (u'1++\U0001f62b++1', 1, 3, u'[2, 1, "IGNOR"]', u'[2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'big', 5, 1, u'2', u'2', u'2', u'5', None, None), 
                                (u'model', 2, 1, u'1', u'2', u'0', u'0', None, None), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600', 1, 4, u'[1, 2, 1, "IGNOR"]', u'[2, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you', 4, 2, u'[10, 6]', u'[15, 8]', u'[2, 2]', u'[4, 4]', u'4', u'2'), 
                                (u'-)', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'-(++\U0001f62b', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'\U0001f308++\U0001f600', 3, 2, u'[2, 2]', u'[2, 2]', None, None, u'2', u'0'), 
                                (u'=)', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'right', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'but++you++but++you++\U0001f600++\U0001f308', 1, 6, u'[5, 3, "IGNOR", "IGNOR", 1, 1]', u'[5, 4, "IGNOR", "IGNOR", 1, 1]', None, None, u'1', u'0'), 
                                (u'#shetlife', 3, 1, u'0', u'0', u'1', u'2', None, None), 
                                (u'?', 2, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'but++you++\U0001f600++\U0001f308', 1, 4, u'[3, 1, 1, 1]', u'[3, 2, 1, 1]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600++\U0001f308++\U0001f600', 1, 6, u'[1, 3, 2, "IGNOR", "IGNOR", "IGNOR"]', u'[2, 3, 2, "IGNOR", "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'\U0001f600++\U0001f308', 3, 2, u'[3, 3]', u'[3, 3]', None, None, u'3', u'0'), 
                                (u'explanation', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'you++but++you++\U0001f600++\U0001f308++\U0001f600', 1, 6, u'[3, 3, "IGNOR", 2, 1, "IGNOR"]', u'[4, 3, "IGNOR", 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you++but++you++\U0001f600', 1, 5, u'[5, 3, "IGNOR", "IGNOR", 1]', u'[5, 4, "IGNOR", "IGNOR", 1]', None, None, u'1', u'0'), 
                                (u'\U0001f62b++1', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'?++1++\U0001f62b', 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600++\U0001f308++\U0001f600', 1, 5, u'[3, 1, 2, 1, "IGNOR"]', u'[3, 2, 2, 1, "IGNOR"]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 6, u'[3, 1, 2, 2, "IGNOR", "IGNOR"]', u'[3, 2, 2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600', 1, 2, u'[1, 1]', u'[2, 1]', None, None, u'1', u'0'), 
                                (u'you++\U0001f600++\U0001f308++\U0001f600++\U0001f308', 1, 5, u'[1, 2, 2, "IGNOR", "IGNOR"]', u'[2, 2, 2, "IGNOR", "IGNOR"]', None, None, u'1', u'0'), 
                                (u'very++pity', 1, 2, u'[2, 2]', u'[4, 4]', u'[1, 1]', u'[3, 4]', u'1', u'1'), 
                                (u'1', 2, 1, u'2', u'2', u'0', u'0', None, None), 
                                (u'\U0001f600', 5, 1, u'4', u'4', u'0', u'0', None, None), 
                                (u'you++but', 2, 2, u'[4, 6]', u'[4, 8]', u'[2, 2]', u'[4, 6]', u'2', u'2'), 
                                (u'=)++\U0001f600++\U0001f308', 1, 3, u'[1, 1, 1]', u'[1, 1, 1]', None, None, u'1', u'0'), 
                                (u'you++but++you', 2, 3, u'[6, 6, "IGNOR"]', u'[8, 8, "IGNOR"]', None, None, u'2', u'0'), 
                                (u'you', 8, 1, u'7', u'9', u'2', u'4', None, None), 
                                (u'-(', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'\U0001f62b', 3, 1, u'3', u'3', u'0', u'0', None, None), 
                                (u'?++1', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'but++you++\U0001f600', 1, 3, u'[3, 1, 1]', u'[3, 2, 1]', None, None, u'1', u'0'), 
                                (u'1++\U0001f62b', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u':-(', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'.++:-(', 1, 2, u'[1, 1]', u'[1, 1]', None, None, u'1', u'0'), 
                                (u'glad', 1, 1, u'1', u'1', u'0', u'0', None, None), 
                                (u'you++\U0001f600++\U0001f308', 1, 3, u'[1, 1, 1]', u'[2, 1, 1]', None, None, u'1', u'0')
                            ]



        #p(baseline ,"baseline")
        

        #assert baseline == right_baseline
        baseline.should.be.equal(right_baseline)
        #assert stats._compute_baseline_sum() > 0








    @attr(status='stable')
    #@wipd
    def test_recompute_syntagma_repetativity_scope_621(self):
        
        self.prj_folder()
        #self.blogger_corpus()
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



        
        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, full_repetativ_syntagma=True)
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))
        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        stats.optimize_db()

        ### RepCompution 
        assert stats._full_repetativ_syntagma == True
        assert stats.recompute_syntagma_repetativity_scope(False)
        assert stats._full_repetativ_syntagma == False
        assert stats.recompute_syntagma_repetativity_scope(True)
        assert stats._full_repetativ_syntagma == True
 




        #stats = Stats(mode=self.mode)
        stats = Stats(mode=self.mode,use_cash=True, status_bar=True)#, )
        stats.init(self.tempdir_project_folder, name, language, visibility,  corpus_id=corpus_id,  version= version, encryption_key=encryption_key, full_repetativ_syntagma=False)
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))
        stats.compute(corp,stream_number=1,adjust_to_cpu=False, freeze_db=False)
        stats.optimize_db()

        ### RepCompution 
        assert stats._full_repetativ_syntagma == False
        assert stats.recompute_syntagma_repetativity_scope(True)
        assert stats._full_repetativ_syntagma == True
        assert stats.recompute_syntagma_repetativity_scope(False)
        assert stats._full_repetativ_syntagma == False




    @attr(status='stable')
    #@wipd
    def test_reconstruct_syntagma_630(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))
        
        indexes = {'repl': {u'pos': 10, u'index_of_repl': 9, u'id': 0, u'polarity': 11, u'in_redu': 12, u'context_infoL2': 20, u'context_infoL3': 18, u'context_infoL1': 22, u'context_infoL4': 16, u'context_infoL5': 14, u'contextR2': 25, u'contextR3': 27, u'contextR1': 23, u'contextR4': 29, u'contextR5': 31, u'rle_word': 6, u'index_in_redufree': 4, u'contextL1': 21, u'contextL4': 15, u'contextL5': 13, u'redufree_len': 2, u'repl_length': 8, u'contextL2': 19, u'contextL3': 17, u'context_infoR1': 24, u'context_infoR2': 26, u'context_infoR3': 28, u'context_infoR4': 30, u'context_infoR5': 32, u'index_in_corpus': 3, u'normalized_word': 5, u'doc_id': 1, u'repl_letter': 7}, 'baseline': {u'occur_repl_uniq': 3, u'syntagma': 0, u'hight_scope_uniq_occur_redu': 8, u'occur_redu_exhausted': 6, u'occur_redu_uniq': 5, u'hight_scope_uniq_occur_repl': 7, u'occur_syntagma_all': 1, u'scope': 2, u'occur_repl_exhausted': 4}, 'redu': {u'orig_words': 6, u'pos': 8, u'id': 0, u'polarity': 9, u'redu_length': 7, u'context_infoL2': 17, u'context_infoL3': 15, u'context_infoL1': 19, u'context_infoL4': 13, u'context_infoL5': 11, u'contextR2': 22, u'contextR3': 24, u'contextR1': 20, u'contextR4': 26, u'contextR5': 28, u'index_in_redufree': 4, u'contextL4': 12, u'contextL5': 10, u'redufree_len': 2, u'contextL1': 18, u'contextL2': 16, u'contextL3': 14, u'context_infoR1': 21, u'context_infoR2': 23, u'context_infoR3': 25, u'context_infoR4': 27, u'context_infoR5': 29, u'index_in_corpus': 3, u'normalized_word': 5, u'doc_id': 1}}

        ######## rep_type = 'repl'##########

        ########################
        ##### order_output_by_syntagma_order = False ######
        #######################
        
        ######## rep_type = 'repl'##########

        ### Case 1.1 
        rep_type = 'repl'
        reps = [
                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                    (15, 10000, u'[8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), 
                    (17, 11111, u'[5, 12]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'), 
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                    (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                ]
        
        inp_syntagma_splitted = [u'klitze', u'kleine']
        scope = 2 
        minimum_columns = False
        #indexes = self.col_index_min if minimum_columns else self.col_index_orig
        order_output_by_syntagma_order = False
        right_output = {
                            8888: {
                                    0: {
                                            0: [u'klitze', (1,)], 
                                            1: [u'kleine', (2, 3)]
                                        }}, 
                            10000: {
                                    0: {
                                            1: [u'klitze', (15,)]}}, 
                            11111: {0: {1: [u'klitze', (17,)]
                                    }}}

        right_length = {8888: [4, 9], 10000: [8], 11111: [5, 12]}

        output_raw,length = stats._reconstruct_syntagma(rep_type, reps,order_output_by_syntagma_order,indexes)
        #p((output_raw,length))
        preparated_output  = {d:{s:{t:ids for t, ids in s_data.iteritems()} for s, s_data in doc_data.iteritems()} for d, doc_data in output_raw.iteritems()}
        #p(preparated_output, "preparated_output")
        preparated_output.should.be.equal(right_output)
        length.should.be.equal(right_length)




        ######## rep_type = 'redu'##########
        
        ### Case 1.1 
        rep_type = 'redu'
        reps = [
                    (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                    (4, 12222, u'[11]', u'[0, 1]', u'[0, 1]', u'klitze', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'), 
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                ]
        
        inp_syntagma_splitted = [u'klitze', u'kleine']
        scope = 2 
        minimum_columns = False
        order_output_by_syntagma_order = False
        right_output = {
                            8888: {0: 
                                    {
                                        0: [u'klitze', (1,)], 
                                        1: [u'kleine', (2,)]}}, 
                            12222: {0: 
                                    {
                                        1: [u'klitze', (4,)]}}}

        right_length ={8888: [4, 9], 12222: [11]}

        output_raw,length = stats._reconstruct_syntagma(rep_type, reps, order_output_by_syntagma_order,indexes)
        #p((output_raw,length))
        preparated_output  = {d:{s:{t:ids for t, ids in s_data.iteritems()} for s, s_data in doc_data.iteritems()} for d, doc_data in output_raw.iteritems()}
        #p(preparated_output, "preparated_output")
        preparated_output.should.be.equal(right_output)
        length.should.be.equal(right_length)



        # #####################################################################################################################
        


        ########################
        ##### order_output_by_syntagma_order = True ######
        #######################

        ######## rep_type = 'repl'##########

        ### Case 1.1 
        rep_type = 'repl'
        reps = [
                    (u'klitze', 
                        [
                            (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                            (15, 10000, u'[8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), 
                            (17, 11111, u'[5, 12]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]')]), 
                    (u'kleine', 
                        [
                            (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                            (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')])]
        
        inp_syntagma_splitted = [u'klitze', u'kleine']
        scope = 2 
        minimum_columns = False
        order_output_by_syntagma_order = True
        right_output = {
                            8888: 
                                {0: 
                                    {
                                        0: [u'klitze', (1,)], 
                                        1: [u'kleine', (2, 3)]}}, 
                            10000: {0: {
                                        1: [u'klitze', (15,)]}}, 
                            11111: {0: {
                                        1: [u'klitze', (17,)]}}}

        right_length = {8888: [4, 9], 10000: [8], 11111: [5, 12]}

        output_raw,length = stats._reconstruct_syntagma(rep_type, reps, order_output_by_syntagma_order,indexes)
        #p((output_raw,length))
        preparated_output  = {d:{s:{t:ids for t, ids in s_data.iteritems()} for s, s_data in doc_data.iteritems()} for d, doc_data in output_raw.iteritems()}
        #p(preparated_output, "preparated_output")
        preparated_output.should.be.equal(right_output)
        length.should.be.equal(right_length)



        ### Case 1.2
        rep_type = 'repl'

        reps = (
                        ('number', 
                            (
                                (20, 11111, u'[5, 12]', u'[1, 6]', u'[1, 6]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), 
                                (21, 11111, u'[5, 12]', u'[1, 7]', u'[1, 7]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None), 
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None))), 
                        ('number', 
                            (
                                (21, 11111, u'[5, 12]', u'[1, 7]', u'[1, 7]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None), 
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None), 
                                (24, 11111, u'[5, 12]', u'[1, 10]', u'[1, 10]', u'5', u'5^5', u'5', 5, 0, u'number', u'["neutral", 0.0]', None, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', None, None, None, None, None, None, None, None))), 
                        ('number', 
                            (
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None), 
                                (24, 11111, u'[5, 12]', u'[1, 10]', u'[1, 10]', u'5', u'5^5', u'5', 5, 0, u'number', u'["neutral", 0.0]', None, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', None, None, None, None, None, None, None, None))))



        
        scope = 3 
        minimum_columns = False
        order_output_by_syntagma_order = True
        right_output = {
                            11111: {
                                        1: {
                                                8: [u'number', (22, 22, 22)], 
                                                9: [u'number', (23, 23, 23)], 
                                                10: [u'number', (24, 24)], 
                                                6: [u'number', (20,)], 
                                                7: [u'number', (21, 21)]
                                                }}}


        right_length = {11111: [5, 12]}

        output_raw,length = stats._reconstruct_syntagma(rep_type, reps, order_output_by_syntagma_order,indexes,syntagma_type="pos")
        #p((output_raw,length))
        preparated_output  = {d:{s:{t:ids for t, ids in s_data.iteritems()} for s, s_data in doc_data.iteritems()} for d, doc_data in output_raw.iteritems()}
        #p(preparated_output, "preparated_output")
        preparated_output.should.be.equal(right_output)
        length.should.be.equal(right_length)








    @attr(status='stable')
    #@wipd
    def test_exctract_full_syntagmas_631(self):
        stats = Stats(mode=self.mode)


        ########################
        ##### scope = 1 ######
        #######################


        #####################
        ## scope = 1 ######
        ###################

        ### Case 1.1 
        inp_syntagma_splitted = ("klitze",)
        redu_free_elem_length = { 10000:[5,1,1], 11111:[2,5,6]}
        scope = 1
        reconstructed_syntagmas = {
                                    11111:{
                                            0:{
                                                1:["klitze",(18,)],
                                               },
                                            1:{
                                                1:["klitze",(20,)],
                                                2:["kleine",(22,)],
                                               },
                                            2:{
                                                0:["klitze",(29,)],
                                                2:["klitze",(26,)],
                                                4:["klitze",(27,)],
                                               }
                                           }
                                  }


        right_full_syntagmas = (((0, 1),), ((1, 1),), ((2, 0),), ((2, 2),), ((2, 4),))
        right_allow_ids = (18, 27, 20, 26, 29)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])



        ########################
        ##### scope = 2 ######
        ########################


        ### Case 2.0
        inp_syntagma_splitted = ("klitze","kleine")
        redu_free_elem_length = { 10000:[5,1,1], 11111:[2,5,4]}
        scope = 2
        reconstructed_syntagmas = {
                                    11111:{
                                            0:{
                                                1:["klitze",(18,)],
                                                2:["kleine",(19,)],
                                               },

                                           }
                                  }


        right_full_syntagmas = (((0, 1), (0, 2)),)
        right_allow_ids = (18, 19)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p(full_syntagmas, allow_ids)
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])




        ### Case 2.1 
        inp_syntagma_splitted = ("klitze","kleine")
        redu_free_elem_length = { 10000:[5,1,1], 11111:[2,5,4]}
        scope = 2
        reconstructed_syntagmas = {
                                    11111:{
                                            0:{
                                                1:["klitze",(18,)],
                                                2:["kleine",(19,)],
                                               },
                                            1:{
                                                1:["klitze",(20,)],
                                                2:["kleine",(22,)],
                                               }
                                           }
                                  }


        right_full_syntagmas = (((0, 1), (0, 2)), ((1, 1), (1, 2)))
        right_allow_ids = (18, 19, 20, 22)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)

        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])




        ### Case 2.2
        inp_syntagma_splitted = ("klitze","kleine")
        redu_free_elem_length = {  11111:[2,5,4]}
        scope = 2
        reconstructed_syntagmas = {
                                    11111:{
                                            0:{
                                                1:["klitze",(18,)],
                                                2:["kleine",(19,)],
                                               },
                                            1:{
                                                1:["klitze",(20,)],
                                                4:["klitze",(22,)],
                                               },
                                            2:{
                                                0:["kleine",(24,554,)],
                                                2:["kleine",(29,56,)],
                                               }
                                           }
                                  }


        right_full_syntagmas = (((0, 1), (0, 2)), ((1, 4), (2, 0)))
        right_allow_ids = (18, 19, 22, 24, 554)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])




        ### Case 2.3
        
        # inp_syntagma_splitted  = [u'klitze', u'kleine']

        # _rep  = [
        #             (u'klitze', 
        #                 [
        #                     (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
        #                     (15, 10000, u'[8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), 
        #                     (17, 11111, u'[5, 12]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'),), 
        #             (u'kleine', 
        #                 [
        #                     (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
        #                     (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
        #                     ,)]
        inp_syntagma_splitted  = [u'klitze', u'kleine']
        redu_free_elem_length = {8888: [4, 9], 10000: [8], 11111: [5, 12]}
        scope = 2
        reconstructed_syntagmas = {
                                    8888: {0: {
                                                0:["klitze",(1,)], 
                                                1:["kleine",(2, 3,)]
                                               }
                                           }, 
                                    10000: {0: {
                                                1:["klitze",(15,)]
                                                }
                                            }, 
                                    11111: {0: {
                                                1:["klitze",(17,)]
                                                }
                                            }
                                    }


        right_full_syntagmas = (((0, 0), (0, 1)),)
        right_allow_ids = (1, 2, 3)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])





        ### Case 2.4
        #
        # inp_syntagma_splitted  = [u'klitze', u'kleine']

        # _rep  = [
        #             (u'klitze', 
        #                 [
        #                     (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
        #                     (4, 12222, u'[11]', u'[0, 1]', u'[0, 1]', u'klitze', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'),), 
        #             (u'kleine', 
        #                 [
        #                     (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
        #                     ,)]
        inp_syntagma_splitted  = [u'klitze', u'kleine']
        redu_free_elem_length = {8888: [4, 9], 12222: [11]}
        scope = 2
        reconstructed_syntagmas = {
                                    8888: {0: {
                                                0:["klitze",(1,)], 
                                                1:["kleine",(2,)]
                                                }
                                          }, 
                                    12222: {0: {
                                                1:["klitze",(4,)]
                                                }
                                            }
                                  }


        right_full_syntagmas = (((0, 0), (0, 1)),)
        right_allow_ids = (1, 2)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])





        ### Case 2.5
        # inp_syntagma_splitted  = [u'klitze', u'kleine']

        # _rep  = [
        #             (u'klitze', 
        #                 [
        #                     (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
        #                     (4, 12222, u'[11]', u'[0, 1]', u'[0, 1]', u'klitze', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'),), 
        #             (u'kleine', 
        #                 [
        #                     (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
        #                     ,)]
        inp_syntagma_splitted  = [u'klitze', u'kleine']
        redu_free_elem_length = {8888: [4, 9], 12222: [11]}
        scope = 2
        reconstructed_syntagmas = {
                                    8888: {0: {
                                                0:["klitze",(1,)], 
                                                1:["kleine",(2,)],
                                                2:["klitze",(2,)], 
                                                3:["kleine",(3,)],
                                                }
                                          }, 
                                    12222: {0: {
                                                1:["klitze",(4,)]
                                                }
                                            }
                                  }


        right_full_syntagmas = (((0, 0), (0, 1)), ((0, 2), (0, 3)))
        right_allow_ids = (1, 2, 3)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        #p(set([ True if len(syn)== scope else False for syn in  full_syntagmas ,),)
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])





        ########################
        ##### scope = 3 ######
        ########################

        ### Case 3.1
        inp_syntagma_splitted = ("klitze","kleine","iii")
        redu_free_elem_length = {8888:[2, 3], 10000:[3,4], 11111:[2,5,4]}
        scope = 3
        reconstructed_syntagmas = {
                                    8888:{
                                            0:{
                                                0:["klitze",(1,)], 
                                                1:["kleine",(2, 3,)]
                                               }, 
                                            1:{
                                                0:["iii",(10,)]
                                               }, 
                                          },
                                    10000:{
                                            0: {
                                                1:["kleine",(15,)]
                                                }
                                           }, 
                                    11111:{
                                            0:{
                                                1:["kleine",(17,)]
                                               }
                                           }
                                  }
#
        right_full_syntagmas = (((0, 0), (0, 1), (1, 0)),)
        right_allow_ids = (1, 2, 3, 10)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])

        


        ########################
        ##### scope = 3 ######
        ########################

        ### Case 3.2
        inp_syntagma_splitted = ("klitze","kleine","iii")
        redu_free_elem_length = {8888:[4, 5], 10000:[5,1,1], 11111:[2,5,4]}
        scope = 3
        reconstructed_syntagmas = {
                                    8888:{
                                            0:{
                                                0:["klitze",(1,)], 
                                                1:["kleine",(2, 3,)],
                                                2:["iii",(4, 5,)],
                                               }, 
                                            1:{
                                                1:["klitze",(10,)],
                                                2:["kleine",(11,)],
                                                3:["i",(12,)],
                                               }, 
                                          },
                                  }
#
        right_full_syntagmas = (((0, 0), (0, 1), (0, 2)), ((1, 1), (1, 2), (1, 3)))
        right_allow_ids = (1, 2, 3, 4, 5, 10, 11, 12)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])





        ########################
        ##### scope = 3 ######
        ########################

        ### Case 3.3
        inp_syntagma_splitted = ("klitze","kleine","iii")
        redu_free_elem_length = { 10000:[5,1,1], 11111:[2,5,4]}
        scope = 3
        reconstructed_syntagmas = {
                                    10000:{
                                            0: {
                                                4:["klitze",(15,)],
                                                },
                                            1: {
                                                0:["kleine",(16,)],
                                                },
                                            2: {
                                                0:["iii",(17,)],
                                                },
                                           }
                                  }


        right_full_syntagmas = (((0, 4), (1, 0), (2, 0)),)
        right_allow_ids = (15, 16, 17)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)

        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])





        ########################
        ##### scope = 6 ######
        ########################

        ### Case 6.1
        inp_syntagma_splitted = ("klitze","kleine","iii",",","oder","wie")
        redu_free_elem_length = { 10000:[5,2,2,1], 11111:[2,5,4]}
        scope = 6
        reconstructed_syntagmas = {
                                    10000:{
                                            0: {
                                                4:["klitze",(15,)],
                                                },
                                            1: {
                                                0:["kleine",(16,)],
                                                1:["iii",(19,)],
                                                },
                                            2: {
                                                0:[",",(17,)],
                                                1:["oder",(34,)],
                                                },
                                            3: {
                                                0:["wie",(17,)],
                                                },
                                           }
                                  }


        right_full_syntagmas = (((0, 4), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0)),)
        right_allow_ids = (15, 16, 19, 17, 34, 17)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])


        ### Case 6.2
        inp_syntagma_splitted = ("klitze","kleine","iii",",","oder","wie")
        redu_free_elem_length = { 10000:[10,3,4,5], 11111:[7,4,2,1]}
        scope = 6
        reconstructed_syntagmas = {
                                    10000:{
                                            0: {
                                                0:["klitze",(15,)],
                                                1:["kleine",(16,)],
                                                2:["iii",(17,)],
                                                3:[",",(18,)],
                                                4:["oder",(19,)],
                                                5:["wie",(20,)],
                                                },
                                            1: {
                                                0:["klitze",(164,)],
                                                1:["kleine",(193,)],
                                                },
                                            2: {
                                                0:["klitze",(172,)],
                                                1:["kleine",(343,)],
                                                },
                                           },
                                    11111:{
                                            0: {
                                                4:["klitze",(23,)],
                                                5:["kleine",(25,)],
                                                6:["iii",(64,)],
                                                },
                                            1: {
                                                0:[",",(152,)],
                                                1:["oder",(114,)],
                                                2:["wie",(1,)],
                                                },
                                            2: {
                                                0:["klitze",(147,)],
                                                1:["kleine",(344,)],
                                                },
                                            3: {
                                                0:["iii",(178,)],
                                                },
                                           }
                                  }


        right_full_syntagmas = (((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)), ((0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2)))
        right_allow_ids = (15, 16, 17, 18, 19, 20, 23, 25, 64, 152, 114, 1)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])




        # ### Case 6.3
        inp_syntagma_splitted = ("klitze","kleine","iii",",","oder","wie")
        redu_free_elem_length = { 10000:[10,10,10,10], 11111:[7,4,2,1]}
        scope = 6
        reconstructed_syntagmas = {
                                    10000:{
                                            0: {
                                                2:["klitze",(15,)],
                                                3:["kleine",(16,)],
                                                4:["iii",(17,)],
                                                6:[",",(18,)],
                                                7:["oder",(19,)],
                                                8:["wie",(20,)],
                                                },
                                            2: {
                                                4:["klitze",(152,)],
                                                5:["kleine",(163,)],
                                                6:["iii",(174,)],
                                                7:[",",(185,)],
                                                8:["oder",(196,)],
                                                9:["wie",(207,)],
                                                },
                                            3: {
                                                1:["klitze",(150,)],
                                                2:["kleine",(160,)],
                                                3:["iii",(170,)],
                                                4:[",",(180,)],
                                                5:["oder",(190,)],
                                                6:["wie",(200,)],
                                                },
                                           },
                                  }


        right_full_syntagmas = (((2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9)), ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)))
        right_allow_ids = (160, 163, 196, 200, 170, 174, 207, 180, 150, 152, 185, 190)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)== scope else False for syn in  full_syntagmas ])




        ###############################
        ##############################
        ### mixes scope ############


        ### Case __.1
        syntagma_type = "pos"
        inp_syntagma_splitted = [u'number', u'number', u'number']
        redu_free_elem_length = {11111: [5, 6, 14]}
        scope = 3
        reconstructed_syntagmas = {
                                    11111: {
                                                2: {
                                                        8: [u'number', (33,)], 
                                                        9: [u'number', (34, 34)], 
                                                        10: [u'number', (35, 35, 35)], 
                                                        11: [u'number', (36, 36, 36)], 
                                                        12: [u'number', (37, 37)]
                                                    }
                                            }
                                   }



        right_full_syntagmas = (((2, 8), (2, 9), (2, 10)),)
        right_allow_ids = (33, 34, 35)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])


        ### Case __.2
        syntagma_type = "pos"
        inp_syntagma_splitted = ("NN","NP","NN")
        redu_free_elem_length = {11111: [5, 12]}
        scope = 3
        reconstructed_syntagmas = {
                                        11111: {
                                                    1: {
                                                            6: ["NN",(22, 22, 22)], 
                                                            7: ["NP",(23, 23, 23)], 
                                                            8: ["NN",(24, 24)], 
                                                            9: ["NN",(221, 221, 221)], 
                                                            10: ["NP",(232, 233, 236)], 
                                                            11: ["NN",(240, 248)], 
                                                        }
                                                }
                                    }


        right_full_syntagmas = (((1, 6), (1, 7), (1, 8)), ((1, 9), (1, 10), (1, 11)))
        right_allow_ids = (232, 233, 236, 240, 24, 22, 23, 248, 221)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])




        ### Case __.3
        syntagma_type = "pos"
        inp_syntagma_splitted = ("NN","NP","NN","NP")
        redu_free_elem_length = {11111: [5, 12]}
        scope = 4
        reconstructed_syntagmas = {
                                        11111: {
                                                    1: {
                                                            6: ["NN",(22, 22, 22)], 
                                                            7: ["NP",(23, 23, 23)], 
                                                            8: ["NN",(24, 24)], 
                                                            9: ["NP",(221, 221, 221)], 
                                                            10: ["NN",(232, 233, 236)], 
                                                            11: ["NP",(240, 248)], 
                                                        }
                                                }
                                    }


        right_full_syntagmas = (((1, 6), (1, 7), (1, 8), (1, 9)),)
        right_allow_ids = (24, 221, 22, 23)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])



        ### Case __.4
        syntagma_type = "lexem"
        inp_syntagma_splitted = ("klitze","kleine", "klitze")
        redu_free_elem_length = {11111: [5, 15]}
        scope = 3
        reconstructed_syntagmas = {
                                        11111: {
                                                    1: {
                                                            6: ["klitze",(22, 22, 22)], 
                                                            7: ["kleine",(23, 23, 23)], 
                                                            8: ["klitze",(24, 24)], 
                                                            9: ["klitze",(22, 22, 22)], 
                                                            10: ["kleine",(23, 23, 23)], 
                                                            11: ["klitze",(24, 24)],  
                                                        }
                                                }
                                    }


        right_full_syntagmas = (((1, 6), (1, 7), (1, 8)), ((1, 9), (1, 10), (1, 11)))
        right_allow_ids = (24, 22, 23)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])


        ### Case __.4
        syntagma_type = "lexem"
        inp_syntagma_splitted = ("klitze","kleine", "klitze", "kleine")
        redu_free_elem_length = {11111: [5, 15]}
        scope = 4
        reconstructed_syntagmas = {
                                        11111: {
                                                    1: {
                                                            6: ["klitze",(22, 22, 22)], 
                                                            7: ["kleine",(23, 23, 23)], 
                                                            8: ["klitze",(22, 22, 22)], 
                                                            9: ["kleine",(23, 23, 23)],
                                                            10: ["klitze",(22, 22, 22)], 
                                                            11: ["kleine",(23, 23, 23)], 
                                                        }
                                                }
                                    }


        right_full_syntagmas = (((1, 6), (1, 7), (1, 8), (1, 9)),)
        right_allow_ids = (22, 23)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])


        ### Case __.5
        syntagma_type = "lexem"
        inp_syntagma_splitted = ("klitze","kleine",)
        redu_free_elem_length = {11111: [5, 15]}
        scope = 2
        reconstructed_syntagmas = {
                                        11111: {
                                                    1: {
                                                            6: ["klitze",(22, 22, 22)], 
                                                            7: ["kleine",(23, 23, 23)], 
                                                            8: ["klitze",(22, 22, 22)], 
                                                            9: ["kleine",(23, 23, 23)],
                                                            10: ["klitze",(22, 22, 22)], 
                                                            11: ["kleine",(23, 23, 23)], 
                                                        }
                                                }
                                    }


        right_full_syntagmas = (((1, 6), (1, 7)), ((1, 8), (1, 9)), ((1, 10), (1, 11)))
        right_allow_ids = (22, 23)

        full_syntagmas, allow_ids = stats._exctract_full_syntagmas(reconstructed_syntagmas, scope,redu_free_elem_length,inp_syntagma_splitted,syntagma_type=syntagma_type)
        #p((full_syntagmas, allow_ids))
        full_syntagmas.should.be.equal(right_full_syntagmas)
        set(allow_ids).should.be.equal(set(right_allow_ids))
        assert False not in set([ True if len(syn)>= scope else False for syn in  full_syntagmas ])












    @attr(status='stable')
    #@wipd
    def test_filter_full_rep_syn_632(self):
        stats = Stats(mode=self.mode)

        #############################################################
        ####### order_output_by_syntagma_order = True ####
        ###############################################################

        #####rep_type = 'repl'######

        ### Case 1.1 
        rep_type = 'repl'
        _rep = (
                    (u'klitze', 
                        (
                            (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                            (15, 10000, u'[8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), 
                            (17, 11111, u'[5, 12]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'))), 
                    (u'kleine', 
                        (
                            (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                            (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                            )))
        
        allowed_ids = set((1, 2, 3))

        order_output_by_syntagma_order = True

        right_filtered_reps = (
                                (u'klitze', 
                                    (
                                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),)), 
                                (u'kleine', 
                                    (
                                        (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                        (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                                        )))


        filtered_reps = stats._filter_full_rep_syn(rep_type,_rep, allowed_ids,order_output_by_syntagma_order, 0)
        #p((filtered_reps))
        tuple(filtered_reps).should.be.equal(tuple(right_filtered_reps))





        #####rep_type = 'redu'######

        ### Case 2.1 
        rep_type = 'redu'
        _rep = (
                (u'klitze', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                        (4, 12222, u'[11]', u'[0, 1]', u'[0, 1]', u'klitze', u'{"klitze": 4}', 4, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u',', u'["symbol"]', u'die', u'["PRELS"]', u'ich', u'["PPER"]'))), 
                (u'kleine', 
                    (
                        (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                        )))
        
        allowed_ids = set((1, 2))

        order_output_by_syntagma_order = True

        right_filtered_reps = (
                                (u'klitze', 
                                    (
                                        (1, 8888, u'[4, 9]', u'[0, 0]', u'[0, 0]', u'klitze', u'{"klitze": 1, "kli^4tze": 1}', 2, u'NN', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),)), 
                                (u'kleine', 
                                    (
                                        (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'{"kle^5ine": 1, "klein^3e": 1}', 2, u'NE', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                                        )))

        filtered_reps = stats._filter_full_rep_syn(rep_type,_rep, allowed_ids,order_output_by_syntagma_order, 0)
        #p((filtered_reps))
        tuple(filtered_reps).should.be.equal(tuple(right_filtered_reps))






        # ########################################################################################################################
        # ########################################################################################################################
        # ########################################################################################################################




        # #############################################################
        # ####### order_output_by_syntagma_order = False ####
        # ############################################################



        # #####rep_type = 'redu'######

        ### Case 1.1 
        rep_type = 'redu'
        _rep = (
                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                    (15, 10000, u'[8]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'\xfcberaschung', u'["NN"]', u'@sch\xf6nesleben', u'["mention"]', u'#machwasdaraus', u'["hashtag"]', u'#bewegedeinarsch', u'["hashtag"]'), 
                    (17, 11111, u'[5, 12]', u'[0, 1]', u'[0, 1]', u'klitze', u'klitze^4', u'e', 4, 5, u'VAPPER', u'["neutral", 0.0]', None, None, None, None, None, None, None, None, None, u'eine', u'["ART"]', u'kleine', u'["ADJA"]', u'sache', u'["NN"]', u'.', u'["symbol"]', u'die', u'["PDS"]', u'aber', u'["ADV"]'), 
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                    (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                )
        
        allowed_ids = set((1, 2))

        order_output_by_syntagma_order = False

        right_filtered_reps = (
                                (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                                (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                              )

        filtered_reps = stats._filter_full_rep_syn(rep_type,_rep, allowed_ids,order_output_by_syntagma_order, 0)
        #p((filtered_reps))
        tuple(filtered_reps).should.be.equal(tuple(right_filtered_reps))







    @attr(status='stable')
    #@wipd 
    def test_delete_dublicats_in_reps_633(self):
        stats = Stats(mode=self.mode)

        #############################################################
        ####### order_output_by_syntagma_order = True ####
        ###############################################################

        ### Case 1.1 
        order_output_by_syntagma_order = True
        _rep = (
                (u'klitze', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),

                        )), 

                (u'kleine', 
                    (
                        (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                        (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                        (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                        )))

        right_dublicates_free = (
                                    (u'klitze', 
                                        (
                                            (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                                            )), 
                                    (u'kleine', 
                                        (
                                            (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                            (3, 8888, u'[4, 9]', u'[0, 3]', u'[0, 1]', u'kleine', u'klein^3e', u'n', 3, 4, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]')
                                            )))

        dublicats_free = stats._delete_dublicats_in_reps(_rep, order_output_by_syntagma_order, 0)
        #p((dublicats_free))
        tuple(right_dublicates_free).should.be.equal(tuple(dublicats_free))




        ### Case 1.2
        stats._full_repetativ_syntagma = True
        order_output_by_syntagma_order = True
        _rep = (
                (u'klitze', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),

                        )), 

                (u'kleine', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        )))

        right_dublicates_free = ()

        dublicats_free = stats._delete_dublicats_in_reps(_rep, order_output_by_syntagma_order, 0)
        #p((dublicats_free))
        tuple(right_dublicates_free).should.be.equal(tuple(dublicats_free))







        ### Case 1.3
        stats._full_repetativ_syntagma = False
        order_output_by_syntagma_order = True
        _rep = (
                (u'klitze', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),

                        )), 

                (u'kleine', 
                    (
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                        )))

        right_dublicates_free = (
                                    (u'klitze', ()), 
                                    (u'kleine', 
                                        (
                                            (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                                            )))

        dublicats_free = stats._delete_dublicats_in_reps(_rep, order_output_by_syntagma_order, 0)
        #p((dublicats_free))
        tuple(right_dublicates_free).should.be.equal(tuple(dublicats_free))




        ### Case 1.4
        stats._full_repetativ_syntagma = True
        order_output_by_syntagma_order = True
        _rep = (
                        ('number', 
                            (
                                (20, 11111, u'[5, 12]', u'[1, 6]', u'[1, 6]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'), 
                                (21, 11111, u'[5, 12]', u'[1, 7]', u'[1, 7]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None), 
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None))), 
                        ('number', 
                            (
                                (21, 11111, u'[5, 12]', u'[1, 7]', u'[1, 7]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None), 
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None), 
                                (24, 11111, u'[5, 12]', u'[1, 10]', u'[1, 10]', u'5', u'5^5', u'5', 5, 0, u'number', u'["neutral", 0.0]', None, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', None, None, None, None, None, None, None, None))), 
                        ('number', 
                            (
                                (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None), 
                                (24, 11111, u'[5, 12]', u'[1, 10]', u'[1, 10]', u'5', u'5^5', u'5', 5, 0, u'number', u'["neutral", 0.0]', None, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', None, None, None, None, None, None, None, None))))


        right_dublicates_free = (
                                    ('number', 
                                        (
                                            (20, 11111, u'[5, 12]', u'[1, 6]', u'[1, 6]', u'1', u'1^5', u'1', 5, 0, u'number', u'["neutral", 0.0]', None, u'aber', u'["ADV"]', u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]'),)), 
                                    ('number', 
                                        (
                                            (21, 11111, u'[5, 12]', u'[1, 7]', u'[1, 7]', u'2', u'2^4', u'2', 4, 0, u'number', u'["neutral", 0.0]', None, u'trotzdem', u'["PAV"]', u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 3, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None),)), 
                                    ('number', 
                                        (
                                            (22, 11111, u'[5, 12]', u'[1, 8]', u'[1, 8]', u'3', u'3^5', u'3', 5, 0, u'number', u'["neutral", 0.0]', None, u'wichtig', u'["ADJA"]', u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 4, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None), 
                                            (23, 11111, u'[5, 12]', u'[1, 9]', u'[1, 9]', u'4', u'4^4', u'4', 4, 0, u'number', u'["neutral", 0.0]', None, u'ist', u'["NN"]', u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 5, u'["number"]', 6, u'["number"]', None, None, None, None, None, None), 
                                            (24, 11111, u'[5, 12]', u'[1, 10]', u'[1, 10]', u'5', u'5^5', u'5', 5, 0, u'number', u'["neutral", 0.0]', None, u'!', u'["symbol"]', 1, u'["number"]', 2, u'["number"]', 3, u'["number"]', 4, u'["number"]', 6, u'["number"]', None, None, None, None, None, None, None, None)
                                            )))

        dublicats_free = stats._delete_dublicats_in_reps(_rep, order_output_by_syntagma_order, 0)
        #p((dublicats_free))
        tuple(right_dublicates_free).should.be.equal(tuple(dublicats_free))





        # #############################################################
        # ####### order_output_by_syntagma_order = False ####
        # ############################################################



        # #####rep_type = 'redu'######

        ### Case 2.1 
        order_output_by_syntagma_order = False
        _rep = (
                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'),
                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'), 
                )

        right_dublicates_free = (
                                    (1, 8888, u'[4, 9]', u'[0, 1]', u'[0, 0]', u'klitze', u'kli^4tze', u'i', 4, 2, u'NN', u'["neutral", 0.0]', u'[0, 0]', None, None, None, None, None, None, None, None, None, None, u'kleine', u'["NE", {"kle^5ine": 1, "klein^3e": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]'),
                                    (2, 8888, u'[4, 9]', u'[0, 2]', u'[0, 1]', u'kleine', u'kle^5ine', u'e', 5, 2, u'NE', u'["neutral", 0.0]', u'[0, 2]', None, None, None, None, None, None, None, None, u'klitze', u'["NN", {"klitze": 1, "kli^4tze": 1}]', u'\xfcberaschung', u'["NN"]', u'.', u'["symbol"]', u'trotzdem', u'["PAV"]', u'hat', u'["VAFIN"]', u'sie', u'["PPER"]'), 
                                )
        
        dublicats_free = stats._delete_dublicats_in_reps(_rep, order_output_by_syntagma_order, 0)
         
        #p((dublicats_free))
        tuple(dublicats_free).should.be.equal(tuple(right_dublicates_free))









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



    ####### 700 #######


    @attr(status='stable')
    #@wipd
    def test_compute_rep_sum_700(self):
        self.prj_folder()
        #self.blogger_corpus()
        self.test_dbs()
        stats = Stats(mode=self.mode,use_cash=True)#, )
        stats.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_stats_de))
        
        ################################################
        #### "repl" ####
        ################################################
        ## Case 1.1
        summery = stats.compute_rep_sum("*", "repl")
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'a': {3: [1, {u'\xfcbe^4r^5a^3schun^6g^3': 1}], 4: [1, {u'ka^4n^5': 1}], 6: [1, {u'ta^6g^6': 1}]}, u'z': {3: [1, {u'kli^4tz^3': 1}]}, u'e': {8: [2, {u'kle^4i^5n^4e^8': 1, u'ble^8ibt': 1}], 3: [4, {u'kle^3i^3n^3': 1, u'klein^4e^3s^4': 2, u'kleine^3r^2e^5': 1}], 4: [10, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'ble^4ibt': 1, u'kle^4i^5n^4e^8': 1, u'kle^4i^5n^3e^2s^3': 2, u'eine^4': 1, u'kleine^4s^7': 2, u'klitze^4': 2}], 5: [6, {u'kle^5ine': 1, u'kleinere^5': 1, u'kle^5in^5e': 1, u'kle^5i^2n^4e^5': 2, u'kleine^3r^2e^5': 1}], 7: [1, {u'kli^4tze^7': 1}]}, u'g': {3: [1, {u'\xfcbe^4r^5a^3schun^6g^3': 1}], 6: [1, {u'ta^6g^6': 1}]}, u'4': {4: [1, {u'4^4': 1}]}, u')': {3: [3, {u'-)^3': 3}], 4: [1, {u':-)^4': 1}]}, u'h': {3: [1, {u'auswah^3l^4': 1}]}, u'l': {4: [1, {u'auswah^3l^4': 1}]}, u'n': {3: [5, {u'kle^4i^5n^3e^2s^3': 2, u'kle^3i^3n^3': 1, u'klein^3e^2s': 1, u'klein^3e': 1}], 4: [4, {u'kle^4i^5n^4e^8': 1, u'klein^4e^3s^4': 2, u'kle^5i^2n^4e^5': 1}], 5: [5, {u'klein^5': 1, u'ka^4n^5': 1, u'kle^5in^5e': 1, u'm\xe4dchen^5': 2}], 6: [2, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'kan^6': 1}]}, u'1': {8: [1, {u'1^8': 1}], 5: [1, {u'1^5': 1}], 6: [1, {u'1^6': 1}]}, u'i': {8: [1, {u'wichti^8g': 1}], 3: [2, {u'kle^3i^3n^3': 1, u'kli^3tzes^3': 1}], 4: [3, {u'kli^4tz': 1, u'kli^4tze^7': 1, u'kli^4tz^3': 1}], 5: [4, {u'kle^4i^5n^3e^2s^3': 2, u'kle^4i^5n^4e^8': 1, u'geni^5es^8t^5': 1}]}, u'3': {5: [1, {u'3^5': 1}]}, u'r': {4: [2, {u'\xfcber^4aschung': 2}], 5: [2, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'\xfcber^5aschung': 1}]}, u'5': {5: [1, {u'5^5': 1}]}, u'\U0001f600': {5: [1, {u'\U0001f600^5': 1}]}, u'2': {4: [1, {u'2^4': 1}]}, u's': {8: [1, {u'geni^5es^8t^5': 1}], 3: [3, {u'kle^4i^5n^3e^2s^3': 2, u'kli^3tzes^3': 1}], 4: [5, {u'kleines^4': 1, u'klitzes^4': 1, u'genies^4t^2': 1, u'klein^4e^3s^4': 2}], 6: [1, {u'is^6t': 1}], 7: [2, {u'kleine^4s^7': 2}]}, u'.': {5: [2, {u'.^5': 2}]}, u'u': {12: [1, {u'hu^12ngrig': 1}]}, u'\U0001f62b': {4: [1, {u'\U0001f62b^4': 1}]}, u't': {5: [1, {u'geni^5es^8t^5': 1}]}}
        summery.should.be.equal(right_summery)
        # i=0
        # for letter, letter_data in summery.iteritems():
        #     for rep_num, rep_num_data in letter_data.iteritems():
        #         i+=1
        #         #print repr(letter), rep_num,rep_num_data
        #         print i, letter,rep_num, rep_num_data
        # print "\n\n\n"


        #### "repl" ####
        ## Case 1.2
        summery = stats.compute_rep_sum("*", "repl", ignore_num=True, ignore_symbol=True)
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'a': {3: [1, {u'\xfcbe^4r^5a^3schun^6g^3': 1}], 4: [1, {u'ka^4n^5': 1}], 6: [1, {u'ta^6g^6': 1}]}, u'e': {8: [2, {u'kle^4i^5n^4e^8': 1, u'ble^8ibt': 1}], 3: [4, {u'kle^3i^3n^3': 1, u'klein^4e^3s^4': 2, u'kleine^3r^2e^5': 1}], 4: [10, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'ble^4ibt': 1, u'kle^4i^5n^4e^8': 1, u'kle^4i^5n^3e^2s^3': 2, u'eine^4': 1, u'kleine^4s^7': 2, u'klitze^4': 2}], 5: [6, {u'kle^5ine': 1, u'kleinere^5': 1, u'kle^5in^5e': 1, u'kle^5i^2n^4e^5': 2, u'kleine^3r^2e^5': 1}], 7: [1, {u'kli^4tze^7': 1}]}, u'g': {3: [1, {u'\xfcbe^4r^5a^3schun^6g^3': 1}], 6: [1, {u'ta^6g^6': 1}]}, u'i': {8: [1, {u'wichti^8g': 1}], 3: [2, {u'kle^3i^3n^3': 1, u'kli^3tzes^3': 1}], 4: [3, {u'kli^4tz': 1, u'kli^4tze^7': 1, u'kli^4tz^3': 1}], 5: [4, {u'kle^4i^5n^3e^2s^3': 2, u'kle^4i^5n^4e^8': 1, u'geni^5es^8t^5': 1}]}, u'h': {3: [1, {u'auswah^3l^4': 1}]}, u'l': {4: [1, {u'auswah^3l^4': 1}]}, u'n': {3: [5, {u'kle^4i^5n^3e^2s^3': 2, u'kle^3i^3n^3': 1, u'klein^3e^2s': 1, u'klein^3e': 1}], 4: [4, {u'kle^4i^5n^4e^8': 1, u'klein^4e^3s^4': 2, u'kle^5i^2n^4e^5': 1}], 5: [5, {u'klein^5': 1, u'ka^4n^5': 1, u'kle^5in^5e': 1, u'm\xe4dchen^5': 2}], 6: [2, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'kan^6': 1}]}, u')': {3: [3, {u'-)^3': 3}], 4: [1, {u':-)^4': 1}]}, u's': {8: [1, {u'geni^5es^8t^5': 1}], 3: [3, {u'kle^4i^5n^3e^2s^3': 2, u'kli^3tzes^3': 1}], 4: [5, {u'kleines^4': 1, u'klitzes^4': 1, u'genies^4t^2': 1, u'klein^4e^3s^4': 2}], 6: [1, {u'is^6t': 1}], 7: [2, {u'kleine^4s^7': 2}]}, u'r': {4: [2, {u'\xfcber^4aschung': 2}], 5: [2, {u'\xfcbe^4r^5a^3schun^6g^3': 1, u'\xfcber^5aschung': 1}]}, u'u': {12: [1, {u'hu^12ngrig': 1}]}, u'\U0001f600': {5: [1, {u'\U0001f600^5': 1}]}, u'z': {3: [1, {u'kli^4tz^3': 1}]}, u'\U0001f62b': {4: [1, {u'\U0001f62b^4': 1}]}, u't': {5: [1, {u'geni^5es^8t^5': 1}]}}
        summery.should.be.equal(right_summery)



        #### "repl" ####
        ## Case 1.3
        summery = stats.compute_rep_sum("*", "repl", ignore_num=True, ignore_symbol=True, word_examples_sum_table=False)
        summery = {letter:{rep_num:[rep_num_data[0]] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'a': {3: [1], 4: [1], 6: [1]}, u'e': {8: [2], 3: [4], 4: [10], 5: [6], 7: [1]}, u'g': {3: [1], 6: [1]}, u'i': {8: [1], 3: [2], 4: [3], 5: [4]}, u'h': {3: [1]}, u'l': {4: [1]}, u'n': {3: [5], 4: [4], 5: [5], 6: [2]}, u')': {3: [3], 4: [1]}, u's': {8: [1], 3: [3], 4: [5], 6: [1], 7: [2]}, u'r': {4: [2], 5: [2]}, u'u': {12: [1]}, u'\U0001f600': {5: [1]}, u'z': {3: [1]}, u'\U0001f62b': {4: [1]}, u't': {5: [1]}}
        summery.should.be.equal(right_summery)


        #### "repl" ####
        ## Case 1.4
        summery = stats.compute_rep_sum("*", "repl", ignore_num=True, ignore_symbol=True,sentiment="positive")
        summery = summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u')': {3: [3, {u'-)^3': 3}], 4: [1, {u':-)^4': 1}]}, u'\U0001f600': {5: [1, {u'\U0001f600^5': 1}]}}
        summery.should.be.equal(right_summery)
       


        #### "repl" ####
        ## Case 1.5
        summery = stats.compute_rep_sum(["klitze"], "repl", ignore_num=True, ignore_symbol=True,word_examples_sum_table=True)
        summery = summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'i': {4: [1, {u'kli^4tze^7': 1}]}, u'e': {4: [2, {u'klitze^4': 2}], 7: [1, {u'kli^4tze^7': 1}]}}
        summery.should.be.equal(right_summery)


        #### "repl" ####
        ## Case 1.6
        summery = stats.compute_rep_sum(["klitze", "kleine"], "repl", ignore_num=True, ignore_symbol=True)
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'i': {4: [1, {u'kli^4tze^7': 1}]}, u'e': {4: [1, {u'klitze^4': 1}], 5: [2, {u'kle^5ine': 1, u'kle^5in^5e': 1}], 7: [1, {u'kli^4tze^7': 1}]}, u'n': {3: [1, {u'klein^3e': 1}], 5: [1, {u'kle^5in^5e': 1}]}}
        summery.should.be.equal(right_summery)



        #### "repl" ####
        ## Case 1.7
        summery = stats.compute_rep_sum(["klitze", "kleine"], "repl", ignore_num=True, ignore_symbol=True,stemmed_search=True)
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'i': {3: [2, {u'kle^3i^3n^3': 1, u'kli^3tzes^3': 1}], 4: [3, {u'kli^4tz': 1, u'kli^4tze^7': 1, u'kli^4tz^3': 1}]}, u's': {3: [1, {u'kli^3tzes^3': 1}], 4: [2, {u'klitzes^4': 1, u'kleines^4': 1}]}, u'z': {3: [1, {u'kli^4tz^3': 1}]}, u'e': {3: [1, {u'kle^3i^3n^3': 1}], 4: [1, {u'klitze^4': 1}], 5: [2, {u'kle^5ine': 1, u'kle^5in^5e': 1}], 7: [1, {u'kli^4tze^7': 1}]}, u'n': {3: [3, {u'klein^3e^2s': 1, u'kle^3i^3n^3': 1, u'klein^3e': 1}], 5: [2, {u'kle^5in^5e': 1, u'klein^5': 1}]}}
        summery.should.be.equal(right_summery)


        #### "repl" ####
        ## Case 1.5
        summery = stats.compute_rep_sum(["klitze"], "repl", ignore_num=True, ignore_symbol=True)
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'i': {4: [1, {u'kli^4tze^7': 1}]}, u'e': {4: [2, {u'klitze^4': 2}], 7: [1, {u'kli^4tze^7': 1}]}}
        summery.should.be.equal(right_summery)


        #### "repl" ####
        ## Case 1.6 
        summery = stats.compute_rep_sum(["klitze", "kleine"], "repl", ignore_num=True, ignore_symbol=True,stemmed_search=True)
        summery = {letter:{rep_num:[rep_num_data[0], dict(rep_num_data[1])] for rep_num, rep_num_data in letter_data.iteritems()} for letter, letter_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'i': {3: [2, {u'kle^3i^3n^3': 1, u'kli^3tzes^3': 1}], 4: [3, {u'kli^4tz': 1, u'kli^4tze^7': 1, u'kli^4tz^3': 1}]}, u's': {3: [1, {u'kli^3tzes^3': 1}], 4: [2, {u'klitzes^4': 1, u'kleines^4': 1}]}, u'z': {3: [1, {u'kli^4tz^3': 1}]}, u'e': {3: [1, {u'kle^3i^3n^3': 1}], 4: [1, {u'klitze^4': 1}], 5: [2, {u'kle^5ine': 1, u'kle^5in^5e': 1}], 7: [1, {u'kli^4tze^7': 1}]}, u'n': {3: [3, {u'klein^3e^2s': 1, u'kle^3i^3n^3': 1, u'klein^3e': 1}], 5: [2, {u'kle^5in^5e': 1, u'klein^5': 1}]}}
        summery.should.be.equal(right_summery)
        


        # ################################################
        # #### "redu" ####
        # ##############################################
        ## Case 2.1
        summery = stats.compute_rep_sum("*", "redu")
        summery = {word:{redu_length:occur for redu_length, occur in word_data.iteritems()} for word, word_data in summery.iteritems()}
        #p(summery)
        right_summery = {u'klitze': {2: 1, 4: 1}, u'klitz': {3: 1}, u'geniest': {2: 1}, u'-)': {2: 1}, u'kleine': {2: 1}, u'bleibt': {2: 1}, u'kan': {2: 1}, u'kleinere': {2: 1}, u'kleines': {2: 1, 3: 2}, u'klitzes': {2: 1}, u'klein': {2: 1}}
        summery.should.be.equal(right_summery)
        # i=0
        # for word, word_data in summery.iteritems():
        #     for redu_length, occur in word_data.iteritems():
        #         i+= 1
        #         print word,redu_length, occur
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







