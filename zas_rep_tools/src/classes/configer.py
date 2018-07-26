#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : XXX{Information about this code}XXX
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######
#
#
#
#
#
from __future__ import absolute_import

import os
import copy
import sys
import logging
import inspect
import shutil
import traceback
import shelve
import time
import json



from collections import defaultdict
from raven import Client
from cached_property import cached_property
import inspect
from consolemenu import *
from consolemenu.items import *
from validate_email import validate_email
import urllib2
import twitter
from nltk.tokenize import TweetTokenizer

#import types
#from collections import OrderedDict
from zas_rep_tools.src.utils.debugger import p

from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, MyZODB,transaction, path_to_zas_rep_tools, internet_on
from zas_rep_tools.src.utils.logger import main_logger
import zas_rep_tools.src.utils.db_helper as db_helper
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus

from zas_rep_tools.src.classes.exporter import Exporter
from zas_rep_tools.src.classes.reader import Reader
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.classes.stats import Stats

#logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb

class Configer(object):


    def __init__(self, rewrite=False,stop_if_db_already_exist = True,
                logger_folder_to_save=False,  logger_usage=True, logger_level=logging.INFO,
                logger_save_logs=True, logger_num_buffered=5, error_tracking=True,
                ext_tb=False, logger_traceback=False, mode="prod", ):


        #p(logger_save_logs)
        ## Set Mode: Part 1

        self._mode = mode
        #p(self._mode)
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs = set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs
        #p((logger_save_logs,_logger_save_logs), c="r")
        ## Logger Initialisation
        self._logger_level = logger_level
        self._logger_traceback =logger_traceback
        self._logger_folder_to_save = logger_folder_to_save
        self._logger_usage = logger_usage
        self._logger_save_logs = logger_save_logs
        self.logger = main_logger(self.__class__.__name__, level=self._logger_level, folder_for_log=self._logger_folder_to_save, use_logger=self._logger_usage, save_logs=self._logger_save_logs)

        ## Set Mode: Part 2:
        print_mode_name(self._mode, self.logger)


        self.logger.debug('Beginn of creating an instance of {}()'.format(self.__class__.__name__))


        #Input: Incaplusation:
        self._error_tracking = error_tracking
        self._ext_tb = ext_tb
        self._rewrite = rewrite
        self._stop_if_db_already_exist = stop_if_db_already_exist

        #p(inpdata)

        #InstanceAttributes: Initialization

        self._path_to_zas_rep_tools = path_to_zas_rep_tools
        self._path_to_user_config_data = os.path.join(self._path_to_zas_rep_tools, "user_config/user_data.fs")
        self._user_data= self._get_user_config_db()
        if not self._user_data:
            sys.exit()
        #self._myzodb = False
        
        self._suported_user_info = ["error_tracking", "project_folder", "twitter_creditials", "email"]



        self._path_to_testdbs =  "data/tests_data/testDBs/testFolder"

        self._path_to_testsets = {
                    "blogger":"data/tests_data/Corpora/BloggerCorpus",
                    "twitter":"data/tests_data/Corpora/TwitterCorpus"
                    }

        self._types_folder_names_of_testsets = {
                                "txt":{
                                        "highrepetativ":"txt/HighRepetativSubSet",
                                        "fake":"txt/SmallFakeSubset",
                                        "small":"txt/SmallSubset"
                                    },
                                "csv":{
                                    "highrepetativ":"csv/HighRepetativSubSet",
                                    "fake":"csv/SmallFakeSubset",
                                    "small":"csv/SmallSubset"
                                },
                                "xml":{
                                    "highrepetativ":"xml/HighRepetativSubSet",
                                    "fake":"xml/SmallFakeSubset",
                                    "small":"xml/SmallSubset"
                                },
                                "json":{
                                    "highrepetativ":"json/HighRepetativSubSet",
                                    "fake":"json/SmallFakeSubset",
                                    "small":"json/SmallSubset"
                                },
                                "sqlite":{
                                    "highrepetativ":"sqlite/HighRepetativSubSet",
                                    "fake":"sqlite/SmallFakeSubset",
                                    "small":"sqlite/SmallSubset"
                                }
                            }


        self._test_dbs = {
                    "plaintext":{
                                "blogger":{
                                            "en":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_en_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_en_extern_plaintext.db"
                                                  },

                                            "de":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_de_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_de_extern_plaintext.db"
                                                 },

                                            "ru":{},
                                            "test":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_test_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_test_extern_plaintext.db"
                                                   },


                                        },
                                "twitter":{
                                            "en":{},
                                            "de":{
                                                    #"corpus":"9588_corpus_twitter_streamed_de_intern_plaintext.db",
                                                    #"stats": "9588_6361_stats_streamed_de_intern_plaintext.db"
                                                  },
                                            "ru":{},
                                            "test":{},

                                        }
                                },
                    "encrypted":{
                                "blogger":{
                                            "en":{
                                                    #"corpus":"7614_corpus_blogs_bloggerCorpus_en_extern_encrypted.db",
                                                    #"stats":"7614_3497_stats_bloggerCorpus_en_extern_encrypted.db"
                                                 },
                                            "de":{},
                                            "ru":{},
                                            "test":{},

                                        },
                                "twitter":{
                                            "en":{},
                                            "de":{
                                                    "corpus":"9588_corpus_twitter_streamed_de_intern_encrypted.db",
                                                    "stats": "9588_6361_stats_streamed_de_intern_encrypted.db"
                                                 },
                                            "ru":{},
                                            "test":{},

                                        }
                                }
                    }
                


        self._init_info_data = {
                "blogger":{ "id":{"corpus":7614, "stats":3497},
                            "name":"bloggerCorpus",
                            "platform_name":"blogs",
                            "version":"1",
                            "language":"en",
                            "created_at":None,
                            "source":"LanguageGoldMine",
                            "license":"CreativCommon",
                            "visibility":"extern",
                            "template_name":"blogger",
                            "encryption_key": {"corpus":"corpus", "stats":"stats"}
                          },

                "twitter":{ "id":{"corpus":9588, "stats":6361},
                            "name":"streamed",
                            "platform_name":"twitter",
                            "version":"1",
                            "language":"de",
                            "created_at":None,
                            "source":"Twitter API",
                            "license":"Twitter Developer Agreement",
                            "visibility":"intern",
                            "template_name":"twitter",
                            "encryption_key": {"corpus":"corpus", "stats":"stats"}
                          },
                }





        self._columns_in_doc_table = {
                    "blogger": [column[0]  for column in db_helper.default_columns_and_types_for_corpus_documents+db_helper.extended_columns_and_types_for_corpus_documents_blogger],
                    "twitter": [column[0]  for column in db_helper.default_columns_and_types_for_corpus_documents+db_helper.extended_columns_and_types_for_corpus_documents_twitter]
                        }
        #p(self._columns_in_doc_table )
        self._columns_in_info_tabel = {
                    "corpus": [column[0]  for column in db_helper.attributs_names_corpus],
                    "stats": [column[0]  for column in db_helper.attributs_names_stats]
                        }

        self._columns_in_stats_tables = {
                        "redu": [column[0]  for column in db_helper.default_columns_and_types_for_stats_reduplications],
                        "repl" : [column[0]  for column in db_helper.default_columns_and_types_for_stats_replications],
                        "baseline":{
                                    "repl":[column[0]  for column in db_helper.default_columns_and_types_for_stats_repl_baseline],
                                    "redu":[column[0]  for column in db_helper.default_columns_and_types_for_redu_baseline]
                                    }
                        }

        # text_elements = [
        #         ["schöööööönen", "taaaaaag", "dirrrrrr"],
        #         ["kliiiiitze", "kliiiiiittttzzzzeee", "kleeeeeinnn", "kleinnn"],
        #         ["üblich", "üüüüübbbbblllliiiiiichhh", "essss"],
        #         ["😀", "😀", "😀", "😀", "😀"],
        #         ["pitty", "piiittyyy", "day"],
        #         ["доооооооброоооооггггоо", "доброоогооо ", "дняяяяяяяяяяяяя"]
        #         ]
        
        self._tokenizer = TweetTokenizer()

        self._lang_order = ["en", "de", "ru", "other"]
        self._text_elements_collection = {
                "en":[
                        "It was verrrryyyyy vvveRRRRRRrry very piiiiiiiiity for me -((((( @real_trump #sheetlife #readytogo http://www.absurd.com", # [u'It', u'was', u'verrrryyyyy', u'vvveRRRRRRrry', u'very', u'piiiiiiiiity', u'for', u'me', u'-', u'(', u'(', u'(', u'@real_trump', u'#sheetlife', u'#readytogo', u'http://www.absurd.com']
                        "glaaaaaaad to seeeeeeeee you -))))", #[u'glaaaaaaad', u'to', u'seeeeeeeee', u'you', u'-', u')', u')', u')']
                        "a baddddd bad bbbbbbbaaaaaa bbbbaaaaddddd baaaaaaad news, which we can not accept. -(((( 😫😫😫😫 😫😫😫😫😫 😫😫😫 #sheetlife #sheetlife http://www.noooo.com", #[u'a', u'baddddd', u'bad', u'bbbbbbbaaaaaa', u'bbbbaaaaddddd', u'baaaaaaad', u'news', u'-', u'(', u'(', u'(', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'\ud83d', u'\ude2b', u'#sheetlife', u'#sheetlife', u'http://www.noooo.com']
                        "Tiny tiny tiny tiny tiny tiny mooooooodelllllll, which we can use for explain a biiig biiiiiiiiiiiiiiig things.", #[u'Tiny', u'tiny', u'tiny', u'tiny', u'tiny', u'tiny', u'mooooooodelllllll']
                        "tiny model, but a big explanation.",
                        "tinnnyy tiny tiny surprise",
                        "it was really bad surprise for me 😫😫😫😫, buuuuuuuuuut i really reallly reeeeeallllyyy liked it =)))))))))) 😀😀😀😀😀🌈🌈🌈🌈🌈🌈🌈😀",
                    ],

                "de":[
                        "Klitze kliiiitze kleEEEEine kleinnne Überaschung -)))) -))) ",  # [u'Klitze', u'kliiiitze', u'kleEEEEine', u'\xdcberaschung', u'-', u')', u')', u')', u'-', u')', u')', u')']
                        "einen wunderschönen Taaaaaagggggg wünsche ich euch 😀😀😀😀😀🌈🌈🌈🌈🌈🌈🌈", #[u'einnennnnnn', u'toooolllleeeeen', u'Taaaaaagggggg', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08', u'\ud83c', u'\udf08'], [u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00', u'\ud83d', u'\ude00']
                        "eine klitzeeee kleine Überrrraschung",
                        "eine klitzeeee kleine Sache",
                        "eine klitze klitze klitze klitze kleine Überrrraschung, die ich mal gerne hatte.",
                    ],

                "ru":[
                        "Oчень оооооченнннь ооооччччееееннннньььь хорошееего дняяяяяяяяя", #[u'O\u0447\u0435\u043d\u044c', u'\u043e\u043e\u043e\u0447\u0435\u043d\u043d\u043d\u044c', u'\u043e\u043e\u043e\u0447\u0447\u0447\u0435\u0435\u0435\u043d\u043d\u043d\u044c\u044c\u044c', u'\u0445\u043e\u0440\u043e\u0448\u0435\u0435\u0435\u0433\u043e', u'\u0434\u043d\u044f\u044f\u044f']
                        "самммооово сааамово  приятногооооо прииииииииятного  ужииииина 🥡🍽🍽🍽🍽🍽🍽🍽🍽🍽🍽", #[u'\u0441\u0430\u043c\u043c\u043c\u043e\u043e\u043e\u0432\u043e', u'\u0441\u0430\u0430\u0430\u043c\u043e\u0432\u043e', u'\u043f\u0440\u0438\u044f\u0442\u043d\u043e\u0433\u043e\u043e\u043e', u'\u043f\u0440\u0438\u0438\u0438\u044f\u0442\u043d\u043e\u0433\u043e', u'\u0443\u0436\u0438\u0438\u0438\u043d\u0430', u'\ud83e', u'\udd61', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d', u'\ud83c', u'\udf7d']
                    ],

                "other":[
                        "اللغة العربية رائعة",
                    ],

                }

        # self._text_elements_as_byte_str_untokenized = [text_item for lang, text_items in self._text_elements.iteritems() for text_item in text_items]

        # self._text_elements_as_unicode_str_untokenized  = [t_elem.decode("utf-8") for t_elem in self._text_elements_as_byte_str_untokenized ]

        # self._text_elements_as_byte_str_tokenized = [self._tokenizer.tokenize(t_elem)  for t_elem in self._text_elements_as_byte_str_untokenized]
        # self._text_elements_as_unicode_str_tokenized = [self._tokenizer.tokenize(t_elem)  for t_elem in self._text_elements_as_unicode_str_untokenized]
        


        self._get_user_config_db() 


        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})

        #p(self._docs_row_values(token=False, unicode_str=True), c="r")
        #p(self._text_elements_as_unicode_str_untokenized)
        if not self._check_correctness_of_the_test_data():
            self.logger.error("TestDataCorruption: Please check test data.", exc_info=self._logger_traceback)
            sys.exit()

        self.logger.debug('Intern InstanceAttributes was initialized')


        self.logger.debug('An instance of {}() was created '.format(self.__class__.__name__))


    def __del__(self):
        pass
        # if self._user_data:
        #     self._user_data.close()
        # if self._user_data:
        #     transaction.commit()
        #     if self._myzodb:
        #         self._myzodb.close()
        #     self.logger.debug("UserDataDB was closed.")
        ############################################################
        ####################__init__end#############################
        ############################################################


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################Extern########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

    def row_text_elements(self, lang="all"):
        return copy.deepcopy(self._row_text_elements(lang=lang))
    
    def text_elements(self, token=True, unicode_str=True,lang="all"):
        return copy.deepcopy(self._text_elements(token=token, unicode_str=unicode_str, lang=lang))

    def docs_row_values(self,token=True, unicode_str=True, lang="all"):
        return copy.deepcopy(self._docs_row_values(token=token,unicode_str=unicode_str, lang=lang))

    def docs_row_dict(self, token=True, unicode_str=True, all_values=False, lang="all"):
        '''
        just one dict with colums as key and list of all values as values for each columns()key
        '''
        return copy.deepcopy(self._docs_row_dict(token=token, unicode_str=unicode_str, all_values=all_values, lang=lang))

    def docs_row_dicts(self, token=True, unicode_str=True,  lang="all"):
        '''
        list of dicts  with colums and values for each row
        '''
        return copy.deepcopy(self._docs_row_dicts(token=token, unicode_str=unicode_str, lang=lang))





    def _row_text_elements(self, lang="all"):
        if lang == "test":
            lang ="all"
        if lang == "all":
            return [text_item for lang in self._lang_order for text_item in self._text_elements_collection[lang]]
        else:
            if lang in self._text_elements_collection:
                return self._text_elements_collection[lang]
            else:
                self.logger.error("No test-text-elements exist for given language: '{}'.".format(lang))


    def _text_elements(self, token=True, unicode_str=True, lang="all"):
        if lang == "test":
            lang ="all"
        if token:
            if unicode_str:
                    #sys.exit()
                return [t_elem.split()  for t_elem in self._text_elements(token=False, unicode_str=True,lang=lang)]
                #return [self._tokenizer.tokenize(t_elem)  for t_elem in self._text_elements(token=False, unicode_str=True,lang=lang)]
                #return self._text_elements_as_unicode_str_tokenized
            else:
                return [t_elem.split()  for t_elem in self._text_elements(token=False, unicode_str=False,lang=lang)]
                #return [self._tokenizer.tokenize(t_elem)  for t_elem in self._text_elements(token=False, unicode_str=False,lang=lang)]
                #return self._text_elements_as_byte_str_tokenized

        elif not token:
            if unicode_str:
                #for t_elem in self._row_text_elements(lang=lang):
                #    p((t_elem, type(t_elem)))
                #sys.exit()
                #json.loads(t_elem)
                return [json.loads(r'"{}"'.format(t_elem)) for t_elem in self._row_text_elements(lang=lang) ]
                #return [t_elem.decode("utf-8") for t_elem in self._row_text_elements(lang=lang) ]
                #return self._text_elements_as_unicode_str_untokenized
            else:
                return self._row_text_elements(lang=lang)



    def _docs_row_values(self,token=True, unicode_str=True, lang="all"):
        if lang == "test":
            lang ="all"
        text_element = self._text_elements(token=token, unicode_str=unicode_str, lang=lang)
        #self.logger.critical(text_element)
        if lang == "en":
            text_element = self._text_elements(token=token, unicode_str=unicode_str, lang=lang)
            docs_row_values_en = {
                    "blogger":[
                        [1, 1111, text_element[0], u'w', 37, u'IT', u'lion' ],
                        [2, 2222, text_element[1], u'm', 23, u'Care', u'fish' ],
                        [3, 3333, text_element[2], u'w', 22, u'Finance', u'aquarius' ],
                        [4, 4444, text_element[3], u'm', 27, u'IT', u'gemini' ],
                        [5, 5555, text_element[4], u'w', 35, u'Air Industry', u'lion' ],
                        [6, 6666, text_element[5], u'm', 21, u'Industry', "crawfish"  ],
                        [7, 7777, text_element[6], u'w', 37, u'IT', u'lion' ],
                        ],

                    "twitter":[
                        [1 ,1111, text_element[0], u"20/06/2014", u"en", u"Iphone", u"22/03/2014", u"Die Welt ist schön", 45, 76, 765, 34567890, u"en", u"MotherFucker", u"realBro", u"True", "planet Earth", False, False, False ],
                        [2 ,2222, text_element[1], u"03/02/2013", u"en", u"Iphone", u"29/06/2012", u"Kein Plan", 45, 76, 765, 34567890, u"en", u"MotherFucker", u"realBro", u"True", "planet Earth", False, False, False ],
                        [3 ,3333, text_element[2], u"21/06/2014", u"en", u"WebAPI", u"21/07/2017", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"MotherFucker", u"realBro", u"True", "planet Earth", False, False, False ],
                        [4 ,4444, text_element[3], u"20/04/2014", u"fr", u"Iphone", u"12/06/2011", u"Nööö", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [5 ,5555, text_element[4], u"20/06/2011", u"ru", u"Android", u"12/06/2012", u"Was willste, alter?", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [6 ,6666, text_element[5], u"30/09/2014", u"ru", u"Iphone", u"20/03/2013", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [7 ,7777, text_element[6], u"01/06/2014", u"de", u"Android", u"22/06/2011", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        ]
                    }
            return docs_row_values_en
        
        elif lang == "de":
            text_element = self._text_elements(token=token, unicode_str=unicode_str, lang=lang)
            #p((text_element))
            docs_row_values_de = {
                    "blogger":[
                        [8, 8888, text_element[0], u'm', 23, u'Care', u'fish' ],
                        [9, 9999, text_element[1], u'w', 22, u'Finance', u'aquarius' ],
                        [10, 10000, text_element[2], u'w', 35, u'Air Industry', u'lion' ],
                        [11, 11111, text_element[3], u'm', 21, u'Industry', "crawfish"  ],
                        [12, 12222, text_element[4], u'w', 37, u'IT', u'lion' ],
                        ],

                    "twitter":[
                        [8 ,8888, text_element[0], u"20/06/2007", u"de", u"Iphone", u"20/02/2009", u"Jööööö", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [9 ,9999, text_element[1], u"20/04/2014", u"it", u"WebAPI", u"01/06/2011", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [10 ,10000, text_element[2], u"21/06/2014", u"en", u"WebAPI", u"21/07/2017", u"Neiiiiin", 45, 76, 765, 34567890, u"en", u"MotherFucker", u"realBro", u"True", "planet Earth", False, False, False ],
                        [11 ,11111, text_element[3], u"20/04/2014", u"fr", u"Iphone", u"12/06/2011", u"Nööö", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [12 ,12222, text_element[4], u"20/06/2011", u"ru", u"Android", u"12/06/2012", u"Was willste, alter?", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        ]
                    }
            return docs_row_values_de

        elif lang == "ru":
            text_element = self._text_elements(token=token, unicode_str=unicode_str, lang=lang)
            docs_row_values_ru = {
                    "blogger":[
                        [13, 13333, text_element[0], u'm', 23, u'Care', u'fish' ],
                        [14, 14444, text_element[1], u'w', 22, u'Finance', u'aquarius' ],
                        ],

                    "twitter":[
                        [13 ,13333, text_element[0], u"30/09/2014", u"ru", u"Iphone", u"20/03/2013", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        [14 ,14444, text_element[1], u"01/06/2014", u"de", u"Android", u"22/06/2011", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ],
                        ]
                    }
            return docs_row_values_ru

        elif lang == "other":
            text_element = self._text_elements(token=token, unicode_str=unicode_str, lang=lang)
            docs_row_values_other = {
                "blogger":[
                    [15, 15555, text_element[0], u'w', 22, u'Finance', u'aquarius' ],
                    ],

                "twitter":[
                    [15 ,16666, text_element[0], u"20/04/2014", u"it", u"WebAPI", u"01/06/2011", u"Neiiiiin", 45, 76, 765, 98765, u"en", u"Lighter", u"LivelyLife", u"True", "planet Earth", False, False, False ]
                    ]
                }
            return docs_row_values_other

        elif lang == "all":
            temp_dict = defaultdict(list)
            for language in ["en", "de", "ru", "other"]:
                output_for_current_lang = self._docs_row_values(token=token, unicode_str=unicode_str, lang=language)

                for k,v in output_for_current_lang.iteritems():
                    temp_dict[k] += v

            return temp_dict





    def _docs_row_dict(self, token=True, unicode_str=True, all_values=True , lang="all"):
        '''
        just one dict with colums as key and list of all values as values for each columns()key
        '''
        if lang == "test":
            lang ="all"
        docs_row_values = self._docs_row_values(token=token, unicode_str=unicode_str, lang=lang)
        #p(docs_row_values,"docs_row_values")
        if all_values:
            return {template_name:{k:v for k,v in zip(columns, zip(*docs_row_values[template_name]))} for template_name, columns in  self._columns_in_doc_table.iteritems()}
        else:
            return {template_name:{col:row[0] for col, row in data.iteritems()}  for template_name, data in  self._docs_row_dict(token=token, unicode_str=unicode_str,lang=lang,all_values=True).iteritems()}



    def _docs_row_dicts(self, token=True, unicode_str=True, lang="all"):
        '''
        list of dicts  with colums and values for each row
        '''
        if lang == "test":
            lang ="all"
        docs_row_values = self._docs_row_values(token=token, unicode_str=unicode_str, lang=lang)
        docs_row_dicts = { template_name:[dict(zip(columns, row)) for row in docs_row_values[template_name]] for template_name, columns in  self._columns_in_doc_table.iteritems()}
        return docs_row_dicts


    ###########################Config Values#######################

    @cached_property
    def path_to_zas_rep_tools(self):
        return copy.deepcopy(self._path_to_zas_rep_tools)

    @cached_property
    def path_to_testdbs(self):
        return copy.deepcopy(self._path_to_testdbs)       

    @cached_property
    def test_dbs(self):
        return copy.deepcopy(self._test_dbs)             

    @cached_property
    def init_info_data(self):
        return copy.deepcopy(self._init_info_data)     

    @cached_property
    def columns_in_doc_table(self):
         return copy.deepcopy(self._columns_in_doc_table)            

    @cached_property
    def columns_in_info_tabel(self):
        return copy.deepcopy(self._columns_in_info_tabel)             

    @cached_property
    def columns_in_stats_tables(self):
        return copy.deepcopy(self._columns_in_stats_tables)     


    @cached_property
    def path_to_testsets(self):
         return copy.deepcopy(self._path_to_testsets)   

    @cached_property
    def types_folder_names_of_testsets(self):
         return copy.deepcopy(self._types_folder_names_of_testsets)  


    def clean_user_data(self):
        if self._user_data.clean():
            return True
        else:
            return False

    def get_data_from_user(self, user_info_to_get=False, rewrite=False):
        if not rewrite:
            rewrite = self._rewrite
        if user_info_to_get:
            if isinstance(user_info_to_get, (unicode, str)):
                user_info_to_get = [user_info_to_get]
        else:
            user_info_to_get = self._suported_user_info


        for user_info_name in user_info_to_get:
            if user_info_name not in self._suported_user_info:
                self.logger.error("UserDataGetterError:  '{}' - data not supported.  ".format(user_info_name), exc_info=self._logger_traceback)
                continue

            if user_info_name == "error_tracking":
                if rewrite:
                    self._cli_menu_error_agreement()
                    continue

                if "error_tracking" not in self._user_data:
                    self._cli_menu_error_agreement()

            elif user_info_name == "project_folder":
                if rewrite:
                    self._cli_menu_get_from_user_project_folder()
                    continue
                if "project_folder" not in self._user_data:
                    self._cli_menu_get_from_user_project_folder()

            elif user_info_name == "twitter_creditials":
                if rewrite:
                    self._cli_menu_get_from_user_twitter_credentials()
                    continue

                if "twitter_creditials" not in self._user_data:
                    self._cli_menu_get_from_user_twitter_credentials()


            elif user_info_name == "email":
                if rewrite:
                    self._cli_menu_get_from_user_emails()
                    continue

                if "email" not in self._user_data:
                    self._cli_menu_get_from_user_emails()

            else:
                self.logger.critical("Not supported user_data_getter ('{}').".format(user_info_name))






        self._test_dbs = {
                    "plaintext":{
                                "blogger":{
                                            "en":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_en_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_en_extern_plaintext.db"
                                                  },

                                            "de":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_de_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_de_extern_plaintext.db"
                                                 },

                                            "ru":{},
                                            "test":{
                                                    "corpus":"7614_corpus_blogs_bloggerCorpus_test_extern_plaintext.db",
                                                    "stats":"7614_3497_stats_bloggerCorpus_test_extern_plaintext.db"
                                                   },


                                        },
                                "twitter":{
                                            "en":{},
                                            "de":{
                                                    #"corpus":"9588_corpus_twitter_streamed_de_intern_plaintext.db",
                                                    #"stats": "9588_6361_stats_streamed_de_intern_plaintext.db"
                                                  },
                                            "ru":{},
                                            "test":{},

                                        }
                                },
                    "encrypted":{
                                "blogger":{
                                            "en":{
                                                    #"corpus":"7614_corpus_blogs_bloggerCorpus_en_extern_encrypted.db",
                                                    #"stats":"7614_3497_stats_bloggerCorpus_en_extern_encrypted.db"
                                                 },
                                            "de":{},
                                            "ru":{},
                                            "test":{},

                                        },
                                "twitter":{
                                            "en":{},
                                            "de":{
                                                    "corpus":"9588_corpus_twitter_streamed_de_intern_encrypted.db",
                                                    "stats": "9588_6361_stats_streamed_de_intern_encrypted.db"
                                                 },
                                            "ru":{},
                                            "test":{},

                                        }
                                }
                    }
                


 
    def create_test_dbs(self, rewrite=False, abs_path_to_storage_place = False,corp_log_ignored=False,
                        use_original_classes = True, corp_lang_classification=True, 
                        corp_pos_tagger=True, corp_sent_splitter=True, corp_sentiment_analyzer=True, corp_status_bar=True):
        #p(abs_path_to_storage_place, "abs_path_to_storage_place")
        if not abs_path_to_storage_place:
            abs_path_to_storage_place = os.path.join(self._path_to_zas_rep_tools, self._path_to_testdbs)
        
        #sys.exit()
        if not  rewrite:
            rewrite = self._rewrite
        #for 
        for template_name, init_data in  self._init_info_data.iteritems():
            #p(template_name)
            for encryption in ["plaintext", "encrypted"]:
                for dbtype in ["corpus", "stats"]:
                    # if exist  and rewrite=True -> remove existed db


                    #p(self._columns_in_info_tabel[dbtype])
                    dbname = self._init_info_data[template_name]["name"]
                    #language = self._init_info_data[template_name]["language"]
                    visibility = self._init_info_data[template_name]["visibility"]
                    platform_name = self._init_info_data[template_name]["platform_name"]
                    license = self._init_info_data[template_name]["license"]
                    template_name = self._init_info_data[template_name]["template_name"]
                    version = self._init_info_data[template_name]["version"]
                    source = self._init_info_data[template_name]["source"]
                    encryption_key = self._init_info_data[template_name]["encryption_key"][dbtype] if  encryption=="encrypted" else False
                    corpus_id = self._init_info_data[template_name]["id"]["corpus"]
                    stats_id = self._init_info_data[template_name]["id"]["stats"]
                    #p((dbtype, encryption_key))
                    
                    # for which languages create 
                    if encryption == "encrypted":
                        if template_name == "twitter":
                            languages = ["de"]
                        elif template_name == "blogger":
                            continue
                            #languages = ["en"]

                    elif encryption == "plaintext":
                        if template_name == "twitter":
                            continue
                            #languages = ["de"]
                        elif template_name == "blogger":
                            languages = ["de", "en", "test"]

                    for language in languages:

                        # If Rewrite is on, delete  db for current attributes. if this exist in the 'self._test_dbs'. If not, than ignore.
                        try:
                            path_to_db = os.path.join(abs_path_to_storage_place, self._test_dbs[encryption][template_name][language][dbtype])
                            if rewrite:
                                if os.path.isfile(path_to_db):
                                    os.remove(path_to_db)
                                    self.logger.debug("RewriteOptionIsON: Following DB was deleted from TestDBFolder: '{}'. TestDBCreationScript will try to created this DB.".format(path_to_db))
                                else:
                                    self.logger.debug("11111{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                    self.logger.debug("RewriteOptionIsON: Following DB wasn't found in the TestDBFolder and wasn't deleted: '{}'. TestDBCreationScript will try to created this DB.".format(path_to_db))              
                            else:
                                if os.path.isfile(path_to_db):
                                    self.logger.debug("RewriteOptionIsOFF: '{}'-DB exist and will not be rewrited/recreated.".format(path_to_db))
                                    continue

                        except KeyError, k:
                            self.logger.debug("KeyError: DBName for '{}:{}:{}:{}' is not exist in the 'self._test_dbs'. TestDBCreationScript will try to created this DB. ".format(encryption,template_name,language,dbtype))
                            continue
                        except Exception, e:
                            self.logger.error("See Exception: '{}'. (line 703). Creation of the TestDBs was aborted.".format(e), exc_info=self._logger_traceback)
                            sy.exit()

                        self.logger.debug("2222{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                        db_id = corpus_id if dbtype == "corpus" else stats_id
                        self.logger.info("TestDBCreationProcess: Was started for DB with following attributes: 'dbtype='{}'; id='{}'; encryption='{}'; template_name='{}'; language='{}'. ".format(dbtype, db_id,encryption,template_name,language ))
                        if dbtype=="corpus":
                            self.logger.debug("3333{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                            if not use_original_classes:
                                db = DBHandler(logger_level=logging.ERROR,logger_traceback=self._logger_traceback,
                                        logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage,
                                        logger_save_logs= self._logger_save_logs, mode=self._mode,
                                        error_tracking=self._error_tracking,  ext_tb= self._ext_tb,
                                        stop_if_db_already_exist=self._stop_if_db_already_exist, rewrite=self._rewrite)
                                was_initialized = db.init(dbtype, abs_path_to_storage_place, dbname, language, visibility, platform_name=platform_name, license=license , template_name=template_name, version=version , source=source, corpus_id=corpus_id, stats_id=stats_id, encryption_key=encryption_key)
                                # self.logger.critical("was_initialized={}".format(was_initialized))
                                # sys.exit()
                                #!!!!
                                #self.logger.debug("444{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                if not was_initialized:
                                    if self._stop_if_db_already_exist:
                                        self.logger.debug("DBInitialisation: DBName for '{}:{}:{}:{}' wasn't initialized. Since 'self._stop_if_db_already_exist'-Option is on, current Script will ignore current DB and will try to create next one.".format(encryption,template_name,language,dbtype))
                                        continue
                                    else:
                                        self.logger.error("DBInitialisationError: DBName for '{}:{}:{}:{}' wasn't initialized. TestDBCreation was aborted.".format(encryption,template_name,language,dbtype))
                                        return False
                                #self.logger.debug("5555{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                rows_to_insert = self.docs_row_values(token=True, unicode_str=True)[template_name]
                                path_to_db = db.path()
                                #self.logger.debug("6666{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                if not path_to_db:
                                    self.logger.error("Path for current DB wasn't getted. Probably current corpus has InitializationError. TestDBCreation was aborted.")
                                    sys.exit()

                                db.lazyinsert("documents",rows_to_insert)
                                #self.logger.debug("77777{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                #p(( len(db.getall("documents")), len(rows_to_insert)))
                                if "Connection" not in str(type(db)):
                                    pass

                                if len(db.getall("documents")) != len(rows_to_insert):
                                    
                                    #db.close()
                                    #p(db._db)
                                    os.remove(path_to_db)
                                    #shutil.rmtree(path_to_db)
                                    self.logger.error("TestDBsCreation(InsertionError): Not all rows was correctly inserted into DB. This db was ignored and not created.", exc_info=self._logger_traceback)
                                    #sys.exit()
                                    sys.exit()
                                    continue
                            else:
                                #if corp_language:
                                #    language = corp_language
                                corp = Corpus(language=language, lang_classification=corp_lang_classification,
                                    pos_tagger=corp_pos_tagger, sent_splitter=corp_sent_splitter,
                                    sentiment_analyzer=corp_sentiment_analyzer,
                                    logger_level=logging.ERROR, logger_traceback=self._logger_traceback,
                                    logger_folder_to_save=self._logger_folder_to_save,
                                    logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs,
                                    mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb,
                                    stop_if_db_already_exist=self._stop_if_db_already_exist, rewrite=self._rewrite)
                                #p(corp.info())
                                self.logger.debug("444{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                was_initialized = corp.init(abs_path_to_storage_place,dbname, language, visibility,platform_name,
                                    license=license , template_name=template_name, version=version, source=source,
                                    corpus_id=corpus_id, encryption_key=encryption_key)
                                self.logger.debug("555{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                #self.logger.critical("was_initialized={}".format(was_initialized))
                                
                                if not was_initialized:
                                    if self._stop_if_db_already_exist:
                                        self.logger.debug("DBInitialisation: DBName for '{}:{}:{}:{}' wasn't initialized. Since 'self._stop_if_db_already_exist'-Option is on, current Script will ignore current DB and will try to create next one.".format(encryption,template_name,language,dbtype))
                                        continue
                                    else:
                                        self.logger.error("DBInitialisationError: DB for '{}:{}:{}:{}' wasn't initialized. TestDBCreation was aborted.".format(encryption,template_name,language,dbtype))
                                        return False
                                self.logger.debug("666{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                #
                                #rows_to_insert = self._docs_row_values[template_name]
                                #self.docs_row_values(token=False, unicode_str=True)[template_name]
                                rows_as_dict_to_insert = self.docs_row_dicts(token=False, unicode_str=True)[template_name]
                                #p(rows_as_dict_to_insert,"rows_as_dict_to_insert")
                                #self.logger.critical(rows_as_dict_to_insert)
                                path_to_db = corp.db.path()
                                fname_db = corp.db.fname()
                                self.logger.debug("777{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                if not path_to_db or not fname_db:
                                    self.logger.error("Path or FileName for current CorpusDB wasn't getted. (lang='{}', dbname='{}', id='{}',platform_name='{}', visibility='{}', encryption_key='{}') Probably current corpus has InitializationError. TestDBCreation was aborted.".format(language, dbname,corpus_id, platform_name, visibility, encryption_key))
                                    sys.exit()
                                #p((path_to_db,fname_db))
                                was_inserted = corp.insert(rows_as_dict_to_insert, status_bar=corp_status_bar, log_ignored=corp_log_ignored)
                                #p(was_inserted , "was_inserted ")
                                self.logger.debug("888{}:{}:{}:{}".format(dbname, language, platform_name, dbtype))
                                self.logger.critical("'{}': Following rows was inserted:\n '{}'. \n\n".format(fname_db, '\n'.join("--->"+str(v) for v in  list(corp.docs())  )  ))
                                #p(list(corp.docs()), "fname_db")
                                #if encryption == "encrypted":
                                #    sys.exit()
                                #sys.exit()
                                if not was_inserted:
                                    os.remove(path_to_db)
                                    self.logger.error("Rows wasn't inserted into the '{}'-DB. This DB was deleted and script of creating testDBs was aborted.".format(fname_db))
                                    sys.exit()
                                    return False
                                    #continue
                                else:
                                    if not corp_lang_classification:
                                        if len(corp.docs()) != len(rows_as_dict_to_insert):
                                            os.remove(path_to_db)
                                            #shutil.rmtree(path_to_db)
                                            self.logger.error("TestDBsCreation(InsertionError): Not all rows was correctly inserted into DB. This DB was deleted and script of creating testDBs was aborted.", exc_info=self._logger_traceback)
                                            #sys.exit()
                                            sys.exit()
                                            return False
                                            #continue
                                    else:
                                        self.logger.debug("'{}'-TestDB was created. Path: '{}'.".format(fname_db,path_to_db))
                                

                        elif dbtype=="stats":
                            ## here insert all rows into stats dbs
                            db = DBHandler(logger_level=logging.ERROR,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb, stop_if_db_already_exist=self._stop_if_db_already_exist, rewrite=self._rewrite)
                            db.init(dbtype, abs_path_to_storage_place, dbname, language, visibility, platform_name=platform_name, license=license , template_name=template_name, version=version , source=source, corpus_id=corpus_id, stats_id=stats_id, encryption_key=encryption_key)
            
        self.logger.info("TestDBs was initialized.")


    def create_test_data(self, abs_path_to_storage_place=False, use_original_classes = True, corp_lang_classification=False, 
                         corp_pos_tagger=True, corp_sent_splitter=True, corp_sentiment_analyzer=True, corp_status_bar=True, corp_log_ignored=False):
        #if not  corp_language:
        #    corp_language = "de"
        self.create_testsets(rewrite=False,abs_path_to_storage_place=abs_path_to_storage_place,silent_ignore = True)
        self.create_test_dbs(rewrite=False, abs_path_to_storage_place=abs_path_to_storage_place, use_original_classes=use_original_classes, corp_log_ignored=corp_log_ignored,
                            corp_lang_classification=corp_lang_classification,
                            corp_pos_tagger=corp_pos_tagger, corp_sent_splitter=corp_sent_splitter,
                            corp_sentiment_analyzer=corp_sentiment_analyzer, corp_status_bar=corp_status_bar)
        self.logger.info("Test Data was initialized.")

    def create_testsets(self, rewrite=False, abs_path_to_storage_place=False, silent_ignore = True):
        return list(self.create_testsets_in_diff_file_formats(rewrite=rewrite, abs_path_to_storage_place=abs_path_to_storage_place,silent_ignore=silent_ignore))

    def create_testsets_in_diff_file_formats(self, rewrite=False, abs_path_to_storage_place=False, silent_ignore = True):
        #p(abs_path_to_storage_place)
        #sys.exit()
        if not  rewrite:
            rewrite = self._rewrite
        if not abs_path_to_storage_place:
            abs_path_to_storage_place = self._path_to_zas_rep_tools
        #p("fghjk")

        try:
            # make test_sets for Blogger Corp 
            for  file_format, test_sets in self._types_folder_names_of_testsets.iteritems():
                for  name_of_test_set, folder_for_test_set in test_sets.iteritems():
                    if file_format == "txt":
                        continue
                    abs_path_to_current_test_case = os.path.join(abs_path_to_storage_place, self._path_to_testsets["blogger"], folder_for_test_set)
                    #p((file_format, name_of_test_set))
                    #p(abs_path_to_current_test_case)
                    if rewrite:
                        if os.path.isdir(abs_path_to_current_test_case):
                            shutil.rmtree(abs_path_to_current_test_case)
                            #os.remove(abs_path_to_current_test_case)

                    if not os.path.isdir(abs_path_to_current_test_case):
                        os.makedirs(abs_path_to_current_test_case)

                    #
                    #sys.exit()
                    #p(self._types_folder_names_of_testsets)
                    path_to_txt_corpus = os.path.join(self.path_to_zas_rep_tools,self._path_to_testsets["blogger"] , self._types_folder_names_of_testsets["txt"][name_of_test_set] )
                    #p(path_to_txt_corpus, c="r")

                    #sys.exit()
                            

                    reader = Reader(path_to_txt_corpus, "txt", regex_template="blogger",logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)
                    exporter = Exporter(reader.getlazy(),  rewrite=rewrite, silent_ignore=silent_ignore, logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)

                    if file_format == "csv":
                        if name_of_test_set == "small":
                            flag = exporter.tocsv(abs_path_to_current_test_case, "blogger_corpus",self._columns_in_doc_table["blogger"], rows_limit_in_file=5)
                            if not flag:
                                yield False
                            else:
                                yield True
                        else:
                            flag= exporter.tocsv(abs_path_to_current_test_case, "blogger_corpus",self._columns_in_doc_table["blogger"], rows_limit_in_file=2)
                            if not flag:
                                yield False
                            else:
                                yield True
                        
                    

                    elif file_format == "xml":
                        if name_of_test_set == "small":
                            flag = exporter.toxml(abs_path_to_current_test_case, "blogger_corpus", rows_limit_in_file=5)
                            if not flag:
                                yield False
                            else:
                                yield True
                        else:
                            flag = exporter.toxml(abs_path_to_current_test_case, "blogger_corpus", rows_limit_in_file=2)
                            if not flag:
                                yield False
                            else:
                                yield True


                    elif file_format == "json":
                        if name_of_test_set == "small":
                            flag = exporter.tojson(abs_path_to_current_test_case, "blogger_corpus", rows_limit_in_file=5)
                            if not flag:
                                yield False
                            else:
                                yield True
                        
                        else:
                            flag = exporter.tojson(abs_path_to_current_test_case, "blogger_corpus", rows_limit_in_file=2)
                            if not flag:
                                yield False
                            else:
                                yield True
  


                    elif file_format == "sqlite":
                        flag = exporter.tosqlite(abs_path_to_current_test_case, "blogger_corpus",self._columns_in_doc_table["blogger"])
                        if not flag:
                            yield False
                        else:
                            yield True

            self.logger.info("TestSets (diff file formats) was initialized.")
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("SubsetsCreaterError: Throw following Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
                
        







####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
######################################INTERN########################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################





    def _get_user_config_db(self):
        #try:
        try:
            if not os.path.isdir(os.path.split(self._path_to_user_config_data)[0]):
                self.logger.debug(" 'user_config' folder was created in '{}' ".format(os.path.split(self._path_to_user_config_data)[0]))
                os.mkdir(os.path.split(self._path_to_user_config_data)[0])
            db = MyZODB(self._path_to_user_config_data)
            db["permission"] = True
            return db
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            if "permission" in str(e).lower():
                self.logger.error("UserConfigDBGetterError: Problem with permission. Probably solution. Please execute same command with 'sudo'-Prefix and enter your admin password. Exception: '{}'. ".format(e) ,exc_info=self._logger_traceback)
            else: 
                self.logger.error("UserConfigDBGetterError: '{}'. ".format(e) ,exc_info=self._logger_traceback)
            return False
 
 





    def _cli_menu_get_from_user_project_folder(self):

        getted_project_folder  = False

        def _get_input(args):
            getted_input = input(args)
            return str(getted_input)
        # Create the menu
        menu1 = SelectionMenu(["No", "Yes"],
                                title="Set Project Folder.",
                                #subtitle="(via Email)",
                                prologue_text="Every created database will be saved in the project folder. Before you can work with this tool you need to set up an Project Folder. Do you want to do it now? (if you want to use current directory as project folder just type an dot. exp: '.' )",
                                #epilogue_text="222"
                                )

        menu1.show()
        menu1.join()
        selection1 = menu1.selected_option
        #print selection1

        if selection1 == 1:
            status = True
            while status:
                prj_fldr = raw_input("Enter Project Folder: ")
                if os.path.isdir(prj_fldr):
                    getted_project_folder = prj_fldr
                    status = False
                else: 
                    self.logger.critical("DirValidation: Given project Folder is not exist. Please retype it. (or type 'Ctrl+D' or 'Ctrl+C' to interrupt this process.)")
                    #print 

        if getted_project_folder:
            if getted_project_folder ==".":
                getted_project_folder = os.getcwd()
            self._user_data["project_folder"] = getted_project_folder
        
        return  getted_project_folder 



    def _cli_menu_get_from_user_emails(self):
        getted_emails = []
        # Create the menu
        menu1 = SelectionMenu(["No", "Yes"],
                    title="User Notification.",
                    subtitle="(via Email)",
                    prologue_text="This package can send to the users some important information. For example some day statistics for Twitter-Streamer or if some error occurs. Do you want to use this possibility? (Your email adress will stay on you Computer and will not be send anywhere.)",
                    #epilogue_text="222"
                    )

        menu1.show()
        menu1.join()
        selection1 = menu1.selected_option
        #print selection1

        if selection1 == 1:
            # Part 1: Get number of emails 
            status = True
            while status:
                menu2 = ConsoleMenu(
                                    title="Number of email addresses.",
                                    #subtitle="(via Email)",
                                    prologue_text="How much email addresses do you want to set?",
                                    #epilogue_text="222"
                                    )
                one_email = SelectionItem("one", 0)
                number_of_emails = FunctionItem("many", function=raw_input, args=["Enter a number:  "], should_exit=True)
                
                menu2.append_item(one_email)
                menu2.append_item(number_of_emails)
                menu2.show()
                menu2.join()
                getted_number = number_of_emails.return_value
                selection2 = menu2.selected_option
                #print selection2, getted_number
                if selection2 == 0:
                    status = False
                    number = 1
                else:
                    try:
                        if unicode(getted_number).isnumeric() or isinstance(getted_number, int):
                            number = int(getted_number)
                            status = False
                            
                        else:
                            self.logger.error("InputErr: Given Object is not an integer. Please retype your input! (in 5 seconds...)", exc_info=self._logger_traceback) 
                            time.sleep(3)

                    except Exception, e:
                        self.logger.critical("EmailNumberGetterError: '{}'. ".format(e))

            ## Part2 : Get Email 
            getted_emails = []
            i=0
            while i < number:
                email = str(raw_input("(#{} from {}) Enter Email: ".format(i+1, number)))
                is_valid = validate_email(email)
                if is_valid:
                    getted_emails.append(email)
                    i+= 1
                else: 
                    self.logger.warning( "EmailValidationError: Given Email is not valid. Please retype it.")
                    
        else:
            pass    

        self._user_data["email"] = getted_emails

        return getted_emails
       





    def _cli_menu_error_agreement(self):
        menu = SelectionMenu(["No", "Yes"],
                    title="Error-Tracking Agreement.",
                    #subtitle="(agreement)",
                    prologue_text="This package use a nice possibility of the online error tracking.\n It means, if you will get an error than the developers could get an notice about it in the real time. Are you agree to send information about errors directly to developers?",
                    #epilogue_text="222"
                    )
        menu.show()
        selection = menu.selected_option
        self._user_data["error_tracking"] = False if selection==0 else True

        return selection





    def _cli_menu_get_from_user_twitter_credentials(self):
        if not internet_on():
            self.logger.critical("InternetConnectionError: No Internet connection was found. Please check your connection to Internet and repeat this step. (Internet Connection is needed to validate your Twitter Credentials.)")
            sys.exit()
            #return []

        getted_credentials = []

        def _get_input(args):
            getted_input = input(args)
            return str(getted_input)
        # Create the menu
        menu1 = SelectionMenu(["No", "Yes"],
                    title="Twitter API Credentials.",
                    #subtitle="",
                    prologue_text="If you want to stream Twitter via official Twitter API than you need to enter your account Credentials. To get more information about it - please consult a README File of this package  (https://github.com/savin-berlin/zas-rep-tools). Under 'Start to use streamer' you can see  how you can exactly get this data. Do you want to enter this data now?",
                    #epilogue_text="222"
                    )


        menu1.show()
        menu1.join()
        selection1 = menu1.selected_option
        #print selection1

        if selection1 == 1:
            # Part 1: Get number of emails 
            status = True
            while status:
                menu2 = ConsoleMenu(
                                    title="Number of twitter accounts.",
                                    #subtitle="(via Email)",
                                    prologue_text="How much twitter accounts do you want to set up?",
                                    #epilogue_text="222"
                                    )
                one_email = SelectionItem("one", 0)
                number_of_emails = FunctionItem("many", function=raw_input, args=["Enter a number:  "], should_exit=True)
                
                menu2.append_item(one_email)
                menu2.append_item(number_of_emails)
                menu2.show()
                menu2.join()
                getted_number = number_of_emails.return_value
                selection2 = menu2.selected_option
                #print selection2, getted_number
                if selection2 == 0:
                    status = False
                    number = 1
                else:
                    try:
                        if unicode(getted_number).isnumeric() or isinstance(getted_number, int):
                            number = int(getted_number)
                            status = False
                            
                        else:
                            self.logger.error("InputErr: Given Object is not an integer. Please retype your input! (in 5 seconds...)", exc_info=self._logger_traceback)
                            #print "InputErr: Given Object is not an integer. Please retype your input! (in 5 seconds...)"
                            time.sleep(3)

                    except Exception, e:
                        self.logger.error("EmailNumberGetterError: '{}'. ".format(e), exc_info=self._logger_traceback)

            ## Part2 : Get Email 
            i=0
            while i < number:
                print "\n\n(#{} from {}) Enter Twitter Credentials: ".format(i+1, number)
                consumer_key = raw_input("Enter consumer_key: ")
                consumer_secret = raw_input("Enter consumer_secret: ")
                access_token = raw_input("Enter access_token: ")
                access_token_secret = raw_input("Enter access_token_secret: ")

                
                if internet_on():
                    api = twitter.Api(consumer_key=consumer_key,
                                    consumer_secret=consumer_secret,
                                    access_token_key=access_token,
                                    access_token_secret=access_token_secret)
                    try:
                        if api.VerifyCredentials():
                            getted_credentials.append({"consumer_key":consumer_key,
                                        "consumer_secret":consumer_secret,
                                        "access_token":access_token,
                                        "access_token_secret":access_token_secret
                                        })
                            i +=1
                        else:
                            print "InvalidCredential: Please retype them."

                    except Exception, e:
                        if "Invalid or expired token" in str(e):
                            self.logger.critical("InvalidCredential: Please retype them.")
                        elif "Failed to establish a new connection" in str(e):
                            self.logger.critical("InternetConnectionFailed: '{}' ".format(e))
                        else:
                            self.logger.critical("TwitterCredentialsCheckerError: '{}' ".format(e))
                        
                else:
                    self.logger.critical("InternetConnectionError: No Internet connection was found. Please check your connection to Internet and repeat this step. (Internet Connection is needed to validate your Twitter Credentials.)")
                    sys.exit()

        else:
            pass    

        self._user_data["twitter_creditials"] = getted_credentials

        return getted_credentials







    def _check_correctness_of_the_test_data(self):

        ## Check mapping of columns and values 
        try:
            for template, data_columns in self._columns_in_doc_table.iteritems():
                for  data_values in self.docs_row_values(token=True, unicode_str=True)[template]:
                    #p((len(data_columns), len(data_values)))
                    if len(data_columns) != len(data_values):
                        self.logger.error("TestDataCorruption: Not same number of columns and values.", exc_info=self._logger_traceback)
                        return False

        except Exception, e:
            #p([(k,v) for k,v in self._columns_in_doc_table.iteritems()])
            #p(self.docs_row_values(token=True, unicode_str=True))
            self.logger.error("TestDataCorruption: Test Data in Configer is inconsistent. Probably  - Not same template_names in columns and rows. See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            return False
        return True
        #sys.exit()

        # ##### Encrypted #######

    ###########################Preprocessing###############







####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
###################################Other Classes#####################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################









