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
import random
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN
import json


from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.classes.reader import Reader
from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, LenGen, path_to_zas_rep_tools, get_number_of_streams_adjust_cpu
from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.basetester import BaseTester


import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama





class TestZAScorpusCorpus(BaseTester,unittest.TestCase):
    #_multiprocess_can_split_ = True
    _multiprocess_shared_  = True
    #@classmethod 
    def setUp(self):
        super(type(self), self).setUp()



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
    def test_initialization_of_the_corpus_instance_000(self):
        self.test_dbs()
        corp = Corpus(mode=self.mode)
        #p(self.db_blogger_plaintext_corp_en)
        corp.open(os.path.join(self.tempdir_testdbs, self.db_blogger_plaintext_corp_en))
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
        self.prj_folder()
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


        corp = Corpus(mode=self.mode)
        #corp = Corpus(logger_level=logging.DEBUG,mode=self.mode)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
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
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


        corp = Corpus(mode=self.mode)
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name, encryption_key=encryption_key, source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   
        assert corp.exist()
   
        
        

    @attr(status='stable')
    #@wipd
    def test_open_plaintext_blogger_corpus_502(self):
        #self.prj_folder()
        self.test_dbs()
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


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
  
    
        corp.corpdb.get_all_attr()['name'].should.be.equal(name)
        corp.corpdb.get_all_attr()['language'].should.be.equal(language)
        corp.corpdb.get_all_attr()['visibility'].should.be.equal(visibility)
        corp.corpdb.get_all_attr()['platform_name'].should.be.equal(platform_name)
        corp.corpdb.get_all_attr()['typ'].should.be.equal(typ)
        corp.corpdb.get_all_attr()['id'].should.be.equal(corpus_id)
        corp.corpdb.get_all_attr()['license'].should.be.equal(license)
        corp.corpdb.get_all_attr()['version'].should.be.equal(version)
        corp.corpdb.get_all_attr()['template_name'].should.be.equal(template_name)
        corp.corpdb.get_all_attr()['source'].should.be.equal(source)

        assert corp.exist()
   
    @attr(status='stable')
    #@wipd
    def test_open_encrypted_twitter_corpus_503(self):
        self.test_dbs()
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

        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_twitter_encrypted_corp_de), encryption_key=encryption_key)
    

        corp.corpdb.get_all_attr()['name'].should.be.equal(name)
        corp.corpdb.get_all_attr()['language'].should.be.equal(language)
        corp.corpdb.get_all_attr()['visibility'].should.be.equal(visibility)
        corp.corpdb.get_all_attr()['platform_name'].should.be.equal(platform_name)
        corp.corpdb.get_all_attr()['typ'].should.be.equal(typ)
        corp.corpdb.get_all_attr()['id'].should.be.equal(corpus_id)
        corp.corpdb.get_all_attr()['license'].should.be.equal(license)
        corp.corpdb.get_all_attr()['version'].should.be.equal(version)
        corp.corpdb.get_all_attr()['template_name'].should.be.equal(template_name)
        corp.corpdb.get_all_attr()['source'].should.be.equal(source)

        assert corp.exist()
   






