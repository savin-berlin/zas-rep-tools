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
from collections import defaultdict
from nose.plugins.attrib import attr
from testfixtures import tempdir, TempDirectory
from distutils.dir_util import copy_tree 
#import glob
import json
import time

from zas_rep_tools.src.classes.configer import Configer
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.reader import Reader




from zas_rep_tools.src.utils.debugger import p, wipd, wipdn, wipdl, wipdo
from zas_rep_tools.src.utils.logger import *
from zas_rep_tools.src.utils.helpers import NestedDictValues



import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama

# create test data, id needed

#Configer(mode="dev", rewrite=True).create_test_data(use_original_classes=True, corp_status_bar=True, corp_log_ignored=True, corp_language="en", corp_lang_classification=False, corp_pos_tagger="tweetnlp")

class TestZASconfigerConfiger(unittest.TestCase):
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


    def _get_meta_data_by_db_file_name(self, db_fname_to_search):

        for encryption, encryption_data in self.configer.test_dbs.iteritems():
            for template_name, template_name_data in encryption_data.iteritems():
                for language, language_data in template_name_data.iteritems():
                    for db_type, db_fname in language_data.iteritems():
                        #p((db_fname_to_search,db_fname))
                            if db_fname_to_search == db_fname:
                                return (encryption, template_name, language,db_type)
        return (None,None,None,None)


    ##### xx :0== ######

    @attr(status='stable')
    #@wipd
    def test_init_configer_000(self):
        configer = Configer(mode="test")




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
   
    #@attr(status='stable')
    #@wipd
    def test_create_all_test_dbs_5(self):
        c = Configer(mode="dev", rewrite=True)
        #p(c.text_elements(token=True, unicode_str=True))
        #c.create_test_dbs(use_original_classes=True, corp_status_bar=True, corp_log_ignored=True,corp_lang_classification=True)
        p(c._docs_row_dict(token=True, unicode_str=True, all_values=True , lang="all") )
        # p("fghjl")
        # time.sleep(2)
        # p("fghjl")
        # p("fghjl")
        # time.sleep(2)
        # p("fghjl")
        # p("fghjl")
        # p("fghjl")
        # time.sleep(2)
        # p("fghjl")
        # p("fghjl")
        # p("fghjl")
        # time.sleep(2)
        # p("fghjl")
        #c.create_test_dbs(abs_path_to_storage_place=self.tempdir_project_folder, use_original_classes=True, corp_status_bar=True, corp_log_ignored=True, corp_language="en", corp_lang_classification=False, corp_pos_tagger="tweetnlp")
        #p(Configer(mode="test").self.docs_row_values(token=True, unicode_str=True))

    @attr(status='stable')
    #@wipd
    def test_create_all_test_dbs_created_with_dbhandler_500(self):
        #abs_path_to_storage_place=os.path.join(self.path_to_zas_rep_tools, self.path_to_testdbs)
        abs_path_to_storage_place=self.tempdir_project_folder
        configer = Configer(mode="test", rewrite=True)
         
        configer.create_test_dbs(rewrite=True, abs_path_to_storage_place=abs_path_to_storage_place, use_original_classes=False)
        #configer.create_test_dbs(rewrite=False, abs_path_to_storage_place=self.path_to_zas_rep_tools)

        created_dbs = [filename for filename in os.listdir(abs_path_to_storage_place) if ".db" in filename]
        #number_db_which_should_be_created = len(self.configer.init_info_data) * len(["corpus","stats"]) * len(["plaintext", "encrypted"])
        number_db_which_should_be_created = len(list(NestedDictValues(self.configer._test_dbs)))
        #p((created_dbs,number_db_which_should_be_created ))
        #p(number_db_which_should_be_created, "number_db_which_should_be_created")
        #sys.exit()
        #p((len(created_dbs), number_db_which_should_be_created))
        if len(created_dbs) != number_db_which_should_be_created:
            assert False

        for db_name in created_dbs:
            #p(db_name)
            encryption, template_name, language, db_type= self._get_meta_data_by_db_file_name(db_name)
            #p((encryption, template_name, language, db_type))
            #sys.exit()
            #p(encryption)
            if not encryption:
                assert False

            db = DBHandler(mode="test")
            if encryption == "encrypted":
                encryption_key=self.configer.init_info_data[template_name]["encryption_key"][db_type]
                db.connect(os.path.join(abs_path_to_storage_place,db_name), encryption_key=encryption_key)
            else:
                db.connect(os.path.join(abs_path_to_storage_place,db_name))

            if db_type == "corpus":
                for item1, item2 in zip(self.configer.docs_row_values(token=True, unicode_str=True, lang="all")[template_name], db.getall("documents")):
                    for i1,i2 in zip(item1, item2):
                        if isinstance(i1, (list,tuple,dict)):
                            #p(i1)
                            i1 = json.dumps(i1)
                            #continue
                        if  i1 == False :
                            i1=0
                        if  i1 == True :
                            i1=1
                        if unicode(i1) != unicode(i2):
                            p((unicode(i1) , unicode(i2)))
                            assert False
            elif db_type == "stats":
                ### Here for stats
                pass

    def _unidiff_output(self,expected, actual):
        """
        Helper function. Returns a string containing the unified diff of two multiline strings.
        """

        import difflib
        expected=expected.splitlines(1)
        actual=actual.splitlines(1)

        diff=difflib.unified_diff(expected, actual)

        return ''.join(diff)

    @attr(status='stable')
    #@wipd
    def test_create_all_test_dbs_created_with_corpus_and_stats_classes_501(self):
        #abs_path_to_storage_place=os.path.join(self.path_to_zas_rep_tools, self.path_to_testdbs)
        abs_path_to_storage_place=self.tempdir_project_folder

        configer = Configer(mode="test", rewrite=False)
        #configer.create_test_dbs(abs_path_to_storage_place=abs_path_to_storage_place, use_original_classes=True, corp_status_bar=True, corp_log_ignored=True,corp_lang_classification=True)
        configer.create_test_dbs(abs_path_to_storage_place=abs_path_to_storage_place, use_original_classes=True, corp_status_bar=True, corp_log_ignored=True,corp_lang_classification=True)

        created_dbs = [filename for filename in os.listdir(abs_path_to_storage_place) if ".db" in filename]
        number_db_which_should_be_created = len(list(NestedDictValues(self.configer._test_dbs)))
        if len(created_dbs) != number_db_which_should_be_created:
            assert False

        for db_name in created_dbs:
            #p(db_name)
            encryption, template_name, language, db_type= self._get_meta_data_by_db_file_name(db_name)
            #p((encryption, template_name, language, db_type))
            #sys.exit()
            #p(encryption)
            if not encryption:
                assert False

            db = DBHandler(mode="test")
            if encryption == "encrypted":
                encryption_key=self.configer.init_info_data[template_name]["encryption_key"][db_type]
                db.connect(os.path.join(abs_path_to_storage_place,db_name), encryption_key=encryption_key)
            else:
                db.connect(os.path.join(abs_path_to_storage_place,db_name))

            if db_type == "corpus":
                #p(language)
                #p(self.configer.docs_row_values(token=True, unicode_str=True, lang="de")[template_name])
                #p(self.configer.docs_row_values(token=True, unicode_str=True, lang="all"))
                #sys.exit()
                for item1, item2 in zip(self.configer.docs_row_values(token=True, unicode_str=True, lang=language)[template_name], db.getall("documents")):
                    #p((item1, item2), "item1, item2")
                    for i1,i2 in zip(item1, item2):
                        if isinstance(i1, (list,tuple,dict)):
                            # #p(i1)
                            i2= json.loads(i2)
                            i2 = [token[0] for sent_container in i2 for token in sent_container[0] ]
                            i1 = "".join(i1)
                            i2 = "".join(i2)
                            if i1!=i2:
                                #p((i1,i2))
                                assert False
                        if  i1 == False :
                            i1=0
                        if  i1 == True :
                            i1=1
                        if unicode(i1) != unicode(i2):
                            #p((i1, i2), "i1, i2", c="r")
                            assert False
                #sys.exit()
            elif db_type == "stats":
                ### Here for stats
                pass






    @attr(status='stable')
    #@wipd
    def test_create_all_test_cases_for_diff_fileformats_502(self):
        configer = Configer(mode="test")
        abs_path_to_storage_place=self.tempdir_project_folder

        #sys.exit()
        #configer.create_testsets_in_diff_file_formats(rewrite=True,abs_path_to_storage_place=abs_path_to_storage_place)  
        returned_flags = set(list(configer.create_testsets_in_diff_file_formats(rewrite=False,abs_path_to_storage_place=abs_path_to_storage_place)))
        #p(returned_flags)
        #if  not (len(returned_flags) > 1) or True not in returned_flags:
        #    return False
        #sys.exit()
        for  file_format, test_sets in configer.types_folder_names_of_testsets.iteritems():
            for  name_of_test_set, folder_for_test_set in test_sets.iteritems():
                if file_format == "txt":
                    continue

                if file_format == "sqlite":
                    continue
                abs_path_to_current_test_case = os.path.join(abs_path_to_storage_place, configer._path_to_testsets["blogger"], folder_for_test_set)
                #p(abs_path_to_current_test_case, c="r")

                if not os.path.isdir(abs_path_to_current_test_case):
                    os.makedirs(abs_path_to_current_test_case)


                #p(configer._types_folder_names_of_testsets)
                path_to_txt_corpus = os.path.join(configer.path_to_zas_rep_tools,configer._path_to_testsets["blogger"] , configer._types_folder_names_of_testsets["txt"][name_of_test_set] )
                #p(path_to_txt_corpus)
                reader_txt = Reader(path_to_txt_corpus, "txt", regex_template="blogger", mode="test")
                reader_current_set = Reader(abs_path_to_current_test_case, file_format,  mode="test")
                #p((list(reader_txt.getlazy()), ))
                data_from_txt = defaultdict(list)
                data_from_current_set = defaultdict(list)
                for item in reader_txt.getlazy():
                    for k,v in item.iteritems():
                        if unicode(v).isnumeric():
                            v = int(v)
                        data_from_txt[k].append(v)
                        

                for item in reader_current_set.getlazy():
                    for k,v in item.iteritems():
                        if unicode(v).isnumeric():
                            v = int(v)
                        data_from_current_set[k].append(v)
                
                for col in self.configer.columns_in_doc_table["blogger"]:
                   #p(col)
                   if col != "rowid":
                       for txt_item, current_set_item in zip(sorted(data_from_txt[col]),sorted(data_from_current_set[col])):
                            #p((repr(txt_item), repr(current_set_item)))
                            if txt_item != current_set_item:
                                assert False





    #@attr(status='stable')
    #@wipd
    def test_get_user_data_for_error_tracking(self):
        configer = Configer(mode="test")        
        
        #p(configer._cli_menu_error_agreement())
        #p(configer._user_data)

        #p(configer._cli_menu_get_from_user_twitter_credentials())
        #p(configer._user_data)

        #p(configer._cli_menu_get_from_user_emails())
        #p(configer._user_data)

        # p(configer._cli_menu_get_from_user_project_folder())
        # p(configer._user_data)

     
        #p(configer._user_data.clean())
        # p(configer._user_data)

        #configer.get_data_from_user()
        # p(configer._user_data)

        #configer.get_data_from_user(rewrite=True)
        #p(configer._user_data)

        # configer.get_data_from_user("email", rewrite=True)
        # p(configer._user_data)



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







