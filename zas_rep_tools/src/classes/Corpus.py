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
#import regex
import logging
import threading
#import multiprocessing
import time
#import datetime
import Queue
#import cPickle as pickle
import json
import traceback
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from textblob_de import TextBlobDE
import langid
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_HALF_DOWN, ROUND_DOWN



from collections import defaultdict
from raven import Client
#from cached_property import cached_property
#import types
import execnet
from nltk.tokenize import TweetTokenizer
#import subprocess
import enlighten

from  zas_rep_tools.src.extensions.tweet_nlp.ark_tweet_nlp.CMUTweetTagger import check_script_is_present, runtagger_parse
#from somajo import Tokenizer, SentenceSplitter
#from zas_rep_tools.src.classes.configer import Configer


from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, LenGen, path_to_zas_rep_tools, char_is_emoji, text_has_emoji, char_is_punkt, text_has_punkt, text_is_punkt, text_is_emoji, categorize_token_list, removetags, remove_html_codded_chars, get_number_of_streams_adjust_cpu, Rle
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.reader import Reader
from zas_rep_tools.src.utils.logger import *
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation



import platform
if platform.uname()[0].lower() !="windows":
    #p("hjklhjk")
    import colored_traceback
    colored_traceback.add_hook()
    os.system('setterm  -back black -fore white -store -clear')
    #os.system('setterm -term linux -back 0b2f39 -fore a3bcbf -store -clear')
else:
    import colorama
    os.system('color 09252d') # change background colore of the terminal 