###################    :550############################################ 
    @attr(status='stable')
    #@wipd
    def test_insert_without_preprocession_550(self):
        self.prj_folder()
        self.blogger_lists()
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


        corp = Corpus(mode=self.mode, preprocession=False)
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        #p(len(self.input_list_blogger_corpus_high_repetativ_subset))
        corp.insert(self.input_list_blogger_corpus_high_repetativ_subset)
        #p(list(corp.docs(output="dict")))
        #sys.exit()
        for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
            #del row_from_corp["id"]
            { unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})

        assert corp.total_error_insertion_during_last_insertion_process == 0

    @attr(status='stable')
    #@wipd
    def test_insert_with_preprocession_from_json_in_one_thread_on_twitter_example_551(self):
        self.prj_folder()
        self.twitter_corpus()
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
        language="en"
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True, mode=self.mode)
        corp = Corpus( preprocession=True,  sent_splitter="somajo", pos_tagger=True, language=language, logger_traceback=True, ext_tb=True, mode=self.mode, use_test_pos_tagger=True) #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
   

        corp.insert(reader.getlazy())
        inserted_rows_into_db = len(list(corp.corpdb.lazyget("documents")))
        corp.inserted_insertion_status_general
        #p((inserted_rows_into_db , corp.inserted_insertion_status_general))
        if inserted_rows_into_db != sum(corp.inserted_insertion_status_general.values()):
            assert False
        assert corp.total_error_insertion_during_last_insertion_process == 0




    @attr(status='stable')
    #@wipd
    def test_insert_with_preprocession_from_json_in_many_thread_on_twitter_example_552(self):
        self.prj_folder()
        self.twitter_corpus()
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
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True, mode=self.mode)
        corp = Corpus( sent_splitter="somajo", pos_tagger="someweta", language=language, logger_traceback=True, ext_tb=True, mode=self.mode, use_test_pos_tagger=True) #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        #p(reader.files_at_all_was_found)
        #corp.total_ignored_last_insertion
        corp.insert(reader.getlazy(stream_number=-1, min_files_pro_stream=7))
        inserted_rows_into_db = len(list(corp.corpdb.lazyget("documents")))
        #p(inserted_rows_into_db, "inserted_rows_into_db")
        if inserted_rows_into_db != sum(corp.inserted_insertion_status_general.values()):
            assert False

        if reader.files_at_all_was_found != (inserted_rows_into_db+corp.total_ignored_last_insertion):
            assert False

        assert corp.total_error_insertion_during_last_insertion_process == 0


    @attr(status='stable')
    #@wipd
    def test_preprocessing_on_example_of_blogger_corp_553(self):
        self.prj_folder()
        self.blogger_corpus()
        self.blogger_lists()
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
        #pos_tagger = False
        sentiment_analyzer = "textblob"
        lang_classification = True
        del_url = True
        del_punkt = True
        del_num = True
        del_html = True
        del_mention = True
        del_hashtag = True
        case_sensitiv = True
        typ= "corpus"
        language="de"
        diff_emoticons = True

        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode=self.mode)
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, #use_test_pos_tagger=True,
                sent_splitter=sent_splitter, pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer,
                language=language,lang_classification=lang_classification, del_url=del_url,
                del_punkt=del_punkt, del_num=del_num, del_mention=del_mention, diff_emoticons=diff_emoticons,
                del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,
                logger_traceback=True, status_bar=True,mode=self.mode,use_test_pos_tagger=False) #text_field_name=""
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        corp.insert(self.input_list_blogger_corpus_high_repetativ_subset)


        assert corp.total_inserted_during_last_insert == len(self.input_list_blogger_corpus_high_repetativ_subset)
        assert corp.total_error_insertion_during_last_insertion_process == 0
        assert corp.total_ignored_last_insertion == 0

        # check, if there rows was matched
        for row_from_corp, row_from_input in  zip(corp.docs(output="dict"),self.input_list_blogger_corpus_high_repetativ_subset):
            #p(row_from_corp, "row_from_corp")
            #p(row_from_input, "row_from_input")
            del row_from_corp["text"]
            del row_from_input["text"]
            {unicode(k):unicode(v) for k,v in row_from_input.iteritems()}.should.be.equal({unicode(k):unicode(v) for k,v in row_from_corp.iteritems()})


        # check if preprocessing was right
        for row_from_corp in  corp.docs(output="dict"):
            if row_from_corp["id"]==324114:
                #pass
                #p((row_from_corp["id"],324114))
                output_text =  u'[[[["-)))", "EMOASC"], ["-)", "EMOASC"], ["-P", "EMOASC"], ["Neeeeeeeeeeeeeeeeiiiiiiinnnnn", "NN"]], ["neutral", 0.0]], [[["Bitte", "PTKANT"], ["nicht", "PTKNEG"], ["\\ud83d\\ude02\\ud83d\\ude02\\ud83d\\ude02", "EMOIMG"], ["Test", "NN"], ["Version", "NN"], ["von", "APPR"], ["einem", "ART"], ["Tweeeeeeeeet", "NN"], ["=)))))))", "EMOASC"], ["noch", "ADV"], ["einen", "ART"], ["Tweeeeeeeeet", "NN"], ["=)))))))", "EMOASC"], ["\\ud83d\\ude05\\ud83d\\ude05", "EMOIMG"]], ["neutral", 0.0]]]'
                if row_from_corp["text"] != output_text:
                    p(row_from_corp["text"], "row_from_corp",c="r")
                    #p(output_text, "output_text",c="r")
                    assert False
            elif row_from_corp["id"]==416465:
                output_text = u'[[[["Einen", "ART"], ["weiteren", "ADJA"], ["Thread", "NN"], ["eingef\\u00fcgt", "VVPP"], ["ju", "NE"], ["Huuuuuuuu", "NE"], ["=)", "EMOASC"], ["\\ud83d\\udc9b\\ud83d\\udc9b\\ud83d\\udc9b", "EMOIMG"], ["den", "ART"], ["vierten", "ADJA"], ["Threadddddd", "NN"], ["wooooowwwwww", "NE"], ["\\u263a", "EMOIMG"], ["\\ufe0f", "$("], ["\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c", "EMOIMG"], ["Das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["Teeeeest", "NN"], ["Tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["positive", 0.7]], [[["Weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["Zeichen", "NN"], ["beinhalten", "VVINF"], ["sollte", "VMFIN"], ["\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c", "EMOIMG"], ["Das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["Teeeeest", "NN"], ["Tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["Weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["Zeichen", "NN"], ["\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c", "EMOIMG"], ["Das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["Teeeeest", "NN"], ["Quoted", "NE"], ["Tweet", "NN"], ["das", "PDS"], ["als", "APPR"], ["extended", "NN"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["Weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["Zeichen", "NN"], ["beinhalten", "VVINF"], ["sollte", "VMFIN"], ["\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c\\ud83d\\ude1c", "EMOIMG"], ["Das", "PDS"], ["ist", "VAFIN"], ["einnnneeeen", "ART"], ["Teeeeest", "NN"], ["Tweeeets", "NE"], ["das", "ART"], ["als", "APPR"], ["extended", "NE"], ["klassifiziert", "VVPP"], ["werden", "VAINF"], ["sollte", "VMFIN"]], ["neutral", 0.0]], [[["Weil", "KOUS"], ["es", "PPER"], ["bis", "APPR"], ["Zeichen", "NN"], ["\\ud83d\\ude1c\\ud83d\\ude1c", "EMOIMG"], ["h", "NN"]], ["neutral", 0.0]]]'
                if row_from_corp["text"] != output_text:
                    #pass
                    p(row_from_corp["text"], "row_from_corp",c="r")
                    #p((row_from_corp["text"], output_text))
                    assert False
            elif row_from_corp["id"]==322624:
                output_text = u'[[[["Eine", "ART"], ["Teeeeeest", "NN"], ["Diskussion", "NN"], ["wird", "VAFIN"], ["er\\u00f6ffnet", "VVPP"], ["-rep-tools", "NE"], ["Einen", "ART"], ["Test", "NN"], ["Retweet", "NN"], ["wird", "VAFIN"], ["gepostet", "VVPP"]], ["neutral", 0.0]], [[["Juhuuuuuu", "ITJ"], ["=)", "EMOASC"], ["\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00", "EMOIMG"], ["noooooooch", "ADV"], ["einen", "ART"], ["Tweeeeeeeeet", "NN"], ["=)))))))", "EMOASC"]], ["neutral", 0.0]]]'
                if row_from_corp["text"] != output_text:
                    #pass
                    p(row_from_corp["text"], "row_from_corp",c="r")
                    #p((row_from_corp["text"], output_text))
                    assert False




    @attr(status='stable')
    #@wipd
    def test_insert_one_thread_on_example_of_blogger_corp_554(self):
        self.prj_folder()
        self.blogger_corpus()
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
        sentiment_analyzer = False
        lang_classification = False
        del_url = True
        del_punkt = True
        del_num = True
        del_html = True
        del_mention = True
        del_hashtag = True
        case_sensitiv = True
        typ= "corpus"
        language="de"

        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode=self.mode)
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter,
        pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer,
        language=language,lang_classification=lang_classification, del_url=del_url,
        del_punkt=del_punkt, del_num=del_num, del_mention=del_mention, use_test_pos_tagger=True,
        del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,
        logger_traceback=True, status_bar=True,mode=self.mode)#, thread_safe=True) #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)


        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        corp.insert(reader.getlazy(stream_number=1, min_files_pro_stream=1))
        number_to_insert = len(reader.getlazy(stream_number=1, min_files_pro_stream=1))
        
        assert corp.total_inserted_during_last_insert == number_to_insert
        assert corp.total_error_insertion_during_last_insertion_process == 0
        assert corp.total_ignored_last_insertion == 0



    @attr(status='stable')
    #@wipd
    def test_insert_parallel_many_threads_on_example_of_blogger_corp_555(self):
        self.prj_folder()
        self.blogger_corpus()
        self.blogger_lists()
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
        pos_tagger = True
        sent_splitter = True
        sentiment_analyzer = True
        lang_classification = True
        del_url = True
        del_punkt = True
        del_num = True
        del_html = True
        del_mention = True
        del_hashtag = True
        case_sensitiv = True
        typ= "corpus"
        language="de"

        reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode=self.mode)
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter,
        pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer,
        language=language,lang_classification=lang_classification, del_url=del_url,
        del_punkt=del_punkt, del_num=del_num, del_mention=del_mention,
        del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,
        logger_traceback=True, status_bar=True,mode=self.mode,use_test_pos_tagger=True)#, thread_safe=True) #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
        corp.insert([self.input_list_blogger_corpus_high_repetativ_subset[:1],self.input_list_blogger_corpus_high_repetativ_subset[1:]])
        
        if corp.total_inserted_during_last_insert != len(self.input_list_blogger_corpus_high_repetativ_subset):
            assert False

        assert corp.total_inserted_during_last_insert == len(self.input_list_blogger_corpus_high_repetativ_subset)
        assert corp.total_error_insertion_during_last_insertion_process == 0
        assert corp.total_ignored_last_insertion == 0


    @attr(status='stable')
    #@wipd
    def test_insert_parallel_many_threads_on_example_of_twitter_corp_556(self):
        self.prj_folder()
        self.twitter_corpus()
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
        language="en"
        
        reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True, ext_tb=True,mode=self.mode)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter,
        pos_tagger=pos_tagger, language=language,del_url=del_url, del_punkt=del_punkt,use_test_pos_tagger=True,
        del_num=del_num, case_sensitiv=case_sensitiv,logger_traceback=True, status_bar=True,mode=self.mode) #text_field_name=""
        #corp = Corpus(logger_level=logging.DEBUG)
        corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)

        corp.insert(reader.getlazy())

        assert corp.total_error_insertion_during_last_insertion_process == 0







    #### DOCs Getter 600############
    

    @attr(status='stable')
    #@wipd
    def test_get_docs_single_600(self):
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
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
            
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True)["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))    

        columns = inp_dict.keys()
        rows = inp_dict.values()

        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")

        number_of_rows_in_db = corp.corpdb.rownum("documents")
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
        encryption_key = self.configer.init_info_data["blogger"]["encryption_key"]["corpus"]
        corpus_id = self.configer.init_info_data["blogger"]["id"]["corpus"]
        stats_id = self.configer.init_info_data["blogger"]["id"]["stats"]
        typ= "corpus"


        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
            
        inp_dict = self.configer.docs_row_dict( token=True, unicode_str=True, all_values=True,lang="en")["blogger"]
        num_of_insertions = len(random.choice(inp_dict.values()))    

        columns = inp_dict.keys()
        rows = inp_dict.values()

        id_index = self.configer.columns_in_doc_table["blogger"].index("id")
        text_index = self.configer.columns_in_doc_table["blogger"].index("text")


        number_of_rows = corp.corpdb.rownum("documents")
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





    #### Preprocessors 700############



    def _init_variables_for_preprocessing_test(self):
        ####################################
        ################ EN #################
        ####################################

        ### BYTE STRINGS ####
        ### Sent 1
        self.test_byte_str_en_1 = "I loved it. But it was verrrryyyyy vvveRRRRRRrry very piiiiiiiiity pity pity piiitttyyy for me...... :-(((((  @real_trump #sheetlife #readytogo http://www.absurd.com"

        ### Sent 2
        self.test_byte_str_en_2 = "a baddddd bad bbbbbbbaaaaaad bbbbaaaaddddd baaaaaaad news, which we can not accept. -(((( 😫😫😫😫 😫😫😫😫😫 😫😫😫 #sheetlife #sheetlife http://www.noooo.com" 


        ## UNICODE STRINGS ###
        ### Sent 1
        self.test_unicode_str_en_1 = self.test_byte_str_en_1.decode("utf-8")
        self.test_unicode_str_en_1_tokenized_not_cleaned_with_emoji_normalization = [([(u'I', u'regular'), (u'loved', u'regular'), (u'it', u'regular'), (u'.', u'symbol'), (u'But', u'regular'), (u'it', u'regular'), (u'was', u'regular'), (u'verrrryyyyy', u'regular'), (u'vvveRRRRRRrry', u'regular'), (u'very', u'regular'), (u'piiiiiiiiity', u'regular'), (u'pity', u'regular'), (u'pity', u'regular'), (u'piiitttyyy', u'regular'), (u'for', u'regular'), (u'me', u'regular'), (u'......', u'symbol'), (u':-(((((', 'EMOASC'), (u'@real_trump', u'mention'), (u'#sheetlife', u'hashtag'), (u'#readytogo', u'hashtag'), (u'http://www.absurd.com', u'URL')], (None, None))]
        self.test_unicode_str_en_1_tokenized_not_cleaned_without_emoji_normalization = [([(u'I', u'regular'), (u'loved', u'regular'), (u'it', u'regular'), (u'.', u'symbol'), (u'But', u'regular'), (u'it', u'regular'), (u'was', u'regular'), (u'verrrryyyyy', u'regular'), (u'vvveRRRRRRrry', u'regular'), (u'very', u'regular'), (u'piiiiiiiiity', u'regular'), (u'pity', u'regular'), (u'pity', u'regular'), (u'piiitttyyy', u'regular'), (u'for', u'regular'), (u'me', u'regular'), (u'......', u'symbol'), (u':-(((((', 'EMOASC'), (u'@real_trump', u'mention'), (u'#sheetlife', u'hashtag'), (u'#readytogo', u'hashtag'), (u'http://www.absurd.com', u'URL')], (None, None))]
        assert self.test_unicode_str_en_1_tokenized_not_cleaned_with_emoji_normalization == self.test_unicode_str_en_1_tokenized_not_cleaned_without_emoji_normalization
        self.test_unicode_str_en_1_tokenized_cleaned = [([(u'I', u'regular'), (u'loved', u'regular'), (u'it', u'regular'), (u'But', u'regular'), (u'it', u'regular'), (u'was', u'regular'), (u'verrrryyyyy', u'regular'), (u'vvveRRRRRRrry', u'regular'), (u'very', u'regular'), (u'piiiiiiiiity', u'regular'), (u'pity', u'regular'), (u'pity', u'regular'), (u'piiitttyyy', u'regular'), (u'for', u'regular'), (u'me', u'regular'), (u':-(((((', 'EMOASC')], (None, None))]
        
        ### Sent 2        
        self.test_unicode_str_en_2 = self.test_byte_str_en_2.decode("utf-8")
        self.test_unicode_str_en_2_tokenized_not_cleaned_with_emoji_normalization = [([(u'a', u'regular'), (u'baddddd', u'regular'), (u'bad', u'regular'), (u'bbbbbbbaaaaaad', u'regular'), (u'bbbbaaaaddddd', u'regular'), (u'baaaaaaad', u'regular'), (u'news', u'regular'), (u',', u'symbol'), (u'which', u'regular'), (u'we', u'regular'), (u'can', u'regular'), (u'not', u'regular'), (u'accept', u'regular'), (u'.', u'symbol'), (u'-((((', 'EMOASC'), (u'\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b', 'EMOIMG'), (u'#sheetlife', u'hashtag'), (u'#sheetlife', u'hashtag'), (u'http://www.noooo.com', u'URL')], (None, None))]
        self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization = [([(u'a', u'regular'), (u'baddddd', u'regular'), (u'bad', u'regular'), (u'bbbbbbbaaaaaad', u'regular'), (u'bbbbaaaaddddd', u'regular'), (u'baaaaaaad', u'regular'), (u'news', u'regular'), (u',', u'symbol'), (u'which', u'regular'), (u'we', u'regular'), (u'can', u'regular'), (u'not', u'regular'), (u'accept', u'regular'), (u'.', u'symbol'), (u'-((((', 'EMOASC'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'\U0001f62b', 'EMOIMG'), (u'#sheetlife', u'hashtag'), (u'#sheetlife', u'hashtag'), (u'http://www.noooo.com', u'URL')], (None, None))]
        assert self.test_unicode_str_en_2_tokenized_not_cleaned_with_emoji_normalization != self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization
        self.test_unicode_str_en_2_tokenized_cleaned = [([(u'a', u'regular'), (u'baddddd', u'regular'), (u'bad', u'regular'), (u'bbbbbbbaaaaaad', u'regular'), (u'bbbbaaaaddddd', u'regular'), (u'baaaaaaad', u'regular'), (u'news', u'regular'), (u'which', u'regular'), (u'we', u'regular'), (u'can', u'regular'), (u'not', u'regular'), (u'accept', u'regular'), (u'-((((', 'EMOASC'), (u'\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b', 'EMOIMG')], (None, None))]

        ####################################
        ####################################


        self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization 


        ####################################
        ################ DE #################
        ####################################

        ### BYTE STRINGS ####
        ### Sent 1
        self.test_byte_str_de_1 = "einen wunderschönen Taaaaaagggggg wünsche ich euch 😀😀😀😀😀🌈🌈🌈🌈🌈🌈🌈 Genieeeeeeeeeeesst das Leben. Bleeeeeeeeibt bleeeeibt Huuuuuuuuuuuungrig. "        

        ### Sent 2
        self.test_byte_str_de_2 = "eine klitzeeee kleine Sache.  Die aber trotzdem wichtiiiiiiiig isssssst! 11111 2222 33333 4444 55555"    


        ## UNICODE STRINGS ###
        ### Sent 1
        self.test_unicode_str_de_1 = self.test_byte_str_de_1.decode("utf-8")
        self.test_unicode_str_de_1_tokenized_not_cleaned_with_emoji_normalization = [([(u'einen', u'regular'), (u'wundersch\xf6nen', u'regular'), (u'Taaaaaagggggg', u'regular'), (u'w\xfcnsche', u'regular'), (u'ich', u'regular'), (u'euch', u'regular'), (u'\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600', 'EMOIMG'), (u'\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308', 'EMOIMG'), (u'Genieeeeeeeeeeesst', u'regular'), (u'das', u'regular'), (u'Leben', u'regular'), (u'.', u'symbol'), (u'Bleeeeeeeeibt', u'regular'), (u'bleeeeibt', u'regular'), (u'Huuuuuuuuuuuungrig', u'regular'), (u'.', u'symbol')], (None, None))]
        self.test_unicode_str_de_1_tokenized_not_cleaned_without_emoji_normalization = [([(u'einen', u'regular'), (u'wundersch\xf6nen', u'regular'), (u'Taaaaaagggggg', u'regular'), (u'w\xfcnsche', u'regular'), (u'ich', u'regular'), (u'euch', u'regular'), (u'\U0001f600', 'EMOIMG'), (u'\U0001f600', 'EMOIMG'), (u'\U0001f600', 'EMOIMG'), (u'\U0001f600', 'EMOIMG'), (u'\U0001f600', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'\U0001f308', 'EMOIMG'), (u'Genieeeeeeeeeeesst', u'regular'), (u'das', u'regular'), (u'Leben', u'regular'), (u'.', u'symbol'), (u'Bleeeeeeeeibt', u'regular'), (u'bleeeeibt', u'regular'), (u'Huuuuuuuuuuuungrig', u'regular'), (u'.', u'symbol')], (None, None))]
        self.test_unicode_str_de_1_tokenized_cleaned =  [([(u'einen', u'regular'), (u'wundersch\xf6nen', u'regular'), (u'Taaaaaagggggg', u'regular'), (u'w\xfcnsche', u'regular'), (u'ich', u'regular'), (u'euch', u'regular'), (u'\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600', 'EMOIMG'), (u'\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308', 'EMOIMG'), (u'Genieeeeeeeeeeesst', u'regular'), (u'das', u'regular'), (u'Leben', u'regular'), (u'Bleeeeeeeeibt', u'regular'), (u'bleeeeibt', u'regular'), (u'Huuuuuuuuuuuungrig', u'regular')], (None, None))]
        

        ### Sent 2
        self.test_unicode_str_de_2 = self.test_byte_str_de_2.decode("utf-8")
        self.test_unicode_str_de_2_tokenized_not_cleaned_with_emoji_normalization = [([(u'eine', u'regular'), (u'klitzeeee', u'regular'), (u'kleine', u'regular'), (u'Sache', u'regular'), (u'.', u'symbol'), (u'Die', u'regular'), (u'aber', u'regular'), (u'trotzdem', u'regular'), (u'wichtiiiiiiiig', u'regular'), (u'isssssst', u'regular'), (u'!', u'symbol'), (u'11111', u'number'), (u'2222', u'number'), (u'33333', u'number'), (u'4444', u'number'), (u'55555', u'number')], (None, None))]
        self.test_unicode_str_de_2_tokenized_not_cleaned_without_emoji_normalization = [([(u'eine', u'regular'), (u'klitzeeee', u'regular'), (u'kleine', u'regular'), (u'Sache', u'regular'), (u'.', u'symbol'), (u'Die', u'regular'), (u'aber', u'regular'), (u'trotzdem', u'regular'), (u'wichtiiiiiiiig', u'regular'), (u'isssssst', u'regular'), (u'!', u'symbol'), (u'11111', u'number'), (u'2222', u'number'), (u'33333', u'number'), (u'4444', u'number'), (u'55555', u'number')], (None, None))]
        self.test_unicode_str_de_2_tokenized_cleaned = [([(u'eine', u'regular'), (u'klitzeeee', u'regular'), (u'kleine', u'regular'), (u'Sache', u'regular'), (u'Die', u'regular'), (u'aber', u'regular'), (u'trotzdem', u'regular'), (u'wichtiiiiiiiig', u'regular'), (u'isssssst', u'regular')], (None, None))]
        

        ####################################
        ####################################




    def _get_test_corp(self, preprocession=False,tokenizer=False, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", status_bar=False, mode="test", init=False, clean=True, emojis_normalization=True, use_test_pos_tagger=True):
        #self._init_variables_for_preprocessing_test()

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
        preprocession = preprocession
        tokenizer = tokenizer
        pos_tagger = pos_tagger
        sent_splitter = sent_splitter
        sentiment_analyzer = sentiment_analyzer
        lang_classification = lang_classification
        status_bar= status_bar
        if clean:
            del_url = True
            del_punkt = True
            del_num = True
            del_html = True
            del_mention = True
            del_hashtag = True
        else:
            del_url = False
            del_punkt = False
            del_num = False
            del_html = False
            del_mention = False
            del_hashtag = False

        case_sensitiv = True


        typ= "corpus"
        language=lang

        #reader = Reader(os.path.join(self.tempdir_blogger_corp, self.txt_blogger_small_fake_set), "txt", regex_template="blogger", mode=self.mode)
        #reader = Reader(os.path.join(self.tempdir_twitter_corp, self.json_twitter_set), "json", formatter_name="twitter",logger_traceback=True)
        corp = Corpus(preprocession=preprocession,tokenizer=tokenizer, sent_splitter=sent_splitter,
        pos_tagger=pos_tagger,sentiment_analyzer=sentiment_analyzer, use_test_pos_tagger=use_test_pos_tagger,
        language=language,lang_classification=lang_classification, del_url=del_url,
        del_punkt=del_punkt, del_num=del_num, del_mention=del_mention, 
        del_hashtag=del_hashtag, del_html=del_html, case_sensitiv=case_sensitiv,
        logger_traceback=True, status_bar=status_bar,mode=mode, emojis_normalization=emojis_normalization)#, thread_safe=True) #text_field_name=""
        

        

        if not init:
            return corp
        else:
            corp.init(self.tempdir_project_folder, name, language, visibility, platform_name,  source=source, license=license, template_name=template_name,  version= version, corpus_id=corpus_id)
            #if status_bar:
                
            return corp






    def _check_sents_structure(self, sents):
        for sent_container in sents:

            # Check 1: If sent_container contain from 2 Elements
            try:
                ### Check 
                sent_container[0] # sent
                sent_container[1] # Place for Sentiment
                assert True
            except KeyError:
                assert False


            # Check 1.1: If sentiment contain from 2 Elements
                try:
                    ### Check 
                    sent_container[1][0] # sent
                    sent_container[1][1] # Place for Sentiment
                    assert True
                except KeyError:
                    assert False
                assert len(sent_container[1]) == 2

            # Check 2: If token_container contains from 2 Elements
            for token_contaner in sent_container[0]:
                    try:
                        token_contaner[0]
                        token_contaner[1]
                    except KeyError:
                        assert False


    def _check_en_sentences(self, corp):
        ################FAKE SENTS########################
        sents = corp._preprocessing("Hey, what's up???. Wanna meet?")
        #p(len(sents))
        len(sents).should.be.equal(2)
        # sent = "glaaaaaaad ( to seeeeeeeee --- ...  you -)))) -:))"
        # p(sent, "1sent")
        # sents = corp._preprocessing(sent)
        # p(sents, "2sent")

        ################################################
        ################SENT 1#######################
        sents1 = corp._preprocessing(self.test_unicode_str_en_1)
        #p(len(sents1))
        len(sents1).should.be.equal(2)
        
        self._check_sents_structure(sents1)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
        #p(tokens_after_preprocessing, "tokens_after_preprocessing")
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_1.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


        ################################################
        ################SENT 2#######################
        sents2 = corp._preprocessing(self.test_unicode_str_en_2)
        #p(len(sents2))
        len(sents2).should.be.equal(1)

        self._check_sents_structure(sents2)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_2.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)



    def _check_de_sentences(self, corp):
        ################FAKE SENT########################
        sents = corp._preprocessing("Hey, Was geeeeht??. Wollennnn wa chatenn?")
        #p(len(sents))
        len(sents).should.be.equal(2)

        ################################################
        ################SENT 1#######################
        sents1 = corp._preprocessing(self.test_unicode_str_de_1)
        #p(len(sents1))
        len(sents1).should.be.equal(2)


        self._check_sents_structure(sents1)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_1.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


        ################################################
        ################SENT 2#######################
        sents2 = corp._preprocessing(self.test_unicode_str_de_2)
        #p(len(sents2))
        len(sents2).should.be.equal(2)

        self._check_sents_structure(sents2)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_2.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)





    def _check_en_sentence(self, corp):
        ################FAKE SENT########################
        sents = corp._preprocessing("Hey, what's up???. Wanna meet?")
        #p(len(sents))
        len(sents).should.be.equal(1)

        ################################################
        ################SENT 1#######################
        sents1 = corp._preprocessing(self.test_unicode_str_en_1)
        #p(len(sents1))
        len(sents1).should.be.equal(1)

        self._check_sents_structure(sents1)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_1.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


        ################################################
        ################SENT 2#######################
        sents2 = corp._preprocessing(self.test_unicode_str_en_2)
        #p(len(sents2))
        len(sents2).should.be.equal(1)

        self._check_sents_structure(sents2)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_2.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)



    def _check_de_sentence(self, corp):
        ################FAKE SENT########################
        sents = corp._preprocessing("Hey, Was geeeeht??. Wollennnn wa chatenn?")
        #p(len(sents))
        len(sents).should.be.equal(1)

        ################################################
        ################SENT 1#######################
        sents1 = corp._preprocessing(self.test_unicode_str_de_1)
        #p(len(sents1))
        len(sents1).should.be.equal(1)


        self._check_sents_structure(sents1)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_1.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


        ################################################
        ################SENT 2#######################
        sents2 = corp._preprocessing(self.test_unicode_str_de_2)
        #p(len(sents2))
        len(sents2).should.be.equal(1)

        self._check_sents_structure(sents2)

        # Check 3: If there the right text was preprocessed
        tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
        joined_sent_after_preproc = "".join(tokens_after_preprocessing)
        joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_2.split(" "))
        joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)









    @attr(status='stable')
    #@wipd
    def test_preprocessors_if_preproc_are_disabled_700(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        mode = self.mode
        corp = self._get_test_corp(preprocession=False,tokenizer=False, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", mode =mode )
        #corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()
        answer1["status"].should.be.equal(False)
        answer1["desc"].should.be.equal("PreprocessorsWasDisabled")



    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_disabled_tokenizer_701(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        mode = "silent"
        #corp._init_insertions_variables()
        try:
            corp = self._get_test_corp(preprocession=True,tokenizer=False, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en",mode=mode )
            answer1 = corp._init_preprocessors()
            assert False # because, if preproc are enabled and tokenizer is disabled, than it is not possible to preprocess
        except:
            assert True




    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_not_clean_with_emoji_normalization_702(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        ####################################################
        ############ EN ###################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", mode=mode, init=True, clean=False, emojis_normalization=True)

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        
        ###### Input in Byte  ######
        corp._preprocessing(self.test_byte_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_en_1), "corp._preprocessing(self.test_byte_str_en_1)")
        corp._preprocessing(self.test_byte_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_en_2), "corp._preprocessing(self.test_byte_str_en_2)")


        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_en_1), "corp._preprocessing(self.test_unicode_str_en_1)")
        corp._preprocessing(self.test_unicode_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_en_2), "corp._preprocessing(self.test_unicode_str_en_2)")


        ####################################################
        ############# DE ######################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="de", mode=mode, init=True, clean=False, emojis_normalization=True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        ######Input in Byte  ######
        corp._preprocessing(self.test_byte_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_de_1), "corp._preprocessing(self.test_byte_str_de_1)")
        corp._preprocessing(self.test_byte_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")

        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_de_1), "corp._preprocessing(self.test_unicode_str_de_1)")
        corp._preprocessing(self.test_unicode_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_not_cleaned_with_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_without_not_clean_without_emoji_normalization_703(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        ####################################################
        ############ EN ###################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", mode=mode, init=True, clean=False, emojis_normalization=False)

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        
        ######Input in Byte  ######
        corp._preprocessing(self.test_byte_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_en_1), "corp._preprocessing(self.test_byte_str_en_1)")
        corp._preprocessing(self.test_byte_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_en_2), "corp._preprocessing(self.test_byte_str_en_2)")


        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_en_1), "corp._preprocessing(self.test_unicode_str_en_1)")
        corp._preprocessing(self.test_unicode_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_en_2), "corp._preprocessing(self.test_unicode_str_en_2)")


        ####################################################
        ############# DE ######################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="de", mode=mode, init=True, clean=False, emojis_normalization=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        ######Input in Byte  ######
        corp._preprocessing(self.test_byte_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_de_1), "corp._preprocessing(self.test_byte_str_de_1)")
        corp._preprocessing(self.test_byte_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_byte_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")

        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_de_1), "corp._preprocessing(self.test_unicode_str_de_1)")
        corp._preprocessing(self.test_unicode_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_not_cleaned_without_emoji_normalization )
        # p(corp._preprocessing(self.test_unicode_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_with_clean_704(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        ####################################################
        ############ EN ###################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", mode=mode, init=True, clean=True)

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        
        ######Input in Byte  ######
        corp._preprocessing(self.test_byte_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_cleaned )
        # p(corp._preprocessing(self.test_byte_str_en_1), "corp._preprocessing(self.test_byte_str_en_1)")
        corp._preprocessing(self.test_byte_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_cleaned )
        # p(corp._preprocessing(self.test_byte_str_en_2), "corp._preprocessing(self.test_byte_str_en_2)")


        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_en_1).should.be.equal(self.test_unicode_str_en_1_tokenized_cleaned )
        # p(corp._preprocessing(self.test_unicode_str_en_1), "corp._preprocessing(self.test_unicode_str_en_1)")
        corp._preprocessing(self.test_unicode_str_en_2).should.be.equal(self.test_unicode_str_en_2_tokenized_cleaned )
        # p(corp._preprocessing(self.test_unicode_str_en_2), "corp._preprocessing(self.test_unicode_str_en_2)")


        ####################################################
        ############# DE ######################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="de", mode=mode, init=True, clean=True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        ######Input in Byte  ######
        corp._preprocessing(self.test_byte_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_cleaned )
        # p(corp._preprocessing(self.test_byte_str_de_1), "corp._preprocessing(self.test_byte_str_de_1)")
        corp._preprocessing(self.test_byte_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_cleaned )
        # p(corp._preprocessing(self.test_byte_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")

        ###### Input in  UNICODE ######
        corp._preprocessing(self.test_unicode_str_de_1).should.be.equal(self.test_unicode_str_de_1_tokenized_cleaned )
        # p(corp._preprocessing(self.test_unicode_str_de_1), "corp._preprocessing(self.test_unicode_str_de_1)")
        corp._preprocessing(self.test_unicode_str_de_2).should.be.equal(self.test_unicode_str_de_2_tokenized_cleaned )
        # p(corp._preprocessing(self.test_unicode_str_de_2), "corp._preprocessing(self.test_byte_str_de_2)")







    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentimentanalysis_705(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=False, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)


        self._check_en_sentence(corp)

        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=False, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(1)

        self._check_de_sentence(corp)


    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_languageclassification_706(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)


        self._check_en_sentence(corp)

        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)

        self._check_de_sentence(corp)





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentimentanalysis_enabled_languageclassification_707(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)


        self._check_en_sentence(corp)

        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=False,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)

        self._check_de_sentence(corp)



    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_708(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=False, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)


        self._check_en_sentences(corp)

        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=False, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)

        self._check_de_sentences(corp)





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_language_classification_709(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)

        ################FAKE SENT########################
        sents = corp._preprocessing("Hey, what's up???. Wanna meet?")
        #p(len(sents))
        len(sents).should.be.equal(2)

        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=False,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)


        self._check_de_sentences(corp)





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_sentimentanalysis_710(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=False, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)

        ################FAKE SENT########################
        sents = corp._preprocessing("Hey, what's up???. Wanna meet?")
        #p(len(sents))
        len(sents).should.be.equal(2)

        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=False, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(2)


        self._check_de_sentences(corp)



    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_sentimentanalysis_enabled_language_classification_711(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)

        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################


        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=False,sentiment_analyzer=True,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)

        self._check_de_sentences(corp)





    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_postagger_712(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=False,
            lang_classification=False, lang="en", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()


        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)
        
        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################

        del corp
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=False,
            lang_classification=False, lang="de", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)

        self._check_de_sentences(corp)






    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_postagger_enabled_sentimentanalysis_713(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=True,
            lang_classification=False, lang="en", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()


        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)


        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################

        del corp
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=True,
            lang_classification=False, lang="de", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(3)

        self._check_de_sentences(corp)






    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_postagger_enabled_languagesclassification_714(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=False,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()


        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(4)


        self._check_en_sentences(corp)


        ####################################################
        ############ DE ###################
        ####################################################

        del corp
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=False,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(4)

        self._check_de_sentences(corp)







    @attr(status='stable')
    #@wipd
    def test_preprocessors_with_enabled_tokenizer_enabled_sentsplitter_enabled_postagger_enabled_sentimentanalysis_enabled_languagesclassification_715(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()

        ####################################################
        ############ EN ###################
        ####################################################

        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=True,
            lang_classification=True, lang="en", mode=mode, init=True, clean=False, status_bar = True, use_test_pos_tagger=True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()


        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(4)

        self._check_en_sentences(corp)

        ####################################################
        ############ DE ###################
        ####################################################

        del corp
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True,
            sent_splitter=True,pos_tagger=True,sentiment_analyzer=True,
            lang_classification=True, lang="de", mode=mode, init=True, clean=False, status_bar = True)
        #p(self.configer._docs_row_values(token=False, unicode_str=True, lang="en")["blogger"])


        corp._init_insertions_variables()
        corp.status_bars_manager =  corp._get_status_bars_manager()
        answer1 = corp._init_preprocessors()

        answer1["status"].should.be.equal(True)
        answer1["desc"].should.be.equal(4)

        self._check_de_sentences(corp)


    #### SentSplitter 730############
    @attr(status='stable')
    #@wipd
    def test_splitter_sentences_in_the_test_corps_730(self):
        #self.prj_folder()

        ##### DE #########
        self.test_dbs()
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))
        docs = list(corp.docs(output="list"))
        docs_dict = list(corp.docs(output="dict"))

        #p(docs, "DE_docs")
        len(docs).should.be.equal(5) # if not, than it means that test set was changed!!! Do human based validation fist!
        
        #p(docs_dict[0]) #{u'star_constellation': u'fish', u'text': u'[[[["Klitze", "NN"], ["kliiiitze", "VMFIN"], ["kleEEEEine", "NE"], ["kleinnne", "ADJA"], ["\\u00dcberaschung", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Trotzdem", "PAV"], ["hat", "VAFIN"], ["sie", "PPER"], ["mich", "PPER"], ["gl\\u00fccklich", "ADJD"], ["gemacht", "VVPP"], ["!", "symbol"], [":-))))", "EMOASC"], ["-)))", "EMOASC"]], ["positive", 0.5]]]', u'age': 23, u'working_area': u'Care', u'rowid': 8, u'gender': u'm', u'id': 8888}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'Klitze', u'kliiiitze', u'kleEEEEine', u'kleinnne', u'\xdcberaschung', u'.', u'Trotzdem', u'hat', u'sie', u'mich', u'gl\xfccklich', u'gemacht', u'!', u':-))))', u'-)))'])
        #p(len(json.loads(docs[0][2])))
        len(json.loads(docs[0][2])).should.be.equal(2)

        #p(docs_dict[1]) #{u'star_constellation': u'aquarius', u'text': u'[[[["einen", "ART"], ["wundersch\\u00f6nen", "ADJA"], ["Taaaaaagggggg", "NN"], ["w\\u00fcnsche", "VVFIN"], ["ich", "PPER"], ["euch", "PRF"], [".", "symbol"]], ["neutral", 0.0]], [[["Genieeeeeeeeeeesst", "NN"], ["geniiiiiiiiiiiiist", "VVFIN"], ["das", "ART"], ["Leben", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Bleeeeeeeeibt", "NN"], ["bleeeeibt", "VVFIN"], ["Huuuuuuuuuuuungrig", "NN"], [".", "symbol"], ["\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00", "EMOIMG"], ["\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08", "EMOIMG"]], ["neutral", 0.0]]]', u'age': 22, u'working_area': u'Finance', u'rowid': 9, u'gender': u'w', u'id': 9999}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'einen', u'wundersch\xf6nen', u'Taaaaaagggggg', u'w\xfcnsche', u'ich', u'euch', u'.', u'Genieeeeeeeeeeesst', u'geniiiiiiiiiiiiist', u'das', u'Leben', u'.', u'Bleeeeeeeeibt', u'bleeeeibt', u'Huuuuuuuuuuuungrig', u'.', u'\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600', u'\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308'])
        #p(len(json.loads(docs[1][2])))
        len(json.loads(docs[1][2])).should.be.equal(3)

        #p(docs_dict[2]) #{u'star_constellation': u'lion', u'text': u'[[[["eine", "ART"], ["klitzeeee", "VAPPER"], ["kleine", "ADJA"], ["\\u00dcberrrraschung", "NN"], ["@sch\\u00f6nesleben", "mention"], ["#machwasdaraus", "hashtag"], ["#bewegedeinArsch", "hashtag"], ["https://www.freiesinternet.de", "URL"]], ["neutral", 0.0]]]', u'age': 35, u'working_area': u'Air Industry', u'rowid': 10, u'gender': u'w', u'id': 10000}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'eine', u'klitzeeee', u'kleine', u'\xdcberrrraschung', u'@sch\xf6nesleben', u'#machwasdaraus', u'#bewegedeinArsch', u'https://www.freiesinternet.de'])
        #p(len(json.loads(docs[2][2])))
        len(json.loads(docs[2][2])).should.be.equal(1)

        #p(docs_dict[3]) # {u'star_constellation': u'crawfish', u'text': u'[[[["eine", "ART"], ["klitzeeee", "VAPPER"], ["kleine", "ADJA"], ["Sache", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Die", "PDS"], ["aber", "ADV"], ["trotzdem", "PAV"], ["wichtiiiiiiiig", "ADJA"], ["isssssst", "NN"], ["!", "symbol"], ["11111", "number"], ["2222", "number"], ["33333", "number"], ["4444", "number"], ["55555", "number"], ["6", "number"]], ["neutral", 0.0]]]', u'age': 21, u'working_area': u'Industry', u'rowid': 11, u'gender': u'm', u'id': 11111}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'eine', u'klitzeeee', u'kleine', u'Sache', u'.', u'Die', u'aber', u'trotzdem', u'wichtiiiiiiiig', u'isssssst', u'!', u'11111', u'2222', u'33333', u'4444', u'55555', u'6'])
        #p(len(json.loads(docs[3][2])))
        len(json.loads(docs[3][2])).should.be.equal(2)

        #p(docs_dict[4]) #{u'star_constellation': u'lion', u'text': u'[[[["Eine", "ART"], ["klitze", "NN"], ["klitze", "ADJD"], ["klitze", "PTKIFG"], ["klitze", "ADJD"], ["kleine", "ADJA"], ["\\u00dcberrrraschung", "NN"], [",", "symbol"], ["die", "PRELS"], ["ich", "PPER"], ["mal", "PTKMA"], ["gerne", "ADV"], ["hatte", "VAFIN"], [".", "symbol"]], ["neutral", 0.0]]]', u'age': 37, u'working_area': u'IT', u'rowid': 12, u'gender': u'w', u'id': 12222}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'Eine', u'klitze', u'klitze', u'klitze', u'klitze', u'kleine', u'\xdcberrrraschung', u',', u'die', u'ich', u'mal', u'gerne', u'hatte', u'.'])
        #p(len(json.loads(docs[4][2])))
        len(json.loads(docs[4][2])).should.be.equal(1)

        # for row in docs:
        #     for sent_container in json.loads(row[2]):
        #         print row[1], len(json.loads(row[2]))
        #         sent_str = [token_container[0] for token_container in sent_container[0]]
        #         print " ".join(sent_str)
        #         print "\n\n"



        ##### EN ########
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        docs = list(corp.docs(output="list"))
        docs_dict = list(corp.docs(output="dict"))

        len(docs).should.be.equal(7) # if not, than it means that test set was changed!!! Do human based validation fist!
        #p(docs, "EN_docs")

        #p(docs_dict[0]) #{u'star_constellation': u'lion', u'text': u'[[[["I", "PRP"], ["loved", "VBD"], ["it", "PRP"], [".", "symbol"]], ["positive", 0.7]], [[["But", "CC"], ["it", "PRP"], ["was", "VBD"], ["also", "RB"], ["verrrryyyyy", "JJ"], ["vvveRRRRRRrry", "NNP"], ["very", "RB"], ["piiiiiiiiity", "JJ"], ["pity", "NN"], ["pity", "NN"], ["piiitttyyy", "NN"], ["for", "IN"], ["me", "PRP"], ["......", "symbol"], [":-(((((", "EMOASC"], ["@real_trump", "mention"], ["#sheetlife", "hashtag"], ["#readytogo", "hashtag"], ["http://www.absurd.com", "URL"]], ["negative", -0.1875]]]', u'age': 37, u'working_area': u'IT', u'rowid': 1, u'gender': u'w', u'id': 1111}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'I', u'loved', u'it', u'.', u'But', u'it', u'was', u'also', u'verrrryyyyy', u'vvveRRRRRRrry', u'very', u'piiiiiiiiity', u'pity', u'pity', u'piiitttyyy', u'for', u'me', u'......', u':-(((((', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com'])
        #p(len(json.loads(docs[0][2])))
        len(json.loads(docs[0][2])).should.be.equal(2)

        #p(docs_dict[1]) #{u'star_constellation': u'fish', u'text': u'[[[["glaaaaaaad", "NN"], ["to", "TO"], ["seeeeeeeee", "VB"], ["you", "PRP"], ["-", "symbol"], ["))))", "\'\'"]], ["neutral", 0.0]]]', u'age': 23, u'working_area': u'Care', u'rowid': 2, u'gender': u'm', u'id': 2222}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'glaaaaaaad', u'to', u'seeeeeeeee', u'you', u'-))))'])
        #p(len(json.loads(docs[1][2])))
        len(json.loads(docs[1][2])).should.be.equal(1)

        #p(docs_dict[2]) #{u'star_constellation': u'aquarius', u'text': u'[[[["a", "DT"], ["baddddd", "JJ"], ["bad", "JJ"], ["bbbbbbbaaaaaa", "NNS"], ["bbbbaaaaddddd", "VBD"], ["baaaaaaad", "JJ"], ["news", "NN"], [",", "symbol"], ["which", "WDT"], ["we", "PRP"], ["can", "MD"], ["not", "RB"], ["accept", "VB"], [".", "symbol"], ["-", "symbol"], ["((((", "NN"], ["\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b", "EMOIMG"], ["#sheetlife", "hashtag"], ["#sheetlife", "hashtag"], ["http://www.noooo.com", "URL"]], ["negative", -0.6999999999999998]]]', u'age': 22, u'working_area': u'Finance', u'rowid': 3, u'gender': u'w', u'id': 3333}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'a', u'baddddd', u'bad', u'bbbbbbbaaaaaad', u'bbbbaaaaddddd', u'baaaaaaad', u'news', u',', u'which', u'we', u'can', u'not', u'accept', u'.', u'-((((', u'\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b\U0001f62b', u'#sheetlife', u'#sheetlife', u'http://www.noooo.com'])
        #p(len(json.loads(docs[2][2])))
        len(json.loads(docs[2][2])).should.be.equal(1)

        #p(docs_dict[3]) #{u'star_constellation': u'gemini', u'text': u'[[[["Tiny", "JJ"], ["tiny", "JJ"], ["tiny", "JJ"], ["tiny", "JJ"], ["tiqny", "JJ"], ["tiny", "JJ"], ["mooooooodelllllll", "NN"], [",", "symbol"], ["which", "WDT"], ["we", "PRP"], ["can", "MD"], ["use", "VB"], ["for", "IN"], ["explain", "VB"], ["a", "DT"], ["biiig", "NN"], ["biiiiiiiiiiiiiiig", "NN"], ["things", "NNS"], [".", "symbol"]], ["neutral", 0.0]]]', u'age': 27, u'working_area': u'IT', u'rowid': 4, u'gender': u'm', u'id': 4444}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'Tiny', u'tiny', u'tiny', u'tiny', u'tiny', u'tiny', u'mooooooodelllllll', u',', u'which', u'we', u'can', u'use', u'for', u'explain', u'a', u'biiig', u'biiiiiiiiiiiiiiig', u'things', u'.'])
        #p(len(json.loads(docs[3][2])))
        len(json.loads(docs[3][2])).should.be.equal(1)

        #p(docs_dict[4]) # {u'star_constellation': u'lion', u'text': u'[[[["Tiny", "JJ"], ["model", "NN"], [",", "symbol"], ["but", "CC"], ["a", "DT"], ["big", "JJ"], ["big", "JJ"], ["big", "JJ"], ["explaaaaanation", "NN"], [".", "symbol"]], ["neutral", 0.0]], [[["Riiiiiight", "UH"], ["?", "symbol"]], ["neutral", 0.0]], [[["What", "WP"], ["do", "VBP"], ["youuuuuu", "PRP"], ["think", "VB"], ["about", "IN"], ["it", "PRP"], ["????", "symbol"]], ["neutral", 0.0]]]', u'age': 35, u'working_area': u'Air Industry', u'rowid': 5, u'gender': u'w', u'id': 5555}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'Tiny', u'model', u',', u'but', u'a', u'big', u'big', u'big', u'explaaaaanation', u'.', u'Riiiiiight', u'?', u'What', u'do', u'youuuuuu', u'think', u'about', u'it', u'????'])
        #p(len(json.loads(docs[4][2])))
        len(json.loads(docs[4][2])).should.be.equal(3)

        #p(docs_dict[5]) # {u'star_constellation': u'crawfish', u'text': u'[[[["tinnnyy", "JJ"], ["tiny", "JJ"], ["tiny", "JJ"], ["surprise", "NN"]], ["neutral", 0.0]]]', u'age': 21, u'working_area': u'Industry', u'rowid': 6, u'gender': u'm', u'id': 6666}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[5][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[5][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'tinnnyy', u'tiny', u'tiny', u'surprise'])
        #p(len(json.loads(docs[5][2])))
        len(json.loads(docs[5][2])).should.be.equal(1)

        #p(docs_dict[6]) #{u'star_constellation': u'lion', u'text': u'[[[["it", "PRP"], ["was", "VBD"], ["really", "RB"], ["bad", "JJ"], ["surprise", "NN"], ["for", "IN"], ["me", "PRP"], ["\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b\\ud83d\\ude2b", "EMOIMG"], [",", "symbol"], ["buuuuuuuuuut", "MD"], ["i", "PRP"], ["really", "RB"], ["reallly", "VBD"], ["reeeeeallllyyy", "PRP"], ["liked", "VBD"], ["it", "PRP"], ["=))))))))))", "EMOASC"], [":P", "EMOASC"], ["\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00\\ud83d\\ude00", "EMOIMG"], ["\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08\\ud83c\\udf08", "EMOIMG"], ["\\ud83d\\ude00", "EMOIMG"]], ["positive", 0.27]]]', u'age': 37, u'working_area': u'IT', u'rowid': 7, u'gender': u'w', u'id': 7777}
        #p([tokencontainer[0] for sentcontainer in json.loads(docs[6][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[0] for sentcontainer in json.loads(docs[6][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'it', u'was', u'really', u'bad', u'surprise', u'for', u'me', u'\U0001f62b\U0001f62b\U0001f62b\U0001f62b', u',', u'buuuuuuuuuut', u'i', u'really', u'reallly', u'reeeeeallllyyy', u'liked', u'it', u'=))))))))))', u':P', u'\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600', u'\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308', u'\U0001f600'])
        #p(len(json.loads(docs[6][2])))
        len(json.loads(docs[6][2])).should.be.equal(1)







    #### SentSplitter ############
    @attr(status='stable')
    #@wipd
    def test_check_results_of_pos_tagging_with_someweta_in_the_test_corps_731(self):
        #self.prj_folder()

        ##### DE #########
        self.test_dbs()
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_de))
        docs = list(corp.docs(output="list"))
        docs_dict = list(corp.docs(output="dict"))

        #p(docs, "DE_docs")
        len(docs).should.be.equal(5) # if not, than it means that test set was changed!!! Do human based validation fist!
        
        # p(docs_dict[0])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'NN', u'VMFIN', u'NE', u'ADJA', u'NN', u'symbol', u'PAV', u'VAFIN', u'PPER', u'PPER', u'ADJD', u'VVPP', u'symbol', u'EMOASC', u'EMOASC'])
        #p(len(json.loads(docs[0][2])))
        len(json.loads(docs[0][2])).should.be.equal(2)

        #p(docs_dict[1]) 
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'ART', u'ADJA', u'NN', u'VVFIN', u'PPER', u'PRF', u'symbol', u'NN', u'VVFIN', u'ART', u'NN', u'symbol', u'NN', u'VVFIN', u'NN', u'symbol', u'EMOIMG', u'EMOIMG'])
        #p(len(json.loads(docs[1][2])))
        len(json.loads(docs[1][2])).should.be.equal(3)

        #p(docs_dict[2])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'ART', u'VAPPER', u'ADJA', u'NN', u'mention', u'hashtag', u'hashtag', u'URL'])
        #p(len(json.loads(docs[2][2])))
        len(json.loads(docs[2][2])).should.be.equal(1)

        #p(docs_dict[3]) 
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'ART', u'VAPPER', u'ADJA', u'NN', u'symbol', u'PDS', u'ADV', u'PAV', u'ADJA', u'NN', u'symbol', u'number', u'number', u'number', u'number', u'number', u'number'])
        #p(len(json.loads(docs[3][2])))
        len(json.loads(docs[3][2])).should.be.equal(2)

        #p(docs_dict[4])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'ART', u'NN', u'ADJD', u'PTKIFG', u'ADJD', u'ADJA', u'NN', u'symbol', u'PRELS', u'PPER', u'PTKMA', u'ADV', u'VAFIN', u'symbol'])
        #p(len(json.loads(docs[4][2])))
        len(json.loads(docs[4][2])).should.be.equal(1)



        # ##### EN ########
        corp = Corpus(mode=self.mode)
        corp.open(os.path.join(self.tempdir_testdbs,self.db_blogger_plaintext_corp_en))
        docs = list(corp.docs(output="list"))
        docs_dict = list(corp.docs(output="dict"))
        #p(len(docs), "len(docs)")
        len(docs).should.be.equal(7) # if not, than it means that test set was changed!!! Do human based validation fist!
        #p(docs, "EN_docs")

        # p(docs_dict[0]) 
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[0][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'PRP', u'VBD', u'PRP', u'symbol', u'CC', u'PRP', u'VBD', u'RB', u'JJ', u'NNP', u'RB', u'JJ', u'NN', u'NN', u'NN', u'IN', u'PRP', u'symbol', u'EMOASC', u'mention', u'hashtag', u'hashtag', u'URL'])
        #p(len(json.loads(docs[0][2])))
        len(json.loads(docs[0][2])).should.be.equal(2)

        #p(docs_dict[1])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[1][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'NN', u'TO', u'VB', u'PRP', u'EMOASC'])
        #p(len(json.loads(docs[1][2])))
        len(json.loads(docs[1][2])).should.be.equal(1)

        #p(docs_dict[2])
        #p([tokencontainer[1] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[2][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'DT', u'JJ', u'JJ', u'NNS', u'IN', u'JJ', u'NN', u'symbol', u'WDT', u'PRP', u'MD', u'RB', u'VB', u'symbol', u'EMOASC', u'EMOIMG', u'hashtag', u'hashtag', u'URL'])
        #p(len(json.loads(docs[2][2])))
        len(json.loads(docs[2][2])).should.be.equal(1)

        # p(docs_dict[3]) 
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[3][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'JJ', u'JJ', u'JJ', u'JJ', u'JJ', u'JJ', u'NN', u'symbol', u'WDT', u'PRP', u'MD', u'VB', u'IN', u'VB', u'DT', u'NN', u'NN', u'NNS', u'symbol'])
        #p(len(json.loads(docs[3][2])))
        len(json.loads(docs[3][2])).should.be.equal(1)

        # p(docs_dict[4]) 
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[4][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'JJ', u'NN', u'symbol', u'CC', u'DT', u'JJ', u'JJ', u'JJ', u'NN', u'symbol', u'UH', u'symbol', u'WP', u'VBP', u'PRP', u'VB', u'IN', u'PRP', u'symbol'])
        #p(len(json.loads(docs[4][2])))
        len(json.loads(docs[4][2])).should.be.equal(3)

        # p(docs_dict[5])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[5][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[5][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'JJ', u'JJ', u'JJ', u'NN'])
        #p(len(json.loads(docs[5][2])))
        len(json.loads(docs[5][2])).should.be.equal(1)

        # p(docs_dict[6])
        # p([tokencontainer[1] for sentcontainer in json.loads(docs[6][2]) for tokencontainer in sentcontainer[0]])
        [tokencontainer[1] for sentcontainer in json.loads(docs[6][2]) for tokencontainer in sentcontainer[0]].should.be.equal([u'PRP', u'VBD', u'RB', u'JJ', u'NN', u'IN', u'PRP', u'EMOIMG', u'symbol', u'MD', u'PRP', u'RB', u'VBD', u'PRP', u'VBD', u'PRP', u'EMOASC', u'EMOASC', u'EMOIMG', u'EMOIMG', u'EMOIMG'])
        #p(len(json.loads(docs[6][2])))
        len(json.loads(docs[6][2])).should.be.equal(1)



    #### Emoji Normalization 800############


    @attr(status='stable')
    #@wipd
    def test_emoji_normalization_800(self):
        self.prj_folder()
        self._init_variables_for_preprocessing_test()
        ####################################################
        ############ EN ###################
        ####################################################
        mode = self.mode
        corp = self._get_test_corp(preprocession=True,tokenizer=True, sent_splitter=False,pos_tagger=False,sentiment_analyzer=False,lang_classification=False, lang="en", mode=mode, init=True, clean=False, emojis_normalization=True)

        corp._init_insertions_variables()
        answer1 = corp._init_preprocessors()


        corp._normalize_emojis(self.test_unicode_str_en_1_tokenized_not_cleaned_without_emoji_normalization[0][0]).should.be.equal(self.test_unicode_str_en_1_tokenized_not_cleaned_with_emoji_normalization[0][0])
        corp._normalize_emojis(self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization[0][0]).should.be.equal(self.test_unicode_str_en_2_tokenized_not_cleaned_with_emoji_normalization[0][0])
        #p(corp._normalize_emojis(self.test_unicode_str_en_2_tokenized_not_cleaned_without_emoji_normalization))
        corp._normalize_emojis(self.test_unicode_str_de_1_tokenized_not_cleaned_without_emoji_normalization[0][0]).should.be.equal(self.test_unicode_str_de_1_tokenized_not_cleaned_with_emoji_normalization[0][0])
        corp._normalize_emojis(self.test_unicode_str_de_2_tokenized_not_cleaned_without_emoji_normalization[0][0]).should.be.equal(self.test_unicode_str_de_2_tokenized_not_cleaned_with_emoji_normalization[0][0])

        inp = [(u'\U0001f600', u'emoticon'), (u'\U0001f600', u'emoticon'), (u'\U0001f600', u'emoticon'), (u'\U0001f600', u'emoticon'), (u'\U0001f600', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon'), (u'\U0001f308', u'emoticon')]
        outp = [(u'\U0001f600\U0001f600\U0001f600\U0001f600\U0001f600', u'emoticon'), (u'\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308\U0001f308', u'emoticon') ]       
        corp._normalize_emojis(inp).should.be.equal(outp)


#################################END##################################################
############################EXTERN METHODS############################################
######################################################################################







####################################################################################################
####################################################################################################
###################### STOP STABLE TESTS #########################################################
####################################################################################################
####################################################################################################








    # def _check_en_sentences(self, corp):
    #     ################FAKE SENT########################
    #     sents = corp._preprocessing("Hey, what's up???. Wanna meet?")
    #     #p(len(sents))
    #     len(sents).should.be.equal(2)

    #     ################################################
    #     ################SENT 1#######################
    #     sents1 = corp._preprocessing(self.test_unicode_str_en_1)
    #     #p(len(sents1))
    #     len(sents1).should.be.equal(2)

    #     self._check_sents_structure(sents1)

    #     # Check 3: If there the right text was preprocessed
    #     tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
    #     joined_sent_after_preproc = "".join(tokens_after_preprocessing)
    #     joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_1.split(" "))
    #     joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


    #     ################################################
    #     ################SENT 2#######################
    #     sents2 = corp._preprocessing(self.test_unicode_str_en_2)
    #     #p(len(sents2))
    #     len(sents2).should.be.equal(1)

    #     self._check_sents_structure(sents2)

    #     # Check 3: If there the right text was preprocessed
    #     tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
    #     joined_sent_after_preproc = "".join(tokens_after_preprocessing)
    #     joined_sent_bevore_preproc = "".join(self.test_unicode_str_en_2.split(" "))
    #     joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)



    # def _check_de_sentences(self, corp):
    #     ################FAKE SENT########################
    #     sents = corp._preprocessing("Hey, Was geeeeht??. Wollennnn wa chatenn?")
    #     #p(len(sents))
    #     len(sents).should.be.equal(2)

    #     ################################################
    #     ################SENT 1#######################
    #     sents1 = corp._preprocessing(self.test_unicode_str_de_1)
    #     #p(len(sents1))
    #     len(sents1).should.be.equal(2)


    #     self._check_sents_structure(sents1)

    #     # Check 3: If there the right text was preprocessed
    #     tokens_after_preprocessing = [token_contaner[0] for sent_container in sents1 for token_contaner in sent_container[0]]
    #     joined_sent_after_preproc = "".join(tokens_after_preprocessing)
    #     joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_1.split(" "))
    #     joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)


    #     ################################################
    #     ################SENT 2#######################
    #     sents2 = corp._preprocessing(self.test_unicode_str_de_2)
    #     #p(len(sents2))
    #     len(sents2).should.be.equal(2)

    #     self._check_sents_structure(sents2)

    #     # Check 3: If there the right text was preprocessed
    #     tokens_after_preprocessing = [token_contaner[0] for sent_container in sents2 for token_contaner in sent_container[0]]
    #     joined_sent_after_preproc = "".join(tokens_after_preprocessing)
    #     joined_sent_bevore_preproc = "".join(self.test_unicode_str_de_2.split(" "))
    #     joined_sent_after_preproc.should.be.equal(joined_sent_bevore_preproc)





















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







