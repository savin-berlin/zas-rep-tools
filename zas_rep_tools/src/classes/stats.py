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


import os
import sys
from raven import Client
import types
import Queue
import enlighten
import json
from collections import defaultdict,Counter
import copy
import threading
import time
from itertools import izip



from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, path_to_zas_rep_tools, Rle, categorize_token_list, get_categories, instance_info, SharedCounterExtern, SharedCounterIntern, Status,function_name,statusesTstring, ngrams,nextLowest, get_number_of_streams_adjust_cpu,LenGen
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.reader import Reader
from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.classes.exporter import Exporter
from zas_rep_tools.src.utils.zaslogger import ZASLogger
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus
from zas_rep_tools.src.classes.basecontent import BaseContent, BaseDB


import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama


class Stats(BaseContent,BaseDB):

    supported_phanomena_to_export = ["repl", "redu", "baseline"]
    supported_syntagma_type= ["lexem", "pos"]
    supported_sentiment = ["negative","positive","neutral"]


    def __init__(self, repl_up=3, log_ignored=True, ignore_hashtag=True, force_cleaning = False,
                case_sensitiv = True, text_field_name="text", id_field_name="id", status_bar=True,
                ignore_url=True,  ignore_mention=True, ignore_punkt=True, ignore_num=True,**kwargs):
        super(type(self), self).__init__(**kwargs)


        #Input: Encapsulation:

        self.force_cleaning_flags = []
        
        self._status_bar = status_bar
        #self._preprocession = preprocession
        self._repl_up = repl_up
        self._log_ignored = log_ignored
        self._ignore_hashtag =ignore_hashtag
        self._ignore_url = ignore_url
        self._ignore_mention = ignore_mention
        self._ignore_punkt = ignore_punkt
        self._ignore_num = ignore_num
        self._force_cleaning = force_cleaning
        self._case_sensitiv  = case_sensitiv
        self._text_field_name = text_field_name
        self._id_field_name = id_field_name


        #InstanceAttributes: Initialization
        self.statsdb = False
        self.corp = False
        self._corp_info = False
        #self._init_insertion_variables()

        self.preprocessors = defaultdict(dict)
        self._init_preprocessors(thread_name="Thread0")

        self.logger.debug('Intern InstanceAttributes was initialized')


        self.logger.debug('An instance of Stats() was created ')

        ## Log Settings of the Instance
        attr_to_flag = False
        attr_to_len = False
        self._log_settings(attr_to_flag =attr_to_flag,attr_to_len =attr_to_len)




        ############################################################
        ####################__init__end#############################
        ############################################################

    def __del__(self):
        super(type(self), self).__del__()



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

    def _init_insertion_variables(self):

        self.threads_error_bucket = Queue.Queue()
        self.threads_status_bucket = Queue.Queue()
        self.threads_success_exit = []
        self.threads_unsuccess_exit = []
        self._threads_num = 0
        self.status_bars_manager =  self._get_status_bars_manager()
        self.preprocessors = defaultdict(dict)
        #self.baseline_replication = defaultdict(lambda:defaultdict(lambda: 0) )
        #self.baseline_reduplication = defaultdict(lambda:defaultdict(lambda: 0) )
        self._terminated = False
        #self.baseline_ngramm_lenght = self._context_left + 1 +self._context_right
        self.baseline_ngramm_lenght =  1 +self._context_right
        self.temporized_baseline = defaultdict(int)
        self.active_threads = []
        self.main_status_bar_of_insertions = False
        self._timer_on_main_status_bar_was_reset = False
        self._start_time_of_the_last_insertion = False
        self._end_time_of_the_last_insertion = False
        self._last_insertion_was_successfull = False
        self.counters_attrs = defaultdict(lambda:defaultdict(dict))
        self._avaliable_scope = self._context_right+1


    ###########################INITS + Open##########################



    def additional_attr(self):
        additional_attributes = {
                "repl_up":self._repl_up,
                #"log_ignored":self._log_ignored,
                "ignore_hashtag":self._ignore_hashtag,
                "ignore_url":self._ignore_url,
                "ignore_mention":self._ignore_mention,
                "ignore_punkt":self._ignore_punkt,
                "ignore_num":self._ignore_num,
                "force_cleaning":self._force_cleaning ,
                "case_sensitiv":self._case_sensitiv,
                }
        return additional_attributes




    def init(self, prjFolder, DBname, language,  visibility, corpus_id, 
                    encryption_key=False,fileName=False,  version=False, stats_id=False, was_space_optimized=False,
                    context_left=5, context_right=5,):

        if self.statsdb:
            self.logger.error("StatsInitError: An active Stats Instance was found. Please close already initialized/opened Stats, before new initialization.", exc_info=self._logger_traceback)
            return False
         
        if context_left != context_right:
            self.logger.error("Context (left and right sides) Length are un-equal.")
            return False 

        if context_right < 3:
            self.logger.error("Given Context-Length is lower as an allow minimum, which is 3.")
            return False
        #self._context_left = context_left 
        #self._context_right = context_right
        self.statsdb = DBHandler( **self._init_attributesfor_dbhandler())
        was_initialized = self.statsdb.init("stats", prjFolder, DBname, language,  visibility, corpus_id=corpus_id,
                    encryption_key=encryption_key,fileName=fileName, version=version,
                    stats_id=stats_id, was_space_optimized=was_space_optimized, context_left=context_left, context_right=context_right  )

        if not was_initialized:
            self.logger.error("StatsInit: Current Stats for following attributes  wasn't initialized: 'dbtype='{}'; 'dbname'='{}; corp_id='{}'; 'stats_id'='{}'; encryption_key='{}'; .".format("stats", DBname,corpus_id, stats_id,encryption_key))
            return False

        if self.statsdb.exist():
            self.add_context_columns( context_left, context_right)
            self.statsdb.update_attrs(self.additional_attr())
            self.set_all_intern_attributes_from_db()
            self.logger.settings("InitStatsDBAttributes: {}".format( instance_info(self.statsdb.get_all_attr(), attr_to_len=False, attr_to_flag=False, as_str=True)))
            self.logger.info("StatsInit: '{}'-Stats was successful initialized.".format(DBname))
            self._contextR1index = {
                    "repl":self._get_col_index("contextR1", "replications"),
                    "redu":self._get_col_index("contextR1", "reduplications")
                    }
            self._normalized_word_index = {
                    "repl":self._get_col_index("normalized_word", "replications"),
                    "redu":self._get_col_index("normalized_word", "reduplications")
                    }
            return True
        else:
            self.logger.error("StatsInit: '{}'-Stats wasn't  initialized.".format(DBname), exc_info=self._logger_traceback)
            return False

    def close(self):
        self.statsdb.close()
        self.statsdb = False
        self.corp = False
        self._corp_info = False

    def _close(self):
        self.statsdb._close()
        self.statsdb = False
        self.corp = False
        self._corp_info = False

    def open(self, path_to_stats_db, encryption_key=False):

        if self.statsdb:
            self.logger.error("StatsInitError: An active Stats Instance was found. Please close already initialized/opened Stats, before new initialization.", exc_info=self._logger_traceback)
            return False

        self.statsdb = DBHandler( **self._init_attributesfor_dbhandler())
        self.statsdb.connect(path_to_stats_db, encryption_key=encryption_key)


        if self.statsdb.exist():
            if self.statsdb.typ() != "stats":
                self.logger.error("Current DB is not an StatsDB.")
                self._close()
                return False
            self.logger.info("StatsOpener: '{}'-Stats was successful opened.".format(os.path.basename(path_to_stats_db)))
            self.set_all_intern_attributes_from_db()
            self.logger.settings("OpenedStatsDBAttributes: {}".format( instance_info(self.statsdb.get_all_attr(), attr_to_len=False, attr_to_flag=False, as_str=True)))
            self._contextR1index = {
                                "repl":self._get_col_index("contextR1", "replications"),
                                "redu":self._get_col_index("contextR1", "reduplications")
                                }
            self._normalized_word_index = {
                    "repl":self._get_col_index("normalized_word", "replications"),
                    "redu":self._get_col_index("normalized_word", "reduplications")
                    }
            return True
        else:
            self.logger.error("StatsOpener: Unfortunately '{}'-Stats wasn't opened.".format(os.path.basename(path_to_stats_db)), exc_info=self._logger_traceback)
            return False


    def set_all_intern_attributes_from_db(self):
        #{u'name': u'bloggerCorpus', u'created_at': u'2018-07-26 17:49:11', u'visibility': u'extern', u'version': u'1', u'corpus_id': 7614, u'typ': u'stats', u'id': 3497}
        info_dict = self.info()
        self._name = info_dict["name"]
        self._created_at = info_dict["created_at"]
        self._visibility = info_dict["visibility"]
        self._version = info_dict["version"]
        self._corpus_id = info_dict["corpus_id"]
        self._typ = info_dict["typ"]
        self._id = info_dict["id"]
        self._was_space_optimized = info_dict["was_space_optimized"]
        self._context_left = info_dict["context_left"]
        self._context_right = info_dict["context_right"]
        self._avaliable_scope = self._context_right+1

        self._repl_up =  info_dict["repl_up"]
        #self._log_ignored =  info_dict["log_ignored"]
        self._ignore_hashtag =  info_dict["ignore_hashtag"]
        self._ignore_url =  info_dict["ignore_url"]
        self._ignore_mention =  info_dict["ignore_mention"]
        self._ignore_punkt =  info_dict["ignore_punkt"]
        self._ignore_num =  info_dict["ignore_num"]
        self._force_cleaning  =  info_dict["force_cleaning"]
        self._case_sensitiv =  info_dict["case_sensitiv"]


    def _get_col_index(self, col_name, table_name):
        try:
            return self.statsdb.col(table_name).index(col_name)
        except ValueError, e:
            self.logger.error("'{}'-Colum is not in the '{}'-Table.".fromat(col_name, table_name))
            return False

    def _init_attributesfor_dbhandler(self):
        init_attributes_db_handler = {
                        "stop_if_db_already_exist":self._stop_if_db_already_exist,
                        "rewrite":self._rewrite,
                        "logger_level":self._logger_level,
                        "optimizer":self._optimizer,
                        "in_memory":self._in_memory,
                        "logger_traceback":self._logger_traceback,
                        "logger_folder_to_save":self._logger_folder_to_save,
                        "logger_usage":self._logger_usage,
                        "logger_save_logs":self._logger_save_logs,
                        "thread_safe":self._thread_safe,
                        "mode":self._mode,
                        "error_tracking":self._error_tracking,
                        "ext_tb":self._ext_tb,
                        "isolation_level":self._isolation_level,
                        "optimizer_page_size":self._optimizer_page_size,
                        "optimizer_cache_size":self._optimizer_cache_size,
                        "optimizer_locking_mode":self._optimizer_locking_mode,
                        "optimizer_synchronous":self._optimizer_synchronous,
                        "optimizer_journal_mode":self._optimizer_journal_mode,
                        "optimizer_temp_store":self._optimizer_temp_store,
                        "use_cash":self._use_cash,
                        }
        return init_attributes_db_handler


    
    def add_context_columns(self, context_left, context_right):
       self._add_context_columns("replications", context_left, context_right)
       self._add_context_columns("reduplications", context_left, context_right)

    def _add_context_columns(self, table_name, context_left, context_right):
        #p("ghjkl")
        exist_columns = self.statsdb.col(table_name)
        #p(exist_columns,"exist_columns", c="r")


        for context_number in reversed(range(1,context_left+1)):

            ### WordCell####
            name = "contextL{}".format(context_number)
            exist_columns = self.statsdb.col(table_name)
            if name not in exist_columns:
                if self.statsdb.add_col(table_name, name, "JSON"):
                    self.logger.debug("'{}'-Columns was inserted into '{}'-Table. ".format(name, table_name))
                else:
                    return False
            else:
                self.logger.error("'{}'-Column is already exist in the '{}'-Table. ColumnInsertion was aborted. ".format(name, table_name))
                #yield False
                return False

            ### Additional Info Col ####
            name = "context_infoL{}".format(context_number)
            exist_columns = self.statsdb.col(table_name)
            if name not in exist_columns:
                if self.statsdb.add_col(table_name, name, "JSON"):
                    self.logger.debug("'{}'-Columns was inserted into '{}'-Table. ".format(name, table_name))
                else:
                    return False
            else:
                self.logger.error("'{}'-Column is already exist in the '{}'-Table. ColumnInsertion was aborted. ".format(name, table_name))
                #yield False
                return False

        for context_number in range(1,context_right+1):
            ### WordCell####
            name = "contextR{}".format(context_number)
            if name not in exist_columns:
                self.statsdb.add_col(table_name, name, "JSON")
                self.logger.debug("'{}'-Columns was inserted into '{}'-Table. ".format(name, table_name))
                #yield True
            else:
                self.logger.error("'{}'-Column is already exist in the '{}'-Table. ColumnInsertion was aborted. ".format(name, table_name))
                return  False
                #return 


            ### Additional Info Col ####
            name = "context_infoR{}".format(context_number)
            if name not in exist_columns:
                self.statsdb.add_col(table_name, name, "JSON")
                self.logger.debug("'{}'-Columns was inserted into '{}'-Table. ".format(name, table_name))
                #yield True
            else:
                self.logger.error("'{}'-Column is already exist in the '{}'-Table. ColumnInsertion was aborted. ".format(name, table_name))
                return  False
                #return 
        exist_columns = self.statsdb.col(table_name)
        #p(exist_columns,"exist_columns", c="r")
        return True
        #sys.exit()




    def info(self):
        if not self._check_stats_db_should_exist():
            return False

        if not self._check_db_should_be_an_stats():
            return False

        return self.statsdb.get_all_attr()



    def get_streams_from_corpus(self,inp_corp,stream_number,datatyp="dict"):
        row_num = inp_corp.corpdb.rownum("documents")
        rows_pro_stream = row_num/stream_number
        streams = []
        num_of_getted_items = 0
        for i in range(stream_number):
            thread_name = "Thread{}".format(i)
            if i < (stream_number-1): # for gens in between 
                gen = inp_corp.corpdb.lazyget("documents",limit=rows_pro_stream, offset=num_of_getted_items,thread_name=thread_name, output=datatyp)
                num_of_getted_items += rows_pro_stream
                streams.append((thread_name,LenGen(gen, rows_pro_stream)))
            else: # for the last generator
                gen = inp_corp.corpdb.lazyget("documents",limit=-1, offset=num_of_getted_items,thread_name=thread_name, output=datatyp)
                streams.append((thread_name,LenGen(gen, row_num-num_of_getted_items)))
        return streams







    ###########################Getters#######################

    # def get_data(self, inp_syntagma,baseline=True, repl=True, redu=True):
    #     if baseline:
    #         self.get_baseline(inp_syntagma)

    #     if repl:
    #         self.get_repl(inp_syntagma)
 
    #     if redu:
    #         self.get_redu(inp_syntagma)


    # supported_phanomena_to_export = ["repl", "redu", "baseline"]
    # supported_syntagma_type= ["lexem", "pos"]
    # supported_sentiment = ["negativ","positiv","neutral"]

    def _get_header(self,repl=False, redu=False, baseline=False):
        header = []
        return header


    def _get_export_phanomena(self,repl=False, redu=False, baseline=False):
        to_export = []
        if repl:
            to_export.append("repl")
        if redu:
            to_export.append("redu")
        if baseline:
            to_export.append("baseline")
        return to_export




    


    def export(self,path_to_export_dir, syntagma="*", repl=False, redu=False, baseline=False, syntagma_type="lexem", sentiment=False, fname=False, export_file_type="csv", rows_limit_in_file=1000000, encryption_key=False):
        export_file_type =  export_file_type.lower()
        fname =fname if fname else "export_{}".format(time.time())
        if export_file_type not in Exporter.supported_file_formats:
            self.logger.error("ExportError: '{}'-FileType is not supported. Please use one of the following file type: '{}'.".format(export_file_type, Exporter.supported_file_formats))
            return False
        
        header = self._get_header(self,repl=False, redu=False, baseline=False)
        rows_generator = self._export_generator(syntagma="*", repl=False, redu=False, baseline=False, syntagma_type="lexem", sentiment=False,)
        exporter = Exporter(rows_generator,rewrite=True )
        if export_file_type == "csv":
            exporter.tocsv(path_to_export_dir, fname, header, rows_limit_in_file=rows_limit_in_file)

        elif export_file_type == "xml":
            exporter.toxml(path_to_export_dir, fname, rows_limit_in_file=rows_limit_in_file, root_elem_name="export", row_elem_name="line")
            
        elif export_file_type == "sqlite":
            exporter.tosqlite(path_to_export_dir, fname, header,  encryption_key=encryption_key, table_name="Export")

        elif export_file_type == "json":
            exporter.tojson(path_to_export_dir, fname, rows_limit_in_file=rows_limit_in_file,)




    def _export_generator(self,inp_syntagma="*",repl=False, redu=False, baseline=False, syntagma_type="lexem", sentiment=False,):
        return self.get_data(inp_syntagma=inp_syntagma,repl=repl, redu=redu, baseline=baseline, syntagma_type="lexem", sentiment=False,)


        #return ""



    def _clean_baseline_table(self, thread_name="Thread0"):
        if not self._check_stats_db_should_exist():
            return False
            #return

        ### compute syntagmas to delete
        syntagmas_to_delete = []
        for baseline_container in self._baseline("*",max_scope=False):
            #inp_syntagma =  self._preprocess_syntagma(inp_syntagma,thread_name=thread_name, syntagma_type=syntagma_type)
            #if not inp_syntagma:
                #yield False
                #return 
            data =  self._get_data_for_one_syntagma(baseline_container[0],repl=True, redu=True, baseline=False, syntagma_type="lexem", thread_name=thread_name,search_just_in_full_repetativ_syntagma=True)
            #p(repr(data), "data")
            if not data:
                #p(baseline_container[0], "baseline_container[0]")
                #p(, c="r")
                syntagmas_to_delete.append(("++".join(baseline_container[0]),))

        row_num_bevore = self.statsdb.rownum("baseline")
        ##### delete syntagmas from baseline-table
        qeary = "DELETE FROM baseline WHERE syntagma = ? ;"
        
        self.statsdb.executemany(qeary,syntagmas_to_delete)
        row_num_after = self.statsdb.rownum("baseline")

        if (row_num_bevore-row_num_after) == len(syntagmas_to_delete):
            return True
        else:
            False



    def optimize_db(self,thread_name="Thread0"):
        if not self._was_space_optimized:
            if self._clean_baseline_table(thread_name=thread_name):
                #p(self._was_space_optimized,"self._was_space_optimized")
                self.statsdb.update_attr("was_space_optimized", True)
                self.set_all_intern_attributes_from_db()
                self.statsdb.commit()
                #self._was_space_optimized
                #p(self._was_space_optimized,"self._was_space_optimized")
                if self._was_space_optimized:
                    return True
                else:
                    return False
            else:
                self.logger.info("OptimizationError: StatsDB wasn't space optimized.")
                return False
        else:
            self.logger.warning("Current StatsDB was already optimized!")
            return False



    def get_data(self,inp_syntagma="*",repl=False, redu=False, baseline=False, syntagma_type="lexem", sentiment=False,thread_name="Thread0", max_scope=False,search_just_in_full_repetativ_syntagma=False, sort_by="syntagma"):
        #p(inp_syntagma, "11inp_syntagma")
        if not self._check_stats_db_should_exist():
            yield False
            return 

        #if not isinstance(inp_syntagma, (list,tuple))
        if syntagma_type not in Stats.supported_syntagma_type:
            self.logger.error("Given SyntagmaType '{}' is not supported. Please select one of the following types: '{}'.".format(syntagma_type, Stats.supported_syntagma_type))
            yield False
            return 

        if not inp_syntagma:
           yield False
           return 

        if sentiment and sentiment not in Stats.supported_sentiment:
            self.logger.error("Given SentimentType '{}' is not supported. Please select one of the following types: '{}'. (!should be given in lower case!)".format(sentiment, Stats.supported_sentiment))
            yield False
            return 

        to_export = self._get_export_phanomena(repl=redu, redu=redu, baseline=baseline)
        if not to_export:
            self.logger.error("No Phenomena to export was selected. Please choice phanomena to export from the following list: '{}'. ".format(Stats.supported_phanomena_to_export))

        if inp_syntagma == "*":
            for baseline_container in self._baseline("*",max_scope=False):
                #inp_syntagma =  self._preprocess_syntagma(inp_syntagma,thread_name=thread_name, syntagma_type=syntagma_type)

                data =  self._get_data_for_one_syntagma(baseline_container[0],repl=repl, redu=redu, baseline=False, syntagma_type=syntagma_type, sentiment=sentiment,thread_name=thread_name, max_scope=max_scope,search_just_in_full_repetativ_syntagma=True)
                
                if data:
                    data["baseline"] = baseline_container
                    yield data
                else:
                    continue

        else:
            inp_syntagma =  self._preprocess_syntagma(inp_syntagma,thread_name=thread_name, syntagma_type=syntagma_type)
            if not inp_syntagma:
                yield False
                return 
            data =  self._get_data_for_one_syntagma(inp_syntagma,repl=repl, redu=redu, baseline=baseline, syntagma_type=syntagma_type, sentiment=sentiment,thread_name=thread_name, max_scope=max_scope,search_just_in_full_repetativ_syntagma=search_just_in_full_repetativ_syntagma)
            if data:
                yield data

    def _get_index_by_codepoint(self,  codepoint, typ):

        if typ == "repl":
            word_index = self._normalized_word_index["repl"]
            r1_index = self._contextR1index["repl"]
        else:
            word_index = self._normalized_word_index["redu"]
            r1_index = self._contextR1index["redu"]

        if codepoint == 0:
            #rep[]
            return word_index
        elif codepoint == 1:
            return r1_index
        else:
            return r1_index + (2* (codepoint-1))





    def _extract_all_syntagmas(self, entry, typ):
        all_syntagmas = set()
        
        for rep in entry:
            done = False
            for index in xrange(1, self._avaliable_scope+1):
                temp_syntagma = []
                for i in xrange(index):
                    #p(self._get_index_by_codepoint(i, typ), "self._get_index_by_codepoint(i, typ)")
                    word = rep[self._get_index_by_codepoint(i, typ)]
                    #temp_syntagma.append(word)
                    if word:
                        temp_syntagma.append(word)
                    else:
                        #break
                        done=True
                        if done: break
                
                #p(temp_syntagma,"{}temp_syntagma".format(typ))
                all_syntagmas.add(tuple(temp_syntagma))
                #all_syntagmas.add(temp_syntagma)
                if done: break
                #all_syntagmas.append(temp_syntagma)
                
        #p(all_syntagmas,"set_all_syntagmas")
        return all_syntagmas



    def _get_data_for_one_syntagma(self,inp_syntagma, repl=False, redu=False, baseline=False, syntagma_type="lexem", sentiment=False,thread_name="Thread0", max_scope=False, search_just_in_full_repetativ_syntagma=False,):
        _repl = []
        _redu = []
        _baseline = []
        scope = len(inp_syntagma)
        #p(syntagma_type, "syntagma_type")
        if not self._is_syntagma_scope_right(scope):
            #self.logger.error("The Length ('{}') of  Given SyntagmaToSearch ('{}') is  bigger as allow ('{}'). Please recompute StatsDB with the bigger ContextNumber.".format(scope, inp_syntagma,self._avaliable_scope))
            #if isinstance()
            return False

        #p(scope,"scope2")
        where1 = False
        if repl:
            if not where1:
                where1 = self._get_where_statement(inp_syntagma,scope=scope,thread_name=thread_name, with_context=True,syntagma_type=syntagma_type, sentiment=sentiment)
            #p(where1,"where1_repl", c="b")
            _repl = self._get_repls(inp_syntagma,scope,where1,thread_name=thread_name,search_just_in_full_repetativ_syntagma=search_just_in_full_repetativ_syntagma)
        if redu:
            if not where1:
                where1 = self._get_where_statement(inp_syntagma,scope=scope,thread_name=thread_name, with_context=True,syntagma_type=syntagma_type, sentiment=sentiment)
            #p(where1,"where1_redu", c="b")
            _redu = self._get_redus(inp_syntagma,scope,where1,thread_name=thread_name,search_just_in_full_repetativ_syntagma=search_just_in_full_repetativ_syntagma)

        #p((repl,_repl, redu, _redu))

        if baseline:
            if syntagma_type == "lexem":
                where2 = self._get_where_statement(inp_syntagma,scope=scope,thread_name=thread_name, with_context=False,syntagma_type=syntagma_type, sentiment=sentiment)
                _baseline = list(self._baseline(inp_syntagma,scope=scope,where=where2))
            else:
                all_syntagmas = []
                if _repl:
                    all_syntagmas += self._extract_all_syntagmas(_repl, "repl")
                if _redu:
                    all_syntagmas += self._extract_all_syntagmas(_redu, "redu")

                #p(all_syntagmas,"all_syntagmas")

                for temp_syntagma in set(all_syntagmas):
                    where2 = self._get_where_statement(temp_syntagma,scope=scope,thread_name=thread_name, with_context=False,syntagma_type=syntagma_type, sentiment=sentiment)
                    _baseline += list(self._baseline(temp_syntagma,scope=scope,where=where2))


        
        if not _repl and not _redu and not _baseline:
            return {}

        return {"repl":_repl, "redu":_redu, "baseline":_baseline,"syntagma":inp_syntagma}



    def _get_repls(self,inp_syntagma,scope,where,thread_name="Thread0", search_just_in_full_repetativ_syntagma=False,):
        #p(search_just_in_full_repetativ_syntagma,"search_just_in_full_repetativ_syntagma",c="r")
        _repl = []
        for w in where:
            #p(w, "w_in_repl", c="c")
            current_repls = list(self._repl(inp_syntagma,scope=scope,where=w,thread_name=thread_name))
            #p(current_repls,"2current_repls",c="r")
            if current_repls:
                #p(current_repls,"2current_repls",c="r")
                _repl += current_repls
            else:
                if search_just_in_full_repetativ_syntagma:
                    return []
                break
        return _repl
     
    def _get_redus(self,inp_syntagma,scope,where,thread_name="Thread0", search_just_in_full_repetativ_syntagma=False,):
        _redu = []
        for w in where:
            #p(w, "w_in_redu", c="c")
            current_redus = list(self._redu(inp_syntagma,scope=scope,where=w,thread_name=thread_name))
            if current_redus:
                _redu += current_redus
            else:
                if search_just_in_full_repetativ_syntagma:
                    return []
                break
        return _redu

    def _preprocess_syntagma(self, inp_syntagma,thread_name="Thread0", syntagma_type="lexem"):

        #p(inp_syntagma,"inp_syntagma")
        if not isinstance(inp_syntagma, (list,tuple)):
            self.logger.error("Given inp_syntagma ('{}') is from an un-support type ('{}')".format(inp_syntagma, type(inp_syntagma)))
            return False
        if syntagma_type == "lexem":
            inp_syntagma = [self.preprocessors[thread_name]["rle"].del_rep(token) for token in inp_syntagma]
        
        return inp_syntagma
        #p(inp_syntagma,"inp_syntagma")
        #if not self._case_sensitiv:
        #    inp_syntagma = [token.lower() for token in inp_syntagma]

        


    def _get_where_statement(self,inp_syntagma,scope=False, syntagma_type="lexem", sentiment=False,thread_name="Thread0", with_context=True):
        ### Syntagma Preprocessing
        wheres = []
        if with_context: # for repl and redu
            normalized_word_tag_name = "normalized_word" if syntagma_type == "lexem" else "pos"
            context_tag_name_r = "contextR"  if syntagma_type == "lexem" else "context_infoR"
            context_tag_name_l = "contextL"  if syntagma_type == "lexem" else "context_infoL"

            for token_index in xrange(scope):
                last_token_index = scope-1
                where = []
                for i, token in  zip(range(scope),inp_syntagma):
                    if i < token_index:
                        #json_extract("text", "$[1]")
                        col_name = u"{}{}".format(context_tag_name_l,token_index-i)

                        search_pattern = u"{}='{}'".format(col_name,token) if syntagma_type == "lexem" else  u'json_extract("{}", "$[0]")  = "{}"'.format(col_name,token)
                        #search_pattern = u"='{}'".format(token) if syntagma_type == "lexem" else  u"LIKE '%{}%'".format(token)
                        where.append(search_pattern)
                        #where.append(u"{}{} {} ".format(context_tag_name_l,token_index-i,search_pattern))

                    elif i == token_index:
                        where.append(u"{}='{}' ".format(normalized_word_tag_name,token))
                    elif i > token_index:
                        col_name = u"{}{}".format(context_tag_name_r,i-token_index)
                        search_pattern = u"{}='{}'".format(col_name,token) if syntagma_type == "lexem" else  u'json_extract("{}", "$[0]")  = "{}"'.format(col_name,token)
                        #search_pattern = u"='{}'".format(token) if syntagma_type == "lexem" else  u"LIKE '%{}%'".format(token)
                        where.append(search_pattern)
                        #where.append(u"{}{} {} ".format(context_tag_name_l,token_index-i,search_pattern))

                        # #search_pattern = u"='{}'".format(token) if syntagma_type == "lexem" else  u"LIKE '%{}%'".format(token)
                        # search_pattern = u"='{}'".format(token) if syntagma_type == "lexem" else  u"LIKE '%{}%'".format(token)
                        # where.append(u"{}{} {} ".format(context_tag_name_r,i-token_index,search_pattern))

                if sentiment:
                    where.append(u"polarity LIKE '%{}%'".format(sentiment))
                #p(where,"where111")
                wheres.append(where)
            #p(wheres, "wheres")
            return wheres


        else: # for baseline
            #p(inp_syntagma,"inp_syntagma")
            syntagma_qeary = u"syntagma= '{}'".format("++".join([unicode(t) for t in inp_syntagma]))
            return [syntagma_qeary]



    def _repl(self, inp_syntagma="*", scope=False,where=False, output="list", size_to_get=1000,thread_name="Thread0"):
        #p(where, "whererepl")
        if inp_syntagma == "*":
            for row in  self.statsdb.lazyget("replications",  output=output, case_sensitiv=self._case_sensitiv):
                yield row
        else:
            if not where:
                self.logger.error("Where wasn't given.")
                yield False
                return
            for row in self.statsdb.lazyget("replications",  where=where, connector_where="AND", output=output, case_sensitiv=self._case_sensitiv):
                yield row


    def _redu(self, inp_syntagma="*",scope=False,  where=False, connector_where="AND", output="list", size_to_get=1000,thread_name="Thread0"):
        #p(where, "where")
        #p(where, "whereredu")
        if inp_syntagma == "*":
            for row in  self.statsdb.lazyget("reduplications",  where=where, connector_where=connector_where, output=output, case_sensitiv=self._case_sensitiv):
                yield row
        else:
            if not where:
                self.logger.error("Where wasn't given.")
                yield False
                return
            for row in self.statsdb.lazyget("reduplications",  where=where, connector_where="AND", output=output, case_sensitiv=self._case_sensitiv):
                yield row


    def _baseline(self, inp_syntagma="*",scope=False, max_scope=False,  where=False, connector_where="AND", output="list", size_to_get=1000,thread_name="Thread0" ):
        if inp_syntagma == "*":
            for row in  self.statsdb.lazyget("baseline",  where=where, connector_where=connector_where, output=output, case_sensitiv=self._case_sensitiv):
                extracted = row[0].split("++")
                if max_scope:
                    #p(len(extracted),"len(extracted)")
                    #p(extracted)
                    if  len(extracted) <= max_scope:
                        yield (extracted, row[1])
                else:
                    yield (extracted, row[1])
        else:
            if not where:
                self.logger.error("Where wasn't given.")
                yield False
                return

            for row in self.statsdb.lazyget("baseline",  where=where, connector_where="AND", output=output, case_sensitiv=self._case_sensitiv):
                yield (row[0].split("++"), row[1]) 



    def _is_syntagma_scope_right(self, scope_num):
        #self._context_left
        #self._context_right
        if scope_num > self._avaliable_scope:
            #self.logger.error("")
            return False
        else:
            return True



    # def _repetitions_generator(self):
    #     if scope == 1:
    #         for word in self.baseline():
    #             current_bunch_of_rows = False
    #             if baseline:
    #                 pass
    #                 current_bunch_of_rows = to_row(current_bunch_of_rows)

    #             if repl:
    #                 if repl in word:
    #                     pass
    #                     current_bunch_of_rows = to_row(current_bunch_of_rows)

    #             if redu:
    #                 if redu in word:
    #                     pass
    #                     current_bunch_of_rows = to_row(current_bunch_of_rows)

    #     if scope > 1:
    #         for phrase in self.reduplications():
    #             pass



    # def export(output_file_name, output_file_format="csv", baseline=True, repl=False, redu=False, search_pattern=False, scope="*", context_left=False, context_right=False, meta_data=False, linguistic_data=False):
    #     #stats.export(output_file_name, output_file_format=output_file_format,baseline=baseline, repl=repl, redu=redu, search_pattern=splitted_search_pattern_paradigma, scope=scope, context_left=context_left, context_right=context_right, meta_data=splitted_meta_data, linguistic_data=splitted_linguistic_data)
    #     self._repetitions_generator()
    #     export = Exporter()
    #     export.tocsv(self._repetitions_generator())









    ###########################Setters####################


    def compute(self,inp_corp, stream_number=1, datatyp="dict", text_field_name="text", adjust_to_cpu=True,min_files_pro_stream=1000,cpu_percent_to_get=50,output="dict",  thread_name="Thread0", create_def_indexes=True):
        try:
            if not isinstance(inp_corp, Corpus):
                self.logger.error("Given InpObject is not from Corpus type. Insert was aborted!")
                return False

            if  self._was_space_optimized: ## insert "was_space_optimized" as attribute to the StatsDB!!!
               msg = "Current StatsDB is closed for new Insertions because it  was already SizeOptimized and all temporary Data was deleted"
               self.logger.error(msg)
               self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
               self._terminated = True
               return False


            self._init_insertion_variables()

            self.corp = inp_corp
            self._corp_info  = self.corp.info()
            
            #self.status_bars_manager =  self._get_status_bars_manager()

            ##### Status-Bar - Name of the processed DB
            if self._status_bar:
                if self._in_memory:
                    dbname = ":::IN-MEMORY-DB:::"
                else:
                    dbname = '{}'.format(self.statsdb.fname())
                status_bar_starting_corpus_insertion = self._get_new_status_bar(None, self.status_bars_manager.term.center( dbname) , "", counter_format=self.status_bars_manager.term.bold_white_on_cyan("{fill}{desc}{fill}"))
                status_bar_starting_corpus_insertion.refresh()



            if adjust_to_cpu:
                stream_number= get_number_of_streams_adjust_cpu( min_files_pro_stream, inp_corp.corpdb.rownum("documents"), stream_number, cpu_percent_to_get=cpu_percent_to_get)
                if stream_number is None or stream_number==0:
                    #p((self._get_number_of_left_over_files(),self.counter_lazy_getted),"self._get_number_of_left_over_files()")
                    self.logger.error("Number of input files is 0. Not generators could be returned.", exc_info=self._logger_traceback)
                    return []

            streams= self.get_streams_from_corpus(inp_corp, stream_number, datatyp=datatyp)
            #p(streams, "streams")
            ## threads
            if self._status_bar:
                status_bar_threads_init = self._get_new_status_bar(len(streams), "ThreadsStarted", "threads")
            

            #i=1
            self._threads_num = len(streams)
            if self._threads_num>1:
                if self._status_bar:
                    unit = "rows"
                    self.main_status_bar_of_insertions = self._get_new_status_bar(0, "AllThreadsTotalInsertions", unit)
                    self.main_status_bar_of_insertions.refresh()
                    #self.main_status_bar_of_insertions.total = 0


            for stream in streams:
                gen = stream[1]
                if not self._isrighttype(gen):
                    self.logger.error("StatsComputationalError: Given InpData not from right type. Please give an list or an generator.", exc_info=self._logger_traceback)
                    return False
                #p(gen)

                thread_name = stream[0]
                processThread = threading.Thread(target=self._compute, args=(gen,datatyp,  thread_name,text_field_name), name=thread_name)
                processThread.setDaemon(True)
                processThread.start()
                self.active_threads.append(processThread)
                if self._status_bar:
                    status_bar_threads_init.update(incr=1)
                #i+=1
                time.sleep(1)

            self.logger.info("'{}'-thread(s) was started. ".format(len(self.active_threads)))

            time.sleep(3)

            if not self._wait_till_all_threads_are_completed("Insert"):
                return False


            self.statsdb._write_cashed_insertion_to_disc(with_commit=True)



            ## save attributes from the main counter
            if self._status_bar:
                if self.main_status_bar_of_insertions:
                    self.counters_attrs["compute"]["start"] = self.main_status_bar_of_insertions.start
                    self.counters_attrs["compute"]["end"] = self.main_status_bar_of_insertions.last_update
                    self.counters_attrs["compute"]["total"] = self.main_status_bar_of_insertions.total
                    self.counters_attrs["compute"]["desc"] = self.main_status_bar_of_insertions.desc
                else:
                    self.counters_attrs["compute"] = False


            #self._print_summary_status()


            self.statsdb.commit()
            if create_def_indexes:
                self.statsdb.init_default_indexes(thread_name=thread_name)
                self.statsdb.commit()

            if self._status_bar:
                inserted_repl = self.statsdb.rownum("replications")
                inserted_redu = self.statsdb.rownum("reduplications")
                uniq_syntagma_in_baseline = self.statsdb.rownum("baseline")

                status_bar_total_summary = self._get_new_status_bar(None, self.status_bars_manager.term.center("Repl:'{}'; Redu:'{}'; UniqSyntagmaBaseline: '{}'.".format(inserted_repl, inserted_redu,uniq_syntagma_in_baseline ) ), "",  counter_format=self.status_bars_manager.term.bold_white_on_cyan('{fill}{desc}{fill}\n'))
                status_bar_total_summary.refresh()
                self.status_bars_manager.stop()

            self.logger.info("Current StatsDB has '{}' rows in the Replications Table.".format(inserted_repl))
            self.logger.info("Current StatsDB has '{}' rows in the Reduplications Table.".format(inserted_redu))
            self.logger.info("Current StatsDB has '{}' rows in the Baseline Table.".format(uniq_syntagma_in_baseline))

            if len(self.threads_unsuccess_exit) >0:
                self.logger.error("StatsComputational process is failed. (some thread end with error)")
                raise ProcessError, "'{}'-Threads end with an Error.".format(len(self.threads_unsuccess_exit))
                return False
            else:
                self.logger.info("StatsComputational process end successful!!!")
                return True

            self._last_insertion_was_successfull = True
            self._end_time_of_the_last_insertion = time.time()



            #self._wait_till_all_threads_are_completed()

            #self._print_summary_status()
            #self.opened_gateways.terminate()



            # if len(self.threads_unsuccess_exit) >0:
            #     return False
            # else:
            #     return True


        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("ComputeError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
        except KeyboardInterrupt:
            self.logger.warning("KeyboardInterrupt: Process was stopped from User. Some inconsistence in the current DB may situated.")
            sys.exit()
           




    def _compute(self, inp_data, datatyp="dict",  thread_name="Thread0", text_field_name="text", baseline_insertion_border=100000,add_also_repeted_redu_to_baseline=True):
        try:
            if not self._check_corp_should_exist():
                self._terminated = True
                msg = "StatsObj wasn't found."
                self.logger.error(msg)
                self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                return False

            if not self._corp_info:
                self._terminated = True
                msg = "CorpInfo wasn't found."
                self.logger.error(msg)
                self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                return False

            status_bar_insertion_in_the_current_thread = self._initialisation_computation_process( inp_data,text_field_name=text_field_name,  thread_name=thread_name, )
            if self._status_bar:
                if not  status_bar_insertion_in_the_current_thread: return False


            # if self._status_bar:
            #     status_bar_of_insertions = self._get_new_status_bar(len(inp_data), "{}:Insertion".format(thread_name), "files")


            
            #p(inp_data,"inp_data")

            for row_as_dict in inp_data:
                if self._status_bar:
                    status_bar_insertion_in_the_current_thread.update(incr=1)
                    if self._threads_num>1:
                        self.main_status_bar_of_insertions.update(incr=1)
                #p(row_as_dict[self._text_field_name], "row_as_dict[self._text_field_name]")
                text_elem = json.loads(row_as_dict[self._text_field_name])
                row_as_dict[self._text_field_name]  = self._preprocess(text_elem,thread_name=thread_name)
                #p(row_as_dict, c="m")

                ### Extraction 
                extracted_repl_in_text_container, repl_free_text_container, rle_for_repl_in_text_container = self.extract_replications(text_elem, thread_name=thread_name)
                extracted_redu_in_text_container, redu_free_text_container, mapping_redu = self.extract_reduplications(repl_free_text_container, rle_for_repl_in_text_container, thread_name=thread_name)
                computed_baseline = self.compute_baseline(redu_free_text_container,extracted_redu_in_text_container,add_also_repeted_redu=add_also_repeted_redu_to_baseline)

                ### Insertion
                self.insert_repl_into_db(row_as_dict,text_elem,extracted_repl_in_text_container, repl_free_text_container,rle_for_repl_in_text_container,redu_free_text_container,mapping_redu)
                self.insert_redu_into_db(row_as_dict,text_elem,extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container, repl_free_text_container, mapping_redu)
                self.baseline_lazyinsertion_into_db(computed_baseline,baseline_insertion_border=baseline_insertion_border)


            self.baseline_insert_left_over_data()


            if self._status_bar:
                status_bar_insertion_in_the_current_thread.refresh()
                self.counters_attrs["_compute"][thread_name]["start"] = status_bar_insertion_in_the_current_thread.start
                self.counters_attrs["_compute"][thread_name]["end"] = status_bar_insertion_in_the_current_thread.last_update
                self.counters_attrs["_compute"][thread_name]["total"] = status_bar_insertion_in_the_current_thread.total
                self.counters_attrs["_compute"][thread_name]["desc"] = status_bar_insertion_in_the_current_thread.desc
                status_bar_insertion_in_the_current_thread.close(clear=False)


            self.threads_status_bucket.put({"name":thread_name, "status":"done"})
            self.logger.debug("_Compute: '{}'-Thread is done and was stopped.".format(thread_name))
            return True


        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            msg = "_ComputeError: See Exception: '{}'. ".format(e)
            self.logger.error(msg, exc_info=self._logger_traceback)
            self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
            return False










##



    def _set_rle(self,  thread_name="Thread0"):
        try:
            self.logger.debug("INIT-RLE: Start the initialization of Run_length_encoder for '{}'-Thread.".format(thread_name))
            self.preprocessors[thread_name]["rle"] = Rle(self.logger)
            self.logger.debug("INIT-RLE: Run_length_encoder for '{}'-Thread was initialized.".format(thread_name))
            return True
        except Exception, e:
            self.logger.error("Exception was encountered: '{}'. ".format(e), exc_info=self._logger_traceback)
            return False

    def _init_preprocessors(self, thread_name="Thread0"):
        try:

            if not self._set_rle(thread_name):
                self.logger.error("RLE in '{}'-Thread wasn't initialized. Script will be aborted.".format(thread_name), exc_info=self._logger_traceback)
                self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
                return False

            # if self._status_bar:
            #     status_bar_preprocessors_init = self._get_new_status_bar(1, "{}:PreprocessorsInit".format(thread_name), "unit")


            # if self._set_rle(thread_name):
            #     if self._status_bar:
            #         status_bar_preprocessors_init.update(incr=1)
            #         status_bar_preprocessors_init.refresh()
            # else:
            #     status_bar_preprocessors_init.total -= 1
            #     self.logger.error("RLE in '{}'-Thread wasn't initialized. Script will be aborted.".format(thread_name), exc_info=self._logger_traceback)
            #     self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
            #     return False



            # if self._status_bar:
            #     self.counters_attrs["_init_preprocessors"][thread_name]["start"] = status_bar_preprocessors_init.start
            #     self.counters_attrs["_init_preprocessors"][thread_name]["end"] = status_bar_preprocessors_init.last_update
            #     self.counters_attrs["_init_preprocessors"][thread_name]["total"] = status_bar_preprocessors_init.total
            #     self.counters_attrs["_init_preprocessors"][thread_name]["desc"] = status_bar_preprocessors_init.desc

            self.logger.info("PreprocessorsInit: All Preprocessors for '{}'-Thread was initialized.".format(thread_name))
            return True
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("PreprocessorsInitError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            return False





    def _preprocess(self, text_elem,thread_name="Thread0"):
        if not self.force_cleaning_flags:
            if not self._corp_info["del_url"]:
                if self._ignore_url:
                    self.force_cleaning_flags.append("url")

            if not self._corp_info["del_hashtag"]:
                if self._ignore_hashtag:
                    self.force_cleaning_flags.append("hashtag")

            if not self._corp_info["del_mention"]:
                if self._ignore_mention:
                    self.force_cleaning_flags.append("mention")

            if not self._corp_info["del_punkt"]:
                if self._ignore_punkt:
                    self.force_cleaning_flags.append("punkt")

            if not self._corp_info["del_num"]:
                if self._ignore_num:
                    self.force_cleaning_flags.append("num")

        new_text_elem = []
        for sent_container in text_elem:
            #p(sent_container, "sent_container")
            sent = sent_container[0]
            sentiment = sent_container[1]
            categories = get_categories([token[0] for token in sent])
            temp_sent = []
            i = -1
            for token_container, categorie in zip(sent, categories):
                i+=1
                if self._force_cleaning:
                    if "url" in self.force_cleaning_flags:
                        if categorie.lower() == "url":
                            #p(token)
                            if self._log_ignored:
                                self.logger.outsorted_stats("Following Token was ignored: '{}'. Reason: 'It is an URL'.".format(token_container))
                                #indexes_to_del.append((index_level_1, index_level_2, index_level_3))
                                temp_sent.append([(":cleaned:"),(":URL:")])
                                continue

                    if "hashtag" in self.force_cleaning_flags:
                        if categorie.lower() in "hashtag":
                            #p(token)
                            if self._log_ignored:
                                self.logger.outsorted_stats("Following Token was ignored: '{}'. Reason: 'It is a HashTag'.".format(token_container))
                                temp_sent.append([(":cleaned:"),(":hashtag:")])
                                #indexes_to_del.append((index_level_1, index_level_2, index_level_3))
                                continue

                    if "mention" in self.force_cleaning_flags:
                        if categorie.lower() in  "mention":
                            #p(token)
                            if self._log_ignored:
                                self.logger.outsorted_stats("Following Token was ignored: '{}'. Reason: 'It is a Mention'.".format(token_container))
                                #indexes_to_del.append((index_level_1, index_level_2, index_level_3))
                                temp_sent.append([(":cleaned:"),(":mention:")])
                                continue

                    if "punkt" in self.force_cleaning_flags:
                        if categorie.lower() == "symbol":
                            #p(token)
                            if self._log_ignored:
                                self.logger.outsorted_stats("Following Token was ignored: '{}'. Reason: 'It is a Punctuation'.".format(token_container))
                                #indexes_to_del.append((index_level_1, index_level_2, index_level_3))
                                temp_sent.append([(":cleaned:"),(":punkt:")])
                                continue

                    if "num" in self.force_cleaning_flags:
                        if categorie.lower() == "number":
                            #p(token)
                            if self._log_ignored:
                                self.logger.outsorted_stats("Following Token was ignored: '{}'. Reason: 'It is a Number'.".format(token_container))
                                #indexes_to_del.append((index_level_1, index_level_2, index_level_3))
                                temp_sent.append([(":cleaned:"),(":num:")])
                                continue

                #p(token_container)
                temp_sent.append([token_container[0],token_container[1]])
                #p([token_container[0],token_container[1], i])
                #p(temp_sent, "temp_sent")

            new_text_elem.append([temp_sent, sentiment])

        self.logger.debug("Text-Cleaning for current text_elem is done.")
        #p(new_text_elem, "new_text_elem")
        #sys.exit()
        return new_text_elem


    def extract_reduplications(self,repl_free_text_container,rle_for_repl_in_text_container, thread_name="Thread0"):
        extracted_redu_in_text_container = []
        redu_free_text_container = []
        text_elem_mapping = []
        mapping_redu = []
        #p(text_elem, "text_elem")
        #p(repl_free_text_container, "repl_free_text_container")
        sent_index = -1
        #total_sent_number = len(repl_free_text_container)
        #p(total_sent_number,"total_sent_number")
        for sent in repl_free_text_container:
            ########### SENTENCE LEVEL ##################

            sent_index+= 1
            #p(sent, "sent")
            repl_in_tuples, mapped = self.preprocessors[thread_name]["rle"].encode_to_tuples(sent,mapping=True)
            #p(repl_in_tuples, "repl_in_tuples")
            extracted_reps, rep_free_sent = self.preprocessors[thread_name]["rle"].rep_extraction_sent(repl_in_tuples,mapped)
            #redu_free_index = -1
            for rep in  extracted_reps:
                #redu_free_index += 1
                start_index = rep['start_index_in_orig']
                length = rep['length']
                i_redu_free = rep["index_in_redu_free"]
                repl_free_range = repl_free_text_container[sent_index][start_index:start_index+length]
                rle_range = rle_for_repl_in_text_container[sent_index][start_index:start_index+length]
                addit_info = []
                #p((, ))
                #p(repl_free_range, "repl_free_range")
                #p(rle_range, "rle_range")

                addit_info = [r if r else o for o,r in zip(repl_free_range,rle_range)]
                #addit_info = [r if (r,o[1]) else o for o,r in zip(orig_range,rle_range)]

                #p(addit_info, "addit_info", c="r")
                counts = Counter(addit_info)
                #p(counts, "counts")
                rep_free_sent[i_redu_free] = (rep_free_sent[i_redu_free], dict(counts))

            #p((extracted_reps, rep_free_sent), c="r")
            #p(rep_free_sent, "rep_free_sent")
            extracted_redu_in_text_container.append(extracted_reps)
            redu_free_text_container.append(rep_free_sent)
            mapping_redu.append(mapped)
            #sys.exit()
        return extracted_redu_in_text_container, redu_free_text_container, mapping_redu






    def extract_replications(self, text_elem, thread_name="Thread0"):
        repl_free_text_container = []
        rle_for_repl_in_text_container = []
        extracted_repl_in_text_container = []

        #p(text_elem)
        sent_index = -1
        total_sent_number = len(text_elem)
        for sent_container in text_elem:
            ########### SENTENCE LEVEL ##################
            repl_free_text_container.append([])
            rle_for_repl_in_text_container.append([])
            extracted_repl_in_text_container.append([])
            sent_index+= 1
            
            #p((type(sent_container),sent_container), "sent_container_in_repl_extr")
            try:
                sent = sent_container[0]
                sentiment = sent_container[1]
            except Exception as e:
                #p(sent_container, "sent_container")
                self._terminated = True
                msg = "Given SentContainer has wrong structure! SentContainer: '{}'; Exception: '{}'.".format(sent_container,e)
                self.logger.error(msg)
                self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                return False


            if not self._case_sensitiv:
                sent = [[token_container[0].lower(), token_container[1]] for token_container in sent]


            temp_sent = []
            token_index = -1
            #p(sent, "sent")
            #p(sentiment, "sentiment")
            #total_tokens_number = len(sent)
            ignored_pos = set(["URL", "U"])
            for token_container in sent:
                #repl_free_text_container[sent_index].append([])
                #repl_free_text_container[sent_index].append("")

                ########### TOKEN LEVEL##################
                #p(token_container, "token_container")
                token_index+=1
                try:
                    token = token_container[0]
                    pos = token_container[1]
                    #nr_of_token_in_sent = token_index
                except Exception, e:
                    #p(sent_container, "sent_container")
                    self._terminated = True
                    msg = "Given TokenContainer has wrong structure! '{}'.".format(token_container)
                    self.logger.error(msg)
                    self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                    return False

                #p(token_container, "token_container")
                #p(sent_index, "sent_index", c="r")
                if token != ":cleaned:" and pos not in ignored_pos:
                    #if "absurd.com" in token:
                    #    p((token, pos))
                    repl_in_tuples = self.preprocessors[thread_name]["rle"].encode_to_tuples(token)
                    extracted_reps, rep_free_word,rle_word = self.preprocessors[thread_name]["rle"].rep_extraction_word(repl_in_tuples, get_rle_as_str=True)
                    repl_free_text_container[sent_index].append(rep_free_word)
                    if extracted_reps:
                        #p((extracted_reps, rep_free_word,rle_word))
                        rle_for_repl_in_text_container[sent_index].append(rle_word)
                        extracted_repl_in_text_container[sent_index].append(extracted_reps)
                    else:
                        rle_for_repl_in_text_container[sent_index].append("")
                        extracted_repl_in_text_container[sent_index].append("")
                else:
                    repl_free_text_container[sent_index].append( token)
                    rle_for_repl_in_text_container[sent_index].append("")
                    extracted_repl_in_text_container[sent_index].append("")

                #p((sent_index,token_index, repl_free_text_container[sent_index][token_index],rle_for_repl_in_text_container[sent_index][token_index] ,extracted_repl_in_text_container[sent_index][token_index]))
        #p(repl_free_text_container, "repl_free_text_container")
        return extracted_repl_in_text_container,  repl_free_text_container, rle_for_repl_in_text_container 



    def _get_cleaned_redu_free(self, redu_free_text_container):
        inp_token_list = []
        for sent in redu_free_text_container:
            for token in sent:

                try:
                    token[1].values
                    inp_token_list.append(token[0])
                except (IndexError,AttributeError):
                    inp_token_list.append(token)
        return inp_token_list
        
    def compute_baseline(self, redu_free_text_container,extracted_redu_in_text_container, add_also_repeted_redu=True):
        ## Step 1: Extract ngramm from redu and repl free text element
        inp_token_list = self._get_cleaned_redu_free(redu_free_text_container)
        computed_baseline  = []
        for n in xrange(1,self.baseline_ngramm_lenght+1):
            computed_baseline += [tuple(inp_token_list[i:i+n]) for i in xrange(len(inp_token_list)-n+1)]

        ## Step 2: Add reduplicated unigramms
        if add_also_repeted_redu:
            for sent in extracted_redu_in_text_container:
                for redu in sent:
                    if redu:
                        #p((redu["word"],),"re_wo")
                        computed_baseline += [(redu["word"],)]*(redu["length"]-1) # -1, because 1 occur of this unigramm is already in the baseline
                        

        return computed_baseline



    def temporize_baseline(self, computed_baseline):
        #self.temporized_baseline = defaultdict(int)
        #p(computed_baseline, "computed_baseline")
        for syntagma in computed_baseline:
            #p(syntagma)
            self.temporized_baseline[syntagma] += 1




    def baseline_insert_all_temporized_data(self):
        #p(self.temporized_baseline, "self.temporized_baseline")
        qeary = """
                INSERT OR REPLACE INTO baseline VALUES (
                    :0,
                    COALESCE((SELECT counter FROM baseline WHERE syntagma=:0), 0) + :1
                );"""

        cursor = self.statsdb._db.cursor()
        #self.statsdb.executemany(qeary, self.temporized_baseline.iteritems())
        #p(list(self.temporized_baseline.iteritems()),"self.temporized_baseline.iteritems()")
        cursor.executemany(qeary, [("++".join(syntag), count) for syntag, count in self.temporized_baseline.iteritems()])
        self.temporized_baseline = defaultdict(int)


    def baseline_intime_insertion_into_db(self):
        #p("111")
        #p(self.temporized_baseline, "self.temporized_baseline")
        self.baseline_insert_all_temporized_data()

    def baseline_insert_left_over_data(self):
        #p("222")
        self.baseline_insert_all_temporized_data()


    def baseline_lazyinsertion_into_db(self,computed_baseline, baseline_insertion_border=100000):
        if len(self.temporized_baseline) > baseline_insertion_border:
            self.temporize_baseline(computed_baseline)
            self.baseline_intime_insertion_into_db()
        else:
            self.temporize_baseline(computed_baseline)
        #self.insert_temporized_baseline_into_db()





    def insert_redu_into_db(self,row_as_dict,text_elem,extracted_redu_in_text_container, redu_free_text_container, rle_for_repl_in_text_container, repl_free_text_container, mapping_redu):
        sent_index = -1
        for redu_in_sent in extracted_redu_in_text_container:
            sent_index += 1
            for redu in redu_in_sent:
                #p(redu, c="r")
                #if redu:
                #p(redu_in_sent, "redu_in_sent")
                #p(redu_free_text_container, "redu_free_text_container")
                try:
                    rle_word = rle_for_repl_in_text_container[sent_index][redu['start_index_in_orig']]
                    #p((redu['start_index_in_orig'],rle_for_repl_in_text_container[sent_index][redu['start_index_in_orig']]), "redu['start_index_in_orig']", c="m")
                    #p(redu_free_text_container[sent_index][redu['index_in_redu_free']], "orig_words")

                    input_dict = {
                            "doc_id": row_as_dict[self._id_field_name],
                            "start_index": (sent_index,redu['start_index_in_orig']),
                            #"rle_word": rle_word if rle_word else repl_free_text_container[sent_index][redu['start_index_in_orig']],
                            "pos":text_elem[sent_index][0][redu['start_index_in_orig']][1],
                            "normalized_word": repl_free_text_container[sent_index][redu['start_index_in_orig']],
                            'orig_words':redu_free_text_container[sent_index][redu['index_in_redu_free']][1],
                            "redu_length": redu['length'],
                            "polarity":text_elem[sent_index][1],
                            #"repl_letter": repl_container[0],
                            
                            #"index_of_repl": repl_container[2],
                            }
                    
                except Exception as e:
                    #p(sent_container, "sent_container")
                    self._terminated = True
                    msg = "Given ReduContainer has wrong structure! '{}'. ('{}')".format(repl_container, e)
                    self.logger.error(msg)
                    self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                    return False

                #sent = 
                start_index = redu['start_index_in_orig']
                #redu_length = redu['length']

                if self._context_left:
                    for context_number in range(1,self._context_left+1):
                        col_name_context = "contextL{}".format(context_number)
                        col_name_info = "context_infoL{}".format(context_number)
                        #while True:
                    
                        temp_index = redu['index_in_redu_free'] - context_number
 
                        ## if needed context_item in the current sent 
                        if (temp_index) >= 0:
                            token_index_in_orig_t_elem = mapping_redu[sent_index][temp_index] 
                            try:
                                redu_free_text_container[sent_index][temp_index][1].items()
                                
                                item = redu_free_text_container[sent_index][temp_index][0]
                                info = [text_elem[sent_index][0][token_index_in_orig_t_elem][1],redu_free_text_container[sent_index][temp_index][1]]
                                #info = text_elem[sent_index][0][temp_index][1]

                            except:
                                
                                item = redu_free_text_container[sent_index][temp_index]
                                info = [text_elem[sent_index][0][token_index_in_orig_t_elem][1]]
                            #'start_index_in_orig'
                            #p((col_name_context,item, info), "item", c="m")
                        else: ## if needed context_item not in the current sent 
                            leftover_contextnumber = context_number - redu['index_in_redu_free'] # left over times to go to the left
                            if not context_number: # if the not time to go to the left
                                raise Exception, "WrongContextNumber. It should be >0"
                            number_of_loops = 0
                            while True:
                                number_of_loops += 1
                                temp_sent_index = sent_index - number_of_loops
                                if temp_sent_index < 0:
                                    item = "" #[number_of_loops, temp_sent_index, leftover_contextnumber]
                                    info = []
                                    break 
                                last_sent = redu_free_text_container[temp_sent_index+1]
                                current_sent = redu_free_text_container[temp_sent_index]
                                leftover_contextnumber = leftover_contextnumber if number_of_loops == 1 else leftover_contextnumber-(len(last_sent))
                                if leftover_contextnumber <= len(current_sent) and leftover_contextnumber >= 0:
                                    #item = current_sent[-leftover_contextnumber]
                                    #p(leftover_contextnumber, "leftover_contextnumber")
                                    #info = text_elem[temp_sent_index][0][-leftover_contextnumber][1]
                                    #info = rle_for_repl_in_text_container[sent_index][start_index:start_index+redu['length']]
                                    temp_index = -leftover_contextnumber
                                    token_index_in_orig_t_elem = mapping_redu[temp_sent_index][temp_index] 
                                    try:
                                        redu_free_text_container[temp_sent_index][temp_index][1].items()
                                        item = redu_free_text_container[temp_sent_index][temp_index][0]
                                        info = [text_elem[temp_sent_index][0][token_index_in_orig_t_elem][1],redu_free_text_container[temp_sent_index][temp_index][1]]
                                        #info = text_elem[temp_sent_index][0][temp_index][1]

                                    except:
                                        item = redu_free_text_container[temp_sent_index][temp_index]
                                        info = [text_elem[temp_sent_index][0][token_index_in_orig_t_elem][1]]



                                    break
                                    #text_elem[sent_index][0][redu['index_in_redu_free']][1]

                        #item = json.dumps(item)
                        input_dict.update({col_name_context: item, col_name_info:info})                        


                if self._context_right:
                    #p("---------------------\nRIGHT START", c="c")
                    for context_number in range(1,self._context_right+1):
                        col_name_context = "contextR{}".format(context_number)
                        col_name_info = "context_infoR{}".format(context_number)
                        #while True:
                        temp_index = redu['index_in_redu_free'] + context_number
                        
                        
                        #p((context_number,sent_index,temp_index,len(redu_in_sent)), "context_number,sent_index,temp_index,len(redu_in_sent)")
                        ## if needed context_item in the current sent 
                        if temp_index < len(redu_free_text_container[sent_index]):
                            #item = redu_free_text_container[sent_index][temp_index]
                            
                            token_index_in_orig_t_elem = mapping_redu[sent_index][temp_index] 
                            #p((sent_index,temp_index, token_index_in_orig_t_elem), "sent_index,temp_index, token_index_in_orig_t_elem")
                            try:
                                #p("111")
                                redu_free_text_container[sent_index][temp_index][1].items
                                
                                item = redu_free_text_container[sent_index][temp_index][0]
                                info = [text_elem[sent_index][0][token_index_in_orig_t_elem][1],redu_free_text_container[sent_index][temp_index][1]]
                                #info = text_elem[sent_index][0][temp_index][1]

                            except:
                                #p("222")
                                
                                item = redu_free_text_container[sent_index][temp_index]
                                info = [text_elem[sent_index][0][token_index_in_orig_t_elem][1]]

                            #p((item, info), c="b")
                            #info = rle_for_repl_in_text_container[sent_index][start_index:start_index+redu['length']]
                            #info = text_elem[sent_index][0][temp_index][1]
                            #p((col_name_context,item, info), "item", c="m")
                        else: ## if needed context_item not in the current sent 
                            leftover_contextnumber = context_number - (len(redu_free_text_container[sent_index]) - (redu['index_in_redu_free']+1)) # left over times to go to the left
                            if not leftover_contextnumber: # if the not time to go to the left
                                raise Exception, "1. WrongContextNumber. It should be >0"
                            number_of_loops = 0
                            while True:
                                number_of_loops += 1
                                temp_sent_index = sent_index + number_of_loops
                                if temp_sent_index >= len(redu_free_text_container):
                                    item = ""
                                    info = []
                                    #p((item, info), c="b")
                                    break 
                                last_sent = redu_free_text_container[temp_sent_index-1]
                                current_sent = redu_free_text_container[temp_sent_index]
                                leftover_contextnumber = leftover_contextnumber if number_of_loops == 1 else leftover_contextnumber-(len(last_sent))
                                if leftover_contextnumber <= 0 :
                                    raise Exception, "2. WrongLeftoverContextNumber. It should be >0"
                                if leftover_contextnumber <= len(current_sent) and leftover_contextnumber > 0:
                                    temp_index =leftover_contextnumber-1
                                    token_index_in_orig_t_elem = mapping_redu[temp_sent_index][temp_index] 
                                    #p((temp_sent_index,temp_index, token_index_in_orig_t_elem), "sent_index,temp_index, token_index_in_orig_t_elem")
                                    try:
                                        #p("333")

                                        redu_free_text_container[temp_sent_index][temp_index][1].items
    
                                        item = redu_free_text_container[temp_sent_index][temp_index][0]
                                        info = [text_elem[temp_sent_index][0][token_index_in_orig_t_elem][1],redu_free_text_container[temp_sent_index][temp_index][1]]
                                        #info = text_elem[temp_sent_index][0][temp_index][1]

                                    except:
                                        #p("444")
                                        item = redu_free_text_container[temp_sent_index][temp_index]
                                        info = [text_elem[temp_sent_index][0][token_index_in_orig_t_elem][1]]
                                    #p((item, info), c="b")
                                    #info = [number_of_loops, temp_sent_index, leftover_contextnumber]


                                    #item = current_sent[temp_index]
                                    #info = text_elem[temp_sent_index][0][temp_index][1]
                                    #p((col_name_context,item,info), c="r")
                                    break


                        #item = json.dumps(item)
                        input_dict.update({col_name_context: item, col_name_info:info})  
                #p("RIGHT STOP ---------------------\n", c="c")
                self.statsdb.lazyinsert("reduplications", input_dict)
                #p(input_dict, "input_dict")





    def insert_repl_into_db(self,row_as_dict,text_elem,extracted_repl_in_text_container, repl_free_text_container,rle_for_repl_in_text_container, redu_free_text_container,mapping_redu, thread_name="Thread0"):
        # p(extracted_repl_in_text_container, "extracted_repl_in_text_container")
        # p(repl_free_text_container, "repl_free_text_container")
        # p(rle_for_repl_in_text_container, "rle_for_repl_in_text_container")
        # p(row_as_dict, "row_as_dict")
        #extracted_replications = []
        sent_index = -1
        #p((len(text_elem),text_elem),"text_elem")
        for sent in extracted_repl_in_text_container:
            #p(sent, "sent")
            sent_index += 1
            token_index = -1


            for repls_for_current_token in sent:
                token_index += 1
                if repls_for_current_token:
                    for repl_container in repls_for_current_token:
                        #p(repl_container, "repl_container")
                        
                        if repl_container:
                            try:
                                #p((sent_index, token_index), c="c")
                                current_sent_from_map = mapping_redu[sent_index]
                                next_left_index_in_orig_t_elem = token_index if token_index in current_sent_from_map else nextLowest(current_sent_from_map,token_index)
                                token_index_in_redu_free = current_sent_from_map.index(next_left_index_in_orig_t_elem)
                                it_is_redu = self._is_redu(sent_index,token_index_in_redu_free,redu_free_text_container)
                                input_dict = {
                                    "doc_id": row_as_dict[self._id_field_name],
                                    "token_index": (sent_index,token_index),
                                    "rle_word": rle_for_repl_in_text_container[sent_index][token_index],
                                    "pos":text_elem[sent_index][0][next_left_index_in_orig_t_elem][1]  if it_is_redu else text_elem[sent_index][0][token_index][1],
                                    "normalized_word": repl_free_text_container[sent_index][token_index],
                                    "polarity":text_elem[sent_index][1],
                                    "repl_letter": repl_container[0],
                                    "repl_length": repl_container[1],
                                    "index_of_repl": repl_container[2],
                                    "in_redu": [sent_index,next_left_index_in_orig_t_elem]  if it_is_redu  else []
                                            }
                            except Exception as e:
                                #p(sent_container, "sent_container")
                                self._terminated = True
                                msg = "Given ReplContainer has wrong structure! '{}'. ('{}')".format(repl_container, e)
                                self.logger.error(msg)
                                self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":msg})
                                return False
                            # contextL
                            # context_infoL
                            ## add context
                            if self._context_left:
                                for context_number in range(1,self._context_left+1):
                                    col_name_context = "contextL{}".format(context_number)
                                    col_name_info = "context_infoL{}".format(context_number)
                                    #while True:
                                
                                    #temp_index = token_index - context_number
                                    
                                    #temp_index = token_index - context_number
                                    temp_index = token_index_in_redu_free - context_number
                                    

                                    ## if needed context_item in the current sent 
                                    if (temp_index) >= 0:
                                        temp_next_left_index_in_orig_t_elem = mapping_redu[sent_index][temp_index]

                                        try:
                                            redu_free_text_container[sent_index][temp_index][1].items
                                            
                                            item = redu_free_text_container[sent_index][temp_index][0]
                                            info = [text_elem[sent_index][0][temp_next_left_index_in_orig_t_elem][1],redu_free_text_container[sent_index][temp_index][1]]
                                            #info = text_elem[sent_index][0][temp_index][1]
                                        except:
                                            item = redu_free_text_container[sent_index][temp_index]
                                            info = [text_elem[sent_index][0][temp_next_left_index_in_orig_t_elem][1]]

                                        #item = repl_free_text_container[sent_index][temp_index]
                                        #info = text_elem[sent_index][0][temp_index][1]
                                        #p((col_name_context,item, info), "item", c="m")
                                    else: ## if needed context_item not in the current sent 
                                        #leftover_contextnumber = context_number - token_index # left over times to go to the left
                                        leftover_contextnumber = context_number - token_index_in_redu_free # left over times to go to the left
                                        if not context_number: # if the not time to go to the left
                                            raise Exception, "WrongContextNumber. It should be >0"
                                        number_of_loops = 0
                                        while True:
                                            number_of_loops += 1
                                            temp_sent_index = sent_index - number_of_loops
                                            if temp_sent_index < 0:
                                                item = ""
                                                info = []
                                                break 
                                            last_sent = redu_free_text_container[temp_sent_index+1]
                                            current_sent = redu_free_text_container[temp_sent_index]
                                            leftover_contextnumber = leftover_contextnumber if number_of_loops == 1 else leftover_contextnumber-(len(last_sent))
                                            if leftover_contextnumber <= len(current_sent) and leftover_contextnumber >= 0:
                                                
                                                temp_index = -leftover_contextnumber
                                                temp_next_left_index_in_orig_t_elem = mapping_redu[temp_sent_index][temp_index]
                                                try:
                                                    redu_free_text_container[temp_sent_index][temp_index][1].items
                                                    item = redu_free_text_container[temp_sent_index][temp_index][0]
                                                    info = [text_elem[temp_sent_index][0][temp_next_left_index_in_orig_t_elem][1],redu_free_text_container[temp_sent_index][temp_index][1]]
                                                    #info = text_elem[temp_sent_index][0][temp_index][1]

                                                except:
                                                    item = redu_free_text_container[temp_sent_index][temp_index]
                                                    info = [text_elem[temp_sent_index][0][temp_next_left_index_in_orig_t_elem][1]]



                                                #item = current_sent[-leftover_contextnumber]
                                                # #p(leftover_contextnumber, "leftover_contextnumber")
                                                #info = text_elem[temp_sent_index][0][-leftover_contextnumber][1]
                                                break
                                                #text_elem[sent_index][0][token_index][1]

                                    #item = json.dumps(item)
                                    input_dict.update({col_name_context: item, col_name_info:info})                        


                            if self._context_right:
                                for context_number in range(1,self._context_right+1):
                                    col_name_context = "contextR{}".format(context_number)
                                    col_name_info = "context_infoR{}".format(context_number)
                                    #while True:
                                    #temp_index = token_index + context_number
                                    
                                    temp_index = token_index_in_redu_free + context_number
                                    
                                    ## if needed context_item in the current sent 
                                    if temp_index < len(redu_free_text_container[sent_index]):
                                        ####p((sent_index, temp_index, len(mapping_redu[sent_index])), "temp_next_left_index_in_orig_t_elem")
                                        temp_next_left_index_in_orig_t_elem = mapping_redu[sent_index][temp_index]
                                        #p((col_name_context,item, info), "item", c="m")
                                        #p((sent_index,temp_index,temp_next_left_index_in_orig_t_elem, ), "sent_index,temp_index,temp_next_left_index_in_orig_t_elem,")

                                        
                                        try:
                                            #p("111")
                                            redu_free_text_container[sent_index][temp_index][1].items
                                            
                                            item = redu_free_text_container[sent_index][temp_index][0]
                                            info = [text_elem[sent_index][0][temp_next_left_index_in_orig_t_elem][1],redu_free_text_container[sent_index][temp_index][1]]
                                            #info = text_elem[sent_index][0][temp_index][1]

                                        except:
                                            #p("222")
                                            
                                            item = redu_free_text_container[sent_index][temp_index]
                                            info = [text_elem[sent_index][0][temp_next_left_index_in_orig_t_elem][1]]


                                        #item = repl_free_text_container[sent_index][temp_index]
                                        #info = text_elem[sent_index][0][temp_index][1]

                                    else: ## if needed context_item not in the current sent 
                                        #leftover_contextnumber = context_number - (len(sent) - (token_index+1)) # left over times to go to the left
                                        leftover_contextnumber = context_number - (len(redu_free_text_container[sent_index]) - (token_index_in_redu_free+1)) # left over times to go to the left
                                        if not leftover_contextnumber: # if the not time to go to the left
                                            raise Exception, "1. WrongContextNumber. It should be >0"
                                        number_of_loops = 0
                                        while True:
                                            number_of_loops += 1
                                            temp_sent_index = sent_index + number_of_loops
                                            if temp_sent_index >= len(redu_free_text_container):
                                                item = ""
                                                info = []
                                                break 
                                            last_sent = redu_free_text_container[temp_sent_index-1]
                                            current_sent = redu_free_text_container[temp_sent_index]
                                            leftover_contextnumber = leftover_contextnumber if number_of_loops == 1 else leftover_contextnumber-(len(last_sent))
                                            if leftover_contextnumber <= 0 :
                                                raise Exception, "2. WrongLeftoverContextNumber. It should be >0"
                                            if leftover_contextnumber <= len(current_sent) and leftover_contextnumber > 0:
                                                temp_index =leftover_contextnumber-1
                                                #token_index_in_orig_t_elem = mapping_redu[temp_sent_index][temp_index] 
                                                # p((temp_sent_index,temp_index, token_index_in_orig_t_elem), "sent_index,temp_index, token_index_in_orig_t_elem")
                                                #p((col_name_context,item,info), c="r")
                                                #token_index_in_redu_free = token_index if token_index in mapping_redu[sent_index] else nextLowest(mapping_redu[sent_index],token_index)
                                                #temp_index = token_index_in_redu_free + temp_index
                                                temp_next_left_index_in_orig_t_elem = mapping_redu[temp_sent_index][temp_index]
                                                #p((temp_sent_index,token_index_in_redu_free,temp_index,temp_next_left_index_in_orig_t_elem),"temp_sent_index,token_index_in_redu_free,temp_index,temp_next_left_index_in_orig_t_elem")
                                                try:
                                                    #p("333")

                                                    redu_free_text_container[temp_sent_index][temp_index][1].items
                
                                                    item = redu_free_text_container[temp_sent_index][temp_index][0]
                                                    info = [text_elem[temp_sent_index][0][temp_next_left_index_in_orig_t_elem][1],redu_free_text_container[temp_sent_index][temp_index][1]]
                                                    #info = text_elem[temp_sent_index][0][temp_index][1]

                                                except:
                                                    #p("444")
                                                    item = redu_free_text_container[temp_sent_index][temp_index]
                                                    info = [text_elem[temp_sent_index][0][temp_next_left_index_in_orig_t_elem][1]]


                                                #item = current_sent[leftover_contextnumber-1]
                                                #info = text_elem[temp_sent_index][0][leftover_contextnumber-1][1]
                                                
                                                break


                                    #item = json.dumps(item)
                                    input_dict.update({col_name_context: item, col_name_info:info})  

                            #p(sent, "sent")
                            #p(repl_free_text_container[sent_index][token_index], "repl_free_text_container")
                            #p(rle_for_repl_in_text_container[sent_index][token_index], "rle_for_repl_in_text_container")
                            #p(input_dict, "input_dict")
                            #extracted_replications.append(input_dict)
                            self.statsdb.lazyinsert("replications", input_dict)





    ###################Optimizators########################










    ###########################Other Methods##################


    def exist(self):
        return True if self.statsdb else False


    def db(self):
        if not self._check_stats_db_should_exist():
            return False
        self.logger.debug("DBConnection was passed.")
        return self.statsdb









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







    #######################Status Bars##############

    def _get_new_status_bar(self, total, desc, unit, counter_format=False):
        #counter_format
        if counter_format:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True, counter_format=counter_format)
        else:
            counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit, leave=True)
        return counter

    def _get_status_bars_manager(self):
        config_status_bar = {'stream': sys.stdout,
                  'useCounter': True, 
                  "set_scroll": True,
                  "resize_lock": True
                  }
        enableCounter_status_bar = config_status_bar['useCounter'] and config_status_bar['stream'].isatty()
        return enlighten.Manager(stream=config_status_bar['stream'], enabled=enableCounter_status_bar, set_scroll=config_status_bar['set_scroll'], resize_lock=config_status_bar['resize_lock'])

    def _status_bars(self):
        if self.status_bars_manager:
            return self.status_bars_manager.counters
        else:
            self.logger.error("No activ Status Bar Managers was found.", exc_info=self._logger_traceback)
            return False















    #################################



    def _check_db_should_be_an_stats(self):
        if self.statsdb.typ() != "stats":
            self.logger.error("No active DB was found. You need to connect or initialize a DB first, before you can make any operation on the DB.", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def _wait_till_all_threads_are_completed(self, waitername, sec_to_wait=3, sec_to_log = 15):
        time_counter = sec_to_log
        while not ( (len(self.threads_success_exit) >= len(self.active_threads)) or (len(self.threads_unsuccess_exit) != 0)):
        #while len(self.threads_unsuccess_exit) == 0
            #p(((len(self.threads_success_exit) <= len(self.active_threads))), "(len(self.threads_success_exit) < len(self.active_threads))")
            #p((len(self.threads_unsuccess_exit) == 0), "(len(self.threads_unsuccess_exit) == 0)")
            if time_counter >= sec_to_log:
                time_counter = 0
                self.logger.low_debug("'{}'-Waiter: {}sec was gone.".format(waitername, sec_to_log))

            if not self.threads_status_bucket.empty():
                answer = self.threads_status_bucket.get()
                thread_name = answer["name"]
                status = answer["status"]
                if status == "done":
                    if thread_name not in self.threads_success_exit:
                        self.threads_success_exit.append(answer)
                elif status in  ["failed", "terminated"]:
                    if thread_name not in self.threads_unsuccess_exit:
                        self.threads_unsuccess_exit.append(answer)
                elif status == "ThreadsCrash":
                    if thread_name not in self.threads_unsuccess_exit:
                        self.threads_unsuccess_exit.append(answer)
                        self.terminate_all("ThreadsCrash", thread_name=thread_name)
                    self.logger.critical("'{}'-Thread returned ThreadCrash-Error. |ErrorTrackID:'{}'| (To see more about it track ErrorID in the logs)".format(thread_name,answer["track_id"]))
                    return False
                else:
                    self.logger.error("ThreadsWaiter: Unknown Status was send: '{}'. Break the execution! ".format(status), exc_info=self._logger_traceback)
                    sys.exit()


                self.threads_status_bucket.task_done()

            time.sleep(sec_to_wait)
            time_counter += sec_to_wait
            #self._check_threads()
            self._check_buckets()

        self.logger.debug("Waiter '{}' was stopped. ".format(waitername))

        return True







    def _initialisation_computation_process(self, inp_data, text_field_name="text",  thread_name="Thread0"):
        if self._status_bar:
            if self._threads_num>1:
                if self._status_bar:
                    unit =  "rows"
                    self.main_status_bar_of_insertions.unit = unit
                    self.main_status_bar_of_insertions.total += len(inp_data)

        ### Preprocessors Initialization
        if thread_name not in self.preprocessors:
            if not self._init_preprocessors(thread_name=thread_name):
                self.logger.error("Error during Preprocessors initialization. Thread '{}' was stopped.".format(thread_name), exc_info=self._logger_traceback)
                self.threads_status_bucket.put({"name":thread_name, "status":"failed", "info":"Error during Preprocessors initialization"})
                self._terminated = True
                return False

        self.logger.debug("_InsertionProcess: Was started for '{}'-Thread. ".format(thread_name))
        
        if self._status_bar:
            if self._threads_num>1:
                if not self._timer_on_main_status_bar_was_reset:
                    #p(self.main_status_bar_of_insertions.start, "start1")
                    self.main_status_bar_of_insertions.start= time.time()
                    #p(self.main_status_bar_of_insertions.start, "start2")
                    self._timer_on_main_status_bar_was_reset = True

            unit = "rows"
            status_bar_insertion_in_the_current_thread = self._get_new_status_bar(len(inp_data), "{}:Insertion".format(thread_name), unit)
        self._check_termination(thread_name=thread_name)
        if self._status_bar:
            return status_bar_insertion_in_the_current_thread
        else:
            False


    def _is_redu(self, sent_index, token_index,redu_free_text_container):
        try:
            redu_free_text_container[sent_index][token_index][1].items
            return True
        except:
            return False
    def _check_buckets(self):
        status = False
        if not self.threads_error_bucket.empty():
            while not self.threads_error_bucket.empty():
                e = self.threads_error_bucket.get()
                self.threads_error_bucket.task_done()
                self.logger.error("InsertionError(in_thread_error_bucket): '{}'-Thread throw following Exception: '{}'. ".format(e[0], e[1]), exc_info=self._logger_traceback)
                status = True

        # if not self.channels_error_bucket.empty():
        #     while not self.channels_error_bucket.empty():
        #         e = self.channels_error_bucket.get()
        #         self.channels_error_bucket.task_done()
        #         self.logger.error("InsertionError(in_channel_error_bucket): '{}'-Thread ('{}') throw following Exception: '{}'. ".format(e[0], e[1],e[2]), exc_info=self._logger_traceback)
        #         status = True

        if status:
            self.logger.error("BucketChecker: Some threads/channels throw exception(s). Program can not be executed. ".format(), exc_info=self._logger_traceback)
            sys.exit()




    def _check_termination(self, thread_name="Thread0"):
        if self._terminated:
            self.logger.critical("'{}'-Thread was terminated.".format(thread_name))
            self.threads_status_bucket.put({"name":thread_name, "status":"terminated"})
            sys.exit()

    def _isrighttype(self, inp_data):
        #p(inp_data)
        check = (isinstance(inp_data, list), isinstance(inp_data, LenGen))
        #p(check, "check")
        if True not in check:
            self.logger.error("InputValidationError: Given 'inpdata' is not iterable. ", exc_info=self._logger_traceback)
            return False
        return True



    # def _isrighttype(self, inp_data):
    #     check = (isinstance(inp_data, list), isinstance(inp_data, types.GeneratorType))
    #     if True not in check:
    #         self.logger.error("InputValidationError: Given 'inpdata' is not iterable. ", exc_info=self._logger_traceback)
    #         return False
    #     return True



    def _check_corp_should_exist(self):
        if not self.corp: 
            self.logger.error("No active CorpusObj was found. You need to connect or initialize a Corpus first, before you can make any operation with Stats.", exc_info=self._logger_traceback)
            return False
        else:
            return True


    def _check_stats_db_should_exist(self):
        if not self.statsdb: 
            self.logger.error("No active DB was found. You need to connect or initialize a DB first, before you can make any operation with Stats.", exc_info=self._logger_traceback)
            return False
        else:
            return True

    def _check_stats_db_should_not_exist(self):
        if self.statsdb: 
            self.logger.error("An active DB was found. You need to initialize new empty Instance of DB before you can do this operation.", exc_info=self._logger_traceback)
            return False
        else:
            return True



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