class Corpus(object):

    info = {
            "tagger":{
                        "tweetnlp":{
                                    "url": "http://www.cs.cmu.edu/~ark/TweetNLP/",
                                    "paper":"http://www.cs.cmu.edu/~ark/TweetNLP/owoputi+etal.naacl13.pdf",
                                    "tagset": {
                                                "data":{
                                                         '!': 'interjection',
                                                         '#': 'hashtag (indicates topic/category for tweet)',
                                                         '$': 'numeral',
                                                         '&': 'coordinating conjunction',
                                                         ',': 'punctuation',
                                                         '@': 'at-mention (indicates a user as a recipient of a tweet)',
                                                         'A': 'adjective',
                                                         'D': 'determiner',
                                                         'E': 'emoticon',
                                                         'G': 'other abbreviations, foreign words, possessive endings, symbols, garbage',
                                                         'L': 'nominal + verbal (e.g. i\xe2\x80\x99m), verbal + nominal (let\xe2\x80\x99s)',
                                                         'M': 'proper noun + verbal',
                                                         'N': 'common noun',
                                                         'O': 'pronoun (personal/WH; not possessive)',
                                                         'P': 'pre- or postposition, or subordinating conjunction',
                                                         'R': 'adverb',
                                                         'S': 'nominal + possessive',
                                                         'T': 'verb particle',
                                                         'U': 'URL or email address',
                                                         'V': 'verb including copula, auxiliaries',
                                                         'X': 'existential there, predeterminers',
                                                         'Y': 'X + verbal',
                                                         'Z': 'proper noun + possessive',
                                                         '^': 'proper noun',
                                                         '~': 'discourse marker, indications of continuation across multiple tweets'
                                                      },

                                                },
                                    },
                        "someweta":{
                                    "url": "https://github.com/tsproisl/SoMeWeTa",
                                    "paper":"http://www.lrec-conf.org/proceedings/lrec2018/pdf/49.pdf",
                                    "tagset":{
                                              "name": "STTS IBK tagset",
                                              "url":["http://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/TagSets/stts-table.html", ],
                                              "paper":"https://ids-pub.bsz-bw.de/frontdoor/deliver/index/docId/5065/file/Beisswenger_Bartz_Storrer_Tagset_und_Richtlinie_fuer_das_PoS_Tagging_2015.pdf",
                                              "data": {
                                                         '$(': 'sonstige Satzzeichen; satzintern',
                                                         '$,': 'Komma',
                                                         '$.': 'Satzbeendende Interpunktion',
                                                         'ADJA': 'attributives Adjektiv',
                                                         'ADJD': 'adverbiales oder pr\xc3\xa4dikatives Adjektiv',
                                                         'ADR': 'Adressierung',
                                                         'ADV': 'Adverb',
                                                         'ADVART': 'Kontraktion: Adverb + Artikel',
                                                         'AKW': 'Aktionswort',
                                                         'APPO': 'Postposition',
                                                         'APPR': 'Pr\xc3\xa4position, Zirkumposition links',
                                                         'APPRART': 'Pr\xc3\xa4position mit Artikel',
                                                         'APZR': 'Zirkumposition rechts',
                                                         'ART': 'bestimmter oder unbestimmter Artikel',
                                                         'CARD': 'Kardinalzahl',
                                                         'DM': 'Diskursmarker',
                                                         'EML': 'E-Mail-Adresse',
                                                         'EMOASC': 'Emoticon, als Zeichenfolge dargestellt (Typ \xe2\x80\x9eASCII\xe2\x80\x9c)',
                                                         'EMOIMG': 'Emoticon, als Grafik-Ikon dargestellt (Typ \xe2\x80\x9eImage\xe2\x80\x9c)',
                                                         'FM': 'Fremdsprachliches Material',
                                                         'HST': 'Hashtag',
                                                         'ITJ': 'Interjektion',
                                                         'KOKOM': 'Vergleichspartikel ohne Satz',
                                                         'KON': 'nebenordnende Konjunktion',
                                                         'KOUI': 'unterordnende Konjunktion mit \xe2\x80\x9ezu\xe2\x80\x9c und Infinitiv',
                                                         'KOUS': 'unterordnende Konjunktion mit Satz (VL-Stellung)',
                                                         'KOUSPPER': 'Kontraktion: unterordnende Konjunk- tion mit Satz (VL-Stellung) + irreflexi- ves Personalpronomen',
                                                         'NE': 'Eigennamen',
                                                         'NN': 'Appellativa',
                                                         'ONO': 'Onomatopoetikon',
                                                         'PAV': 'Pronominaladverb',
                                                         'PDAT': 'attributierendes Demonstrativprono- men',
                                                         'PDS': 'substituierendes Demonstrativprono- men',
                                                         'PIAT': 'attributierendes Indefinitpronomen ohne Determiner',
                                                         'PIDAT': 'attributierendes Indefinitpronomen mit Determiner',
                                                         'PIS': 'substituierendes  Indefinitpronomen',
                                                         'PPER': 'irreflexives Personalpronomen',
                                                         'PPERPPER': 'Kontraktion: irreflexives Personalpro- nomen + irreflexives Personalprono- men',
                                                         'PPOSAT': 'attributierendes  Possesivpronomen',
                                                         'PPOSS': 'substituierendes  Possesivpronomen',
                                                         'PRELAT': 'attributierendes Relativpronomen',
                                                         'PRELS': 'substituierendes Relativpronomen',
                                                         'PRF': 'reflexives Personalpronomen',
                                                         'PTKA': 'Partikel bei Adjektiv oder Adverb',
                                                         'PTKANT': 'Antwortpartikel',
                                                         'PTKIFG': 'Intensit\xc3\xa4ts-, Fokus- oder  Gradpartikel',
                                                         'PTKMA': 'Modal- oder Abt\xc3\xb6nungspartikel',
                                                         'PTKMWL': 'Partikel als Teil eines Mehrwort- Lexems',
                                                         'PTKNEG': 'Negationspartikel',
                                                         'PTKVZ': 'abgetrennter Verbzusatz',
                                                         'PTKZU': '\xe2\x80\x9ezu\xe2\x80\x9c vor Infinitiv',
                                                         'PWAT': 'attributierendes  Interrogativpronomen',
                                                         'PWAV': 'adverbiales Interrogativ- oder Relativ- pronomen',
                                                         'PWS': 'substituierendes Interrogativprono- men',
                                                         'TRUNC': 'Kompositions-Erstglied',
                                                         'URL': 'Uniform Resource Locator',
                                                         'VAFIN': 'finites Verb, aux',
                                                         'VAIMP': 'Imperativ, aux',
                                                         'VAINF': 'Infinitiv, aux',
                                                         'VAPP': 'Partizip Perfekt, aux',
                                                         'VAPPER': 'Kontraktion: Auxiliarverb + irreflexives Personalpronomen',
                                                         'VMFIN': 'finites Verb, modal',
                                                         'VMINF': 'Infinitiv, modal',
                                                         'VMPP': 'Partizip Perfekt, modal',
                                                         'VMPPER': 'Kontraktion: Modalverb + irreflexives Personalpronomen',
                                                         'VVFIN': 'finites Verb, voll',
                                                         'VVIMP': 'Imperativ, voll',
                                                         'VVINF': 'Infinitiv, voll',
                                                         'VVIZU': 'Infinitiv mit \xe2\x80\x9ezu\xe2\x80\x9c, voll',
                                                         'VVPP': 'Partizip Perfekt, voll',
                                                         'VVPPER': 'Kontraktion: Vollverb + irreflexives Personalpronomen',
                                                         'XY': 'Nichtwort, Sonderzeichen  enthaltend'
                                                         },
                                            },
                                    }
                    },

            "splitter":{
                        "somajo":{},

                        },

            "tokenizer":{
                        "somajo":{},
                        "nltk":{},
                        },


        }
    #### Tokenizer
    tokenizer_for_languages = {
                    "en":["somajo","nltk"],
                    "de":["somajo"],
                    "test":["somajo"],
                    }
    supported_languages_tokenizer = [key for key in tokenizer_for_languages] 
    supported_tokenizer = set([v  for values in tokenizer_for_languages.itervalues() for v in values])
    

    ### Sent Splitters
    sent_splitter_for_languages = {
                "en":["somajo"],
                "de":["somajo"],
                "test":["somajo"],
                }
    supported_languages_sent_splitter = [key for key in sent_splitter_for_languages] 
    supported_sent_splitter = set([v  for values in sent_splitter_for_languages.itervalues() for v in values])
    


    ###POS-Taggers
    pos_tagger_for_languages = {
                "en":["tweetnlp","someweta"],
                "de":["someweta"],
                "fr":["someweta"],
                "test":["tweetnlp"],
                }
    supported_languages_pos_tagger = [key for key in pos_tagger_for_languages] 
    supported_pos_tagger = set([v  for values in pos_tagger_for_languages.itervalues() for v in values])
    pos_tagger_models = {
            "tweetnlp":{"en":[]},
            "someweta":{
                    "de":["german_web_social_media_2017-12-20.model", "german_newspaper_for_empirist_2017-12-20.model"],
                    "en":["english_newspaper_2017-09-15.model"],
                    "fr":["french_newspaper_2018-06-20.model"],
                    "test":["english_newspaper_2017-09-15.model"],
                    }
            }



    ### Sentiment Anylysers
    sentiment_analyzer_for_languages = {
                    "en":["textblob"],
                    "de":["textblob"],
                    "fr":["textblob"],
                    "test":["textblob"],
                    }
    supported_languages_sentiment_analyzer = [key for key in sentiment_analyzer_for_languages] 
    supported_sentiment_analyzer = set([v  for values in sentiment_analyzer_for_languages.itervalues() for v in values])
    





    #preprocession=True, lang_classification=True,  tokenizer=False, pos_tagger=False,sent_splitter=False, del_url=False, del_punkt = False, case_sensitiv=True, del_num=False, del_mention=False, del_hashtag=False, sentiment_analyzer=True

    def __init__(self, language="de", preprocession=True, lang_classification=False,
                tokenizer=True, pos_tagger=False,sent_splitter=False, sentiment_analyzer=False,
                tok_split_camel_case=True, 
                del_url=False, del_punkt = False, del_num=False, del_mention=False, del_hashtag=False, del_html=False,
                case_sensitiv=True,
                stop_if_db_already_exist=False ,rewrite=False,
                logger_folder_to_save=False,  logger_usage=True, logger_level=logging.INFO,
                logger_save_logs=True, logger_num_buffered=5, error_tracking=True,
                ext_tb=False, logger_traceback=False, mode="free"):
        #p(Metaclass.__dict__)
        
        ## Set Mode: Part 1
        self._mode = mode
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs = set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs
        #p(mode)
        #logger_level = logging.ERROR
        #p(logger_level)
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
        self._language = language
        self._tokenizer= tokenizer
        self._pos_tagger = pos_tagger
        self._sentiment_analyzer = sentiment_analyzer
        self._sent_splitter = sent_splitter
        self._preprocession = preprocession
        self._lang_classification = lang_classification if self._language != "test" else False
        self._del_url = del_url
        self._del_punkt = del_punkt
        self._del_num = del_num
        self._del_mention = del_mention
        self._del_hashtag = del_hashtag
        self._del_html = del_html
        self._case_sensitiv = case_sensitiv

        self._stop_if_db_already_exist = stop_if_db_already_exist
        self._rewrite = rewrite

        #self.insertion_status_extended = defaultdict(lambda:defaultdict(lambda:0))
        self.insertion_status_extended = defaultdict(lambda:lambda:0)
        self.inserted_insertion_status_general = defaultdict(lambda:0)
        self.error_insertion_status_general = defaultdict(lambda:0)
        self.empty_insertion_status_general = defaultdict(lambda:0)

        self._tok_split_camel_case = tok_split_camel_case




        #p(inpdata)

        #InstanceAttributes: Initialization
        self.db = False
        self.preprocessors = defaultdict(dict)
        self.active_threads = []

        self.status_bars_manager =  self._get_status_bars_manager()
        #self.opened_gateways = []
        # locally use "eventlet", remotely use "thread" model
        execnet.set_execmodel("eventlet", "thread")
        self.opened_gateways = execnet.Group()

        self.threads_error_bucket = Queue.Queue()
        # self.threads_success_bucket = Queue.Queue()
        self.threads_status_bucket = Queue.Queue()
        self.threads_success_exit = []
        self.threads_unsuccess_exit = []
        self.channels_error_bucket = Queue.Queue()
        self.status_bars_bucket = Queue.Queue()

        
        # self.preprocessors = {
        #             "thread1": 
        #                     {"splitter":xxx,
        #                      "tokenizer":xxx,
        #                      "pos":xxx, 
        #                         }
        #             }

        self.additional_attr = {
                "preprocession":self._preprocession,
                "tokenizer":self._tokenizer,
                "sent_splitter":self._sent_splitter,
                "pos_tagger":self._pos_tagger,
                "sentiment_analyzer":self._sentiment_analyzer,
                "lang_classification":self._lang_classification,
                "del_url":self._del_url,
                "del_punkt":self._del_punkt ,
                "del_num":self._del_num,
                "del_html":self._del_html,
                "del_mention":self._del_mention,
                "del_hashtag":self._del_hashtag,
                "case_sensitiv":self._case_sensitiv,
                }
        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})

        # Validate Input variables
        if False in set(list(self._valid_input())):
            self.logger.error("InputValidationError: Corpus Instance can not be initialized!", exc_info=self._logger_traceback)
            sys.exit()


        self.logger.debug('Intern InstanceAttributes was initialized')


        self.logger.debug('An instance of Corpus() was created ')


    # def __del__(self):
    #     self.logger.newline(1)


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




    ###########################INITS + Open##########################


    def init(self, prjFolder, DBname, language,  visibility, platform_name,
                    encryption_key=False,fileName=False, source=False, license=False,
                    template_name=False, version=False,
                    additional_columns_with_types_for_documents=False, corpus_id=False):

        if self.db:
            self.logger.error("CorpusInitError: An active Corpus Instance was found. Please close already initialized/opened Corpus, before new initialization.", exc_info=self._logger_traceback)
            return False

        self.db = DBHandler(stop_if_db_already_exist=self._stop_if_db_already_exist, rewrite=self._rewrite,
                    logger_level= self._logger_level, 
                    logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,
                    logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs,
                    mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)
        was_initialized =  self.db.init("corpus", prjFolder, DBname, language, visibility,
            platform_name=platform_name,encryption_key=encryption_key, fileName=fileName,
            source=source, license=license, template_name=template_name, version=version,
            additional_columns_with_types_for_documents=additional_columns_with_types_for_documents,
            corpus_id=corpus_id)
        #p(was_initialized, "was_initialized")
        if not was_initialized:
            self.logger.debug("CorpInit: Current Corpus for following attributes  wasn't initialized: 'dbtype='{}'; 'dbname'='{}; id='{}'; encryption_key='{}'; template_name='{}'; language='{}'.".format("corpus", DBname,corpus_id, encryption_key, template_name, language))
            return False
        #self.db.add_attributs()
        
        self.db.update_attrs(self.additional_attr)

        if self.db.exist():
            self.logger.info("CorpusInit: '{}'-Corpus was successful initialized.".format(DBname))
            return True
        else:
            self.logger.error("CorpusInit: '{}'-Corpus wasn't  initialized.".format(DBname), exc_info=self._logger_traceback)
            return False

    
    def close(self):
        self.db.close()
        self.db = False

    def _close(self):
        self.db._close()
        self.db = False


    def open(self, path_to_corp_db, encryption_key=False):

        if self.db:
            self.logger.error("CorpusOpenerError: An active Corpus Instance was found. Please close already initialized/opened Corpus, before new initialization.", exc_info=self._logger_traceback)
            return False

        self.db = DBHandler(logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)
        self.db.connect(path_to_corp_db, encryption_key=encryption_key)


        if self.db.exist():
            #p(self.db.typ())
            if self.db.typ() != "corpus":
                self.logger.error("Current DB is not an Corpus.")
                self._close()
                return False
            self.logger.info("CorpusOpener: '{}'-Corpus was successful opened.".format(os.path.basename(path_to_corp_db)))
            return True
        else:
            self.logger.error("CorpusOpener: Unfortunately '{}'-Corpus wasn't opened.".format(os.path.basename(path_to_corp_db)), exc_info=self._logger_traceback)
            return False

    def info(self):
        return self.db.get_all_attr()

    ###########################Setters######################






    def _insert(self, inp_data, tablename="documents",text_field_name="text",  thread_name="Thread0", status_bar=False, log_ignored=True):
        try:
            #self._rle = Rle()

            if self._preprocession:
                if thread_name not in self.preprocessors:
                    if not self._init_preprocessors(thread_name=thread_name, status_bar=status_bar):
                        self.logger.error("Error during Preprocessors initialization. Thread '{}' was stopped.".format(thread_name), exc_info=self._logger_traceback)
                        self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":"Error during Preprocessors initialization"})
                        return False
            
            self.logger.debug("_InsertionProcess: Was started for '{}'-Thread. ".format(thread_name))
            if status_bar:
                status_bar_of_insertions = self._get_new_status_bar(len(inp_data), "{}:Insertion".format(thread_name), "files")
            
            for row_as_dict in inp_data:
                #self.logger.critical(row_as_dict)
                #p(row_as_dict)
                text_preprocessed = False
                if self._preprocession:
                    try:
                        if row_as_dict:
                            preproc = self._preprocessing(row_as_dict[text_field_name],thread_name=thread_name, log_ignored=log_ignored)
                            if preproc:
                                text_preprocessed = json.dumps(preproc)
                            else:
                                text_preprocessed = preproc
                            #p(text_preprocessed, "text_preprocessed")
                        else:
                            self.empty_insertion_status_general[thread_name] +=1
                            if status_bar:
                                status_bar_of_insertions.total -= 1
                            if log_ignored:
                                self.logger.warning("IgnoredRow: '{}'. (row was given already empty).".format(row_as_dict))
                            continue

                    except KeyError, e: 
                        print_exc_plus() if self._ext_tb else ""
                        self.logger.error("PreprocessingError: (KeyError) See Exception: '{}'. Probably text_field wasn't matched. The wrong text_field name was given or row  was given as list and not as dict.   ".format(e), exc_info=self._logger_traceback)
                        self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
                        return False
                    except Exception, e:
                        self.logger.error("PreprocessingError:  See Exception: '{}'. ".format(e),  exc_info=self._logger_traceback)
                        self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
                        return False

                    if text_preprocessed:
                        row_as_dict[text_field_name] = text_preprocessed
                    else:
                        #self.logger.warning("Text in the current DictRow (id='{}') wasn't preprocessed. This Row was ignored.".format(row_as_dict["id"]))
                        self.empty_insertion_status_general[thread_name] +=1
                        if status_bar:
                            status_bar_of_insertions.total -= 1
                        if log_ignored:
                            # if isinstance(output, unicode):
                            #     to_log_orig = output.encode("utf-8")
                            # else:
                            #     to_log_orig = output
                            self.logger.warning("IgnoredRow: '{}'. (after Preprocessing. Probably was out-sorted from language classifier). \n\n\n".format(row_as_dict))
                        continue

                if self.db.lazyinsert( tablename, row_as_dict):
                    self.inserted_insertion_status_general[thread_name] +=1
                    if status_bar:
                        status_bar_of_insertions.update(incr=1)
                else:
                    #self.db.
                    self.error_insertion_status_general[thread_name] +=1
                    if status_bar:
                        status_bar_of_insertions.total -= 1
                    if log_ignored:
                        self.logger.warning("IgnoredRow: '{}'. (wasn't inserted into DB.) \n\n\n".format(row_as_dict))
                    continue
                #else:
                #    self.logger.critical("Preprocession was ")

            if status_bar:
                status_bar_of_insertions.refresh()
                status_bar_of_insertions.close(clear=False)
            self.logger.debug("_Insert: '{}'-Thread is done and was stopped.".format(thread_name))
            self.threads_status_bucket.put({"name":thread_name, "status":"done"})
            self.db.commit()
            return True   

        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("_InsertError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
            return False




    def insert(self, inp_data, tablename="documents",text_field_name="text",  thread_name="Thread0", status_bar = True, allow_big_number_of_streams=False, number_of_allow_streams=8, log_ignored=True):
        try:
            #p(type(inp_data), "inp_data")
            #self.logger.critical(("1", type(inp_data),inp_data))
            if isinstance(inp_data, LenGen):
                inp_data= [inp_data]
            elif isinstance(inp_data, list) and isinstance(inp_data[0], dict):
                inp_data = [inp_data]
            #self.logger.critical(("2", type(inp_data),inp_data))
            #p(inp_data)
            # starting computing for this corpus
            #Manager.term
            #self.status_bars_manager.term print(t.bold_red_on_bright_green('It hurts my eyes!'))
            if status_bar:
                status_bar_starting_corpus_insertion = self._get_new_status_bar(None, self.status_bars_manager.term.center('{}'.format(self.db.fname()) ) , "", counter_format=self.status_bars_manager.term.bold_black_on_white("{fill}{desc}{fill}"))
                #status_bar_starting_corpus_insertion.update(incr=10)
                status_bar_starting_corpus_insertion.refresh()
            ## threads
            if status_bar:
                status_bar_threads_init = self._get_new_status_bar(len(inp_data), "ThreadsStarted", "threads")
            i=1

            if len(inp_data)>=number_of_allow_streams:
                if not allow_big_number_of_streams:
                    self.logger.critical("Number of given streams is to big ('{}'). It it allow to have not more as {} streams/threads parallel. If you want to ignore this border set 'allow_big_number_of_streams' to True. But it also could mean, that the type of data_to_insert is not correct. Please check inserted data. It should be generator/list of rows (packed as dict).".format(len(inp_data),number_of_allow_streams))
                    return False

            for gen in inp_data:
                #p(gen, "gen")
                #self.logger.critical(("3", type(gen), gen ))
                if not self._isrighttype(gen):
                    self.logger.error("InsertionError: Given InpData not from right type. Please given an list or an generator.", exc_info=self._logger_traceback)
                    return False


                thread_name = "Thread{}".format(i)
                processThread = threading.Thread(target=self._insert, args=(gen, tablename, text_field_name,  thread_name, status_bar, log_ignored), name=thread_name)
                processThread.setDaemon(True)
                processThread.start()
                self.active_threads.append(processThread)
                if status_bar:
                    status_bar_threads_init.update(incr=1)
                i+=1
                time.sleep(2)

            #p("All Threads was initialized", "insertparallel")  
            self.logger.info("'{}'-thread(s) was started. ".format(len(self.active_threads)))

            time.sleep(3)

            self._wait_till_all_threads_are_completed(thread_name)

            self._print_summary_status()
            self.opened_gateways.terminate()


            
            if status_bar:
                was_inserted = sum(self.inserted_insertion_status_general.values()) 
                error_insertion = sum(self.error_insertion_status_general.values())
                empty_insertion = sum(self.empty_insertion_status_general.values())
                was_ignored = error_insertion + empty_insertion
                status_bar_total_summary = self._get_new_status_bar(None, self.status_bars_manager.term.center("Total_Inserted: '{}';  Total_Ignored: '{}'  ('{}'-error, '{}'-outsorted).".format(was_inserted, was_ignored,error_insertion,empty_insertion ) ), "",  counter_format=self.status_bars_manager.term.bold_black_on_white('{fill}{desc}{fill}'))
                status_bar_total_summary.refresh()
                self.status_bars_manager.stop()

            if len(self.threads_unsuccess_exit) >0:
                return False
            else:
                return True

        except KeyboardInterrupt:
            self.logger.warning("KeyboardInterrupt: Process was stopped from User. Some inconsistence in the current DB may situated.")
            sys.exit()
        except Exception, e:
            self.logger.error(" See Exception: '{}'. ".format(e),  exc_info=self._logger_traceback)




    # def insert(self, inp_data, datatyp="dict", tablename="documents",text_field_name="text",  thread_name="Thread0", status_bar = True):
    #     try:
    #         if not self._isrighttype(inp_data):
    #             self.logger.error("InsertError: Given InputData is not from right type!", exc_info=self._logger_traceback)
    #             return False

    #         thread_name = thread_name
    #         if status_bar:
    #             status_bar_threads_init = self._get_new_status_bar(1, "ThreadsStarted", "threads")
    #         processThread = threading.Thread(target=self._insert, args=(inp_data,datatyp, tablename, text_field_name,  thread_name, status_bar), name=thread_name)
    #         processThread.setDaemon(True)
    #         processThread.start()
    #         if status_bar:
    #             status_bar_threads_init.update(incr=1)

    #         self.active_threads.append(processThread)
    #         self.logger.info("'{}'-thread(s) was started. ".format(len(self.active_threads)))
    #         time.sleep(3)
 
    #         self._wait_till_all_threads_are_completed()
    #         # self._init_status_bar([inp_data])
    #         # self._update_status_bar()
    #         self._print_summary_status()
    #         self.opened_gateways.terminate()
    #     except KeyboardInterrupt:
    #         self.logger.warning("KeyboardInterrupt: Process was stopped from User. Some inconsistence in the current DB may situated.")
    #         sys.exit()


    # def insertparallel(self, list_with_generators, datatyp="dict", tablename="documents",text_field_name="text",  status_bar=True):
    #     try:
    #         if not self._check_db_should_exist():
    #             return False

    #         status_bar_threads_init = self._get_new_status_bar(len(list_with_generators), "ThreadsStarted", "threads")
    #         i=1
    #         for gen in list_with_generators:
    #             if not self._isrighttype(gen):
    #                 self.logger.error("InsertionError: Given InpData not from right type. Please given an list or an generator.", exc_info=self._logger_traceback)
    #                 return False


    #             thread_name = "Thread{}".format(i)
    #             processThread = threading.Thread(target=self._insert, args=(gen,datatyp, tablename, text_field_name,  thread_name, status_bar), name=thread_name)
    #             processThread.setDaemon(True)
    #             processThread.start()
    #             self.active_threads.append(processThread)
    #             status_bar_threads_init.update(incr=1)
    #             i+=1
    #             time.sleep(2)

    #         #p("All Threads was initialized", "insertparallel")  
    #         self.logger.info("'{}'-thread(s) was started. ".format(len(self.active_threads)))

    #         time.sleep(3)

    #         self._wait_till_all_threads_are_completed()

    #         self._print_summary_status()
    #         self.opened_gateways.terminate()
    #     except KeyboardInterrupt:
    #         self.logger.warning("KeyboardInterrupt: Process was stopped from User. Some inconsistence in the current DB may situated.")
    #         sys.exit()




    ###########################Getters#######################

    def _intern_docs_getter(self, columns=False, select=False,  where=False, connector_where="AND", output="list", size_to_fetch=1000, limit=-1, offset=-1):
        if not self._check_db_should_exist():
            yield False
            return 
        for row in self.db.lazyget("documents", columns=columns, select=select, where=where, connector_where=connector_where, output=output, size_to_fetch=size_to_fetch, limit=limit, offset=offset):
            yield row


    def docs(self, columns=False, select=False,  where=False, connector_where="AND", output="list", size_to_fetch=1000, limit=-1, offset=-1, stream_number=1, adjust_to_cpu=True, min_files_pro_stream=1000):
        row_number = self.db.rownum("documents")
        #p((row_number))
        wish_stream_number = stream_number
        if stream_number <1:
            stream_number = 1000000
            adjust_to_cpu = True
            self.logger.debug("StreamNumber is less as 1. Automatic computing of strem number according cpu was enabled.")


        if adjust_to_cpu:
            stream_number= get_number_of_streams_adjust_cpu( min_files_pro_stream, row_number, stream_number)
            if stream_number is None:
                self.logger.error("Number of docs in the table is 0. No one generator could be returned.")
                return []

        
        list_with_generators = []
        number_of_files_per_stream = int(Decimal(float(row_number)/stream_number).quantize(Decimal('1.'), rounding=ROUND_UP))
        


        if stream_number > row_number:
            self.logger.error("StreamNumber is higher as number of the files to read. This is not allowed.")
            return False

        current_index = 0


        for i in range(stream_number):
            #p(i, "i")
            if i < (stream_number-1): # for gens in between 
                new_index = current_index+number_of_files_per_stream
                gen  = self._intern_docs_getter( columns=columns, select=select,  where=where, connector_where=connector_where, output=output, size_to_fetch=size_to_fetch, limit=number_of_files_per_stream, offset=current_index)
                lengen = LenGen(gen, number_of_files_per_stream)
                current_index = new_index
            else: # for the last generator
                gen  = self._intern_docs_getter( columns=columns, select=select,  where=where, connector_where=connector_where, output=output, size_to_fetch=size_to_fetch, limit=-1, offset=current_index)
                lengen = LenGen(gen, row_number-current_index)

            if stream_number == 1:
                if wish_stream_number > 1 or wish_stream_number<=0:
                    #p((stream_number,wish_stream_number))
                    return [lengen]
                else:
                    return lengen
            list_with_generators.append(lengen)

        self.logger.debug(" '{}'-streams was created.".format(stream_number))
        return list_with_generators










    # ###########################Attributes####################


    # def update_attr(self,attribut_name, value):
    #     if not self._check_db_should_exist():
    #         return False

    #     if not self.db.update_attr(attribut_name, value,  dbname="main"):
    #         self.logger.error("AttrUpdate: Bot possible. ", exc_info=self._logger_traceback)
    #         return False

    # def add_attributs(self,attributs_names, values):
    #     if not self._check_db_should_exist():
    #         return False

    #     if not self.db.add_attributs(attributs_names, values, dbname="main"):
    #         self.logger.error("AttrUpdate: Bot possible. ", exc_info=self._logger_traceback)
    #         return False


    # def get_attr(self,attributName, dbname=False):
    #     if not self._check_db_should_exist():
    #         return False
    #     return self.db.get_attr(attributName, dbname="main")


    # def get_all_attr(self):
    #     if not self._check_db_should_exist():
    #         return False
    #     #p(self.db.get_all_attr("main"))
    #     return self.db.get_all_attr(dbname="main")







    ###########################Other Methods##################


    def exist(self):
        return True if self.db else False


    def db(self):
        if not self._check_db_should_exist():
            return False
        self.logger.debug("DBConnection was passed.")
        return self.db









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





    ###########################Input-Validation#############



    def _init_preprocessors(self, thread_name="Thread0", status_bar=False):
        try:
            if status_bar:
                status_bar_preprocessors_init = self._get_new_status_bar(4, "{}:PreprocessorsInit".format(thread_name), "unit")

            if not self._set_tokenizer(split_camel_case=self._tok_split_camel_case, language=self._language, thread_name=thread_name):
                return False
            if status_bar:
                status_bar_preprocessors_init.update(incr=1)
                status_bar_preprocessors_init.refresh()

            if self._sent_splitter:
                #is_tuple = True if True in [self._tok_token_classes,self._tok_extra_info] else False
                if not self._set_sent_splitter( thread_name=thread_name):
                    return False
                if status_bar:
                    status_bar_preprocessors_init.update(incr=1)
                    status_bar_preprocessors_init.refresh()
                    #status_bar_preprocessors_init.update(incr=1)

            if self._pos_tagger:
                if not self._set_pos_tagger(thread_name=thread_name):
                    return False
                if status_bar:
                    status_bar_preprocessors_init.update(incr=1)
                    status_bar_preprocessors_init.refresh()






            self._set_rle(thread_name)
            #self._rle = Rle() # repetitions encoder 
            #self.logger.debug("RleInit: RLE was initialized.")
            status_bar_preprocessors_init.update(incr=1)
            status_bar_preprocessors_init.refresh()


            # if self._sentiment_analyzer:
            #     if not self._set_sentiment_analyzer(thread_name=thread_name):
            #         return False
            #     if status_bar:
            #         status_bar_preprocessors_init.update(incr=1)
            #         status_bar_preprocessors_init.refresh()


            self.logger.info("PreprocessorsInit: All Preprocessors for '{}'-Thread was initialized.".format(thread_name))
            return True
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("PreprocessorsInitError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            return False

        

    def _get_status_bars_manager(self):
        config_status_bar = {'stream': sys.stdout,
                  'useCounter': True, 
                  "set_scroll": True,
                  "resize_lock": True
                  }
        enableCounter_status_bar = config_status_bar['useCounter'] and config_status_bar['stream'].isatty()
        return enlighten.Manager(stream=config_status_bar['stream'], enabled=enableCounter_status_bar, set_scroll=config_status_bar['set_scroll'], resize_lock=config_status_bar['resize_lock'])


    def _set_rle(self,  thread_name="Thread0"):
        self.logger.debug("INIT-RLE: Start the initialization of Run_length_encoder for '{}'-Thread.".format(thread_name))
        self.preprocessors[thread_name]["rle"] = Rle(self.logger)
        self.logger.debug("INIT-RLE: Run_length_encoder for '{}'-Thread was initialized.".format(thread_name))
        return True



    def _status_bars(self):
        if self.status_bars_manager:
            return self.status_bars_manager.counters
        else:
            self.logger.error("No activ Status Bar Managers was found.", exc_info=self._logger_traceback)
            return False




    def _wait_till_all_threads_are_completed(self, thread_name, sec_to_wait=3, sec_to_log = 15):
        time_counter = sec_to_log
        while (len(self.threads_success_exit)+len(self.threads_unsuccess_exit)) < len(self.active_threads):
            if time_counter >= sec_to_log:
                time_counter = 0
                self.logger.debug("Waiting in '{}'. ({}sec was gone.)".format(thread_name, sec_to_log))

            if not self.threads_status_bucket.empty():
                answer = self.threads_status_bucket.get()
                thread_name = answer["name"]
                status = answer["status"]
                if status == "done":
                    if thread_name not in self.threads_success_exit:
                        self.threads_success_exit.append(thread_name)
                elif status == "failed":
                    if thread_name not in self.threads_unsuccess_exit:
                        self.threads_unsuccess_exit.append(thread_name)
                else:
                    self.logger.error("ThreadWaiter: Unknown Status was sended: '{}'. Break the execution! ".format(status), exc_info=self._logger_traceback)
                    sys.exit()


                self.threads_status_bucket.task_done()

            time.sleep(sec_to_wait)
            time_counter += sec_to_wait
            #self._check_threads()
            self._check_buckets()

        self.logger.debug("Stop waiting in '{}'. ".format(thread_name))


    def _get_new_status_bar(self, total, desc, unit, counter_format=False):
        #counter_format
        if counter_format:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True, counter_format=counter_format)
        else:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True)
        return counter

    def _check_if_threads_still_alive(self):
        for thread in self.active_threads:
            if not thread.isAlive():
                yield False
            yield True



    # def _check_threads(self):
    #     if False in set(list(self._check_if_threads_still_alive())):
    #         self.logger.error("One or few Threads are not alive any more. It seems to be an error. Execution of this program is stopped....", exc_info=self._logger_traceback)
    #         sys.exit()


    def _check_buckets(self):
        status = False
        if not self.threads_error_bucket.empty():
            while not self.threads_error_bucket.empty():
                e = self.threads_error_bucket.get()
                self.threads_error_bucket.task_done()
                self.logger.error("InsertionError(in_thread_error_bucket): '{}'-Thread throw following Exception: '{}'. ".format(e[0], e[1]), exc_info=self._logger_traceback)
                status = True

        if not self.channels_error_bucket.empty():
            while not self.channels_error_bucket.empty():
                e = self.channels_error_bucket.get()
                self.channels_error_bucket.task_done()
                self.logger.error("InsertionError(in_channel_error_bucket): '{}'-Thread ('{}') throw following Exception: '{}'. ".format(e[0], e[1],e[2]), exc_info=self._logger_traceback)
                status = True

        if status:
            self.logger.error("BucketChecker: Some threads/channels throw exception(s). Program can not be executed. ".format(), exc_info=self._logger_traceback)
            sys.exit()


    def _print_summary_status(self):
        for thread in self.active_threads:
            thread_name = thread.getName()
            #thread.getName()
            self.error_insertion_status_general[thread_name]
            self.inserted_insertion_status_general[thread_name]
            self.logger.info("Summary for {}: Total inserted: {}; Total ignored: {}, from that was {} was error insertions and {} was out-sorted insertions (exp:  cleaned tweets/texts, ignored retweets, etc.).".format(thread_name, self.inserted_insertion_status_general[thread_name], self.error_insertion_status_general[thread_name]+ self.empty_insertion_status_general[thread_name], self.error_insertion_status_general[thread_name], self.empty_insertion_status_general[thread_name]))
        
        # for thread_name, status in self.inserted_insertion_status_general.iteritems():



    def _valid_input(self):
        if self._language not in Corpus.supported_languages_tokenizer:
            self.logger.error("InputValidationError: Given Language '{}' is not supported by tokenizer.".format(self._language), exc_info=self._logger_traceback)
            yield False

        if self._preprocession:
            ## Choice Tokenizer
            if self._tokenizer is False:
                self.logger.critical("Tokenizer is deactivate. For Text-Preprocessing tokenizer should be activate. Please activate tokenizer and run this tool one more time.")
                yield False
                return
            if not self._tokenizer or self._tokenizer is True:
                self._tokenizer = Corpus.tokenizer_for_languages[self._language][0]

            else:
                if self._tokenizer not in Corpus.supported_tokenizer:
                    self.logger.error("InputValidationError: Given Tokenizer '{}' is not supported.".format(self._tokenizer), exc_info=self._logger_traceback)
                    yield False
                if self._tokenizer not in Corpus.tokenizer_for_languages[self._language]:
                    self.logger.critical("InputValidationError: '{}'-tokenizer is not support '{}'-language. Please use another one. For this session the default one will be used. ".format(self._tokenizer, self._language))
                    self._tokenizer = Corpus.tokenizer_for_languages[self._language][0]
                    #yield False
            self.logger.debug("'{}'-Tokenizer was choiced.".format(self._tokenizer))



            ## Choice Sent Splitter
            if self._sent_splitter:
                if self._language not in Corpus.supported_languages_sent_splitter:
                    self.logger.error("InputValidationError: Given Language '{}' is not supported by Sentences Splitter.".format(self._language), exc_info=self._logger_traceback)
                    yield False
                if self._sent_splitter is True:
                    self._sent_splitter = Corpus.sent_splitter_for_languages[self._language][0]
                else:
                    if self._sent_splitter not in Corpus.supported_sent_splitter:
                        self.logger.error("InputValidationError: Given SentenceSplitter '{}' is not supported.".format(self._sent_splitter), exc_info=self._logger_traceback)
                        yield False
                    if self._sent_splitter not in Corpus.sent_splitter_for_languages[self._language]:
                        self.logger.critical("InputValidationError: '{}'-SentenceSplitter  is not support '{}'-language. Please use another one. For this session the default one will be used. ".format(self._sent_splitter, self._language))
                        self._sent_splitter = Corpus.sent_splitter_for_languages[self._language][0]
                self.logger.debug("'{}'-SentSplitter was choiced.".format(self._sent_splitter))


            ## Choice POS Tagger
            if self._pos_tagger:
                if self._language not in Corpus.supported_languages_pos_tagger:
                    self.logger.error("InputValidationError: Given Language '{}' is not supported by POS-Tagger.".format(self._language), exc_info=self._logger_traceback)
                    yield False
                if self._pos_tagger is True:
                    self._pos_tagger = Corpus.pos_tagger_for_languages[self._language][0]
                else:
                    if self._pos_tagger not in Corpus.supported_pos_tagger:
                        self.logger.error("InputValidationError: Given POS-Tagger '{}' is not supported.".format(self._pos_tagger), exc_info=self._logger_traceback)
                        yield False
                    if self._pos_tagger not in Corpus.pos_tagger_for_languages[self._language]:
                        self.logger.critical("InputValidationError: '{}'-POS-Tagger is not support '{}'-language. Please use another one. For this session the default one will be used. ".format(self._pos_tagger, self._language))
                        self._pos_tagger = Corpus.pos_tagger_for_languages[self._language][0]
                        #yield True
                    if not  self._sent_splitter:
                        self.logger.error("InputError: POS-Tagging require sentence splitter. Please use an option to activate it!",  exc_info=self._logger_traceback)
                        yield False
                self.logger.debug("'{}'-POS-Tagger was choiced.".format(self._pos_tagger))


            if self._sentiment_analyzer:
                if self._language not in Corpus.supported_languages_sentiment_analyzer:
                    self.logger.error("InputValidationError: Given Language '{}' is not supported by SentimentAnalyzer.".format(self._language), exc_info=self._logger_traceback)
                    yield False
                if self._sentiment_analyzer is True:
                    self._sentiment_analyzer = Corpus.sentiment_analyzer_for_languages[self._language][0]
                else:
                    if self._sentiment_analyzer not in Corpus.supported_sentiment_analyzer:
                        self.logger.error("InputValidationError: Given SentimentAnalyzer '{}' is not supported.".format(self._sentiment_analyzer), exc_info=self._logger_traceback)
                        yield False

                self.logger.debug("'{}'-SentimentAnalyzer was choiced.".format(self._sentiment_analyzer))


        else:
            self.logger.warning("Preprocessing is disable. -> it will be not possible to compute statistics for it. Please enable preprocessing, if you want to compute statistics later.")
            #yield False
        yield True 
        return 


        self._del_mention = del_mention
        self._del_hashtag = del_hashtag

    def _clean_sents_list(self, inp_sent_list):
        # Step 1: Find out what exactly should be erased
        tags_to_delete = []
        if self._del_url:
            tags_to_delete.append("URL")
        if self._del_punkt:
            tags_to_delete.append("symbol")
        if self._del_num:
            tags_to_delete.append("number")
        if self._del_mention:
            tags_to_delete.append("mention")
        if self._del_mention:
            tags_to_delete.append("hashtag")
        #p(tags_to_delete)
        # Step 2: Cleaning 
        cleaned = []
        for sents in inp_sent_list:
            cleaned_sent = []
            for token in sents:
                if token[1] not in tags_to_delete:
                    cleaned_sent.append(token)
            cleaned.append(cleaned_sent)

        return cleaned
        # for sent in inp_sent_list:
        #     #print token 
        #     if token[1] in tags_to_delete:
        #         #p(token, c="r")
        #         continue
        #     cleaned.append(token)
        # return cleaned


    def _categorize_token_list(self, inp_token_list):
        if self._tokenizer == "somajo":
            pass ## tokens should be already categorized
        else:
            inp_token_list = categorize_token_list(inp_token_list)
            #p("wertzuiopoiutrert", c="m")
        return inp_token_list


    def _lower_case_sents(self, inpsents):
            lower_cased = []
            for sents in inpsents:
                lower_cased_sent = []
                for token in sents:
                    #p(token[0].lower(), c="m")
                    lower_cased_sent.append((token[0].lower(), token[1]))
                
                lower_cased.append(lower_cased_sent)
            return lower_cased

    ###########################Preprocessing###############
    def _preprocessing(self, inp_str, thread_name="Thread0", log_ignored=True):
        self.logger.debug("Preprocessing: '{}'-Thread do preprocessing.".format( thread_name ))
        output = inp_str
        # Preprocessing woth Python !!! (gut) https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
        # python code: https://de.dariah.eu/tatom/preprocessing.html

        #############Step 0 ########################
        # Step 0:  Noise Removal (https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html)
            # remove text file headers, footers
            # remove HTML, XML, etc. markup and metadata
            # extract valuable data from other formats, such as JSON, or from within databases
            # if you fear regular expressions, this could potentially be the part of text preprocessing in which your worst fears are realized
        was_found= False
        if "Klitze kliiiitze kleEEEEine" in output:
            self.logger.critical(("start",output))
            was_found = True

        if self._del_html:
            output = removetags(output)  
            output = remove_html_codded_chars(output)    # delete html-codded characters sets 
            if was_found:
                self.logger.critical(("del_html",output))
            #p(output, "html_deleted")
        #if self._del_rep:

        #############Step 1 ########################
        #Step 1: Language Classification
        if self._lang_classification:
            output_with_deleted_repetitions = self.preprocessors[thread_name]["rle"].del_rep(output) #output #self._rle.del_rep(output)
            #self.logger.critical(output_with_deleted_repetitions)
            lang = langid.classify(output_with_deleted_repetitions)[0]
            if lang != self._language:
                #p(output_with_deleted_repetitions, "lan_outsorted")
                try:
                    # if isinstance(output_with_deleted_repetitions, unicode):
                    #     to_log_cleaned = output_with_deleted_repetitions.encode("utf-8")
                    # else:
                    #     to_log_cleaned = output_with_deleted_repetitions

                    if isinstance(output, unicode):
                        to_log_orig = output.encode("utf-8")
                    else:
                        to_log_orig = output
                    #to_log_orig = output
                    self.logger.warning("LangClassification: Current TextElement was out-sorted, because given language not equal to recognized language: '{}'!='{}'.  According following Text: '{}'. ".format(self._language, lang, to_log_orig))
                except Exception, e:
                    self.logger.error("LangClassificationResultsStdOut: See Exception: '{}'. ".format(e))
                return []


        #############Step 2 ########################
        # Step 2: Tokenization &  (https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html)
        #p(inp_str, "inp_str")
        output = self.tokenize(output, thread_name=thread_name)
        if was_found:
            self.logger.critical(("tokenize",output))
        #p(output, "tokenized")


        #############Step 3 ########################
        # Step 3: Categorization (if wasn't done before)
        output = self._categorize_token_list(output)
        if was_found:
            self.logger.critical(("categprized",output))
        #p(output, "categorized")

        #############Step 4 ########################
        #Step 4:  Segmentation
        if self._sent_splitter:
            output = self.split_sentences(output, thread_name=thread_name)
            #p((len(sentences),sentences), "sentences", c="r")
            #p(len(output), "splitted")
            #p(output, "splitted")
            #p((len(output),output), "splitted")

        else:
            output = [output]
        if was_found:
            self.logger.critical(("sent_splitter",output))
        #p(output, "sent_splitted")


        #############Step 5 ########################
        # Step 5: normalization - Part1
            #> Stemming or Lemmatization (https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html)
            #remove numbers (or convert numbers to textual representations)
            #remove punctuation (generally part of tokenization, but still worth keeping in mind at this stage, even as confirmation)
        output = self._clean_sents_list(output)
        if was_found:
            self.logger.critical(("cleaned",output))
        #p(output, "cleaned")




        #############Step 6 ########################
        # Step 6: Tagging

        if self._pos_tagger: #u'EMOASC', 'EMOIMG'
            output = [self.tag_pos([token[0] for token in sent], thread_name=thread_name) for sent in output]
            #p(output, "tagged")
        if was_found:
            self.logger.critical(("pos",output))
        #############Step  ########################
        # Step : WDS



        #############Step 7 ########################
        # Step 7: normalization
            #> Stemming or Lemmatization (https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html)
            #> case normalisation (lower case)
            #(NO)remove default stop words (general English stop words) 
        if not self._case_sensitiv:
            output = self._lower_case_sents(output)
            #p(output, "lowercased")
        if was_found:
            self.logger.critical(("lowercased",output))


        #############Step  ########################
        # Step : Emotikons? werden die durch den Tokenizer zu einer Entität?



        #############Step 8 ########################
        # Step 8: Sentiment Analysis
        output_with_sentiment = []
        #p(output, "output")
        for sent in output:
            #p(" ".join([token[0] for token in sent]), c="m")
            #p(sent)
            if self._sentiment_analyzer:
                polarity = self.get_sentiment(" ".join([token[0] for token in sent]))
                #p(polarity, "polarity", c="r")
            else:
                polarity = (None, None)
            output_with_sentiment.append((sent, polarity))
        #for 
        output = output_with_sentiment
        if was_found:
            self.logger.critical(("sentiment",output))
        #p(output, "sentiment")

        was_found =False

        return output



    ############Tokenization#############

    def tokenize(self,inp_str, thread_name="Thread0"):
        self.logger.debug("'{}'-Tokenizer: Tokenizer was called from '{}'-Thread.".format(self._tokenizer, thread_name))
        if self._tokenizer == "somajo":
            return self._tokenize_with_somajo(inp_str, thread_name=thread_name)
        elif self._tokenizer == "nltk":
            return self._tokenize_with_nltk(inp_str, thread_name=thread_name)
        else:
            self.logger.error("TokenizationError: No one Tokenizer was chooses.", exc_info=self._logger_traceback)
            return False


    def _set_tokenizer(self, split_camel_case=True, language="de", thread_name="Thread0"):
        token_classes=True
        extra_info=False
        self.logger.debug("INIT-Tokenizer: Start the initialization of '{}'-Tokenizer for '{}'-Thread.".format(self._tokenizer,thread_name))
        if self._tokenizer == "somajo":
            tokenizer_obj = self._get_somajo_tokenizer( split_camel_case=split_camel_case, token_classes=token_classes, extra_info=extra_info, language=language,thread_name=thread_name)
            if not tokenizer_obj:
                self.logger.error("Tokenizer for '{}'-Thread wasn't initialized.".format(thread_name), exc_info=self._logger_traceback)
                return False
        elif self._tokenizer == "nltk":
            #from nltk import word_tokenize
            #word_tokenize(tweet)
            tokenizer_obj = TweetTokenizer()
        else:
            self.logger.error("INIT-TokenizerError '{}'-tokenizer is not supported. ".format(self._tokenizer), exc_info=self._logger_traceback)
            return False
        self.preprocessors[thread_name]["tokenizer"] = tokenizer_obj
        self.logger.debug("INIT-Tokenizer: '{}'-Tokenizer for '{}'-Thread was initialized.".format(self._tokenizer,thread_name))
        return True


    def _tokenize_with_somajo(self,inp_str, thread_name="Thread0"):
        #p(self.preprocessors)
        #self.logger.exception(self.preprocessors)
        #self.logger.exception(self.preprocessors[thread_name]["tokenizer"])
        self.preprocessors[thread_name]["tokenizer"].send(inp_str)
        return self.preprocessors[thread_name]["tokenizer"].receive()


    def _tokenize_with_nltk(self, inp_str, thread_name="Thread0"):
        return self.preprocessors[thread_name]["tokenizer"].tokenize(inp_str)

    def _get_somajo_tokenizer(self, split_camel_case=True, token_classes=True, extra_info=False, language="de", thread_name="Thread0"):
        self.logger.debug("SomajoTokenizerGetter: Start the initialisation of the SoMaJo-Tokenizer.")
        try:
            args = 'split_camel_case={}, token_classes={}, extra_info={}, language="{}" '.format(split_camel_case, token_classes, extra_info, language)
            gw_id = "tokenizer_{}".format(thread_name)
            gw  = self.opened_gateways.makegateway("popen//python=python3//id={}".format(gw_id))
            channel = gw.remote_exec("""
                import sys
                from somajo import Tokenizer
                #print "hhh"
                tokenizer = Tokenizer({2})
                channel.send("ready")
                while True:
                    received = channel.receive()
                    if received == -1:
                        channel.send("stopped")
                        break
                    channel.send(tokenizer.tokenize(received))
                sys.exit()
                        """.format(self._logger_level, gw_id,args))
            #channel_error_bucket = pickle.dumps(self.channels_error_bucket)
            #channel.send(channel_error_bucket)
            if channel.receive() == "ready":
                self.logger.debug("TokenizerInit: Somajo tokenizer for '{}'-Thread was initialized. ".format(thread_name))
            return channel
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.channels_error_bucket.put((thread_name,"Tokenizer",e))
            self.logger.error("SomajoTokenizerGetterError: '{}'-Thread throw following exception: '{}'. ".format(thread_name, e), exc_info=self._logger_traceback)
            #T, V, TB = sys.exc_info()
            tb = ''.join(traceback.format_exception(sys.exc_info()))
            self.threads_status_bucket.put({"name":thread_name, "status":"failed", "exception":e, "traceback":tb})
            #sys.exit()
            return False
        



    ############Sentence Splitting############

    def split_sentences(self,inp_list, thread_name="Thread0"):
        self.logger.debug("'{}'-SentSplitter: SentSplitter was called from '{}'-Thread.".format(self._sent_splitter, thread_name))
        if self._sent_splitter == "somajo":
            return self._split_sentences_with_somajo(inp_list,thread_name=thread_name)


    def _set_sent_splitter(self, is_tuple=True,thread_name="Thread0"):
        #is_tuple  -means, that input tokens are tuples with additonal information about their type (ex: URLS, Emoticons etc.)
        self.logger.debug("INITSentSplitter: Start the initialization of '{}'-SentSplitter for '{}'-Thread.".format(self._sent_splitter,thread_name))
        #p(self._sent_splitter)
        if self._sent_splitter == "somajo":
            sent_splitter_obj = self._get_somajo_sent_splitter( is_tuple=is_tuple, thread_name=thread_name)
            if not sent_splitter_obj:
                self.logger.error("SentSplitter for '{}'-Thread wasn't initialized.".format(thread_name))
                return False
        self.preprocessors[thread_name]["sent_splitter"] = sent_splitter_obj
        self.logger.debug("INITSentSplitter: '{}'-SentSplitter for '{}'-Thread was initialized.".format(self._sent_splitter,thread_name))
        return True

    def _split_sentences_with_somajo(self,inp_list, thread_name="Thread0"):
        self.logger.debug("SoMaJo-SentSpliter: Start splitting into sentences.")
        self.preprocessors[thread_name]["sent_splitter"].send(inp_list)
        return self.preprocessors[thread_name]["sent_splitter"].receive()


    def _get_somajo_sent_splitter(self, is_tuple=True, thread_name="Thread0"):
        try:
            args = 'is_tuple="{}" '.format(is_tuple)
            gw  = self.opened_gateways.makegateway("popen//python=python3//id=sent_splitter_{}".format(thread_name))
            #self.opened_gateways.append(gw)
            channel = gw.remote_exec("""
                import sys
                from somajo import  SentenceSplitter
                sentence_splitter = SentenceSplitter({})
                channel.send("ready")
                while True:
                    received = channel.receive()
                    if received == -1:
                        channel.send("stopped")
                        break
                    channel.send(sentence_splitter.split(received))
                sys.exit()
                    """.format(args))
            if channel.receive() == "ready":
                self.logger.debug("SentSplitterInit: Somajo SentSplitter for '{}'-Thread was initialized. ".format(thread_name))
            #sys.exit()
            #return channel
            return channel
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("SomajoSentSplitterGetterError: '{}'-Thread throw following exception: '{}'. ".format(thread_name, e), exc_info=self._logger_traceback)
            self.channels_error_bucket.put((thread_name,"SentSplitter",e))
            #T, V, TB = sys.exc_info()
            tb = ''.join(traceback.format_exception(sys.exc_info()))
            self.threads_status_bucket.put({"name":thread_name, "status":"failed", "exception":e, "traceback":tb})
            return False

        








    ###########PoS-Tagging###########

    def tag_pos(self,inp_list, thread_name="Thread0"):
        self.logger.debug("'{}'-POSTagger: POS-tagger was called from '{}'-Thread.".format(self._sent_splitter, thread_name))
        if self._pos_tagger == "someweta":
            return self._tag_pos_with_someweta(inp_list, thread_name=thread_name)
        elif self._pos_tagger == "tweetnlp":
            return self._tag_pos_with_tweetnlp(inp_list)





    def _set_pos_tagger(self, thread_name="Thread0"):
        #p(self._pos_tagger)
        self.logger.debug("INIT-POS-Tagger: Start the initialization of '{}'-pos-tagger for '{}'-Thread.".format(self._pos_tagger,thread_name))
        if self._pos_tagger == "someweta":
            model_name = Corpus.pos_tagger_models[self._pos_tagger][self._language][0]
            path_to_model = os.path.join(path_to_zas_rep_tools,"data/models/SoMeWeTa/",model_name)
            pos_tagger_obj = self._get_someweta_pos_tagger(path_to_model,thread_name=thread_name)
            if not pos_tagger_obj:
                self.logger.error("POS-Tagger for '{}'-Thread wasn't initialized.".format(thread_name), exc_info=self._logger_traceback)
                return False
            #p(pos_tagger_obj)
            #sys.exit()
        elif self._pos_tagger == "tweetnlp":
            if not check_script_is_present():
                self.logger.error("TweetNLP Java-Script File wasn't found", exc_info=self._logger_traceback)
                return False
            pos_tagger_obj = None
        self.preprocessors[thread_name]["pos-tagger"] = pos_tagger_obj
        self.logger.debug("INIT-POS-Tagger: '{}'-pos-tagger for '{}'-Thread was initialized.".format(self._pos_tagger,thread_name))
        return True


    def _tag_pos_with_someweta(self,inp_list, thread_name="Thread0"):
        self.preprocessors[thread_name]["pos-tagger"].send(inp_list)
        tagged = self.preprocessors[thread_name]["pos-tagger"].receive()
        #p(tagged, "tagged_with_someweta")
        return tagged

    def _tag_pos_with_tweetnlp(self,inp_list):
        #CMUTweetTagger.runtagger_parse(['example tweet 1', 'example tweet 2'])
        #p(runtagger_parse(inp_list), "tagged_with_tweet_nlp")
        return runtagger_parse(inp_list)


    def _get_someweta_pos_tagger(self, path_to_model, thread_name="Thread0"):
        try:
            gw  = self.opened_gateways.makegateway("popen//python=python3//id=pos_{}".format(thread_name))
            #self.opened_gateways.append(gw)
            channel = gw.remote_exec("""
                    import sys
                    from someweta import  ASPTagger

                    asptagger = ASPTagger(5, 10)
                    asptagger.load('{}')

                    channel.send("ready")
                    while True:
                        received = channel.receive()
                        if received == -1:
                            channel.send("stopped")
                            break
                        channel.send(asptagger.tag_sentence(received))

                    sys.exit()
                    """.format(path_to_model))
            if channel.receive() == "ready":
                self.logger.debug("POSTaggerInit: Someweta POS-Tagger  for '{}'-Thread was initialized. ".format(thread_name))
            #sys.exit()
            return channel
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("SoMeWeTaPOSTaggerGetterError: '{}'-Thread throw following exception: '{}'. ".format(thread_name,e), exc_info=self._logger_traceback)
            self.channels_error_bucket.put((thread_name,"POSTagger",e))
            #T, V, TB = sys.exc_info()
            tb = ''.join(traceback.format_exception(sys.exc_info()))
            self.threads_status_bucket.put({"name":thread_name, "status":"failed", "exception":e, "traceback":tb})
            return False
        














    ###########Sentiment###########

    def get_sentiment(self,inp_str, thread_name="Thread0"):
        self.logger.debug("'{}'-SentimentAnalyzer: was called from '{}'-Thread.".format(self._sent_splitter, thread_name))
        if self._sentiment_analyzer == "textblob":
            return self._get_sentiment_with_textblob(inp_str, thread_name=thread_name)
        # elif self._pos_tagger == "tweetnlp":
        #     return self._tag_pos_with_tweetnlp(inp_str)





    # def _set_sentiment_analyzer(self, thread_name="Thread0"):
    #     #p(self._pos_tagger)
    #     self.logger.debug("INIT-SentimentAnalyzer: Start the initialization of '{}'-sentiment analyzer for '{}'-Thread.".format(self._sentiment_analyzer,thread_name))
    #     if self._sentiment_analyzer == "textblob":
    #         if self._language == "fr":
    #             sentiment_analyser_obj = 
    #         elif self._language =="de":
    #             sentiment_analyser_obj = 
    #         elif self._language == "en":
    #             sentiment_analyser_obj= 

    #         if not sentiment_analyser_obj:
    #             self.logger.error("SentimentAnalyzer for '{}'-Thread wasn't initialized.".format(thread_name))
    #             return False


    #     self.preprocessors[thread_name]["sentiment_analyser"] = sentiment_analyser_obj
    #     self.logger.debug("INIT-SentimentAnalyzer: '{}'-pos-tagger for '{}'-Thread was initialized.".format(self._sentiment_analyzer,thread_name))
    #     return True




    def get_sent_sentiment_with_textblob_for_en(self, sent_as_str):
        '''
        Utility function to classify sentiment of passed sent_as_str
        using textblob's sentiment method
        '''
        # create TextBlob object of passed sent_as_str text
        analysis = TextBlob(sent_as_str)
        # set sentiment
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return ('positive', polarity)
        elif polarity == 0:
            return ('neutral',polarity)
        else:
            return ('negative',polarity)




    def get_sent_sentiment_with_textblob_for_de(self, sent_as_str):
        '''
        # https://media.readthedocs.org/pdf/textblob-de/latest/textblob-de.pdf
        Utility function to classify sentiment of passed sent_as_str
        using textblob's sentiment method
        '''
        # create TextBlob object of passed sent_as_str text
        analysis = TextBlobDE(sent_as_str)
        # blob.tags # [('Der', 'DT'), ('Blob', 'NN'), ('macht', 'VB'),
        #             #  ('in', 'IN'), ('seiner', 'PRP$'), ...]
        # blob.noun_phrases # WordList(['Der Blob', 'seiner unbekümmert-naiven Weise',
        #             #           'den gewissen Charme', 'hölzerne Regie',
        #             #           'konfuse Drehbuch'])
        # set sentiment
        #for sentence in blob.sentences: print(sentence.sentiment.polarity):
            # 1.0 # 0.0

        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return ('positive', polarity)
        elif polarity == 0:
            return ('neutral',polarity)
        else:
            return ('negative',polarity)

    def get_sent_sentiment_with_textblob_for_fr(self, sent_as_str):
        '''
        #https://github.com/sloria/textblob-fr
        # https://media.readthedocs.org/pdf/textblob-de/latest/textblob-de.pdf
        Utility function to classify sentiment of passed sent_as_str
        using textblob's sentiment method
        '''
        # create TextBlob object of passed sent_as_str text
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        analysis = tb(sent_as_str)
        #analysis.sentiment

        # blob.tags # [('Der', 'DT'), ('Blob', 'NN'), ('macht', 'VB'),
        #             #  ('in', 'IN'), ('seiner', 'PRP$'), ...]
        # blob.noun_phrases # WordList(['Der Blob', 'seiner unbekümmert-naiven Weise',
        #             #           'den gewissen Charme', 'hölzerne Regie',
        #             #           'konfuse Drehbuch'])
        # set sentiment
        polarity = analysis.sentiment[0]
        if polarity > 0:
            return ('positive', polarity)
        elif polarity == 0:
            return ('neutral',polarity)
        else:
            return ('negative',polarity)





    def _get_sentiment_with_textblob(self,inp_str, thread_name="Thread0"):
        if self._language == "de":
            return self.get_sent_sentiment_with_textblob_for_de(inp_str)
        elif self._language in ["en", "test"]:
            return self.get_sent_sentiment_with_textblob_for_en(inp_str)
        elif self._language == "fr":
            return self.get_sent_sentiment_with_textblob_for_fr(inp_str)
        else:
            self.logger.error("SentimentGetterwithTextBlob: Given Language '{}' is not supported. Please use one of the following languages: '{}'. ".format(self._language, Corpus.supported_languages_sentiment_analyzer))
            return False













    def _isrighttype(self, inp_data):
        #p(inp_data)
        check = (isinstance(inp_data, list), isinstance(inp_data, LenGen))
        #p(check, "check")
        if True not in check:
            self.logger.error("InputValidationError: Given 'inpdata' is not iterable. ", exc_info=self._logger_traceback)
            return False
        return True


    def _check_db_should_exist(self):
        if not self.db: 
            self.logger.error("No active DB was found. You need to connect or initialize a DB first, before you can make any operation on the DB.", exc_info=self._logger_traceback)
            return False
        else:
            return True

    def _check_db_should_not_exist(self):
        if self.db: 
            self.logger.error("An active DB was found. You need to initialize new empty Instance of DB before you can do this operation.", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def check_status_gateways(self):
        status= []
        try:
            for gw in self.opened_gateways:
                status.append(gw.remote_status())
        except Exception,e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("GateWaysStatusCheckerError: Throw following Exception '{}'.".format(e), exc_info=self._logger_traceback)
        
        self.logger.info("GateWaysStatusChecker: '{}'-Gateways was asked for their status..".format(len(status)))
        return status


    def close_all_gateways(self):
        closed=0
        try:
            for gw in self.opened_gateways:
                gw.exit()
                closed +=1
        except Exception,e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("GateWaysCloserError: Throw following Exception '{}'.".format(e), exc_info=self._logger_traceback)
        
        self.logger.info("GateWaysCloser: '{}'-Gateways was closed.".format(closed))


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


