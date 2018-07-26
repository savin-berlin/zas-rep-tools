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
#import copy
import sys
#import regex
import logging


#from collections import defaultdict
from raven import Client
#from cached_property import cached_property
import types
import Queue
import enlighten


from zas_rep_tools.src.utils.helpers import set_class_mode, print_mode_name, path_to_zas_rep_tools, Rle
from zas_rep_tools.src.classes.dbhandler import DBHandler
from zas_rep_tools.src.classes.reader import Reader
from zas_rep_tools.src.classes.corpus import Corpus
from zas_rep_tools.src.utils.logger import *
from zas_rep_tools.src.utils.debugger import p
from zas_rep_tools.src.utils.error_tracking import initialisation
from zas_rep_tools.src.utils.traceback_helpers import print_exc_plus

# from zas_rep_tools.src.classes.configer import Configer

import platform
if platform.uname()[0].lower() !="windows":
    import colored_traceback
    colored_traceback.add_hook()
else:
    import colorama


class Stats(object):

    def __init__(self, 
                logger_folder_to_save=False,  logger_usage=True, logger_level=logging.INFO,
                logger_save_logs=True, logger_num_buffered=5, error_tracking=True,
                ext_tb=False, logger_traceback=False, mode="prod"):

        
        ## Set Mode: Part 1
        self._mode = mode
        if mode != "free":
            _logger_level, _logger_traceback, _logger_save_logs = set_class_mode(self._mode)
            logger_level = _logger_level if _logger_level!=None else logger_level
            logger_traceback = _logger_traceback if _logger_traceback!=None else logger_traceback
            logger_save_logs = _logger_save_logs if _logger_save_logs!=None else logger_save_logs
    

    
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

        #p(inpdata)

        #InstanceAttributes: Initialization
        self.db = False
        #self.input_bucket = Queue.Queue()
        self.threads_status_bucket = Queue.Queue()
        self.status_bars_manager =  self._get_status_bars_manager()
        self.corp_attributes = False


        ## Error-Tracking:Initialization #1
        if self._error_tracking:
            self.client = initialisation()
            self.client.context.merge({'tags': self.__dict__})


        self.logger.debug('Intern InstanceAttributes was initialized')


        self.logger.debug('An instance of Stats() was created ')

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


    def init(self, prjFolder, DBname, language,  visibility, corpus_id,
                    encryption_key=False,fileName=False,  version=False, stats_id=False):

        if self.db:
            self.logger.error("StatsInitError: An active Stats Instance was found. Please close already initialized/opened Stats, before new initialization.", exc_info=self._logger_traceback)
            return False

        self.db = DBHandler(logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)
        was_initialized = self.db.init("stats", prjFolder, DBname, language,  visibility, corpus_id=corpus_id,
                    encryption_key=encryption_key,fileName=fileName,  version=version,
                    stats_id=stats_id)

        if not was_initialized:
            self.logger.debug("StatsInit: Current Stats for following attributes  wasn't initialized: 'dbtype='{}'; 'dbname'='{}; corp_id='{}'; 'stats_id'='{}'; encryption_key='{}'; .".format("stats", DBname,corpus_id, stats_id,encryption_key))
            return False

        if self.db.exist():
            self.logger.info("StatsInit: '{}'-Stats was successful initialized.".format(DBname))
            return True
        else:
            self.logger.error("StatsInit: '{}'-Stats wasn't  initialized.".format(DBname), exc_info=self._logger_traceback)
            return False

    def close(self):
        self.db.close()
        self.db = False

    def _close(self):
        self.db._close()
        self.db = False

    def open(self, path_to_stats_db, encryption_key=False):

        if self.db:
            self.logger.error("StatsInitError: An active Stats Instance was found. Please close already initialized/opened Stats, before new initialization.", exc_info=self._logger_traceback)
            return False

        self.db = DBHandler(logger_level= self._logger_level,logger_traceback=self._logger_traceback, logger_folder_to_save=self._logger_folder_to_save,logger_usage=self._logger_usage, logger_save_logs= self._logger_save_logs, mode=self._mode ,  error_tracking=self._error_tracking,  ext_tb= self._ext_tb)
        self.db.connect(path_to_stats_db, encryption_key=encryption_key)


        if self.db.exist():
            if self.db.typ() != "stats":
                self.logger.error("Current DB is not an StatsDB.")
                self._close()
                return False
            self.logger.info("StatsOpener: '{}'-Stats was successful opened.".format(os.path.basename(path_to_stats_db)))
            return True
        else:
            self.logger.error("StatsOpener: Unfortunately '{}'-Stats wasn't opened.".format(os.path.basename(path_to_stats_db)), exc_info=self._logger_traceback)
            return False



    ###########################Setters######################

    def _insert(self, inp_data, datatyp="dict",text_field_name="text",  thread_name="Thread0", status_bar=False):
        try:
            pass
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("_InsertError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
            
        if status_bar:
            status_bar_of_insertions = self._get_new_status_bar(len(inp_data), "{}:Insertion".format(thread_name), "files")

        for row_as_dict in inp_data:
            p(row_as_dict[text_field_name])
        # elif isinstance(inp_data, Queue):
        #     pass

    def insert(self,inp_corp, thread_number=0, datatyp="dict", text_field_name="text",  thread_name="Thread0", status_bar = True):
        try:
            pass
        except Exception, e:
            print_exc_plus() if self._ext_tb else ""
            self.logger.error("_InsertError: See Exception: '{}'. ".format(e), exc_info=self._logger_traceback)
            self.threads_status_bucket.put({"name":thread_name, "status":"failed"})
        except KeyboardInterrupt:
            self.logger.warning("KeyboardInterrupt: Process was stopped from User. Some inconsistence in the current DB may situated.")
            sys.exit()
            
        if not isinstance(inp_corp, Corpus):
            self.logger.error("Given InpObject is not from Corpus type. Insert was aborted!")
            return False


        if status_bar:
            status_bar_threads_init = self._get_new_status_bar(len(inp_data), "ThreadsStarted", "threads")

        self.corp_attributes = inp_corp.db.get_all_attr()

        i=1
        for gen in inp_corp.docs(stream_number=thread_number):
            if not self._isrighttype(gen):
                self.logger.error("InsertionError: Given InpData not from right type. Please give an list or an generator.", exc_info=self._logger_traceback)
                return False
            #p(gen)

            thread_name = "Thread{}".format(i)
            processThread = threading.Thread(target=self._insert, args=(gen,datatyp,  text_field_name,  thread_name, status_bar), name=thread_name)
            processThread.setDaemon(True)
            processThread.start()
            self.active_threads.append(processThread)
            if status_bar:
                status_bar_threads_init.update(incr=1)
            i+=1
            time.sleep(2)

        self.logger.info("'{}'-thread(s) was started. ".format(len(self.active_threads)))

        time.sleep(3)

        self._wait_till_all_threads_are_completed()

        self._print_summary_status()
        #self.opened_gateways.terminate()


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


    def _wait_till_all_threads_are_completed(self):
        while (len(self.threads_success_exit)+len(self.threads_unsuccess_exit)) < len(self.active_threads):
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
            time.sleep(3)
            #self._check_threads()
            self._check_buckets()




    def _get_new_status_bar(self, total, desc, unit):
        counter = self.status_bars_manager.counter(total=total, desc=desc, unit=unit)
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


    ###########################Getters#######################


    def repl(self, columns=False,  where=False, connector_where="AND", output="list", size_to_get=1000):
        if not self._check_db_should_exist():
            yield False
            return 
        for row in   self.db.lazyget("replications", columns=columns, where=where, connector_where=connector_where, output=output, size_to_get=size_to_get):
            yield row


    def redu(self, columns=False,  where=False, connector_where="AND", output="list", size_to_get=1000):
        if not self._check_db_should_exist():
            yield False
            return 
        for row in   self.db.lazyget("reduplications", columns=columns, where=where, connector_where=connector_where, output=output, size_to_get=size_to_get):
            yield row


    # csv = init_csv(baseline=True, repl=True, redu=True, meta_data=["doc_id", ], linguistic_data=["pos", "sentiment"])
    
    # for word in  baseline():
    #     current_bunch_of_rows = False
    #     if baseline:
    #         pass
    #         current_bunch_of_rows = to_row(current_bunch_of_rows)

    #     if repl:
    #         if repl in word:
    #             pass
    #             current_bunch_of_rows = to_row(current_bunch_of_rows)

    #     if redu:
    #         if redu in word:
    #             pass
    #             current_bunch_of_rows = to_row(current_bunch_of_rows)

    #     #to_row

    #     csv.write(current_bunch_of_rows)



    def _repetitions_generator(self):
        if scope == 1:
            for word in self.baseline():
                current_bunch_of_rows = False
                if baseline:
                    pass
                    current_bunch_of_rows = to_row(current_bunch_of_rows)

                if repl:
                    if repl in word:
                        pass
                        current_bunch_of_rows = to_row(current_bunch_of_rows)

                if redu:
                    if redu in word:
                        pass
                        current_bunch_of_rows = to_row(current_bunch_of_rows)

        if scope > 1:
            for phrase in self.reduplications():
                pass



    def export(output_file_name, output_file_format="csv", baseline=True, repl=False, redu=False, search_pattern=False, scope="*", context_left=False, context_right=False, meta_data=False, linguistic_data=False):
        #stats.export(output_file_name, output_file_format=output_file_format,baseline=baseline, repl=repl, redu=redu, search_pattern=splitted_search_pattern_paradigma, scope=scope, context_left=context_left, context_right=context_right, meta_data=splitted_meta_data, linguistic_data=splitted_linguistic_data)
        self._repetitions_generator()
        export = Exporter()
        export.tocsv(self._repetitions_generator())


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







    ###########################P##############




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












